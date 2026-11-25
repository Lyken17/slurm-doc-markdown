# Slurm Workload Manager - resctrl.yaml

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

# resctrl.yaml

Section: Slurm Configuration File (5)  
Updated: Slurm Configuration File  
[Index](#index)

## NAME

resctrl.yaml - Slurm configuration file for the task/resctrl plugin

## DESCRIPTION

**resctrl.yaml** is a YAML-formatted configuration file that defines the
Linux resource control (resctrl) groups that the **task/resctrl** plugin
creates on the compute nodes and confines the steps to.
A resctrl group is a directory under /sys/fs/resctrl whose **schemata** file
limits the memory bandwidth and the cache portions available to the tasks
placed in it.

The plugin uses three groups with fixed names, and this file must define all of
them: **cpu\_only**, **gpu\_one\_per\_socket**, and **gpu\_two\_per\_socket**.
Every step of a job is placed in the group matching the job on that node.
Jobs without GPUs go to **cpu\_only**, jobs with GPUs go to
**gpu\_one\_per\_socket** or **gpu\_two\_per\_socket** according to the most GPUs
attached to any one socket.
Exclusive jobs that own the whole node are left in the resctrl group where
slurmd runs, normally the unrestricted root group.
The limits of a group apply to the group, not to each job, except that Intel
without mba\_MBps throttles each core.

The file is read by slurmd when **TaskPlugin** includes **task/resctrl**,
and must be located in the same directory as **slurm.conf**.
On a node without kernel support for resctrl, without this file, or where the
resctrl filesystem cannot be mounted on /sys/fs/resctrl, slurmd does not manage
the groups.
Otherwise slurmd mounts the resctrl filesystem and sets up the groups with
their **schemata**.
If the file is invalid or cannot be applied, slurmd fails to start or to
reconfigure.

Changes take effect after **scontrol reconfigure** or a restart of slurmd,
which rewrites the **schemata** of the groups.
A change to **mount\_options** is the exception; see below.
The new limits apply at once to the jobs already running in the groups.
Slurm never removes the groups.
Once this file is removed, new steps are no longer placed in them and the
directories keep their last limits.

Additional details are available in the resctrl page:
<<https://slurm.schedmd.com/resctrl.html>>

## PARAMETERS

The file is a YAML dictionary with the following attributes.
Unknown attributes are ignored and reported only at the debug log level, so a
misspelled attribute is not applied and causes no error.

**groups**
:   : A list of groups. This attribute is required. Each group is a YAML dictionary containing:

    : **name** : : The name of the group, one of **cpu\_only**, **gpu\_one\_per\_socket**, or **gpu\_two\_per\_socket**. Each must appear exactly once. This attribute is required. : **schemata** : The contents written to the **schemata** file of the group, one resource per line, exactly as the kernel expects them. Resources and domains left out keep their current values. A resource or a domain the node does not have is rejected, which is fatal to slurmd, so the file must suit every node that reads it. The resources and domains of the node are listed in /sys/fs/resctrl/schemata, and the meaning of the values depends on the hardware and is described in /sys/fs/resctrl/info and in the kernel resctrl documentation. On most systems the memory bandwidth resource ("MB") takes a percentage per memory domain, rounded up to a multiple of /sys/fs/resctrl/info/MB/bandwidth\_gran. A value below /sys/fs/resctrl/info/MB/min\_bandwidth is rejected, not raised. **NOTE**: The value is a ceiling, not a reservation, and the values of different groups may add up to more than 100 percent. This attribute is required.

    : **mount\_options** : Options of the resctrl filesystem, for example "mba\_MBps", used when Slurm mounts it. Ignored when the filesystem is already mounted. Slurm never unmounts it, so a change takes effect only once /sys/fs/resctrl has been unmounted while no jobs run, for example by rebooting the node. Unset by default. **NOTE**: Some options change how the kernel interprets **schemata** values. With "mba\_MBps", where the kernel supports it, "MB" is expressed in MiBps instead of as a percentage.

## EXAMPLE

For nodes whose /sys/fs/resctrl/schemata lists the MB domains 0 and 1:

```
groups:
  # Jobs without GPUs
  - name: cpu_only
    schemata: |
      MB:0=30;1=30
  # Jobs with at most one GPU on a socket
  - name: gpu_one_per_socket
    schemata: |
      MB:0=35;1=35
  # Jobs with two or more GPUs on a socket
  - name: gpu_two_per_socket
    schemata: |
      MB:0=70;1=70
```

## COPYING

Copyright (C) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.

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

**[gres.conf](gres.conf.md)**(5), **[slurm.conf](slurm.conf.md)**(5), **[slurmd](slurmd.md)**(8)

---



## Index

[NAME](#lbAB): [DESCRIPTION](#lbAC): [PARAMETERS](#lbAD): [EXAMPLE](#lbAE): [COPYING](#lbAF): [SEE ALSO](#lbAG)

---

This document was created by
*man2html* using the manual pages.  
Time: 20:23:17 GMT, November 24, 2026