# Slurm Workload Manager - Job I/O Relay Guide

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

# Job I/O Relay Guide

The **relay\_io** plugins forward the output of jobs to an aggregate
location as it is produced, so that it can be collected into a central log
management system. This is intended to enable large-scale monitoring and storage
of Slurm I/O data used for clusters devoted to particularly well-known,
well-understood applications, or those operating in a Cloud-oriented environment
where filesystem logging may not be ideal.

**NOTE**: Relaying is **in addition to** normal output handling. The
files named by **--output** and **--error** are still written and output
is still returned to **srun**; the relay takes a copy. See
[Behavior changes](#behavior) for the differences that remain.

## Contents

* [Configuration](#config)
* [Selecting jobs from job\_submit](#job_submit)
* [The uds\_json plugin](#uds_json)
* [Record format](#records)
* [How output becomes records](#buffering)
* [Delivery](#delivery)
* [Behavior changes](#behavior)
* [Ordering](#ordering)

## Configuration

Relaying is off until a plugin is selected with
[RelayIOPlugin](slurm.conf.md#OPT_RelayIOPlugin) in
**slurm.conf**:

```
RelayIOPlugin=relay_io/uds_json
```

By default no job is relayed unless it specifies the
[--relay-io](sbatch.md#OPT_relay-io)=**yes** job option. A site
that wants relaying to be the default where jobs can opt out with the
**--relay-io=no** job option can set:

```
RelayIODefaultEnabled=yes
```

**slurmctld** settles whether a job is relayed when the job starts
running, reading **RelayIOPlugin** and **RelayIODefaultEnabled** as they
are at that moment, and the job carries the answer until it ends. A change to
**RelayIODefaultEnabled** therefore applies to jobs that start afterwards,
not to jobs already running. That is what keeps such a change from leaving a
job with its start relayed and its end not, which would leave the scraper
waiting for a **job\_end** that never comes. A requeued job is settled again
for its next run.

While a job is pending, what it asked for can still be changed with
[scontrol update](scontrol.md#OPT_RelayIO):

```
scontrol update job 1234 RelayIO=yes
scontrol update job 1234 RelayIO=no
scontrol update job 1234 RelayIO=default
```

Setting **default** puts the job back to **RelayIODefaultEnabled**. A
job that is no longer pending cannot be changed, and the update is refused
because its current run has already been settled.

Each node also loads the plugin from its own **RelayIOPlugin**, and a
node without one relays nothing, whatever was settled at the start. Removing
**RelayIOPlugin** from a node while a job runs there can leave that job
with a **job\_start** and no **job\_end**.

Plugin-specific settings are given with
[RelayIOParameters](slurm.conf.md#OPT_RelayIOParameters):

```
RelayIOParameters=socket=/var/spool/slurmd/relay-io.sock,stepd_ring_mbytes=4,max_log_kbytes=32
```

See the [slurm.conf](slurm.conf.md) man page for the full list
of parameters.

When modifying these options keep in mind that a running slurmstepd keeps
the settings it started with, including its socket path, until it ends.

## Selecting jobs from job\_submit

A site that wants to choose which jobs are relayed, rather than leave it to
the job, can set `job_desc.relay_io` from a
[job\_submit/lua](job_submit_plugins.md) script. The field takes
these values:

* **0** relays nothing from the job.
* **slurm.INFINITE16**, or **slurm.NO\_VAL16** in
  `slurm_job_submit()`, uses **RelayIODefaultEnabled** as it is
  when the job starts.
* **slurm.NO\_VAL16** in `slurm_job_modify()` leaves the job's
  setting unchanged.
* Any other value relays the job.

Set the value in `slurm_job_submit()`, in
`slurm_job_modify()`, or in both. A value set in
`slurm_job_modify()` is applied the same way
`scontrol update job RelayIO=` is, so it applies while the job is
pending. Setting it unconditionally there refuses every update of a job that
is already running.

```
function slurm_job_submit(job_desc, part_rec, submit_uid)
    if job_desc.partition == "audited" then
        job_desc.relay_io = 1
    end
    return slurm.SUCCESS
end
```

## The uds\_json plugin

**relay\_io/uds\_json** writes JSON records to a UNIX domain datagram
socket, one socket per node, which a site-provided scraper reads. One record is
one datagram, so a reader never reassembles or splits anything: each receive
returns exactly one complete record, with no delimiter to scan for.

The scraper is responsible for **creating and binding** the socket named
by the **socket=** parameter, as **SOCK\_DGRAM**; the daemons connect to
it as clients. This means it can be restarted independently of Slurm.

The scraper owns the socket, so it also owns the permissions on it. It
should not be world-writable: **slurmd** connects as **SlurmdUser**, which
defaults to root, and any local user able to connect could otherwise inject
forged records into the log stream.

**NOTE**: Whoever is bound to that path receives the output of every
relayed job on the node, so where the socket lives is a security decision.
Before every connection attempt the daemons check that the socket is really a
socket and is owned by root or **SlurmdUser**, and refuse to send to it
otherwise. Because a datagram socket carries no peer credentials, that
check cannot be confirmed after connecting, so the directory holding the
socket must also be owned by root or **SlurmdUser** and must not be writable
by group or other. The directory is also checked before every connection
attempt. A daemon logs a failed check once, and again only when the reason
changes, and keeps trying.

Every daemon on the node sends to that one socket: **slurmd** for the job
start and end events, and each **slurmstepd** for its own step.

```
                           +-- slurmd       (job events)
                           |
scraper <-- relay-io.sock -+-- slurmstepd  (one step's output)
(binds, reads)             |
                           +-- slurmstepd  (another step's output)
                               (all connect)
```

**max\_log\_kbytes** caps the task output one record carries, 4
kilobytes by default. Output longer than that is split across several records
rather than truncated.

The cap counts the task's output after NULL escaping and UTF-8 sanitizing,
so a NULL takes six bytes of the budget and a byte that is not valid UTF-8
takes three. The identity fields and whatever the JSON escaping costs are
added on top, so the datagram can be larger than the cap. Size
**max\_log\_kbytes** with that in mind, and against what the kernel will
carry in one datagram: a large one needs contiguous physical memory, which is
hardest to find on exactly the node that has been running jobs the longest.

**NOTE**: The kernel queues only **net.unix.max\_dgram\_qlen** datagrams
for a socket, and that limit cannot be raised with **SO\_RCVBUF**. The default
is 10. A scraper that does not read continuously, on a node that produces output
at volume, will cause records to be dropped by the sending daemon. Raise that
sysctl to suit the volume you expect. The kernel reads it when the socket is
created, so raise it before the scraper binds: set it persistently, in
`/etc/sysctl.d/` for example, and restart the scraper after changing
it, or the running socket keeps the old limit.

**NOTE**: A datagram also cannot exceed the sending socket's buffer,
which is **net.core.wmem\_default** and is often around 200KB, raisable only
as far as **net.core.wmem\_max**. **max\_log\_kbytes** must be set below
that, or a record near the cap cannot be sent at all and is dropped. The
**slurmd** log reports such drops as:

```
[/var/spool/slurmd/relay-io.sock] relay dropped 1 record due to EMSGSIZE, the smallest being 30123 bytes
```

The shipped
default of 4 kilobytes leaves room for the worst case, where every byte of a
line escapes to six and the record reaches about 25KB. A site raising
**max\_log\_kbytes** for fewer, larger records has to keep six times the new
value, plus the identity fields, under **net.core.wmem\_default**, or raise
that sysctl to match.

### Verifying it works

`scontrol show config | grep RelayIO` reports what the cluster
believes is configured, which is the quickest way to confirm the settings
took.

To validate the job will use the RelayIO plugin, check
`scontrol show job`, which reports **RelayIO=YES** if relaying is
on for a job. **RelayIO** is not present otherwise.

Start the scraper before the daemons relay to it. Nothing is lost while the
ring still has room: a daemon retries the connection with a backoff and sends
what it is still holding. Once the ring fills, the oldest records are
dropped.

On a successful start, **slurmd** logs the socket it will relay to, at
level **info**:

```
relay_io/uds_json: relaying job output to /var/spool/slurmd/relay-io.sock
```

If that line is absent, **RelayIOPlugin** is not set or the plugin failed
to load, and no job can relay. If it is present but nothing arrives, the usual
cause is that the scraper is not running. When there is no socket file at all,
a daemon logs that at the default level when it first finds the socket
missing, and again only when the reason changes:

```
[/var/spool/slurmd/relay-io.sock] not connecting, the relay_io socket is not present
```

A socket the daemons refuse is logged the same way, with the reason: the
socket or the directory holding it is owned by someone other than root or
**SlurmdUser**, the directory is writable by group or other, or the path is
not a socket.

A valid socket file that is left behind with no scraper bound to it is
quieter, since a daemon retrying a connection every 30 seconds must not fill the
log on a failed connect. To see failed connects, set
**DebugFlags=Protocol**, then look for `connect() failed` in the
logs.

A third cause is the plugin loading but finding nothing to serialize
with:

```
relay_io/uds_json: no serializer for application/json, not relaying
```

That means **SerializerPlugins** is set to a list with no plugin that
serves **application/json**. Relaying is disabled and the daemon carries
on, so nothing else looks wrong.

The start record is emitted when a node first accepts work for the job,
which is before the prolog runs, so a job whose prolog fails still produces a
**job\_start** and a **job\_end**. A pair with no step records between
them is an expected outcome rather than a sign of a lost record.

A receiver small enough to paste is enough to confirm the path end to end,
and to see the record format:

```
import os, socket, stat

path = "/var/spool/slurmd/relay-io.sock"

# Only ever replace a stale socket, never a file that happens to be here.
if os.path.exists(path) and stat.S_ISSOCK(os.stat(path).st_mode):
    os.unlink(path)

os.umask(0o177) # bind() would otherwise use the umask in effect
sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
sock.bind(path)

# The buffer has to exceed max_log_kbytes, or a long record is silently
# truncated: a datagram larger than the buffer loses its remainder.
while True:
    print(sock.recv(8 << 20).decode("utf-8", "replace"))
```

Run it while the real scraper is stopped, since only one process can be
bound to the socket. Run it as root or **SlurmdUser**: the daemons refuse a
socket owned by anyone else, and the directory it binds in is writable by no
one else either. Submit a job with **--relay-io=yes** and the job's
records appear as they are produced. If they do not, the **slurmd** log on
the node that ran the job is where to look next.

## Record format

Every record is one datagram holding a single line of JSON. All records
carry these fields:

* **v**: schema version, currently 1.
* **type**: one of *job\_start*, *job\_end*, *step\_start*,
  *step\_end*, or *log*.
* **time**: when the event was produced, as nanoseconds since the Unix
  epoch. The value is past 2^53, so a consumer has to parse it as a 64-bit
  integer; one that decodes JSON numbers as doubles, as JavaScript does, will
  round it.
* **slurm**: an object identifying where the event came from, with
  **cluster**, **node**, **job\_id**, **sluid**, and
  **user\_name**.

**sluid** is the job's Slurm unique identifier which, unlike
**job\_id**, is never reused.

Job records add fields that describe the job as a whole, rather than
repeating them on every line of its output:

* **slurm.restart\_count**: how many times the job has been requeued, so
  that records from different runs of one job ID can be told apart.
* **slurm.partition** and **slurm.account**.

Step and log records add **slurm.step\_id**, which is a string: either a
step number, or one of "batch" or "interactive".

Any of **user\_name**, **partition**, and **account** may be absent,
since they come from the job's credential. They are left out entirely rather
than emitted as null.

Log records additionally carry:

* **stream**: "stdout" or "stderr".
* **slurm.task\_id\_global** and **slurm.task\_id\_local**.
* **body**: the output itself, including its trailing newline when it has
  one. Always valid UTF-8 from the subset Slurm accepts: any byte that is not part
  of a well-formed sequence, and any code point Slurm rejects, which is
  surrogates, noncharacters, private use, and U+FFF0 through U+FFF8, is replaced
  with U+FFFD. The record therefore always parses, no matter what the task wrote.
  A NULL is replaced with the six-character text `\u0000` rather than
  carried through, since the record is built as a C string. So **body** is not
  a byte-for-byte copy of the task's output: a private use glyph, such as the ones
  a Nerd Font prompt emits, arrives as U+FFFD.
* **partial**: present and true when the record does not end at a line
  boundary, which happens when a task's last line has no newline, when a line is
  long enough that it is emitted before its newline arrives, or when a line does
  not fit in one record. Never present on an **unbuffered** record.
* **unbuffered**: present and true when the step used
  **--unbuffered**.

Example, reformatted for readability:

```
{
	"v":1,
	"type":"log",
	"time":1786000818715000000,
	"slurm":{
		"cluster":"slurm",
		"node":"node1",
		"job_id":174,
		"sluid":"sA0SM5EFW65700",
		"user_name":"alice",
		"step_id":"0",
		"task_id_global":0,
		"task_id_local":0
	},
	"stream":"stdout",
	"body":"hello world\n"
}
```

and the **job\_start** that preceded it:

```
{
	"v":1,
	"type":"job_start",
	"time":1786000818402000000,
	"slurm":{
		"cluster":"slurm",
		"node":"node1",
		"job_id":174,
		"sluid":"sA0SM5EFW65700",
		"user_name":"alice",
		"restart_count":0,
		"partition":"batch",
		"account":"physics"
	}
}
```

## How output becomes records

Normally one record is one line, which is what a reader of the job's output
would have seen. A line that reaches **max\_log\_kbytes** is emitted without
waiting for its newline and marked
**partial**, so that a task which never terminates a line cannot consume
memory without bound. **partial** means only that the record does not end at
a line boundary, so it is also set on a trailing line that had no newline when
the step ended.

With **--unbuffered** there is no line structure to rely on, so output is
emitted in chunks of at most 1KiB marked **unbuffered** instead. Those
records are never marked **partial**: they are cut at an arbitrary offset by
definition,
which **unbuffered** already says. Batch script output is ordinary buffered
output and is split into lines.

A record never ends in the middle of a multi-byte character. A character
split across two reads is held back until the rest of it arrives, so a consumer
can decode each **body** on its own.

A line is also split when it reaches **max\_log\_kbytes**. That cap is
counted after NULL escaping and UTF-8 sanitizing rather than in the bytes the
task wrote, so where a line splits does depend on what is in it: a NULL takes
six of the budget and a byte that is not valid UTF-8 becomes U+FFFD, taking
three. JSON escaping is then added on top, so the record is larger again.
Plain text costs about a byte per byte; a double quote, a backslash, a slash,
or a tab costs two; and a newline or any other control character costs up to
six, depending on which JSON serializer is loaded. About 250 bytes of every
record go to the identity fields as well. These
figures are approximate because more than one serializer can serve
**application/json** and they do not escape identically. So a record
carrying the default 4 kilobytes of plain text is a little over that, while
the same cap filled with control characters produces a record roughly six
times its size.

Each piece but the last is marked **partial**, so a consumer joins records
for the same job, step, task, and stream until it reads one without it. A chain
is also ended by the step's **step\_end** record, which ends every chain
still open for that step on that node: it carries neither a stream nor a task
id, so there is no per-stream terminator to wait for. A task's last line is
marked **partial** when it had no newline, and nothing follows it, so a
consumer that waited for an unmarked record would wait forever.
**unbuffered** records are never marked **partial** even when they are
split, so they are
simply concatenated in arrival order for a given task and stream.

**NOTE**: Joining a **partial** chain is only trustworthy when nothing
was dropped. A record lost from the middle of a split line leaves the pieces on
either side of it looking like a complete line, and nothing in the record says
otherwise. Drops are counted in the node's **slurmd** log and never in the
stream itself, so check there, as described under
[Delivery](#delivery), before relying on a rejoined line. Both
**slurmd** and **slurmstepd** write to **SlurmdLogFile**, the latter
prefixing its lines with `[jobid.stepid]`, and every drop report is
logged at **info**, so **SlurmdDebug** must be at **info** or higher
for this check to mean anything. Searching the log for **relay** finds all of
them; the ring reports read `the relay is not draining fast enough`.
A record is only ever lost from the ring: output on its way to becoming a record
is held until there is room for it, so a task is slowed rather than losing what
it wrote.

## Delivery

A slow or absent scraper never blocks a job. Each daemon holds records in a
fixed-size ring while they wait to be written, and when that ring is full the
**oldest records are dropped first**. If the scraper is not running, or
stops reading, records are lost rather than allowed to stall the job that
produced them.

The ring is a burst buffer, not a durability guarantee. Size it for a brief
scraper restart rather than for a prolonged outage. **stepd\_ring\_mbytes** is
the one to raise for output volume, since every byte of task output goes through
a **slurmstepd**; **slurmd\_ring\_mbytes** only covers **slurmd**'s job
events. A reconnect is retried with a backoff that starts at 250ms and caps at
30 seconds. So size the ring for the output a step produces in that window.
Dropped records are counted and reported in the **slurmd** log: once for the
first record a daemon drops, periodically after that with a running total, and
once more with the final total when the daemon or the step finishes.

A record the kernel refuses as too large for one datagram is dropped as
well, and counted in the same totals. Retrying it would wedge everything behind
it, so it is reported rather than requeued. Since **max\_log\_kbytes** caps the
sanitized body rather than the whole record, a record can exceed what the
kernel will carry even though the body was within the cap. So set that figure
below the datagram size the socket can actually take.

Output on its way to becoming a record is never dropped. Each stream being
relayed holds what the task wrote until the relay has turned it into records,
and once a stream is holding as much as its buffer allows the task waits rather
than losing what it wrote. That buffer holds 128 kilobytes, or twice
**max\_log\_kbytes** when that is larger, so that several records can queue
up before a task is held at all. A task that
outruns the relay is therefore slowed to the rate the relay can serialize,
which is the one case where relaying is not free to the job.

Two further cases lose records. At step end, at daemon shutdown, and for the
slurmd before a `scontrol reconfigure` restarts it, the relay is
given up to five seconds to drain. If the scraper cannot be reached, the relay
makes one more connection attempt instead of waiting. Anything still queued
after that is lost. And a record being sent when the connection drops goes back
to the **front** of the ring, to be sent once the connection is back, but it
is dropped instead if the ring has filled in the meantime.

A stream that **slurmstepd** already reads on its way to **srun**
shares that path, so a stalled **srun** can hold up the relay for that step
as well. A stream that had to be given a pipe can still block the task on that
pipe once it fills, which is a consequence of the pipe rather than of the
relay; see
[Behavior changes](#behavior).

Connections reconnect on their own with a capped backoff, so restarting the
scraper recovers without intervention.

## Behavior changes

Output still reaches the same places: the files named by **--output** and
**--error** are still written, **srun** still displays task output, and
**sattach** still works. Everything is relayed, including output the job
discards:

* A stream directed to **/dev/null**, whether by
  **--output**=**none** or for the tasks **--output**=*taskid* did
  not select, is still relayed. Discarding the local copy is not a statement
  about the aggregate log.
* A step run under a pseudo terminal, such as `srun --pty`, is
  relayed, but the terminal gives rank 0 a single file descriptor for both
  streams, so every record from that rank is reported with a **stream** of
  **stdout**.

What does change is how the bytes reach a file. Where a task used to write
straight to its output file, **slurmstepd** now sits in the middle so that
it can take a copy. The file's contents are unchanged, but:

* When stdout and stderr are directed to the **same** file, the order the
  two streams interleave in that file is no longer the order the task wrote
  them. Each stream on its own is still complete and in order.
* The task's stdout and stderr are pipes rather than regular files, so
  `lseek()` and `ftruncate()` on them fail, a write can
  block once the pipe is full, and concurrent writers are only atomic up to
  **PIPE\_BUF** rather than at any size.
* A failure to write the output file in the slurmstepd closes the task's end
  of that stream. **EAGAIN** and **EWOULDBLOCK** are retried, but any other
  error, such as **ENOSPC** or **EIO**, ends the copy, and the task's next
  write to that stream fails with **EPIPE** and raises **SIGPIPE**. If the
  task were writing to the file itself, then it would have been handed the error
  and could have decided how to handle it, but that is not possible in this case.
  The error is reported in the **slurmd** log, and the step's other streams are
  unaffected.
* The output file is still opened as the job's user, but **slurmstepd**
  writes to it as root. The task's file size limit, such as one set by
  `ulimit -f`, does not stop the file from growing, and a filesystem
  that does not apply quota limits to root does not stop it at the user's quota
  either.

Relaying gives such a stream a pipe of its own, which costs two file
descriptors per stream in **slurmstepd**: the read end of the pipe, and the
output file, which **slurmstepd** now holds open for the life of the step
rather than handing to the task. A stream the job discards costs one, since
there is no file to hold open. Streams
that **slurmstepd** already read, such as those returned to **srun**,
cost nothing extra. Steps with very high task counts per node may need a larger
**LimitNOFILE** than they did before.

## Ordering

Records from one stream of one task arrive in order, though records may be
missing if the ring overflowed. Between streams only progress is promised,
never order: records from different tasks, different steps, or different nodes
may interleave in any order.

**time** is recorded when **slurmstepd** reads the output rather than
when the task wrote it, so it is not sufficient on its own to order records
from different tasks.

The streams of a step are taken from in turn rather than one at a time, so
one task writing at volume does not stop another task's output being relayed
until the first has finished. It does not give the two any particular ratio,
and a task that writes nothing for a while contributes nothing to the order.

A **job\_start** record is emitted by each node the first time that node
starts work for a relayed job, and **job\_end** when that node is finished
with it. **step\_start** and **step\_end** are emitted the same way, once
per node per relayed step, rather than once per task or per stream. A job that
is not relayed produces no records at all.