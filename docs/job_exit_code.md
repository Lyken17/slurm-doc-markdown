# Slurm Workload Manager - Job Exit Codes

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

# Job Exit Codes

A job's exit code (also called its completion code) is captured by
Slurm and saved as part of the job record. It combines two values: the
*exit status*, which is what the job's process returned, and the
number of the signal that terminated it, if any. Slurm displays the pair as
**ExitCode**=<*status*>:<*signal*>.

For sbatch jobs, the exit code that is captured is the exit status of
the batch script. For salloc jobs, the exit code will be the return value of
the exit call that terminates the salloc session. For srun, the exit
code will be the return value of the command that srun executes.

Any non-zero exit code will be assumed to be a job failure and will
result in a Job State of FAILED with a Reason of
"NonZeroExitCode".

The exit status is an 8-bit unsigned number ranging between 0 and
255. While it is possible for a job to return a negative exit status,
Slurm will display it as an unsigned value in the 0 - 255 range.

A job's return code is kept separate from its exit code so that a
failure Slurm itself caused can be told apart from the job's own exit
status. The return code is a 32-bit unsigned number holding a Slurm error
code, and is 0 when no Slurm error code applies.

## Job Step Exit Codes

When a job contains multiple job steps, the exit code of each
executable invoked by srun is saved individually to the job step
record.

A step's exit code is derived from its tasks rather than taken from any
single one. On each node, if a task was killed by a signal, or called
`PMI_Abort()`, that task's status is reported for the node;
otherwise the node reports the highest exit status of its tasks. The step
then reports the highest of its nodes' statuses, so an exit status on one
node can hide a signal on another. Tasks that Slurm killed on the step's
behalf (the surviving tasks after a **scancel** or a step time limit)
are not counted, unless every task was killed that way, in which case the
step reports the status of its first task. A plain
**scancel** of a running step is that case, so such a step reports the
signal that killed it rather than nothing. An out-of-memory condition
takes precedence over any exit status.

## Signaled Jobs

When a job or step is sent a signal that causes its termination,
Slurm also captures the signal number and saves it to the job or step
record.

## Slurm Return Codes

When Slurm itself fails a job and the failure carries a Slurm error
code, that code is recorded as the job's Slurm return code, or **SlurmRC**. A
non-zero return code therefore means Slurm recorded a failure of its own
against the job, rather than simply reporting how the job's processes
exited, and the error code says why. It does not on its own mean Slurm
terminated the job, because a job that ran to completion can still carry
one.

A return code of 0 means no Slurm error code was recorded. It says
nothing about whether the job succeeded, which is what the exit code
reports, and on its own it does not mean the job ran to completion:
Slurm fails jobs for reasons that carry no error code of their own,
such as reaching a deadline or having their partition removed while they
run. Those are reported through the job's state and reason.

Return codes are recorded for jobs only. A job step has an exit code
and a signal, but no return code.

Return codes are Slurm error numbers. To turn one into a message, use
**scontrol errnumstr**:

```
$ scontrol errnumstr 4021
Slurmd could not connect IO
```

A job that Slurm fails with a return code is reported as
**ExitCode=1:0**. If the job had already exited with a non-zero status
before Slurm recorded the error, the job keeps that exit code instead.
Because a job can also exit 1 on its own, **ExitCode=1:0** does not
identify a Slurm failure: check **SlurmRC**, and the job's state and
reason for failures that carry no error code.

**RequeueExit** and **RequeueExitHold** match against a job's
return code when it has one, and against its exit status otherwise. This
allows jobs to be requeued for a specific Slurm failure rather than for
any failure. See [RequeueExit](slurm.conf.md#OPT_RequeueExit)
and [RequeueExitHold](slurm.conf.md#OPT_RequeueExitHold) in
**slurm.conf** for details.

## Displaying Exit Codes and Signals

Slurm displays a job's exit code in the output of **scontrol show
job**, and a job step's exit code in the output of **scontrol show
step**.

When a signal was responsible for a job or step's termination, the
signal number will be displayed after the exit code, delineated by a
colon(:).

A job's Slurm return code is displayed as **SlurmRC** by
**scontrol -d show job**. It can be requested from **sacct** by including
`SlurmRC` in `--format`, or from **squeue** by
including `SlurmRC` in `--Format`:

```
sacct -j <jobid> --format=JobID,ExitCode,SlurmRC
squeue -j <jobid> --Format=JobID,SlurmRC
```

Note that **squeue** offers the field through `--Format`
only. The lowercase `--format` uses a different set of field
codes and does not accept `SlurmRC`.

## Database Job/Step Records

The Slurm control daemon sends job and step records to the Slurm
database when the Slurm accounting\_storage plugin is installed. Job
and step records sent to the Slurm db can be viewed using the
**sacct** command. The default **sacct** output contains an
ExitCode field whose format mirrors the output of **scontrol**
described above.

# Derived Exit Code and Comment String

After reading the above description of a job's exit code, one can
imagine a scenario where a central task of a batch job fails but the
script returns an exit code of zero, indicating success. In many
cases, a user may not be able to ascertain the success or failure of a
job until after they have examined the job's output files.

The job includes a "derived exit code" field.
It is initially set to the value of the highest
exit code returned by all of the job's steps (srun invocations). The
job's derived exit code is determined by the Slurm control daemon
and sent to the database when the accounting\_storage plugin is
enabled.

In addition to the derived exit code, the job record in the Slurm
database contains a comment string. This is initialized to the job's
comment string (when AccountingStoreFlags parameter in the
slurm.conf contains 'job\_comment') and can only be changed by the user.

A new option has been added to the **sacctmgr** command to
provide the user the means to modify these two fields of the job
record. No other modification to the job record is allowed. For
those who prefer a simpler command specifically designed to view and
modify the derived exit code and comment string, the
**sjobexitmod** wrapper has been created (see below).

The user now has the means to annotate a job's exit code after it
completes and provide a description of what failed. This includes the
ability to annotate a successful completion to jobs that appear to
have failed but actually succeeded.

## The sjobexitmod command

The sjobexitmod command is available to display and update the
two derived exit fields of the Slurm db's job record.
**sjobexitmod** can first be used to display the existing exit code
/ string for a job:

```
> sjobexitmod -l 123
JobID Account NNodes NodeList     State ExitCode DerivedExitCode Comment
----- ------- ------ -------- --------- -------- --------------- -------
123        lc      1     tux0 COMPLETED      0:0             0:0
```

If a change is desired, **sjobexitmod** can modify the derived fields:

```
> sjobexitmod -e 49 -r "out of memory" 123

 Modification of job 123 was successful.

> sjobexitmod -l 123
JobID Account NNodes NodeList     State ExitCode DerivedExitCode Comment
----- ------- ------ -------- --------- -------- --------------- -------
123        lc      1     tux0 COMPLETED      0:0            49:0 out of memory
```

The existing **sacct** command also supports the two new derived
exit fields:

```
> sacct -X -j 123 -o JobID,NNodes,State,ExitCode,DerivedExitcode,Comment
JobID   NNodes      State ExitCode DerivedExitCode        Comment
------ ------- ---------- -------- --------------- --------------
123          1  COMPLETED      0:0            49:0  out of memory
```