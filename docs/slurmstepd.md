# Slurm Workload Manager - slurmstepd

# [Slurm Workload Manager](/)

[SchedMD](https://www.schedmd.com/)

## Navigation

[Slurm Workload Manager](/)

Version 25.11

* About

  + [Overview](overview.md)
  + [Release Notes](release_notes.md)
* Using

  + [Documentation](documentation.md)
  + [FAQ](faq.md)
  + [Publications](https://www.schedmd.com/publications/)
* Installing

  + [Download](https://www.schedmd.com/download-slurm/)
  + [Related Software](related_software.md)
  + [Installation Guide](quickstart_admin.md)
* Getting Help

  + [Mailing Lists](mail.md)
  + [Support and Training](https://www.schedmd.com/slurm-support/our-services/)
  + [Troubleshooting](troubleshoot.md)

# slurmstepd

Section: Slurm Component (8)  
Updated: Slurm Component  
[Index](#index)

## NAME

slurmstepd - The job step manager for Slurm.

## SYNOPSIS

**slurmstepd**


## DESCRIPTION

**slurmstepd** is a job step manager for Slurm.
It is spawned by the **slurmd** daemon when a job step is launched
and terminates when the job step does.
It is responsible for managing input and output (stdin, stdout and stderr)
for the job step along with its accounting and signal processing.
**slurmstepd** should not be initiated by users or system administrators.

## ENVIRONMENT VARIABLES:

The following environment variables can be used to override settings
compiled into slurmstepd.

**SLURM\_DEBUG\_FLAGS**
:   Specify debug flags for slurmstepd to use. See DebugFlags in the
    **[slurm.conf](slurm.conf.md)**(5) man page for a full list of flags. The environment
    variable takes precedence over the setting in the slurm.conf.

## SIGNALS

**SIGINT SIGTERM SIGQUIT**
:   **slurmstepd** will shutdown cleanly.

    : **SIGPROF** : Logs connection manager state when debug level is at least info. : **SIGTSTP SIGPIPE SIGUSR1 SIGUSR2 SIGALRM SIGHUP** : These signals are explicitly ignored.

## COPYING

Copyright (C) 2006 The Regents of the University of California.
Copyright (C) 2010-2022 SchedMD LLC.
Produced at Lawrence Livermore National Laboratory (cf, DISCLAIMER).
CODE-OCEC-09-009. All rights reserved.

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

**[slurmd](slurmd.md)**(8)

---



## Index

[NAME](#lbAB): [SYNOPSIS](#lbAC): [DESCRIPTION](#lbAD): [ENVIRONMENT VARIABLES:](#lbAE): [SIGNALS](#lbAF): [COPYING](#lbAG): [SEE ALSO](#lbAH)

---

This document was created by
*man2html* using the manual pages.  
Time: 20:36:11 GMT, January 15, 2026