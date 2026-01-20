# Source: https://slurm.schedmd.com/job_state_codes.html

# Job State Codes

Each job in the Slurm system has a state assigned to it. How the job state is
displayed depends on the method used to identify the state.

## Overview

In the Slurm code, there are **base states** and **state flags**.
Each job has a base state and may have additional state flags set. When using
the [REST API](rest_quickstart.html), both the base state and current
flag(s) will be returned.

When the [squeue](squeue.html) and [sacct](sacct.html)
command report a job state, they represent it as a single state. Both will
recognize all base states but not all state flags. If a recognized flag is
present, it will be reported instead of the base state. Refer to the relevant
command documentation for details.

This page represents all job codes and flags that are represented in the
code. The names provided are the string representations that are used in
user-facing output. For most, the names used in the code are identical, with
`JOB_` at the start.
For more visibility into the job states and flags, set
`DebugFlags=TraceJobs` and `SlurmctldDebug=verbose`
(or higher) in [slurm.conf](slurm.conf.html).

## Job states

Each job known to the system will have one of the following states:

|  |  |
| --- | --- |
| **Name** | **Description** |
| `BOOT_FAIL` | terminated due to node boot failure |
| `CANCELLED` | cancelled by user or administrator |
| `COMPLETED` | completed execution successfully; finished with an [exit code](job_exit_code.html) of zero on all nodes |
| `DEADLINE` | terminated due to reaching the latest start time that allows the job to reach its deadline given its TimeLimit |
| `FAILED` | completed execution unsuccessfully; non-zero [exit code](job_exit_code.html) or other failure condition |
| `NODE_FAIL` | terminated due to node failure |
| `OUT_OF_MEMORY` | experienced out of memory error |
| `PENDING` | queued and waiting for initiation; will typically have a [reason code](job_reason_codes.html) specifying why it has not yet started |
| `PREEMPTED` | terminated due to [preemption](preempt.html); may transition to another state based on the configured PreemptMode and job characteristics |
| `RUNNING` | allocated resources and executing |
| `SUSPENDED` | allocated resources but execution suspended, such as from [preemption](preempt.html) or a [direct request](scontrol.html#OPT_suspend) from an authorized user |
| `TIMEOUT` | terminated due to reaching the time limit, such as those configured in [slurm.conf](slurm.conf.html) or specified for the individual job |

## Job flags

Jobs may have additional flags set:

|  |  |
| --- | --- |
| **Name** | **Description** |
| `COMPLETING` | job has finished or been cancelled and is performing cleanup tasks, including the [epilog](prolog_epilog.html) script if present |
| `CONFIGURING` | job has been allocated nodes and is waiting for them to boot or reboot |
| `EXPEDITING` | the job is immediately eligible for scheduling with the highest possible priority |
| `LAUNCH_FAILED` | failed to launch on the chosen node(s); includes [prolog](prolog_epilog.html) failure and other failure conditions |
| `POWER_UP_NODE` | job has been allocated powered down nodes and is waiting for them to boot |
| `RECONFIG_FAIL` | node configuration for job failed |
| `REQUEUED` | job is being requeued, such as from [preemption](preempt.html) or a [direct request](scontrol.html#OPT_requeue) from an authorized user |
| `REQUEUE_FED` | requeued due to conditions of its sibling job in a [federated](federation.html) setup |
| `REQUEUE_HOLD` | same as `REQUEUED` but will not be considered for scheduling until it is [released](scontrol.html#OPT_release) |
| `RESIZING` | the size of the job is changing; prevents conflicting job changes from taking place |
| `RESV_DEL_HOLD` | held due to deleted reservation |
| `REVOKED` | revoked due to conditions of its sibling job in a [federated](federation.html) setup |
| `SIGNALING` | outgoing signal to job is pending |
| `SPECIAL_EXIT` | same as `REQUEUE_HOLD` but used to identify a [special situation](scontrol.html#OPT_State) that applies to this job |
| `STAGE_OUT` | staging out data ([burst buffer](burst_buffer.html)) |
| `STOPPED` | received SIGSTOP to suspend the job without releasing resources |
| `UPDATE_DB` | sending an update about the job to the database |