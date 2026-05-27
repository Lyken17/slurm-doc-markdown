# Slurm Workload Manager - swait

# [Slurm Workload Manager](/)

[SchedMD](https://www.schedmd.com/)

## Navigation

[Slurm Workload Manager](/)

Version 26.05

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

swait - Block until a job's running steps and pending --async steps complete

## SYNOPSIS

**swait** [*OPTIONS*] [*jobid*[\_*task*] | **s**<*sluid*>]

## DESCRIPTION

**swait** blocks until there are no running steps and no pending
**--async** steps. Use **swait** in a batch script to wait for
all **--async** steps to complete.

**swait** talks directly to the stepmgr; it does not poll
**slurmctld**. The target job must have stepmgr enabled (see
**REQUIREMENTS**).

The positional argument is a numeric job ID, a single array task
(e.g. *1000\_3*), or a SLUID (e.g. *s4SNKN57XZTE00*). Task ranges,
task lists, and het-job component offsets (*jobid*+*offset*) are
not supported. When the target is an array job with more than one task,
a specific task must be selected with *jobid*\_*task*.

With no positional argument, **swait** consults **SLURM\_JOB\_SLUID**
first, and falls back to **SLURM\_JOB\_ID**. This lets **swait** run
inside a batch script or interactive allocation with no arguments and
automatically wait on the enclosing job's steps.

## OPTIONS

**-h**, **--help**
:   Print help information and exit.

    : **-Q**, **--quiet** : Suppress informational messages from appearing on stderr. Errors will still be displayed. Mutually exclusive with **--verbose**. : **--timeout**=*SECS* : Wait at most *SECS* seconds for the job's steps to drain, then exit 1. *SECS* must be a non-negative integer. With no **--timeout**, or with **--timeout**=0, **swait** blocks indefinitely until the steps drain. : **--usage** : Print a short usage line and exit. : **-v**, **--verbose** : Increase verbosity; may be specified multiple times for more detail. Mutually exclusive with **--quiet**. : **-V**, **--version** : Print version information and exit.

## REQUIREMENTS

The target job must have stepmgr enabled, either site-wide via
**SlurmctldParameters=enable\_stepmgr** in **[slurm.conf](slurm.conf.md)**(5), or
per-job via **--stepmgr** to **[salloc](salloc.md)**(1)/**[sbatch](sbatch.md)**(1).
This can be verified with **scontrol show job <jobid>**; look for
**StepMgrEnabled=Yes**.

## ENVIRONMENT VARIABLES

Some **swait** options may be set via environment variables. These
environment variables, along with their corresponding options, are listed below.
(Note: Command line options will always override these settings.)

**SLURM\_JOB\_SLUID**
:   Used to identify the job to monitor when no positional argument is given.
    Takes precedence over **SLURM\_JOB\_ID**.

    : **SLURM\_JOB\_ID** : Used to identify the job to monitor when no positional argument is given and **SLURM\_JOB\_SLUID** is not set. : **SLURM\_CONF** : Location of the Slurm configuration file.

## EXIT STATUS

**0**
:   : There are no running steps, and no pending async steps.

    : **1** : : **--timeout** elapsed before steps completed. : **2** : : **swait** encountered an error.

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

**swait** is only for **--async** steps; if a script merely
backgrounds **srun** commands with the shell, the shell's *wait*
builtin already covers that case and **swait** is not needed. The
exception is when a script mixes both: run **swait** followed by
*wait* so that the stepmgr's pending work and the shell's
background processes have both finished:

```
#!/bin/bash
#SBATCH -n 16
#SBATCH --stepmgr
srun -n 8 ./solve_a &
srun --async -n 8 ./solve_b
swait
wait
```

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
**[scontrol](scontrol.md)**(1), **[squeue](squeue.md)**(1), **[srun](srun.md)**(1), **[slurm.conf](slurm.conf.md)**(5)

---



## Index

[NAME](#lbAB): [SYNOPSIS](#lbAC): [DESCRIPTION](#lbAD): [OPTIONS](#lbAE): [REQUIREMENTS](#lbAF): [ENVIRONMENT VARIABLES](#lbAG): [EXIT STATUS](#lbAH): [EXAMPLES](#lbAI): [COPYING](#lbAJ): [SEE ALSO](#lbAK)

---

This document was created by
*man2html* using the manual pages.  
Time: 20:52:42 GMT, May 26, 2026