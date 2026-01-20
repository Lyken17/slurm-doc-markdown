# Source: https://slurm.schedmd.com/scancel.html

# scancel

Section: Slurm Commands (1)  
Updated: Slurm Commands  
[Index](#index)

## NAME

scancel - Used to signal jobs or job steps that are under the control of Slurm.

## SYNOPSIS

**scancel** [*OPTIONS*...] [*job\_id*[\_*array\_id*][.*step\_id*]] [*job\_id*[\_*array\_id*][.*step\_id*]...]

## DESCRIPTION

**scancel** is used to signal or cancel jobs, job arrays or job steps.
An arbitrary number of jobs or job steps may be signaled using job
specification filters or a space separated list of specific job and/or
job step IDs.
If the job ID of a job array is specified with an array ID value and the job
associated with the array ID value has been split from the array, then only that
job array element will be cancelled.
If the job ID of a job array is specified without an array ID value or the
array ID value corresponds to a job that has not been split from the array,
then all job array elements will be cancelled.
While a heterogeneous job is in a PENDING state, only the entire job can be
cancelled rather than its individual components.
A request to cancel an individual component of a heterogeneous job while in
a PENDING state will return an error.
After the job has begun execution, an individual component can be cancelled
except for component zero. If component zero is cancelled, the whole het job is
cancelled.
A job or job step can only be signaled by the owner of that job or user root.
If an attempt is made by an unauthorized user to signal a job or job step, an
error message will be printed and the job will not be signaled.

## OPTIONS

**-A**, **--account**=*account*
:   Restrict the scancel operation to jobs under this charge account.

    : **--admin-comment**=*comment* : Set the AdminComment on the job while canceling jobs. User must have Administrator privileges on the system. : **-b**, **--batch** : By default, signals other than SIGKILL are not sent to the batch step (the shell script). With this option **scancel** signals only the batch step, but not any other steps. This is useful when the shell script has to trap the signal and take some application defined action. Most shells cannot handle signals while a command is running (i.e. is a child process of the batch step), so the shell needs to wait until the command ends to then handle the signal. Children of the batch step are not signaled with this option. If this is desired, use **-f**, **--full** instead. **NOTE**: If used with **-f**, **--full**, this option is ignored. **NOTE**: This option is not applicable if *step\_id* is specified. **NOTE**: The shell itself may exit upon receipt of many signals. You may avoid this by explicitly trap signals within the shell script (e.g. "trap <arg> <signals>"). See the shell documentation for details. : **-M**, **--clusters**=<*string*> : Cluster to issue commands to. Implies **--ctld**. Note that the **slurmdbd** must be up for this option to work properly, unless running in a federation with **FederationParameters=fed\_display** configured. : **--ctld** : If this option is not used with **--interactive**, **--sibling**, federated job ids, or specific step ids, then this issues a single request to the slurmctld to signal all jobs matching the specified filters. This greatly improves the performance of slurmctld and scancel. Otherwise, this option causes scancel to send each job signal request to the slurmctld daemon rather than directly to the slurmd daemons, which increases overhead, but offers better fault tolerance. **--ctld** is the default behavior on when the **--clusters** option is used. : **-c**, **--cron** : Confirm request to cancel a job submitted by scrontab. This option only has effect with the "explicit\_scancel" option is set in **ScronParameters**. : **-f**, **--full** : By default, signals other than SIGKILL are not sent to the batch step (the shell script). With this option **scancel** also signals the batch script and its children processes. Most shells cannot handle signals while a command is running (i.e. is a child process of the batch step), so the shell needs to wait until the command ends to then handle the signal. Unlike **-b**, **--batch**, children of the batch step are also signaled with this option. **NOTE**: srun steps are also children of the batch step, so steps are also signaled with this option. : **--help** : Print a help message describing all **scancel** options. : **-H**, **--hurry** : Do not stage out any burst buffer data. : **-i**, **--interactive** : Interactive mode. Confirm each job\_id.step\_id before performing the cancel operation. : **-n**, **--jobname**=*job\_name*, **--name**=*job\_name* : Restrict the scancel operation to jobs with this job name. : **--me** : Restrict the scancel operation to jobs owned by the current user. **-w**, **--nodelist=***host1,host2,...* : Cancel any jobs using any of the given hosts. The list may be specified as a comma-separated list of hosts, a range of hosts (host[1-5,7,...] for example), or a filename. The host list will be assumed to be a filename only if it contains a "/" character. : **-p**, **--partition**=*partition\_name* : Restrict the scancel operation to jobs in this partition. : **-q**, **--qos**=*qos* : Restrict the scancel operation to jobs with this quality of service. : **-Q**, **--quiet** : Do not report an error if the specified job is already completed. This option is incompatible with the **--verbose** option. : **-R**, **--reservation**=*reservation\_name* : Restrict the scancel operation to jobs with this reservation name. : **--sibling**=*cluster\_name* : Remove an active sibling job from a federated job. : **-s**, **--signal**=*signal\_name* : The name or number of the signal to send. If this option is not used the specified job or step will be terminated. : **-t**, **--state**=*job\_state\_name* : Restrict the scancel operation to jobs in this state. *job\_state\_name* may have a value of either "PENDING", "RUNNING" or "SUSPENDED". : **--usage** : Print a brief help message listing the **scancel** options. : **-u**, **--user**=*user\_name* : Restrict the scancel operation to jobs owned by the given user. : **-v**, **--verbose** : Print additional logging. Multiple v's increase logging detail. This option is incompatible with the **--quiet** option. : **-V**, **--version** : Print the version number of the scancel command. : **--wckey**=*wckey* : Restrict the scancel operation to jobs using this workload characterization key.

## ARGUMENTS

*job\_id*
:   The Slurm job ID to be signaled.

    : *step\_id* : The step ID of the job step to be signaled. If not specified, the operation is performed at the level of a job. If neither **--batch** nor **--signal** are used, the entire job will be terminated. When **--batch** is used, the batch shell processes will be signaled. The child processes of the shell will not be signaled by Slurm, but the shell may forward the signal. When **--batch** is not used but **--signal** is used, then all job steps will be signaled, but the batch script itself will not be signaled.

## PERFORMANCE

When executing **scancel** without the **--ctld** option; or with the
**--ctld** option and **--interactive**, **--sibling**, or specific
step ids; a remote procedure call is sent to **slurmctld** to get all the
jobs. **scancel** then sends a signal job remote procedure call for each job
that matches the requested filters.

When executing **scancel** with the **--ctld** option and without
**--interactive**, **--sibling**, or specific step ids, a single
remote procedure call is sent to **slurmctld** to signal all jobs matching
the requested filters. It is therefore recommended to use the **--ctld**
option in order to reduce the number of remote procedure calls sent to the
**slurmctld**.

If enough calls from **scancel** or other Slurm client commands that send
remote procedure calls to the **slurmctld** daemon come in at once, it can
result in a degradation of performance of the **slurmctld** daemon, possibly
resulting in a denial of service.

Do not run **scancel** or other Slurm client commands that send remote
procedure calls to **slurmctld** from loops in shell scripts or other
programs. Ensure that programs limit calls to **scancel** to the minimum
necessary for the information you are trying to gather.

## ENVIRONMENT VARIABLES

Some **scancel** options may be set via environment variables. These
environment variables, along with their corresponding options, are listed below.
(Note: Command line options will always override these settings.)

**SCANCEL\_ACCOUNT**
:   **-A**, **--account**=*account*

    : **SCANCEL\_BATCH** : **-b, --batch** : **SCANCEL\_CTLD** : **--ctld** : **SCANCEL\_CRON** : **-c, --cron** : **SCANCEL\_FULL** : **-f, --full** : **SCANCEL\_HURRY** : **-H**, **--hurry** : **SCANCEL\_INTERACTIVE** : **-i**, **--interactive** : **SCANCEL\_NAME** : **-n**, **--name**=*job\_name* : **SCANCEL\_PARTITION** : **-p**, **--partition**=*partition\_name* : **SCANCEL\_QOS** : **-q**, **--qos**=*qos* : **SCANCEL\_STATE** : **-t**, **--state**=*job\_state\_name* : **SCANCEL\_USER** : **-u**, **--user**=*user\_name* : **SCANCEL\_VERBOSE** : **-v**, **--verbose** : **SCANCEL\_WCKEY** : **--wckey**=*wckey* : **SLURM\_CONF** : The location of the Slurm configuration file. : **SLURM\_CLUSTERS** : **-M**, **--clusters** : **SLURM\_DEBUG\_FLAGS** : Specify debug flags for scancel to use. See DebugFlags in the **[slurm.conf](slurm.conf.html)**(5) man page for a full list of flags. The environment variable takes precedence over the setting in the slurm.conf.

## NOTES

If multiple filters are supplied (e.g. **--partition** and **--name**)
only the jobs satisfying all of the filtering options will be signaled.

Cancelling a job step will not result in the job being terminated.
The job must be cancelled to release a resource allocation.

To cancel a job, invoke **scancel** without --signal option. This
will send first a SIGCONT to all steps to eventually wake them up followed by
a SIGTERM, then wait the KillWait duration defined in the slurm.conf file
and finally if they have not terminated send a SIGKILL. This gives
time for the running job/step(s) to clean up.

If a signal value of "KILL" is sent to an entire job, this will cancel
the active job steps but not cancel the job itself.

## AUTHORIZATION

When using SlurmDBD, users who have an AdminLevel defined (Operator
or Admin) and users who are account coordinators are given the
authority to invoke scancel on other users jobs.

## EXAMPLES

: Send SIGTERM to steps 1 and 3 of job 1234:: : ``` $ scancel --signal=TERM 1234.1 1234.3 ``` Cancel job 1234 along with all of its steps:: : ``` $ scancel 1234 ``` Send SIGKILL to all steps of job 1235, but do not cancel the job itself:: : ``` $ scancel --signal=KILL 1235 ``` Send SIGUSR1 to the batch shell processes of job 1236:: : ``` $ scancel --signal=USR1 --batch 1236 ``` Cancel all pending jobs belonging to user "bob" in partition "debug":: : ``` $ scancel --state=PENDING --user=bob --partition=debug ``` Cancel only array ID 4 of job array 1237: : ``` $ scancel 1237_4 ```

## COPYING

Copyright (C) 2002-2007 The Regents of the University of California.
Produced at Lawrence Livermore National Laboratory (cf, DISCLAIMER).
  
Copyright (C) 2008-2011 Lawrence Livermore National Security.
  
Copyright (C) 2010-2022 SchedMD LLC.

This file is part of Slurm, a resource management program.
For details, see <<https://slurm.schedmd.com/>>.

Slurm is free software; you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free
Software Foundation; either version 2 of the License, or (at your option)
any later version.

Slurm is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
details.

## SEE ALSO

**slurm\_kill\_job** (3), **slurm\_kill\_job\_step** (3)

---



## Index

[NAME](#lbAB): [SYNOPSIS](#lbAC): [DESCRIPTION](#lbAD): [OPTIONS](#lbAE): [ARGUMENTS](#lbAF): [PERFORMANCE](#lbAG): [ENVIRONMENT VARIABLES](#lbAH): [NOTES](#lbAI): [AUTHORIZATION](#lbAJ): [EXAMPLES](#lbAK): [COPYING](#lbAL): [SEE ALSO](#lbAM)

---

This document was created by
*man2html* using the manual pages.  
Time: 20:36:11 GMT, January 15, 2026