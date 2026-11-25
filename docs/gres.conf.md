# Slurm Workload Manager - gres.conf

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

# gres.conf

Section: Slurm Configuration File (5)  
Updated: Slurm Configuration File  
[Index](#index)

## NAME

gres.conf - Slurm configuration file for Generic RESource (GRES) management.

## DESCRIPTION

**gres.conf** is an ASCII file which describes the configuration
of Generic RESource(s) (GRES) on each compute node.
If the GRES information in the slurm.conf file does not fully describe those
resources, then a gres.conf file should be included on each compute node. For
cloud nodes, a gres.conf file that includes all the cloud nodes must be on
all cloud nodes and the controller. The file will always be located in the same
directory as **slurm.conf**.

If the GRES information in the slurm.conf file fully describes those resources
(i.e. no "Cores", "File" or "Links" specification is required for that GRES
type or that information is automatically detected), that information may be
omitted from the gres.conf file and only the configuration information in the
slurm.conf file will be used.
The gres.conf file may be omitted completely if the configuration information
in the slurm.conf file fully describes all GRES.

If using the **gres.conf** file to describe the resources available to nodes,
the first parameter on the line should be **NodeName**. If configuring
Generic Resources without specifying nodes, the first parameter on the line
should be **Name**.

Parameter names are case insensitive.
Any text following a "#" in the configuration file is treated
as a comment through the end of that line.
Changes to the configuration file take effect upon restart of
Slurm daemons, daemon receipt of the SIGHUP signal, or execution
of the command "scontrol reconfigure" unless otherwise noted.

**NOTE**: Slurm support for gres/[mps|shard] requires the use of the
select/cons\_tres plugin. For more information on how to configure MPS, see
*<https://slurm.schedmd.com/gres.html#MPS_Management>*.
For more information on how to configure Sharding, see
*<https://slurm.schedmd.com/gres.html#Sharding>*.

For more information on GRES scheduling in general, see
*<https://slurm.schedmd.com/gres.html>*.

The overall configuration parameters available include:

**AutoDetect**
:   The hardware detection mechanisms to enable for automatic GRES configuration.
    Currently, the options are:

    : : **amd** : Automatically detect AMD GPUs through the amdgpu kernel driver in sysfs. No library required. The detected **Type** is the GPU model name from the board FRU, which can differ from the marketing name, or the PCI device ID on a GPU that does not report a model name; take it from **slurmd -G** rather than from vendor tools. Only the SPX compute partition mode is supported. Added in Slurm 26.11. : **full** : On **slurmd**, try all hardware detection mechanisms in order (NVML, NVIDIA, RSMI, AMD, oneAPI, NRT) until GPUs are detected, stopping after the first one that finds a device. **NOTE**: This is the default for dynamic nodes (**slurmd -Z**) when gres.conf has no **AutoDetect** setting and no explicit **Name=gpu** records. : **nrt** : Automatically detect AWS Trainium/Inferentia devices. : **nvidia** : Automatically detect NVIDIA GPUs. No library required, but doesn't detect MIGs or NVlinks. Added in Slurm 24.11. : **nvml** : Automatically detect NVIDIA GPUs. Requires the NVIDIA Management Library (NVML). : **off** : Do not automatically detect any GPUs or TPUs. Used to override other options. : **oneapi** : Automatically detect Intel GPUs. Requires the Intel Graphics Compute Runtime for oneAPI Level Zero and OpenCL Driver (oneapi). : **rsmi** : Automatically detect AMD GPUs. Requires the ROCm System Management Interface (ROCm SMI) Library. : **tpu** : Automatically detect Google Cloud TPU chips in sysfs, by the PCI IDs listed in **[tpu.yaml](tpu.yaml.md)**(5). No library required. The **gres/tpu** plugin detects chips unless **AutoDetect=off** is set, so this has the same effect on TPUs as leaving **AutoDetect** unset. Like any other value, a node-local **AutoDetect=tpu** replaces a global **AutoDetect** for that node. Detected chips replace any **Name=tpu** lines. Added in Slurm 26.11. : *AutoDetect* can be on a line by itself, in which case it will globally apply to all lines in gres.conf by default. In addition, *AutoDetect* can be combined with **NodeName** to only apply to certain nodes. Node-specific *AutoDetect*s will trump the global *AutoDetect*. A node-specific *AutoDetect* only needs to be specified once per node. If specified multiple times for the same nodes, they must all be the same value. To unset *AutoDetect* for a node when a global *AutoDetect* is set, simply set it to "off" in a node-specific GRES line. E.g.: *NodeName=tux3 AutoDetect=off Name=gpu File=/dev/nvidia[0-3]*. *AutoDetect* will automatically detect the device UUID, files, cores, links, and any other hardware. **File** (and **Type**, if set) is used to match a gres.conf record to the corresponding AutoDetect-found device. Once matched, if **Cores**, **Links**, or **UUID** is also specified, the specified value is used to sanity check the auto detected value. If there is a mismatch, then the device is excluded and, if that drops the node below its configured GRES count, the node's state is set to invalid and the node is drained. **NOTE**: On a cloud node, devices are detected when its **slurmd** registers. So Slurm initially sets the GRES count directly from **slurm.conf** without topology and cpu binding information. Jobs scheduled before node registration will be initially allocated as a count-only GRES and after registration the allocation will be adjusted. If this fails, the node is drained and the job is handled as a resume failure (either requeued or killed). : **ChunkOrder** : Controls how devices map onto chunk positions for chunk allocation; see **ChunkSizes** for what chunks and the chunk domain are. A comma-delimited permutation naming the device that occupies each chunk position, so that entry *i* is the device at chunk position *i*. Devices are numbered from 0 within their **Type**, in the order **slurmd** lists them. Without **AutoDetect**, that is the order of the **File** entries. With **AutoDetect**, it is normally PCI bus ID order, which need not match the device file numbers. The output of **slurmd -G** lists the records in this order. Requires **ChunkSizes**. The default is the identity mapping, meaning device enumeration order is chunk order. Chunks are aligned ranges of *chunk positions*, not of device numbers, so this is how an administrator describes a device enumeration order that does not already match the layout of the fabric. Slurm cannot verify that an aligned range of chunk positions is a physically meaningful group of devices. That is the administrator's responsibility. See <<https://slurm.schedmd.com/gres.html#Chunks>> for a worked example. : **ChunkSizes** : A comma-delimited, strictly ascending list of the device group sizes that may be allocated to a job, enabling chunk allocation of this GRES. Every entry must be a multiple of the one before it, so that each size divides the larger ones, and the number of devices in the chunk domain must be a multiple of the largest entry. Unset by default, which disables chunk allocation for this GRES. A job can only request one of these sizes or the whole chunk domain, so include 1 if jobs that request a single device should run on the node. Devices are allocated in aligned chunks, so a chunk of *N* devices begins only at a chunk position that is a multiple of *N*. This keeps a node's free devices in whole chunks rather than fragmenting them into unusable pieces. It is intended for devices with a dedicated interconnect, such as a torus fabric, where the administrator arranges the chunks to match groups of connected devices (see **ChunkOrder**); Slurm does not check that they do. This restricts what a job may request; see <<https://slurm.schedmd.com/gres.html#Chunks>> for those rules. Chunks are formed from the devices of one **Name** and **Type**, referred to as the chunk domain. Each **Type** may set its own **ChunkSizes** and **ChunkOrder**, and every line of that **Type** for any one node must set the same values. A **Type** that sets no **ChunkSizes** is allocated as usual. **Type** is optional. Lines that set no **Type** form a domain of their own. A request that names no type follows the chunk rules on a node whose devices are all of one chunked **Type**. A node that mixes types and chunks any of them is not used for such a request. Requires **File** or **MultipleFiles**, even under **AutoDetect**. The chunk domain may hold at most 1024 devices. Shared GRES (gres/shard, gres/mps) are not supported, nor is gres/gpu on a node that also configures gres/shard or gres/mps. An invalid **ChunkSizes** or **ChunkOrder** value stops **slurmd** when it starts. On **scontrol reconfigure**, a **slurmd** that runs as a daemon or under systemd keeps its previous configuration instead. Check the file with **slurmd -G** before applying it. A layout that does not fit the node's devices, such as a device count that is not a multiple of the largest chunk size, or one of the shared GRES cases above, does not stop **slurmd**. The controller drains the node instead. See <<https://slurm.schedmd.com/gres.html#Chunk_Requirements>>. **Links** is ignored on any record that sets **ChunkSizes**, including link data produced by **AutoDetect**, since the two are different descriptions of the same device topology. : **Count** : Number of resources of this name/type available on this node. The default value is set to the number of **File** values specified (if any), otherwise the default value is one. A suffix of "K", "M", "G", "T" or "P" may be used to multiply the number by 1024, 1048576, 1073741824, etc. respectively. For example: "Count=10G". : **Cores** : Optionally specify the core index numbers matching the specific sockets\* which can use this resource. If this option is used, all the cores in a socket\* must be specified together. While Slurm can track and assign resources at the CPU or thread level, its scheduling algorithms used to co-allocate GRES devices with CPUs operates at a socket\* level for job allocations. Therefore, it is not possible to preferentially assign GRES with different specific CPUs on the same socket\*. \*Sockets may be substituted for NUMA nodes with SlurmdParameters=numa\_node\_as\_socket or l3cache with SlurmdParameters=l3cache\_as\_socket. Multiple cores may be specified using a comma-delimited list or a range may be specified using a "-" separator (e.g. "0,1,2,3" or "0-3"). If a job specifies **--gres-flags=enforce-binding**, then only the identified cores can be allocated with each generic resource. This will tend to improve performance of jobs, but delay the allocation of resources to them. If specified and a job is *not* submitted with the **--gres-flags=enforce-binding** option the identified cores will be preferred for scheduling with each generic resource. If **--gres-flags=disable-binding** is specified, then any core can be used with the resources, which also increases the speed of Slurm's scheduling algorithm but can degrade the application performance. The **--gres-flags=disable-binding** option is currently required to use more CPUs than are bound to a GRES (e.g. if a GPU is bound to the CPUs on one socket, but resources on more than one socket are required to run the job). If any core can be effectively used with the resources, then do not specify the **cores** option for improved speed in the Slurm scheduling logic. A restart of the slurmctld is needed for changes to the Cores option to take effect. **NOTE**: Since Slurm must be able to perform resource management on heterogeneous clusters having various processing unit numbering schemes, a logical core index must be specified instead of the physical core index. That logical core index might not correspond to your physical core index number. Core 0 will be the first core on the first socket, while core 1 will be the second core on the first socket. This numbering coincides with the logical core number (Core L#) seen in "lstopo -l" command output. : **DmemRegion** : Name of the dmem cgroup region providing the device memory of this GRES device, overriding automatic detection. Only valid on a record with a single **File** device, e.g. *DmemRegion=nvidia/0000:01:00/vidmem*. The regions available on the node are listed in */sys/fs/cgroup/dmem.capacity*. If the named region does not exist on the node, or more than one device is explicitly bound to the same region, slurmd fails to start. An explicit binding also takes ownership of the region over any device matched to it automatically, which is then not enforced. A value of *off* excludes this individual device from device memory enforcement (its shards are scheduled but not constrained). See **ConstrainDeviceMemory** in **[cgroup.conf](cgroup.conf.md)**(5). : **File** : Fully qualified pathname of the device files associated with a resource. The name can include a numeric range suffix to be interpreted by Slurm (e.g. *File=/dev/nvidia[0-3]*). This field is generally required if enforcement of generic resource allocations is to be supported (i.e. prevents users from making use of resources allocated to a different user). Enforcement of the file allocation relies upon Linux Control Groups (cgroups) and Slurm's task/cgroup plugin, which will place the allocated files into the job's cgroup and prevent use of other files. Please see Slurm's Cgroups Guide for more information: *<https://slurm.schedmd.com/cgroups.html>*. If **File** is specified then **Count** must be either set to the number of file names specified or not set (the default value is the number of files specified). The exception to this is MPS/Sharding. For either of these GRES, each GPU would be identified by device file using the **File** parameter and **Count** would specify the number of entries that would correspond to that GPU. For MPS, typically 100 or some multiple of 100. For Sharding typically the maximum number of jobs that could simultaneously share that GPU. If using a card with Multi-Instance GPU functionality, or an AMD GPU detected with *AutoDetect=amd*, use **MultipleFiles** instead. **File** and **MultipleFiles** are mutually exclusive. **NOTE**: Either **File** or **MultipleFiles** is required for all *gpu* typed GRES. **NOTE**: If you specify the **File** parameter for a resource on some node, the option must be specified on all nodes and Slurm will track the assignment of each specific resource on each node. Otherwise Slurm will only track a count of allocated resources rather than the state of each individual device file. **NOTE**: Drain a node before changing the count of records with **File** parameters (e.g. if you want to add or remove GPUs from a node's configuration). Failure to do so will result in any job using those GRES being aborted. **NOTE**: A **File** that exists but is not a device node, or one that **AutoDetect** reports but is missing, is logged by slurmd and provides no device, but it still counts toward **Count** and keeps its position in the device numbering, so the devices after it keep their numbers in the GRES environment variables. Listing such a **File** twice keeps slurmd from starting. Remove the entry, or use **Flags**=*env\_uuid* where the numbering matters. **NOTE**: When specifying **File**, **Count** is limited in size (currently 1024) for each node. : **Flags** : Optional flags that can be specified to change configured behavior of the GRES. Allowed values at present are: : : **CountOnly** : Do not attempt to load a plugin of the GRES type as this GRES will only be used to track counts of GRES used. This avoids attempting to load non-existent plugin which can affect filesystems with high latency metadata operations for non-existent files. **NOTE**: If a gres has this flag configured it is global, so all other nodes with that gres will have this flag implied. : **env\_uuid** : Set vendor environment variables using UUIDs instead of numeric device indices. Affects these environment variables: *CUDA\_VISIBLE\_DEVICES* and *ROCR\_VISIBLE\_DEVICES*. *ZE\_AFFINITY\_MASK* and *GPU\_DEVICE\_ORDINAL* are not affected: those runtimes only accept a device index or ordinal, so they always get numeric indices. Requires that UUIDs are available, either from **AutoDetect** or from the **UUID** option. If any device allocated to a job or step has no UUID, all devices in that environment variable use numeric indices; UUIDs and indices are not mixed. For example, instead of "*CUDA\_VISIBLE\_DEVICES=0*", it would look like: "*CUDA\_VISIBLE\_DEVICES=GPU-8932f937-d72c-4106-c12f-20bd9faed9f6*" **NOTE**: With **AutoDetect**, the gres.conf line that sets this flag must carry the same **Type** and **Count** as the node's **Gres** in slurm.conf for the flag to apply to every autodetected GPU. **NOTE**: With *AutoDetect=amd*, a GPU for which the amdgpu kernel driver exposes no UUID has none, so a job allocated such a GPU gets numeric indices for all of its GPUs. : **explicit** : If the flag is set, GRES is not allocated to the job as part of whole node allocation (--exclusive or partition **Exclusive=NODE** set) unless it was explicitly requested by the job. **NOTE**: If a gres has this flag configured it is global, so all other nodes with that gres will have this flag implied. : **one\_sharing** : To be used on a shared gres. If using a shared gres (mps) on top of a sharing gres (gpu) only allow one of the sharing gres to be used by the shared gres. This is the default for MPS. **NOTE**: If a gres has this flag configured it is global, so all other nodes with that gres will have this flag implied. This flag is not compatible with all\_sharing for a specific gres. : **all\_sharing** : To be used on a shared gres. This is the opposite of one\_sharing and can be used to allow all sharing gres (gpu) on a node to be used for shared gres (mps). **NOTE**: If a gres has this flag configured it is global, so all other nodes with that gres will have this flag implied. This flag is not compatible with one\_sharing for a specific gres. : **nvidia\_gpu\_env** : Set environment variable *CUDA\_VISIBLE\_DEVICES* for all GPUs on the specified node(s). : **amd\_gpu\_env** : Set environment variable *ROCR\_VISIBLE\_DEVICES* for all GPUs on the specified node(s). : **intel\_gpu\_env** : Set environment variable *ZE\_AFFINITY\_MASK* for all GPUs on the specified node(s). : **opencl\_env** : Set environment variable *GPU\_DEVICE\_ORDINAL* for all GPUs on the specified node(s). : **no\_gpu\_env** : Set no GPU-specific environment variables. This is mutually exclusive to all other environment-related flags. : If no environment-related flags are specified, then *nvidia\_gpu\_env*, *amd\_gpu\_env*, *intel\_gpu\_env*, and *opencl\_env* will be implicitly set by default. If **AutoDetect** is used and environment-related flags are not specified, then *AutoDetect=nvml* or *AutoDetect=nvidia* will set *nvidia\_gpu\_env*, *AutoDetect=rsmi* or *AutoDetect=amd* will set *amd\_gpu\_env*, and *AutoDetect=oneapi* will set *intel\_gpu\_env*. Conversely, specified environment-related flags will always override **AutoDetect**. Environment-related flags set on one GRES line will be inherited by the GRES line directly below it if no environment-related flags are specified on that line and if it is of the same node, name, and type. Environment-related flags must be the same for GRES of the same node, name, and type. Note that there is a known issue with the AMD ROCm runtime where *ROCR\_VISIBLE\_DEVICES* is processed first, and then *CUDA\_VISIBLE\_DEVICES* is processed. To avoid the issues caused by this, set *Flags=amd\_gpu\_env* for AMD GPUs so only *ROCR\_VISIBLE\_DEVICES* is set. : **Links** : A comma-delimited list of numbers identifying the number of connections between this device and other devices to allow coscheduling of better connected devices. This is an ordered list in which the number of connections this specific device has to device number 0 would be in the first position, the number of connections it has to device number 1 in the second position, etc. A -1 indicates the device itself and a 0 indicates no connection. The list covers every device of this GRES name on the node, whatever its **Type**, so it has one entry per device of that name. If specified, then this line can only contain a single GRES device (i.e. one device file via **File** or one device file group via **MultipleFiles**). Better connected devices are only preferred by default. A job can require that every co-allocated device be linked with **--gres-flags=enforce-links**, or have the preference disregarded with **--gres-flags=ignore-links** (see **[salloc](salloc.md)**(1), **[sbatch](sbatch.md)**(1), and **[srun](srun.md)**(1)). This is an optional value and is usually automatically determined if **AutoDetect** is enabled. A typical use case would be to identify GPUs having NVLink or XGMI connectivity. Note that for GPUs, the minor number assigned by the OS and used in the device file (i.e. the X in */dev/nvidiaX*) is not necessarily the same as the device number/index. The device number is created by sorting the GPUs by PCI bus ID and then numbering them starting from the smallest bus ID. See *<https://slurm.schedmd.com/gres.html#GPU_Management>* **Links** is ignored on any record that sets **ChunkSizes**, since the two are different descriptions of the same device topology. Records of another **Type** are unaffected. : **MultipleFiles** : Fully qualified pathname of the device files associated with a resource. Graphics cards using Multi-Instance GPU (MIG) technology will present multiple device files that should be managed as a single generic resource. The file names can be a comma separated list or it can include a numeric range suffix (e.g. MultipleFiles=/dev/nvidia[0-3]). AMD GPUs detected with *AutoDetect=amd* present two device files each, the render node and the primary node under */dev/dri* (e.g. MultipleFiles=/dev/dri/renderD128,/dev/dri/card0). Drain a node before changing the count of records with the **MultipleFiles** parameter, such as when adding or removing GPUs from a node's configuration. Failure to do so will result in any job using those GRES being aborted. When each GRES presents a single device file, use **File** instead. **MultipleFiles** and **File** are mutually exclusive. : **Name** : Name of the generic resource. Any desired name may be used. The name must match a value in **GresTypes** in *slurm.conf*. Each generic resource has an optional plugin which can provide resource-specific functionality. Generic resources that currently include an optional plugin are: : : **gpu** : Graphics Processing Unit : **mps** : CUDA Multi-Process Service (MPS) : **nic** : Network Interface Card : **shard** : Shards of a gpu : **tpu** : Google Cloud TPU chip. See **[tpu.yaml](tpu.yaml.md)**(5). **NodeName** : An optional NodeName specification can be used to permit one gres.conf file to be used for all compute nodes in a cluster by specifying the node(s) that each line should apply to. The NodeName specification can use a Slurm hostlist specification as shown in the example below. : **Type** : An optional arbitrary string identifying the type of generic resource. For example, this might be used to identify a specific model of GPU, which users can then specify in a job request. For changes to the **Type** option to take effect with a scontrol reconfig all affected **slurmd** daemons must be responding to the **slurmctld**. Otherwise a restart of the **slurmctld** and **slurmd** daemons is required. **NOTE**: If using autodetect functionality and defining the Type in your gres.conf file, the Type specified should match or be a substring of the value that is detected, using an underscore in lieu of any spaces. **NOTE**: On a shared GRES configuration line (*shard* or *mps*) without a **File** parameter, **Type** selects the GPUs the **Count** applies to: every GPU whose type matches receives the (per-device) **Count**, allowing different shard counts per GPU model with one line per type. The slurm.conf "Gres=" specification should then declare the shared GRES per type as node totals using the full GPU type names (e.g. "shard:a100:64" for two A100 GPUs with Count=32); an untyped total is accepted when it equals the sum of the per-device counts. Without **Type**, the **Count** is a node total spread evenly across the GPUs. With **File**, **Type** is ignored and copied from the gres/gpu configuration. : **UUID** : An optional string that uniquely identifies a single device, normally the UUID reported by the vendor tooling (for example **nvidia-smi -L**). The exact format varies by device and **AutoDetect** mechanism; run **slurmd -G** to display the UUID Slurm actually detected for each device rather than guessing at the format. Only **gres/gpu** (and a shared GRES layered on a GPU, such as **mps** or **shard**) consumes this value; other GRES plugins accept it but make no use of it. It is used to set the vendor environment variables when **Flags**=*env\_uuid* is configured. Because this names one physical device, **File** or **MultipleFiles** is required, and **File** may only contain a single device file. A shared GRES (**mps** or **shard**) may still use a **Count** greater than one, since that count describes shared TRES units carved out of the single device. A shared GRES inherits the UUID of the device it shares; a UUID configured on its own line must match. The value may not contain a comma and must be unique among all devices of the same GRES name on a node, whether it was set here or found by **AutoDetect**. If **AutoDetect** also finds a UUID for the device, the two must agree, otherwise the device is excluded from the configuration.

## EXAMPLES

```
##################################################################
# Slurm's Generic Resource (GRES) configuration file
# Define GPU devices with MPS support, with AutoDetect sanity checking
##################################################################
AutoDetect=nvml
Name=gpu Type=gtx560 File=/dev/nvidia0 COREs=0,1
Name=gpu Type=tesla  File=/dev/nvidia1 COREs=2,3
Name=mps Count=100 File=/dev/nvidia0 COREs=0,1
Name=mps Count=100  File=/dev/nvidia1 COREs=2,3
```

```
##################################################################
# Slurm's Generic Resource (GRES) configuration file
# Overwrite system defaults and explicitly configure three GPUs
##################################################################
Name=gpu Type=tesla File=/dev/nvidia[0-1] COREs=0,1
# Name=gpu Type=tesla  File=/dev/nvidia[2-3] COREs=2,3
# NOTE: nvidia2 device is out of service
Name=gpu Type=tesla  File=/dev/nvidia3 COREs=2,3
```

```
##################################################################
# Slurm's Generic Resource (GRES) configuration file
# Use a single gres.conf file for all compute nodes - positive method
##################################################################
## Explicitly specify devices on nodes tux0-tux15
# NodeName=tux[0-15]  Name=gpu File=/dev/nvidia[0-3]
# NOTE: tux3 nvidia1 device is out of service
NodeName=tux[0-2]  Name=gpu File=/dev/nvidia[0-3]
NodeName=tux3  Name=gpu File=/dev/nvidia[0,2-3]
NodeName=tux[4-15]  Name=gpu File=/dev/nvidia[0-3]
```

```
##################################################################
# Slurm's Generic Resource (GRES) configuration file
# Use NVML to gather GPU configuration information
# for all nodes except one
##################################################################
AutoDetect=nvml
NodeName=tux3 AutoDetect=off Name=gpu File=/dev/nvidia[0-3]
```

```
##################################################################
# Slurm's Generic Resource (GRES) configuration file
# Specify some nodes with NVML, some with RSMI, and some with no AutoDetect
##################################################################
NodeName=tux[0-7] AutoDetect=nvml
NodeName=tux[8-11] AutoDetect=rsmi
NodeName=tux[12-15] Name=gpu File=/dev/nvidia[0-3]
```

```
##################################################################
# Slurm's Generic Resource (GRES) configuration file
# Define 'bandwidth' GRES to use as a way to limit the
# resource use on these nodes for workflow purposes
##################################################################
NodeName=tux[0-7] Name=bandwidth Type=lustre Count=4G Flags=CountOnly
```

```
##################################################################
# Slurm's Generic Resource (GRES) configuration file
# Give each GPU a UUID without relying on AutoDetect, so that the
# vendor env vars use UUIDs
##################################################################
Name=gpu File=/dev/nvidia0 Flags=env_uuid       UUID=GPU-8932f937-d72c-4106-c12f-20bd9faed9f6
Name=gpu File=/dev/nvidia1 Flags=env_uuid       UUID=GPU-4ae6da5f-3a1b-49c7-9f2d-0c1e77ab3d10
```

## COPYING

Copyright (C) 2010 The Regents of the University of California.
Produced at Lawrence Livermore National Laboratory (cf, DISCLAIMER).
  
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

**[slurm.conf](slurm.conf.md)**(5)

---



## Index

[NAME](#lbAB): [DESCRIPTION](#lbAC): [EXAMPLES](#lbAD): [COPYING](#lbAE): [SEE ALSO](#lbAF)

---

This document was created by
*man2html* using the manual pages.  
Time: 20:23:17 GMT, November 24, 2026