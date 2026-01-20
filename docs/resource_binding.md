# Source: https://slurm.schedmd.com/resource_binding.html

# Resource Binding

* [Overview](#overview)
* [Srun --cpu-bind option](#srun)
* [Node CpuBind Configuration](#node)
* [Partition CpuBind Configuration](#partition)
* [TaskPluginParam Configuration](#TaskPluginParam)

## Overview

Slurm has a rich set of options to control the default
binding of tasks to resources.
For example, tasks can be bound to individual threads, cores, sockets, NUMA
or boards.
See the slurm.conf and srun man pages for more information about how these
options work.
This document focuses on how default binding configuration can be configured.

Default binding can be configured on a per-node, per-partition or global
basis. The highest priority will be that specified using the srun
[**--cpu-bind**](srun.html#OPT_cpu-bind) option.
The next highest priority binding will be the node-specific binding, if any
node in the job allocation has some [**CpuBind**](slurm.conf.html#OPT_CpuBind) configuration parameter and all other nodes in the job
allocation either have the same or no CpuBind configuration parameter.
The next highest priority binding will be the partition-specific
[**CpuBind**](slurm.conf.html#OPT_CpuBind_1) configuration
parameter (if any).
The lowest priority binding will be that specified by the
[**TaskPluginParam**](slurm.conf.html#OPT_TaskPluginParam)
configuration parameter.

Summary of the order of enforcement:

1. Srun --cpu-bind option
2. Node CpuBind configuration parameter (if all nodes match)
3. Partition CpuBind configuration parameter
4. TaskPluginParam configuration parameter

## Srun --cpu-bind option

The srun [--cpu-bind](srun.html#OPT_cpu-bind) option will always
be used to control task binding. If the --cpu-bind option only includes
"verbose" rather than identifying the entities to be bound to, then the verbose
option will be used together with the default entity based upon Slurm
configuration parameters as described below.

## Node CpuBind Configuration

The next possible source of the resource binding information is the node's
configured [CpuBind](slurm.conf.html#OPT_CpuBind) value, but only
if every node has the same CpuBind value (or no configured CpuBind value).
The node's CpuBind value is configured in the slurm.conf file.
Its value may be viewed or modified using the scontrol command.
To clear a node's CpuBind value use the command:

```
scontrol update NodeName=node01 CpuBind=off
```

## Partition CpuBind Configuration

The next possible source of the resource binding information is the
partition's configured [CpuBind](slurm.conf.html#OPT_CpuBind_1)
value. The partition's CpuBind value is configured in the slurm.conf file.
Its value may be viewed or modified using the scontrol command, similar to how
a node's CpuBind value is changed:

```
scontrol update PartitionName=debug CpuBind=cores
```

## TaskPluginParam Configuration

The last possible source of the resource binding information is the
[TaskPluginParam](slurm.conf.html#OPT_TaskPluginParam)
configuration parameter from the slurm.conf file.