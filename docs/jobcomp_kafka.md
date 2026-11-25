# Slurm Workload Manager - Job Completion Kafka plugin guide

# [Slurm Workload Manager](/)

[SchedMD](https://www.schedmd.com/)

## Navigation

[Slurm Workload Manager](/)

Version 26.11

* About

  + [Overview](overview.md)
  + [Release Notes](release_notes.md)
* Using

  + [Documentation](documentation.md)
  + [FAQ](faq.md)
  + [Publications](publications.md)
* Installing

  + [Download](https://www.schedmd.com/download-slurm/)
  + [Related Software](related_software.md)
  + [Installation Guide](quickstart_admin.md)
* Getting Help

  + [Mailing Lists](mail.md)
  + [Support and Training](https://www.schedmd.com/slurm-support/our-services/)
  + [Troubleshooting](troubleshoot.md)

# Job Completion Kafka plugin guide

When configured, the **jobcomp/kafka** plugin attempts to publish a subset
of the fields for each completed job record to a Kafka server. Since Slurm
25.05 it is also possible to optionally send a subset of job record fields when
the job starts running. Since Slurm 26.11, records can optionally be sent for
additional job state transition events: a job entering the queue, being
requeued, becoming held, and being released. Each of these events, like job
start, can be enabled independently and sent to its own topic. Every record
carries an `event` field naming the event (`job finish`,
`job start`, `job queue`, `job requeue`,
`job hold`, or `job release`) and an
`@event_time` field with the UTC time the record was generated, in
the same format as the other time fields. A job finish record describes the
end of one run of a job, not necessarily the end of the job: the finish record
of a requeued run is followed, when those events are enabled, by a job requeue
record and, once the job runs again, by new job start and job finish records,
all with the same `jobid` value.

## Requirements

The plugin serializes the subset of fields to JSON before each produce
attempt. The serialization is done using the Slurm serialization plugins, so the
**libjson-c** development files are an indirect prerequisite for this plugin.

The plugin offloads part of the client producer work to **librdkafka** and
consumes its API, thus the library development files are another prerequisite.

* [librdkafka](https://github.com/confluentinc/librdkafka)
  development files
* [libjson-c](related_software.md#json) development
  files

## Configuration

The plugin is configured with the following
[slurm.conf](slurm.conf.md) options:

* [**JobCompType**](slurm.conf.md#OPT_JobCompType)
  Should be set to **jobcomp/kafka**.

  ```
  JobCompType=jobcomp/kafka
  ```
* [**JobCompLoc**](slurm.conf.md#OPT_JobCompLoc) This string
  represents an absolute path to a file containing 'key=value' pairs configuring
  [librdkafka properties](https://github.com/confluentinc/librdkafka/blob/master/CONFIGURATION.md). For the plugin to work properly, this file
  needs to exist and at least the **bootstrap.servers** property needs to be
  be configured.

  ```
  JobCompLoc=/arbitrary/path/to/rdkafka.conf
  ```

  **NOTE**: There is no default value for JobCompLoc when this plugin is
  configured, and thus it needs to be explicitly set.

  **NOTE**: The **librdkafka** parameters configured in the file
  referenced by this option take effect upon slurmctld restart.

  **NOTE**: The plugin doesn't validate these parameters, but just logs
  an error and fails if any parameter passed to the library API function
  rd\_kafka\_conf\_set() fails.

  An example configuration file could look like this:

  ```
  bootstrap.servers=kafkahost1:9092
  debug=broker,topic,msg
  linger.ms=400
  log_level=7
  ```
* [**JobCompParams**](slurm.conf.md#OPT_JobCompParams) Comma
  separated list of extra configurable parameters. Please refer to the slurm.conf
  man page for specific details. Example:

  ```
  JobCompParams=flush_timeout=200,poll_interval=3,requeue_on_msg_timeout,
  topic=mycluster
  ```

  Or, to also send job queue and job hold records and deliver the records
  of every enabled event, including job finish, to a single topic:

  ```
  JobCompParams=enable_job_queue,enable_job_hold,topic_all=mycluster-jobs
  ```

  **NOTE**: Changes to this option do not require a slurmctld restart.
  Reconfiguration or SIGHUP is sufficient for them to take effect.

  **NOTE**: Refer to the man page to configure job start, queue, requeue,
  hold, and release events.
* [**DebugFlags**](slurm.conf.md#OPT_DebugFlags) Optional
  **JobComp** debug flag for extra plugin specific logging.

  ```
  DebugFlags=JobComp
  ```

## Plugin Functionality

For each enabled job event, the plugin jobcomp\_p\_record\_job\_event operation
is executed. A subset of the job record fields are serialized into a JSON
string via the Slurm serialization plugins. Then the serialized string is
attempted to be produced using the librdkafka rd\_kafka\_producev() API call,
keyed by the job ID, so the records of a job sent to the same topic land in
the same partition with the default librdkafka partitioner. Retries can
reorder them unless the librdkafka property `enable.idempotence`
is set to `true` in the JobCompLoc file, and messages produced
again by requeue\_on\_msg\_timeout go behind newer ones.
Each job array task and each heterogeneous job component has its own job
ID.

Every record carries, when set, the fields identifying the job and its
state: `event`, `@event_time`, `jobid`,
`sluid`, `original_sluid`, `restart_cnt`,
`cluster`, `username`, `user_id`,
`groupname`, `group_id`, `account`,
`partition`, `qos`, `job_name`,
`state`, `state_reason`, `state_desc`,
`priority`, `@submit`, `@eligible`,
`array_job_id`, `array_task_id`, `het_job_id`,
and `het_job_offset`. The `sluid` field matches the
job's accounting record and changes on every requeue and resize, while
`original_sluid` only changes on a requeue. A requeue increments
`restart_cnt`: the finish record of the run that ended still
carries the old value, the requeue record and every later record carry the
new one. That finish record reports `REQUEUED` when a requeue ended
the run, `NODE_FAIL` or `PREEMPTED` when a node failure
or preemption requeued the job, as accounting does, and the run's own final
state when the job was requeued after finishing, such as by RequeueExit. Job
start and job finish records add the
request and allocation details, such as the nodes, CPU counts, TRES, task
layout, paths, time limit, the admin comment, the comment and the script when
enabled, and for finish records the end time, elapsed time, and exit codes.
The queue, hold, release,
and requeue records carry only the common fields.

Producing a message to librdkafka can be done even if the Kafka server is
down. But an error returned from this call makes it so the message is discarded.
Produced messages accumulate in the librdkafka out queue for up to "linger.ms"
milliseconds (a configurable librdkafka parameter) before building
a message set from the accumulated messages.

Then the librdkafka library transmits a produce request. While no "ACK" is
received, messages are conceptually considered to be "in-flight" according to
the library documentation. The library then receives a produce response, which
can be handled in one of two ways:

**retriable error**
:   The library will automatically attempt a retry if
    no library limit parameter is hit.

**permanent error** or **success**
:   The message will be removed
    from the library out queue and is staged to the library delivery report queue.

The following diagram illustrates the functionality being described:

![](jobcomp_kafka_fig1.png)

The **jobcomp/kafka** plugin has a background poll handler thread that
periodically calls the librdkafka API rd\_kafka\_poll() function. How frequent
the thread makes the call is configurable via JobCompParams=poll\_interval.
The call makes it so that messages in the library delivery report queue are
pulled and handled back to the plugin delivery report callback, which takes
different actions depending on the error message the library set. By default,
successful messages are just logged if DebugFlags=JobComp is enabled, and
messages with permanent errors are discarded, unless the error is message timed
out and JobCompParams is configured with "requeue\_on\_msg\_timeout", which would
instruct the callback to attempt to produce the message again.

**NOTE**: Each enabled event adds records for librdkafka to buffer while
the broker is unreachable, and the job queue event adds one per submission.
With the librdkafka defaults, a record is discarded after
`message.timeout.ms` (300000 milliseconds, or 5 minutes), and new
records are discarded once `queue.buffering.max.messages` (100000)
are queued.
Raise them in the JobCompLoc file for the submission rate and the longest
outage the records must survive, or set JobCompParams=requeue\_on\_msg\_timeout
to produce timed-out records again.

On plugin termination, the fini() operation is executed. The rd\_kafka\_purge()
library API function is called which purges librdkafka out queue messages. The
rd\_kafka\_flush() API call is also called, which waits until all outstanding
produce requests (and potentially other types of requests) are completed.
How much to wait is also configurable via JobCompParams=flush\_timeout
parameter. Purged messages are always saved to the plugin state file in the
Slurm StateSaveLocation, and messages purged while "in-flight" are discarded.

**NOTE**: You must be using librdkafka v1.0.0 or later in order to take
advantage of the purge functionality described above. With previous versions
the outgoing queue can not be purged to the state file on shutdown, which
means that any messages that weren't delivered before the termination of the
kafka plugin will be lost.

On plugin initialization, after parsing the configuration, saved messages in
the state are loaded and attempted to be produced again. So undelivered messages
should be resilient to slurmctld restarts.

The Kafka broker "host:port" list should be explicitly configured in the
file referenced by JobCompLoc option explained above. The default topic is
the configured Slurm ClusterName, but it can also be configured via
JobCompParams=topic parameter. The other events default to per-event
topics named <ClusterName>-job-<event>, where the event is start,
queue, requeue, hold, or release, each configurable via its own JobCompParams
topic parameter. Kafka only preserves message order within a topic partition,
so set JobCompParams=topic\_all to send every enabled event to one topic and
obtain a single stream of records per job, ordered as described above.
The plugin does not create topics, so they must exist on the Kafka cluster
unless its brokers create topics automatically (the
`auto.create.topics.enable` broker property).

The **jobcomp/kafka** plugin mostly logs informational messages to the
JobComp DebugFlag, except for error messages. The librdkafka by default logs
to the application stderr, but the plugin configures the library to forcefully
log to syslog instead. The library logging level and debug contexts are also
configurable via the file referenced by JobCompLoc, as well as the rest of the
library configuration parameters.