# Slurm Workload Manager - swait

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

# swait

Section: Slurm Commands (1)  
Updated: Slurm Commands  
[Index](#index)

## NAME

swait - Wait for a job's steps to complete

## SYNOPSIS

**swait** [*OPTIONS*]
[[*jobid*[\_*task*] | **s**<*sluid*>][.*stepid*]]

## DESCRIPTION

**swait** blocks until there are no running steps and no pending steps.
Use **swait** in a batch script to wait for all **--async** steps
to complete. With a
*jobid*.*stepid* target it instead waits for that one step. With
**--follow** it reports every step's completion until there are no
running or pending steps.

A *jobid*.*stepid* target that has already ended
cannot be distinguished from one that never existed; both exit 3 with no
output.

A pending step holds the wait open, whether it was submitted with
**--async** or not, so **swait** blocks until that step runs and
ends, until the pending step is cancelled, or until it is failed because its
**--step-dependency** can never be satisfied.

A step is seen only once its **srun** has reached the stepmgr. An
**srun** started in the background with **&** may not have done so
yet when **swait** starts, and **swait** then returns without
waiting for it. Use **srun** **--async**, which returns only after
the step is accepted, or wait for background **srun** commands with
the shell's **wait** builtin.

**swait** talks directly to the stepmgr; it does not poll
**slurmctld**. The target job must have stepmgr enabled (see
**REQUIREMENTS**).

The positional argument is a numeric job ID, a single array task
(e.g. *1000\_3*), or a SLUID (e.g. *s4SNKN57XZTE00*). Task ranges,
task lists, and het-job component offsets (*jobid*+*offset*) are
not supported. When the target is an array job with more than one task,
a specific task must be selected with *jobid*\_*task*. A
.*stepid* suffix may also be appended to any of these target forms,
and is mutually exclusive with **--follow**. The target must be a
regular step, not a special step (batch, extern, or interactive).

Heterogeneous (het) step *stepid*s are not supported; **swait**
exits 1, either when it parses the argument or when the stepmgr rejects
the subscribe request. See
<<https://slurm.schedmd.com/heterogeneous_jobs.html>>. However,
**--follow** reports completion of het step components. The
human-readable output does not distinguish one component from another;
use **--json** or **--yaml** and read
**step\_id.step\_het\_component**. That field is a no-val object, that
is, an object with **set**, **infinite**, and **number** fields in
which **number** is meaningful only when **set** is true. Its
**set** field is false for a step that is not a het step component.

With no positional argument, **swait** consults **SLURM\_JOB\_SLUID**
first, and falls back to **SLURM\_JOB\_ID**. This lets **swait** run
inside a batch script or interactive allocation with no arguments and
automatically wait on the enclosing job's steps.

## OPTIONS

**--follow**
:   Report every regular step as it ends, one record per completion, until
    the regular-step set drains, rather than blocking on a single event. A
    final **JobId=***jobid* **steps drained** line is printed when
    the wait ends. Mutually exclusive with a *stepid* target.

    **NOTE**: Completions that arrive close to the drain are not
    guaranteed to be reported, and the order in which they are reported is
    not guaranteed either. **swait** exits as soon as the drain
    notification arrives, so any step-completion notifications still in
    flight are lost. Wait on *jobid*.*stepid* when a specific step's
    result must not be missed.

    : **-h**, **--help** : Print help information and exit. : **--json**, **--json**=*list*, **--json**=<*data\_parser*> : Print completions as JSON, one object per line, using the default data\_parser plugin or an explicit data\_parser with parameters. *list* prints the available plugins to stdout, with a header line on stderr, and exits 0. A plugin too old to know about step completions is rejected at startup with exit 1, before the job is looked up. Unlike other Slurm commands, each completion is printed as it arrives rather than wrapped in a single response object, so no **meta**, **errors**, or **warnings** fields are emitted. Mutually exclusive with **--yaml**. : **-Q**, **--quiet** : Suppress informational messages on stderr and step-completion output on stdout. This covers the whole-set **steps drained** line as well, so stdout is empty even under **--follow**. Errors will still be displayed. Mutually exclusive with **--verbose**. : **--timeout**=*SECS* : Give up after *SECS* seconds and exit 2. The wait completes when the job's steps drain, including under **--follow**, or when a *jobid*.*stepid* target ends. *SECS* must be a non-negative integer. With no **--timeout**, or with **--timeout**=0, **swait** blocks indefinitely. : **--usage** : Print a short usage line and exit. : **-v**, **--verbose** : Increase verbosity; may be specified multiple times for more detail. Mutually exclusive with **--quiet**. At **-v**, **swait** logs **subscribed to stepmgr** *node* on stderr once the stepmgr has accepted its subscribe request. A script that must not signal a step before **swait** is listening can wait for that line. : **-V**, **--version** : Print version information and exit. : **--yaml**, **--yaml**=*list*, **--yaml**=<*data\_parser*> : Print completions as YAML documents (one per completion), using the default data\_parser plugin or an explicit data\_parser with parameters. Takes the same arguments as **--json**. Mutually exclusive with **--json**.

## OUTPUT

Under **--follow** or with a *jobid*.*stepid* target,
unless **--quiet** is given, each step completion is reported on
stdout as one line:

```
StepId=jobid.stepid code=exit:sig [reason=STATE]
StepId=jobid.stepid never-launched reason=STATE
```

**code=** carries the step's exit status and the signal that killed
it, one of which is always 0. **reason=** is added only when the step
reached a failure state such as **TIMEOUT** or **NODE\_FAIL**; a step
that ran to completion has none.

A step killed by a signal reports that signal in **code=**. It
carries a **reason=** only when it also reached a failure state: a
step killed at its time limit is in **TIMEOUT** and reports
**reason=TIMEOUT** next to the signal, while a running step killed by
**[scancel](scancel.md)**(1) reports the signal alone. A nonzero *sig*, not the
presence of **reason=**, is therefore what identifies a signaled
step. Do not read the leading **0** in **code=0:9** as success.

A step that never launched is reported as **never-launched** in place
of **code=**. Such a step is always in a failure state, so it always
carries a **reason=**, normally **FAILED** or **CANCELLED**.
A pending step whose **--step-dependency** becomes impossible to
satisfy is reported this way with **reason=FAILED**.

When the wait ends a final line is printed:

```
JobId=jobid steps drained
```

This line is printed whenever a whole-set wait completes, not just
under **--follow**. A *jobid*.*stepid* wait never prints
it: it prints its target step's line instead, or nothing at all when
the set drains without the target being reported, in which case only
the exit code carries the outcome. **--quiet** suppresses this line
too.

Nothing at all is printed when there is no wait to perform: when the job
already has no running steps and no pending steps, or
when a *jobid*.*stepid* target has already ended. **swait**
returns immediately in both cases: 0 for the whole-set wait, which
completed, and 3 for a per-step target, whose result was never
recorded.

Under **--json** or **--yaml** the same events are emitted as
one object or document per completion, carrying **step\_id**,
**exit\_code**, and **state** (a list of job-state strings, as in
**reason=** above). The drain line becomes an object whose
**step\_id.step\_id** is **entire** and which has no **exit\_code**
or **state**.

**exit\_code** is an object carrying **status** (a list of
exit-status strings such as **SUCCESS**, **ERROR**, **SIGNALED**,
or **PENDING**, which are not the **state** values above),
**return\_code**, and **signal** (an object with **id**
and **name**). A step that never launched has **PENDING** in
**status** and an unset **return\_code**, which is what distinguishes
it from a step that exited 0.

## REQUIREMENTS

The target job must have stepmgr enabled, either site-wide via
**SlurmctldParameters=enable\_stepmgr** in **[slurm.conf](slurm.conf.md)**(5), or
per-job via **--stepmgr** to **[salloc](salloc.md)**(1)/**[sbatch](sbatch.md)**(1).
This can be verified with **scontrol show job <jobid>**; look for
**StepMgrEnabled=Yes**. Against a job without it, **swait** exits 1
with **does not have stepmgr enabled** rather than waiting.

A *jobid*.*stepid* target and **--follow** additionally
require the job's stepmgr, which runs in the job's extern
**[slurmstepd](slurmstepd.md)**(8) on the job's **BatchHost** (visible in
**scontrol show job**), to be Slurm 26.11 or newer.
Against an older stepmgr the subscribe request fails and **swait**
exits 1; it does not fall back to a whole-set wait. Note that
**[slurmd](slurmd.md)**(8) may already be upgraded while a running job's
**[slurmstepd](slurmstepd.md)**(8) is not, so the batch host's package version is not
on its own sufficient.

At most 64 **swait** processes may be subscribed to one job at a time.
Beyond that **swait** exits 1 with **subscriber slots full**.

The target job must already be running. **swait** does not wait for a
job to start; against a **PENDING** job it exits 1 with
**is still pending**.

## ENVIRONMENT VARIABLES

Some **swait** options may be set via environment variables. These
environment variables, along with their corresponding options, are listed below.
(Note: Command line options will always override these settings.)

**SLURM\_JOB\_SLUID**
:   Used to identify the job to monitor when no positional argument is given.
    Takes precedence over **SLURM\_JOB\_ID**.

    : **SLURM\_JOB\_ID** : Used to identify the job to monitor when no positional argument is given and **SLURM\_JOB\_SLUID** is not set. Also used, together with **SLURM\_ARRAY\_JOB\_ID** and **SLURM\_ARRAY\_TASK\_ID**, to confirm that **SLURM\_STEPMGR** describes the target array task. : **SLURM\_STEPMGR** : Hostname of the job's stepmgr. When it is set and the target job matches the job described by the environment, **swait** contacts that host directly and never queries **slurmctld**. Otherwise **swait** looks the stepmgr up through the controller. : **SLURM\_ARRAY\_JOB\_ID** : Array master job ID of the enclosing job. Used together with **SLURM\_ARRAY\_TASK\_ID** to confirm that **SLURM\_STEPMGR** describes the target array task. : **SLURM\_ARRAY\_TASK\_ID** : Array task offset of the enclosing job. See **SLURM\_ARRAY\_JOB\_ID**. : **SLURM\_CONF** : Location of the Slurm configuration file.

## EXIT STATUS

**0**
:   The wait completed: the step set drained, or the target step ended and
    was reported. This reflects only that the wait completed, not a
    *jobid*.*stepid* target's own result; see **code=** in the
    completion output (or **exit\_code**/**state** under
    **--json**/**--yaml**) for the step's actual outcome.

    : **1** : **swait** encountered an error. : **2** : **--timeout** elapsed before the wait completed. : **3** : The step set drained without the *jobid*.*stepid* target being reported: no step with that ID exists in the job, or it ended and was reaped before **swait** subscribed. No result was recorded, so no completion is printed. Use **[sacct](sacct.md)**(1) to retrieve the step's exit code after the fact. Only returned for a per-step target.

## EXAMPLES

Run multiple async steps from a batch script and block on them. The
**--stepmgr** flag may be omitted if stepmgr is enabled site-wide.

```
#!/bin/bash
#SBATCH -n 16
#SBATCH --stepmgr
srun --async -n 8 ./solve_a
srun --async -n 8 ./solve_b
swait
```

Wait on one step and read its exit code. **srun** **--async**
**--parsable** prints the new step's *jobid*.*stepid*, which
is the target **swait** expects.

```
#!/bin/bash
#SBATCH -n 16
#SBATCH --stepmgr
step=$(srun --async --parsable -n 8 ./solve_a)
srun --async -n 8 ./solve_b
swait "$step"   # prints solve_a's exit code if it is still running
swait           # then wait for everything else
```

If **./solve\_a** ends before **swait** subscribes, nothing is printed
and **swait** exits 3; see the note on already-ended step targets in
**DESCRIPTION**.

Follow every step as it ends.

```
$ swait --follow 1234
StepId=1234.0 code=0:0
StepId=1234.1 code=7:0
JobId=1234 steps drained
```

Read one step's result as JSON. The wait must be started while the step
is still running, so take the target from **srun** **--async**
**--parsable** rather than waiting for the drain first. Each
completion is a single-line object in which **step\_id** and
**exit\_code** are themselves objects, and **return\_code** is a
no-val object under the default data\_parser, so read its **number**
field.

```
step=$(srun --async --parsable -n 8 ./solve_a)
swait --json "$step" |
        jq '.exit_code.return_code | if .set then .number else null end'
```

For a step that was signaled or that never launched, **return\_code**
is unset. Under the default data\_parser an unset no-val object still
carries **number**=0, so **set** must be tested before **number**
is trusted; otherwise such a step is indistinguishable from an exit of
0. Read **exit\_code.status** and **exit\_code.signal.name** to tell
those cases apart.

A *jobid*.*stepid* wait emits at most one object. If the set
drains without the target ever being reported, nothing is emitted at
all and **swait** exits 3, so read the exit code rather than waiting
for a terminator. The **entire** drain object is emitted only under
**--follow** or for a whole-set wait.

## COPYING

Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved

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

**[sacct](sacct.md)**(1), **[salloc](salloc.md)**(1), **[sbatch](sbatch.md)**(1), **[scancel](scancel.md)**(1),
**[scontrol](scontrol.md)**(1), **[squeue](squeue.md)**(1), **[srun](srun.md)**(1), **[slurm.conf](slurm.conf.md)**(5),
**[slurmd](slurmd.md)**(8), **[slurmstepd](slurmstepd.md)**(8)

---



## Index

[NAME](#lbAB): [SYNOPSIS](#lbAC): [DESCRIPTION](#lbAD): [OPTIONS](#lbAE): [OUTPUT](#lbAF): [REQUIREMENTS](#lbAG): [ENVIRONMENT VARIABLES](#lbAH): [EXIT STATUS](#lbAI): [EXAMPLES](#lbAJ): [COPYING](#lbAK): [SEE ALSO](#lbAL)

---

This document was created by
*man2html* using the manual pages.  
Time: 20:23:16 GMT, November 24, 2026