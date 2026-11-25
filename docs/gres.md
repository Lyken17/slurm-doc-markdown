# Slurm Workload Manager - Generic Resource (GRES) Scheduling

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

# Generic Resource (GRES) Scheduling

## Contents

* [Overview](#Overview)
* [Configuration](#Configuration)
* [Running Jobs](#Running_Jobs)
* [AutoDetect](#AutoDetect)
* [Socket Affinity](#Socket_Affinity)
* [Device Links](#Device_Links)
* [Device Chunks](#Chunks)
* [Accounting](#Accounting)
* [GPU Management](#GPU_Management)
* [Draining GRES](#Draining_GRES)
* [MPS Management](#MPS_Management)
* [MIG Management](#MIG_Management)
* [Sharding](#Sharding)
* [Shared GRES Usage](#Shared_GRES_Usage)

## Overview

Slurm supports the ability to define and schedule arbitrary Generic RESources
(GRES). Additional built-in features are enabled for specific GRES types,
including Graphics Processing Units (GPUs), CUDA Multi-Process Service (MPS)
devices, and Sharding through an extensible plugin mechanism.

## Configuration

By default, no GRES are enabled in the cluster's configuration.
You must explicitly specify which GRES are to be managed in the
*slurm.conf* configuration file. The configuration parameters of
interest are **GresTypes** and **Gres**.

For more details, see [GresTypes](slurm.conf.md#OPT_GresTypes) and [Gres](slurm.conf.md#OPT_Gres_1) in the *slurm.conf* man page.

Note that the GRES specification for each node works in the same fashion
as the other resources managed. Nodes which are found to have fewer resources
than configured will be placed in a DRAIN state.

Snippet from an example *slurm.conf* file:

```
# Configure four GPUs (with MPS), plus bandwidth
GresTypes=gpu,mps,bandwidth
NodeName=tux[0-7] Gres=gpu:tesla:2,gpu:kepler:2,mps:400,bandwidth:lustre:no_consume:4G
```

Each compute node with generic resources typically contain a *gres.conf*
file describing which resources are available on the node, their count,
associated device files and cores which should be used with those resources.

There are cases where you may want to define a Generic Resource on a node
without specifying a quantity of that GRES. For example, the filesystem type
of a node doesn't decrease in value as jobs run on that node.
You can use the **no\_consume** flag to allow users to request a GRES
without having a defined count that gets used as it is requested.

To view available *gres.conf* configuration parameters, see the
[gres.conf man page](gres.conf.md).

## Running Jobs

Jobs will not be allocated any generic resources unless specifically
requested at job submit time using the options:

*--gres*
:   Generic resources required per node

*--gpus*
:   GPUs required per job

*--gpus-per-node*
:   GPUs required per node. Equivalent to the *--gres* option for GPUs.

*--gpus-per-socket*
:   GPUs required per socket. Requires the job to specify a task socket.

*--gpus-per-task*
:   GPUs required per task. Requires the job to specify a task count.

All of these options are supported by the *salloc*, *sbatch* and
*srun* commands.
Note that all of the *--gpu\** options are only supported by Slurm's
select/cons\_tres plugin.
Jobs requesting these options when the select/cons\_tres plugin is not
configured will be rejected.
The *--gres* option requires an argument specifying which generic resources
are required and how many resources using the form *name[:type:count]*
while all of the *--gpu\** options require an argument of the form
*[type]:count*.
The *name* is the same name as
specified by the *GresTypes* and *Gres* configuration parameters.
*type* identifies a specific type of that generic resource (e.g. a
specific model of GPU).
*count* specifies how many resources are required and has a default
value of 1. For example:  
*sbatch --gres=gpu:kepler:2 ...*.

Requests for typed vs non-typed generic resources must be consistent
within a job. For example, if you request *--gres=gpu:2* with
**sbatch**, you would not be able to request *--gres=gpu:tesla:2*
with **srun** to create a job step. The same holds true in reverse,
if you request a typed GPU to create a job allocation, you should request
a GPU of the same type to create a job step.

Several additional resource requirement specifications are available
specifically for GPUs and detailed descriptions about these options are
available in the man pages for the job submission commands.
As for the *--gpu\** option, these options are only supported by Slurm's
select/cons\_tres plugin.

*--cpus-per-gpu*
:   Count of CPUs allocated per GPU.

*--gpu-bind*
:   Define how tasks are bound to GPUs.

*--gpu-freq*
:   Specify GPU frequency and/or GPU memory frequency.

*--mem-per-gpu*
:   Memory allocated per GPU.

Jobs will be allocated specific generic resources as needed to satisfy
the request. If the job is suspended, those resources do not become available
for use by other jobs.

Job steps can be allocated generic resources from those allocated to the
job using the *--gres* option with the *srun* command as described
above. By default, a job step will be allocated all of the generic resources
that have been requested by the job, except those implicitly requested when a
job is exclusive. If desired, the job step may explicitly specify a
different generic resource count than the job.
This design choice was based upon a scenario where each job executes many
job steps. If job steps were granted access to all generic resources by
default, some job steps would need to explicitly specify zero generic resource
counts, which we considered more confusing. The job step can be allocated
specific generic resources and those resources will not be available to other
job steps. A simple example is shown below.

```
#!/bin/bash
#
# gres_test.bash
# Submit as follows:
# sbatch --gres=gpu:4 -n4 -N1-1 gres_test.bash
#
srun --gres=gpu:2 -n2 --exclusive show_device.sh &
srun --gres=gpu:1 -n1 --exclusive show_device.sh &
srun --gres=gpu:1 -n1 --exclusive show_device.sh &
wait
```

## AutoDetect

If *AutoDetect=nvml*, *AutoDetect=nvidia*, *AutoDetect=rsmi*,
*AutoDetect=amd*, *AutoDetect=nrt*, or *AutoDetect=oneapi* are
set in *gres.conf*, configuration details will automatically be filled in
for any system-detected GPU. This removes the need to explicitly configure GPUs
in gres.conf, though the *Gres=* line in slurm.conf is still required in
order to tell slurmctld how many GRES to expect.

Note that *AutoDetect=nvml*, *AutoDetect=rsmi*,
and *AutoDetect=oneapi* need their corresponding GPU management libraries
installed on the node and found during Slurm configuration in order to work.
Both *AutoDetect=nvml* and *AutoDetect=nvidia* detect NVIDIA GPUs.
*AutoDetect=nvidia* (added in Slurm 24.11) doesn't require the
nvml library to be installed, but doesn't detect MIGs or NVlinks.
Both *AutoDetect=rsmi* and *AutoDetect=amd* detect AMD GPUs.
*AutoDetect=amd* (added in Slurm 26.11) does not require the ROCm SMI
library to be installed, reading the amdgpu kernel driver through sysfs
instead.

With *AutoDetect=amd*, the detected *Type* is the GPU model name,
lowercased with underscores in place of spaces (for example,
*amd\_instinct\_mi355\_oam*), or the PCI device ID (for example,
*0x744c*) on a GPU that does not report a model name. The model name is the
board FRU product name, which can differ from the marketing name, so take the
*Type* from `slurmd -G`. Only the SPX compute partition mode is
supported. Each GPU is a
[MultipleFiles](gres.conf.md#OPT_MultipleFiles) GRES carrying its
render node and its primary node under */dev/dri*, so that
[ConstrainDevices](cgroup.conf.md#OPT_ConstrainDevices) confines
both. [Cores](gres.conf.md#OPT_Cores) and
[Links](gres.conf.md#OPT_Links) are filled from the GPU's CPU
affinity and from its XGMI connections to the other GPUs, and
[Flags=env\_uuid](gres.conf.md#OPT_env_uuid) uses the UUID that the
amdgpu kernel driver exposes for the GPU. A job allocated a GPU for which the
driver exposes no UUID gets numeric indices for all of its GPUs. For
*Flags=env\_uuid* to apply to every autodetected GPU, give the gres.conf
line the same *Type* and *Count* as the node's *Gres* in
slurm.conf.

When AutoDetect needs to load a GPU management library as stated above it
will usually unload this library immediately after the slurmd is started
allowing other processes to access the library afterwards. This is not the case
when *AcctGatherEnergyType=acct\_gather\_energy/gpu* is set in the
slurm.conf. In this configuration the slurmd keeps the plugin selected by
AutoDetect loaded so it can be polled for GPU energy. A plugin that loads
a GPU management library (such as gpu/rsmi) holds that library open for
the lifetime of the plugin. Of the plugins AutoDetect can select, only
*gpu/rsmi* reads energy, through the ROCm System Management Interface
library. It is selected by *AutoDetect=rsmi*, or by
[AutoDetect=full](gres.conf.md#OPT_full) on a node where RSMI
is the first mechanism to detect a device. With any other plugin, no error
is reported and the node's energy stays at zero.

*AutoDetect=nvml* and *AutoDetect=rsmi* also cause the slurmstepd
to load and hold open the library to perform accounting on GPU usage when the
associated step has requested a gpu. If you do not want this to happen
have *JobAcctGatherParams=DisableGPUAcct* in the slurm.conf.

*AutoDetect=nvml*, *AutoDetect=rsmi* and *AutoDetect=oneapi*
will cause the slurmstepd to load and hold open the library to configure the gpu
frequency when *--gpu-freq* is requested with the job.

In the above situations, a process holding a GPU management library open
keeps other processes from resetting the GPU or unloading its kernel
modules. If you are
requiring to make changes in a Prolog or such you will want to not
have *AcctGatherEnergyType=acct\_gather\_energy/gpu* in the slurm.conf. If
jobs share gpus on the node, you may also need to set
*JobAcctGatherParams=DisableGPUAcct* in the slurm.conf.

By default, all system-detected devices are added to the node.
However, if *Type* and *File* in gres.conf match a GPU on
the system, any other properties explicitly specified (e.g.
*Cores*, *Links*, or *UUID*) can be double-checked against it.
If the system-detected GPU differs from its matching GPU configuration, then the
GPU is omitted from the node with an error.
This allows *gres.conf* to serve as an optional sanity check and notifies
administrators of any unexpected changes in GPU properties.

If not all system-detected devices are specified by the slurm.conf
configuration, then the relevant slurmd will be drained. However, it is still
possible to use a subset of the devices found on the system if they are
specified manually (with AutoDetect disabled) in gres.conf.

Example *gres.conf* file:

```
# Configure four GPUs (with MPS), plus bandwidth
AutoDetect=nvml
Name=gpu Type=gp100  File=/dev/nvidia0 Cores=0,1
Name=gpu Type=gp100  File=/dev/nvidia1 Cores=0,1
Name=gpu Type=p6000  File=/dev/nvidia2 Cores=2,3
Name=gpu Type=p6000  File=/dev/nvidia3 Cores=2,3
Name=mps Count=200  File=/dev/nvidia0
Name=mps Count=200  File=/dev/nvidia1
Name=mps Count=100  File=/dev/nvidia2
Name=mps Count=100  File=/dev/nvidia3
Name=bandwidth Type=lustre Count=4G Flags=CountOnly
```

In this example, since *AutoDetect=nvml* is specified, *Cores*
for each GPU will be checked against a corresponding GPU found on the system
matching the *Type* and *File* specified.
Since *Links* is not specified, it will be automatically filled in
according to what is found on the system.
If a matching system GPU is not found, no validation takes place and the GPU is
assumed to be as the configuration says.

For *Type* to match a system-detected device, it must either exactly
match or be a substring of the GPU name reported by slurmd via the AutoDetect
mechanism. This GPU name will have all spaces replaced with underscores. To see
the detected GPUs and their names, run: `slurmd -C`

```
$ slurmd -C
NodeName=node0 ... Gres=gpu:geforce_rtx_2060:1 ...
Found gpu:geforce_rtx_2060:1 with Autodetect=nvml (Substring of gpu name may be used instead)
UpTime=...
```

In this example, the GPU's name is reported as
`geforce_rtx_2060`. So in your slurm.conf and
gres.conf, the GPU *Type* can be set to `geforce`, `rtx`, `2060`, `geforce_rtx_2060`, or any other
substring, and **slurmd** should be able to match it to the system-detected
device `geforce_rtx_2060`.
To check your configuration you may run: `slurmd -G` This will test and print the gres setup based on the current
configuration, including any autodetected gres that are being ignored.

## Socket Affinity Configuration

Slurm's job scheduler handles GRES affinity on a socket basis internally.
However, the *gres.conf* interface allows administrators to specify `Cores` for GPU affinity configuration. This creates
a common misconception that Slurm will respect core-level affinity during job
scheduling, which it does not and never has. This can lead to issues where job
allocations and job steps don't align correctly, since job steps examine cores
while jobs use sockets.

To prevent administrators from specify a core affinity for the device that
Slurm cannot currently respect, Slurm validates that any specified `Cores` align with socket boundaries and will generate
errors if they do not.

When using `AutoDetect=nvml` or other GPU
autodetection methods, GPU core affinity is automatically detected based on the
hardware topology reported by the GPU driver. On many modern systems with
complex cache hierarchies, the autodetected GPU affinity may not align with
Slurm's socket boundaries.

When this mismatch occurs, you'll see errors like:

```
error: _check_core_range_matches_sock: gres/gpu GRES autodetected core affinity 0-7 on node node0 doesn't match socket boundaries. (Socket 0 is cores 0-1)
```

The recommended solution is to configure Slurm to align its socket definition
with the hardware topology using topology parameters such as
`l3cache_as_socket` or
`numa_node_as_socket` and changing
SocketsPerBoard and CoresPerSocket to match.

Before making permanent changes, test how your hardware will be detected with
the parameter:

```
$ slurmd -C --parameters=l3cache_as_socket
NodeName=node0 CPUs=32 Boards=1 SocketsPerBoard=8 CoresPerSocket=2 ThreadsPerCore=2 RealMemory=128762 Parameters=l3cache_as_socket Gres=gpu:nvidia_a100-pcie-40gb:2
```

This command shows how Slurm will detect the hardware with the parameter
applied. The socket count and cores per socket may differ from the physical
hardware, but will match the GPU affinity boundaries. You can compare the
output with `nvidia-smi topo -m` to verify which
topology parameter aligns with your GPU affinity.

Add the parameter to your node configuration in *slurm.conf*. You can
apply it globally via `SlurmdParameters` or
per-node using the `Parameters` option:

```
# Global configuration
SlurmdParameters=l3cache_as_socket

# Per-node configuration (recommended when only some nodes need this)
NodeName=node0 CPUs=32 Boards=1 SocketsPerBoard=8 CoresPerSocket=2 ThreadsPerCore=2 Parameters=l3cache_as_socket Gres=gpu:a100:2
```

With that parameter set, use autodetection in *gres.conf*:

```
AutoDetect=nvml
```

The GPU core affinity will now align with Slurm's socket boundaries, and the
node should come online without errors.

As an alternative, you can manually specify core affinity in *gres.conf*
that aligns with your actual socket boundaries. However, this requires disabling
autodetect:

```
# Manually specify cores for each GPU
NodeName=node0 Autodetect=off Name=gpu Type=a100 File=/dev/nvidia0 Cores=0-15
NodeName=node0 Autodetect=off Name=gpu Type=a100 File=/dev/nvidia1 Cores=16-31
```

**NOTE**: Manual configuration must still align with socket boundaries or
it will be rejected.

## Device Links

Devices on a node may be linked by a high speed interconnect (e.g. GPUs
connected by NVLink). The `Links` option of
*gres.conf* lists, for one device, how many connections it has to every
other device of the same GRES name on the node, whatever its
`Type`. It is filled in automatically when
[AutoDetect](#AutoDetect) is enabled.

Links are a preference by default: a job needing more than one device uses a
greedy approximation algorithm to try to get devices linked together (still may
not get devices linked together, even if there are such devices idle), and
still runs on whatever is available when it cannot. Two
[--gres-flags](srun.md#OPT_gres-flags) options change that:

`--gres-flags=enforce-links`
:   Every device the job is given on a node must be linked to every other
    device the same request gives it there. A typed request such as
    `--gres=gpu:a100:2` is held against the devices
    of that type alone, an untyped one against every device of that GRES name.
    Nodes that cannot supply a large enough linked set are not used, which may
    delay the job in exchange for faster communication between its devices. A
    single device on a node is unaffected.
    `Links` describes connections within one
    node, so this applies only to the devices a job is given on a single node;
    for topology between nodes see the
    [topology/block](topology.md#block) plugin. Mutually exclusive with
    `ignore-links`.

`--gres-flags=ignore-links`
:   The links are not considered, and devices are selected in the order they
    are found.
    Mutually exclusive with
    `enforce-links`.

**NOTE**: With no configured link information, no node can satisfy an
`enforce-links` request for more than one such
device.

**NOTE**: A node can give a job only one linked set, so an
`enforce-links` request that names no count per
node, such as `--gpus`, may be spread over more
nodes than it would be otherwise.

**NOTE**:
[RestrictedCoresPerGPU](slurm.conf.md#OPT_RestrictedCoresPerGPU),
`--gres-flags=enforce-binding` and a request that
names a count per socket such as
`--gpus-per-socket` already tie the job to
particular sockets, and `enforce-links` applies
within that. Where both cannot be met, the link requirement holds: a node whose
linked devices are not on those sockets is not used, and a count per socket
gives way to a linked set drawn from fewer sockets.

**NOTE**: A job allocated whole nodes (e.g. with
`--exclusive`) is given every device on them,
so `enforce-links` then requires that all of
them be linked. On the
four-GPU node below,
`sbatch --exclusive --gres-flags=enforce-links
--gpus-per-node=2` is refused: the job would get all four GPUs, and no
four are linked.

**NOTE**: Neither option applies to shared GRES (e.g.
`mps`, `shard`),
or to devices allocated in [chunks](#Chunks), which ignore
`Links`.

`scontrol show job` reports the options as
`GresEnforceLinks=Yes` and
`GresIgnoreLinks=Yes`, and
[DebugFlags=SelectType](slurm.conf.md#OPT_DebugFlags) logs which
nodes were rejected for the link requirement.

For example, these GPUs form two linked pairs, 0 with 1 and 2 with 3. The
values are spelled out here to show the shape;
[AutoDetect](#AutoDetect) normally fills them in:

```
NodeName=node0 Name=gpu File=/dev/nvidia0 Links=-1,1,0,0
NodeName=node0 Name=gpu File=/dev/nvidia1 Links=1,-1,0,0
NodeName=node0 Name=gpu File=/dev/nvidia2 Links=0,0,-1,1
NodeName=node0 Name=gpu File=/dev/nvidia3 Links=0,0,1,-1
```

`--gres-flags=enforce-links --gpus-per-node=2`
is given one of those pairs, or waits for one to be free.
`--gpus-per-node=4` is refused: no four of these
GPUs are linked. `--gpus=4` names no count per
node, so on a cluster of such nodes it is spread over two of them instead.

Now suppose GPUs 0 and 3 are busy, leaving 1 and 2 free but unlinked. A
two-GPU job with
`--gres-flags=ignore-links` takes them and runs,
and so does one with neither option, since the default only prefers a linked
pair. `enforce-links` waits instead, until a
whole pair is free.

## Device Chunks

Setting [ChunkSizes](gres.conf.md#OPT_ChunkSizes) for a GRES
in gres.conf turns on chunk allocation for it. Devices are then handed out
only in aligned groups: a chunk of *N* devices begins only at a chunk
position that is a multiple of *N*. Since each size divides the next,
the chunks nest: every chunk of 2 lies within a chunk of 4, every chunk of 4
within a chunk of 8, and so on.

This is a simplification of the fabrics some accelerators are wired
together with, such as a 2D or 3D torus. Slurm does not model the fabric
itself. The administrator chooses the sizes, and the order of the devices, so
that each chunk is a well-connected group. Aligned allocation also prevents
fragmentation, whatever the fabric: free devices stay together in whole
chunks, rather than being scattered so that no larger job fits on the
node.

```
# 16 devices, allocatable in groups of 2, 4, 8, or 16
NodeName=node1 Name=gpu File=/dev/nvidia[0-15] ChunkSizes=2,4,8,16
```

A job can only request one of the listed sizes or the whole domain, so this
node is not used for a job that asks for a single device. Include 1 in
**ChunkSizes** if single-device jobs should run on the node.

### Device Order

Chunks are aligned ranges of *chunk positions*. By default chunk
position *i* is device *i*, so the device enumeration order is
assumed to match the fabric layout.

Devices are numbered in the order slurmd lists them. Without
[AutoDetect](#AutoDetect), that is the order of the **File**
entries in gres.conf, so list them in increasing numeric order. With
**AutoDetect**, slurmd sorts the GPUs it finds, normally into PCI bus ID
order, which need not match the device file numbers. To see the order, run
`slurmd -G` on the node. It lists the GRES
records with their **File**, in this order.

[ChunkOrder](gres.conf.md#OPT_ChunkOrder) is optional. Set it
only when the enumeration order does not match the fabric layout; without it,
the identity mapping above applies. It is a permutation whose entry *i*
names the device at chunk position *i*. Devices are numbered from 0
within their **Type**, in ascending order, so the devices of a **Type**
that starts partway through the node's devices are still numbered from 0.

For 16 devices forming a 4×4 fabric that enumerate in row-major order,
an aligned chunk of 4 is a whole row, a 1×4 line. The recursive halving
order below makes it a 2×2 tile instead:

```
NodeName=node1 Name=gpu File=/dev/nvidia[0-15] ChunkSizes=2,4,8,16 \
    ChunkOrder=0,1,4,5,2,3,6,7,8,9,12,13,10,11,14,15
```

The resulting configuration is visible with
`scontrol show node -d`:

```
$ scontrol show node -d node1 | grep GresChunks
GresChunks=gpu:sizes=2/4/8/16;order=0/1/4/5/2/3/6/7/8/9/12/13/10/11/14/15
```

The *order* component is always shown, so it does not by itself mean
**ChunkOrder** was configured. Nodes with no chunk configuration have no
**GresChunks** line at all, which makes it easy to tell whether chunk
allocation is in play on a node.

**ChunkOrder** only permutes how chunks are formed. Device indexes, the
device files jobs see, and the environment variables Slurm sets are all
unchanged.

### What Jobs May Request

Chunk allocation limits what a job may request for that GRES. The rules
below use the *chunk domain*, the devices chunks are formed from: all the
devices of one **Type** (see [below](#Chunk_Requirements)).

Slurm checks the rules on each node. A node whose chunks cannot serve a
request is not used for it, and the job can still run on other nodes, such as
nodes that set no **ChunkSizes**. If no node in the job's partitions can
serve it, the job is rejected at submit with
*Requested node configuration is not available*.

* The per-node count must be exactly one of the configured chunk sizes, or
  every device in the chunk domain. A request that falls between sizes is not
  rounded up, so a node with **ChunkSizes=1,2,4,8** is not used for a request
  for 3 devices.
* A job that may span more than one node must take every device in the
  chunk domain on each node, so a request for half a domain on each of two nodes
  cannot use the node.
* `--gpus-per-socket` can only be used with
  a whole-node allocation. The number of devices it asks for on a node depends on
  how many sockets the job's cores land on, which is not known until the job is
  placed, and the devices would also have to be spread over those sockets, which
  a single aligned chunk does not guarantee.
  `--gpus` cannot be used on its own, since it
  leaves the per-node split up to the scheduler; it is accepted when
  `--gpus-per-node` or
  `--gpus-per-task` fixes that count. Request
  the per-node count explicitly, with `--gres`,
  `--gpus-per-node`,
  `--gpus-per-task`, or
  `--tres-per-task=gres/gpu=N`, which follows the
  same rules as `--gpus-per-task`.
* A request for part of the chunk domain can only use the node when the job
  cannot be spread over more than one node. That is the case for a job with
  `-N1`, a job with a single task, such as
  `sbatch --gres=gpu:2 job.sh`, a job whose
  `--ntasks-per-node` covers all of its tasks,
  such as `-n4 --ntasks-per-node=4`, and a job in
  a partition with **MaxNodes=1**. A job with several tasks and no such
  limit, or with a node range such as
  `--nodes=1-4`, could be spread over several
  nodes, so it cannot use part of a domain.
* A per-task request must additionally fix how many tasks land on a node.
  Use `-N1` for a partial-domain allocation, or
  `--ntasks-per-node` to fix the per-node count.
  A multi-node job is allowed when that count fills the whole domain on each
  node. For example, on four-device domains,
  `-N2 -n4 --ntasks-per-node=2 --gpus-per-task=2`
  requests all four devices per node.

A whole-node allocation is exempt from all of these, including on a node
whose largest chunk size is smaller than the device count. It normally takes
every device on the node. GRES configured with **Flags=explicit** are an
exception: only explicitly requested devices are allocated, but the whole-node
exemption still applies.

A whole-node allocation here means
`--exclusive` with no argument, or a partition
configured with **OverSubscribe=EXCLUSIVE**.
`--core-spec` and
`--thread-spec` also qualify, but only on a
cluster with **AllowSpecResourcesUsage=YES**. That is not the default, and
where it is not set the two options leave the node shared and the chunk rules
apply as usual.

The rules constrain the job allocation. Steps run inside an allocation the
job already holds, so they are not chunk-allocated and may request any subset
of the job's devices.

A request that does not fix how many devices it needs on each node, such as
`--gpus=4` on its own, or
`--gpus-per-task=2 -n4` without
`-N1`, cannot use a chunked node. When no other
node can serve it, it is rejected at submit rather than left pending forever.
[DebugFlags=SelectType](slurm.conf.md#OPT_DebugFlags) logs which
rule turned each node down, in *slurmctld.log*.

When several free chunks of the right size exist, Slurm prefers one whose
next larger chunk is already partly in use, so that completely free larger
chunks stay available for jobs that need them.

Chunk allocation says nothing about which *nodes* a multi-node job
lands on. Grouping the nodes themselves is the job of the
[topology/block](topology.md#block) plugin, which is configured
with **BlockSizes** in *topology.conf*. The two are meant to be used
together on a fabric that spans nodes.

### Requirements and Interactions

Chunks are formed from the devices of one **Type**, its *chunk
domain*. Each **Type** of a GRES may set its own **ChunkSizes** and
**ChunkOrder**, and every gres.conf line of that **Type** for any one
node must set the same values. A **Type** that sets no **ChunkSizes** is
allocated as usual. **Type** is optional: lines that set none form a domain
of their own, as in the first example above.

A request that names a **Type** follows that **Type**'s rules:

```
NodeName=node1 Name=gpu Type=a100 File=/dev/nvidia[0-15] ChunkSizes=2,4,8,16
NodeName=node1 Name=gpu Type=h100 File=/dev/nvidia[16-19] ChunkSizes=2,4
NodeName=node1 Name=gpu Type=l4 File=/dev/nvidia[20-21]
```

In `scontrol show node -d`, each chunked
**Type** is listed separately, named as in a request, and its *order* is
numbered the way **ChunkOrder** is written:

```
GresChunks=gpu:a100:sizes=2/4/8/16;order=0/1/2/3/4/5/6/7/8/9/10/11/12/13/14/15,gpu:h100:sizes=2/4;order=0/1/2/3
```

Here `--gres=gpu:a100:4` gets an aligned
chunk of 4 a100s, `--gres=gpu:h100:2` an aligned
pair of h100s, and `--gres=gpu:l4:1` is
unaffected by chunks.

A request that names no **Type** follows the chunk rules on a node whose
devices are all of one chunked **Type**, as in the first example above. On a
node that mixes **Types** and chunks any of them, such as this one, it could
be given devices of several **Types**, which no chunk describes, so the node
is not used for it. Name a **Type** to use such a node.

Chunk allocation has these requirements:

* **File** or **MultipleFiles** is required. A GRES without device
  files has no device identity to form chunks from.
* Every chunk size must be a multiple of the one before it, and the list
  must ascend, so that each size divides the larger ones evenly. The slurmd
  process exits on a list that does not, so **ChunkSizes=2,3,6** stops the
  node from starting.
* The chunk domain's device count must be a multiple of the largest chunk
  size, and the domain may hold at most 1024 devices. The controller drains a
  node that does not meet this, including one that re-registers after losing a
  device.
* Shared GRES (gres/shard, gres/mps) cannot use **ChunkSizes**. Nor can
  gres/gpu on a node that also configures gres/shard or gres/mps, even when the
  shared GRES is on other GPUs, since the shared allocations are invisible to
  the chunk selection. The controller drains such a node.
* **Links** is ignored, including link data produced by
  **AutoDetect**, since chunks and links are different descriptions of the
  same device topology. The slurmd process logs a warning for each gres.conf
  line whose **Links** value it drops. For the same reason
  [--gres-flags=enforce-links](#Device_Links) is not applied to these
  devices.
* With `--gres-flags=enforce-binding`, the
  chunk must come from devices bound, by **Cores**, to sockets where the job
  can get cores, or from devices with no **Cores**. The job gets cores on
  every socket the chunk's devices are bound to. When no free chunk of the
  requested size meets this, the node is not used for the job.

Because **File** is required, the requirement holds under
**AutoDetect** too: an autodetected node still needs an explicit record to
carry **ChunkSizes**.

```
AutoDetect=nvml
NodeName=node1 Name=gpu Type=a100 File=/dev/nvidia[0-15] ChunkSizes=2,4,8,16
```

The slurmd process checks gres.conf when it starts. It logs the error and
exits, so the node does not register, when:

* a **ChunkSizes** value does not parse, is not strictly ascending, has
  an entry that is not a multiple of the one before it, or has a size of 0 or
  above 1024;
* a **ChunkOrder** value does not parse, has more than 1024 entries,
  repeats an entry, or has an entry outside the range its length allows;
* **ChunkOrder** is set without **ChunkSizes**;
* **ChunkSizes** is set without **File** or
  **MultipleFiles**;
* two lines of the same name and **Type** set *different* values,
  or one of them sets none at all.

When slurmd runs as a daemon or under systemd, an error found on
`scontrol reconfigure` does not stop it. The
running slurmd keeps its previous configuration and logs
*Resuming operation, reconfigure failed.* To catch these errors first,
check the edited file with `slurmd -G`, which
reads gres.conf the same way and reports the same errors.

The controller checks the chunk layout against the node's devices when the
node registers. It drains the node, with the error as the drain reason,
when:

* the chunk domain's device count is not a multiple of the largest chunk
  size, or is smaller than it;
* the chunk domain has more than 1024 devices, or none at all;
* the length of **ChunkOrder** differs from the chunk domain's device
  count;
* **ChunkSizes** is set on gres/shard or gres/mps, or on gres/gpu on a
  node that also configures gres/shard or gres/mps;
* the records of a **Type** reach the controller with different
  values.

The slurmd process cannot check the length of **ChunkOrder**, since only
the controller knows how many devices the node ended up with. It does stop on
records that disagree, so the controller sees that case only as a safeguard.
To return a drained node to service, correct gres.conf, restart slurmd on the
node, and resume the node:

```
$ scontrol update NodeName=node1 State=RESUME
```

## Accounting

GPU memory and GPU utilization can be tracked as
[TRES](https://slurm.schedmd.com/tres.md) for tasks using GPU
resources. If `AccountingStorageTRES=gres/gpu` is configured,
gres/gpumem and gres/gpuutil will automatically be configured and gathered from
GPU jobs. gres/gpumem and gres/gpuutil can also be set individually when
gres/gpu is not set.

gres/gpumem and gres/gpuutil are only available for NVIDIA GPUs when using
`AutoDetect=nvml`, and AMD GPUs when using
`AutoDetect=rsmi`. Devices under
[shard device memory enforcement](#shard_device_memory) feed
gres/gpumem from the kernel instead, regardless of vendor.

NVML does not support utilization metrics for MIGs, so Slurm does not
provide gpumem or gpuutil accounting for MIG devices. See
[NVIDIA's MIG User Guide](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/#gpu-utilization-metrics).

With gpu/rsmi, gres/gpuutil is the percentage of compute units (CUs) that
a task process occupies. gpu/rsmi is used with `AutoDetect=rsmi`.
It is also used with [AutoDetect=full](gres.conf.md#OPT_full)
on a node where RSMI is the first mechanism to detect a device. The ROCm SMI
library reads a per-process counter of occupied CUs from the amdgpu kernel
driver. It divides the total over the GPUs it reads by the number of CUs on
those GPUs. It reads the GPUs that the device cgroup of the slurmstepd
allows:

* With the default
  [ConstrainDevices=no](cgroup.conf.md#OPT_ConstrainDevices),
  it reads every AMD GPU on the node.
* With `ConstrainDevices=yes` and cgroup/v2, it reads the GPUs
  of the job.
* With `ConstrainDevices=yes` and cgroup/v1, it reads the GPUs
  of the step.

For example, on a node with four identical GPUs and the default
`ConstrainDevices=no`, a process that keeps one GPU fully busy
reports a gres/gpuutil of at most 25 percent.

The driver does not always provide the counter:

* It provides the counter only for some GPU generations, depending on the
  driver version.
* It never provides the counter for a GPU that the process cannot access.
  Examples are another task's GPU when each task is bound to its own GPUs
  under `ConstrainDevices=yes`, or the other GPUs of the job when a
  step uses fewer GPUs than its job under cgroup/v2.

When the counter is missing on a GPU that the library reads, the result
depends on the ROCm release:

* Before ROCm 6.1.1, the read fails.
* From ROCm 6.1.1, the library reports an invalid value. Before ROCm
  6.3.0, a GPU that the process cannot access still makes the read fail.
* Also from ROCm 6.1.1, if the library reads a GPU that has the counter
  after the last GPU that lacks it, it reports a wrong value instead of the
  invalid one.

For an invalid value or a value above 100, Slurm records gres/gpumem but
no gres/gpuutil sample. Slurm cannot tell a wrong value of 100 or less from
a real one. When the read fails, Slurm records neither value. It logs
`RSMI: Failed to get usage` for each such process at each
poll.

Here is an example node with two NVIDIA A100 GPUs:

```
$ nvidia-smi -L
GPU 0: NVIDIA A100-PCIE-40GB (UUID: GPU-...)
GPU 1: NVIDIA A100-PCIE-40GB (UUID: GPU-...)
```

The following is an excerpt from an example slurm.conf and gres.conf which
will automatically enable tracking for gres/gpumem and gres/gpuutil.

slurm.conf:

```
AccountingStorageTres=gres/gpu
NodeName=n1 Gres=gpu:a100:2
```

gres.conf:

```
AutoDetect=nvml
```

Here's an example of a job with two tasks that uses one GPU per task, two
GPUs total.

```
$ srun --tres-per-task=gres/gpu:1 -n2 --gpus=2 --mem=2G gpu_burn
GPU 0: NVIDIA A100-PCIE-40GB (UUID: GPU-...)
GPU 0: NVIDIA A100-PCIE-40GB (UUID: GPU-...)
```

After the job has finished, we can see utilization details of these TRES
using sacct. Note that there are multiple tasks here and we can use
TRESUsageIn[Min,Max,Ave,Tot] to examine the "highwater marks" for gpumem and
gpuutil over all the ranks in the step, as is true for other TRESUsage\*
values:

```
$ sacct -j 1277.0 --format=tresusageinave -p
TRESUsageInAve|
cpu=00:00:11,energy=0,fs/disk=87613,gres/gpumem=36266M,gres/gpuutil=100,mem=628748K,pages=0,vmem=0|
$ sacct -j 1277.0 --format=tresusageintot -p
TRESUsageInTot|
cpu=00:00:22,energy=0,fs/disk=175227,gres/gpumem=72532M,gres/gpuutil=200,mem=1257496K,pages=0,vmem=0|
```

## GPU Management

In the case of Slurm's GRES plugin for GPUs, the environment variable
`CUDA_VISIBLE_DEVICES`
is set for each job step to determine which GPUs are
available for its use on each node. This environment variable is only set
when tasks are launched on a specific compute node (no global environment
variable is set for the *salloc* command and the environment variable set
for the *sbatch* command only reflects the GPUs allocated to that job
on that node, node zero of the allocation).
CUDA version 3.1 (or higher) uses this environment
variable in order to run multiple jobs or job steps on a node with GPUs
and ensure that the resources assigned to each are unique. In the example
above, the allocated node may have four or more graphics devices. In that
case, `CUDA_VISIBLE_DEVICES`
will reference unique devices for each file and
the output might resemble this:

```
JobStep=1234.0 CUDA_VISIBLE_DEVICES=0,1
JobStep=1234.1 CUDA_VISIBLE_DEVICES=2
JobStep=1234.2 CUDA_VISIBLE_DEVICES=3
```

**NOTE**: Be sure to specify the *File* parameters in the
*gres.conf* file and ensure they are in the increasing numeric order.

The `CUDA_VISIBLE_DEVICES`
environment variable will also be set in the job's Prolog and Epilog programs.
Note that the environment variable set for the job may differ from that set for
the Prolog and Epilog if Slurm is configured to constrain the device files
visible to a job using Linux cgroup.
This is because the Prolog and Epilog programs run outside of any Linux
cgroup while the job runs inside of the cgroup and may thus have a
different set of visible devices.
For example, if a job is allocated the device "/dev/nvidia1", then
`CUDA_VISIBLE_DEVICES` will be set to a value of
"1" in the Prolog and Epilog while the job's value of
`CUDA_VISIBLE_DEVICES` will be set to a
value of "0" (i.e. the first GPU device visible to the job).
For more information see the
[Prolog and Epilog Guide](prolog_epilog.md).

When possible, Slurm automatically determines the GPUs on the system using
NVML. NVML (which powers the
`nvidia-smi` tool) numbers GPUs in order by their
PCI bus IDs. For this numbering to match the numbering reported by CUDA, the
`CUDA_DEVICE_ORDER` environmental variable must
be set to `CUDA_DEVICE_ORDER=PCI_BUS_ID`.

GPU device files (e.g. */dev/nvidia1*) are
based on the Linux minor number assignment, while NVML's device numbers are
assigned via PCI bus ID, from lowest to highest. Mapping between these two is
nondeterministic and system dependent, and could vary between boots after
hardware or OS changes. For the most part, this assignment seems fairly stable.
However, an after-bootup check is required to guarantee that a GPU device is
assigned to a specific device file.

Please consult the
[NVIDIA CUDA documentation](https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#env-vars) for more information about the
`CUDA_VISIBLE_DEVICES` and
`CUDA_DEVICE_ORDER` environmental variables.

## Draining GRES

Slurm can drain individual GRES, CPUs, or memory and leave the rest of the
node schedulable. Use `scontrol update` with
`TresName=` for the TRES,
`NodeName=` for the node, and
`Index=`,
`Uuid=`, or
`Count=` for which resources.
`Action=Drain` and
`Action=SetDrain` require
`Reason=`:

```
# Drain GPU 3 on node tux1 by index
$ scontrol update TresName=gres/gpu NodeName=tux1 Index=3 \
    Action=Drain Reason=ecc_errors

# Drain a specific GPU by UUID
$ scontrol update TresName=gres/gpu NodeName=tux1 Uuid=GPU-abc123 \
    Action=Drain Reason=ecc_errors

# Drain every a100 on the node
$ scontrol update TresName=gres/gpu:a100 NodeName=tux1 Index=ALL \
    Action=Drain Reason=firmware_update

# Drain part of a count-only GRES or memory by count (one TRES per command)
$ scontrol update TresName=gres/bandwidth NodeName=tux1 Count=2 \
    Action=Drain Reason=hw_check
$ scontrol update TresName=mem NodeName=tux1 Count=4096 \
    Action=Drain Reason=bad_dimm

# Drain CPUs by index (a numeric Count= is refused for CPUs; Count=ALL
# drains every core)
$ scontrol update TresName=cpu NodeName=tux1 Index=0,2-3 \
    Action=Drain Reason=flaky_cores
```

Use `Uuid=` when the device has a UUID. A
UUID names the same card whatever its index, and vendor tools print it (for
example `nvidia-smi -L`). The Slurm index
of a GPU can differ from the number the vendor tool gives it, and
`scontrol show node` does not print the UUID
of each device.

CPUs are drained by whole core. Naming any thread of a core drains every
thread of that core, and each of those threads counts toward the
**cpu** limit of **MaxDrainedTres**. The CPU examples on this page
assume one thread per core. With two threads per core, the drain above
covers CPUs 0-3.

`Action=Resume` returns the named resources
to service.
`Action=SetDrain` makes the drained
set exactly the resources named in the command, so repeating it changes
nothing. `Action=Drain` adds to a drain that is
already there. Memory and count-only GRES keep one reason per TRES (per type
for a typed GRES), so a later `Drain` replaces
that reason:

```
$ scontrol update TresName=gres/gpu NodeName=tux1 Index=3 Action=Resume
$ scontrol update TresName=gres/bandwidth NodeName=tux1 Count=2 \
    Action=SetDrain Reason=hw_check
```

See [scontrol](scontrol.md#OPT_TresName) for every option
of this command. The REST API accepts the equivalent request as
`POST /slurm/v0.0.46/tres/`. Its JSON keys
are `name` (TresName),
`nodes` (NodeName),
`index`,
`uuid`,
`count`,
`reason`, and
`action`, which is
`drain`,
`resume`, or
`set_drain`. A selector of ALL is
`"select_all": true`; an
`index` of ALL is refused.

A node with anything drained is **DEGRADED** until every drain has been
resumed. `State=RESUME` resumes drained TRES
that are present. An absent index stays drained until a device fills it.
When it resumes an automatic UUID-order drain, it drops the
[saved order](#Draining_GRES_Anchoring); the next slurmd
registration saves the replacement order.
`State=UNDRAIN`,
`State=RESUME_KEEP_TRES`, and
`State=IDLE` clear the node
drain and leave those TRES drained. A job already using a drained resource
keeps it until the job ends. That resource takes no new allocations, and the
rest of the node stays schedulable.

### Bounding How Much May Be Drained

**MaxDrainedTres** sets how much of a TRES may be drained before the node
itself is drained:

```
NodeName=tux[1-16] Gres=gpu:a100:8,bandwidth:4G \
    MaxDrainedTres=gres/gpu:2,cpu:4,mem:8192
```

Within the limit the node stays **DEGRADED** and the drained TRES are
not scheduled. Past the limit the node is drained, with a reason naming the
TRES. Licenses and other cluster-scoped TRES are not covered. See
[MaxDrainedTres](slurm.conf.md#OPT_MaxDrainedTres).
`scontrol show node`
prints the configured limit as
**MaxDrainedTres**. The REST node record and
`scontrol --json` report it as
`max_drained_tres`, which is empty when the
node has no limit. `scontrol show node` omits
**MaxDrainedTres** when the node has no limit.

Shared GRES ([shard](#Sharding) and
[mps](#MPS_Management)) cannot be drained directly. Drain the GPU
that backs them. Shards or MPS on that GPU then take no new work, as shown by
`GresUsed`
([Shared GRES Usage](#Shared_GRES_Usage)).

### Seeing What Is Drained

`scontrol show drainedtres` and
**DrainedTRES** on `scontrol show node` list
what is drained and why. `sinfo -R` includes
degraded nodes. A node that is only **DEGRADED** has no reason of its own,
so **-R** shows its **DrainedTRES** list. The field is omitted when
nothing is drained. The REST API node record has the same list in
`drained_tres`.

```
$ scontrol show node tux1
NodeName=tux1 ...
   State=IDLE+DEGRADED ...
   Gres=gpu:a100:8,bandwidth:4G
   DrainedTRES=gres/gpu(IDX:3)(ecc_errors),gres/bandwidth(CNT:2)(hw_check),cpu(IDX:0,2-3)(flaky_cores),mem(CNT:4096)(bad_dimm)
```

An `(IDX:...)` entry is an index in the
saved order when the GRES has a UUID map, and slurmd's order otherwise.
An absent device is an empty index and is listed by that index. See
[Saved Device Order and Absent
Devices](#Draining_GRES_Anchoring).

A `(CNT:...)` entry is a drained count of a
count-only GRES, or of memory in MiB.

Accounting keeps one open event for the node while a tracked TRES is
drained. `sacctmgr show event` lists it, and
**TresReference** names the drained TRES, in the format described in
[sacctmgr](sacctmgr.md#OPT_TresReference). The event's
**TRES** column counts only TRES tracked by
[AccountingStorageTRES](slurm.conf.md#OPT_AccountingStorageTRES).
CPU and memory always count. An untracked GRES, such as **gres/gpu**
when it is not tracked, does not, and a drain of only that GRES records
no event.

The default format of `sacctmgr show event`
does not include **TRES** or **TresReference**, so ask for them:

```
$ sacctmgr -p show event Nodes=tux1 States=Degraded \
    Format=NodeName,Start,End,State,Reason,TRES,TresReference
```

### Saved Device Order and Absent Devices

When every device of a GRES has a UUID and a count of one, slurmctld saves
that order. A device slurmd no longer reports stays at its index with an empty
slot, and the devices after it stay where they are. The index is drained. If
nothing was already drained there, the reason is
**gres/***name***:not\_found**. That drain counts toward
**MaxDrainedTres** for the GRES and the device's type.
`DrainedTRES` names the index. The UUID that
left is kept with the drain and is not printed on that entry, because the
slot is empty. **Uuid** looks up the saved slots, so it does not select an
empty one. **Index** does, including **ALL**.

A new UUID reported in an empty index fills it. The automatic
**not\_found** drain is cleared, and the new device is not drained. A report
that moves a UUID which is still present, or that adds a UUID past the empty
indexes instead of in one of them, is refused. The saved order stays, and the
node is drained with the reason
**GPU UUID order does not match the saved order**. A later report that
fits the saved order clears that automatic drain. With
SlurmctldParameters=[drain\_absent\_gres](slurm.conf.md#OPT_drain_absent_gres)
the node stays up and **DEGRADED** while the drain is within
**MaxDrainedTres**. Without the parameter the same index is drained and the
node is marked invalid. A node with no saved order, because this is its first
registration, is marked invalid when the count is short, and no per-device
hole is recorded. SlurmdParameters=[config\_overrides](slurm.conf.md#OPT_config_overrides) does not
change any of this; an absent device is still drained.

A job keeps those saved indexes, and **scontrol** and accounting show
them.

**NOTE**: An absent index still consumes one configured **Gres**
count. Lowering the configured count to the devices that remain, in the saved
order, drops the extra indexes.
`Action=Resume` of that index is refused.
`Index=ALL`, a
`SetDrain` that would resume that index, and
`State=RESUME`
leave it drained, and scontrol names each device they leave drained.

On a GRES with a saved order, a drain belongs to the device, not to its
index. This is also true of a drain that an administrator set:

* When a new device takes the index of a drained device that slurmd no
  longer reports, the new device is not drained. The old drain is dropped.
* When the configured count is lowered, the drain on a device that is no
  longer configured is dropped. It does not come back if that device is
  installed again. The drains on the remaining devices move with them to
  their new indexes.

If any device of a GRES reports no UUID, the GRES has no saved order. An
absent device leaves no empty slot and gets no **not\_found** drain, and a
drain stays on its index. A device that replaces a drained one at the same
index is drained too. When the configured count is lowered, the drains on
indexes past the new count are dropped.

When slurmd reports no device of a GRES at all, every drain on that GRES
stays. A GPU driver that failed to load looks like this, so the drains are
still in place when the devices are reported again. With
SlurmctldParameters=[drain\_absent\_gres](slurm.conf.md#OPT_drain_absent_gres) and a saved
order, every device is then absent: each empty index is drained as
**not\_found** and the node stays up. Otherwise the node is marked invalid
(**INVAL**).

### Replacing a GPU

A drained GPU keeps the node working between the GPU going bad and the
maintenance that fixes it. To replace a bad GPU:

1. **Drain the bad GPU.** Do this as soon as the GPU is known to be bad. No
   new job is given it, and the rest of the node stays in service:

   ```
   $ scontrol update TresName=gres/gpu NodeName=tux1 Uuid=GPU-abc123 \
       Action=Drain Reason=bad_gpu
   ```
2. **Take the node out of service for the repair.** When the maintenance
   window comes, drain the node or put it in a maintenance reservation, let its
   jobs finish, and replace the GPU.
3. **Return the node to service.** What slurmd reports when it registers
   follows from the [saved device order](#Draining_GRES_Anchoring):
   * The new GPU is reported at the old GPU's index. The old drain is dropped
     and the new GPU is not drained.
   * You did not replace the GPU. Its index stays empty and drained, so no job
     is given it. With SlurmctldParameters=[drain\_absent\_gres](slurm.conf.md#OPT_drain_absent_gres) the node
     stays up.
   * The GPUs are reported in a different order. The report is refused, the
     saved order stays, and the node is drained with the reason **GPU UUID order
     does not match the saved order**. If the new order is correct, run
     `scontrol update NodeName=tux1 State=RESUME`.
     This drops the saved order, so the next registration saves the new one.Then undrain the node with `State=UNDRAIN`,
   which leaves any other drained GPU drained.
   `State=RESUME` resumes those as well, so drain
   again any device that is still bad.

## MPS Management

[CUDA Multi-Process Service (MPS)](https://docs.nvidia.com/deploy/pdf/CUDA_Multi_Process_Service_Overview.pdf) provides a mechanism where GPUs can be
shared by multiple jobs, where each job is allocated some percentage of the
GPU's resources.
The total count of MPS resources available on a node should be configured in
the *slurm.conf* file (e.g. "NodeName=tux[1-16] Gres=gpu:2,mps:200").
Several options are available for configuring MPS in the *gres.conf* file
as listed below with examples following that:

1. No MPS configuration: The count of gres/mps elements defined in the
   *slurm.conf* will be evenly distributed across all GPUs configured on the
   node. For example, "NodeName=tux[1-16] Gres=gpu:2,mps:200" will configure
   a count of 100 gres/mps resources on each of the two GPUs.
2. MPS configuration includes only the *Name* and *Count* parameters:
   The count of gres/mps elements will be evenly distributed across all GPUs
   configured on the node. This is similar to case 1, but places duplicate
   configuration in the gres.conf file.
3. MPS configuration includes the *Name*, *File* and *Count*
   parameters: Each *File* parameter should identify the device file path of a
   GPU and the *Count* should identify the number of gres/mps resources
   available for that specific GPU device.
   This may be useful in a heterogeneous environment.
   For example, some GPUs on a node may be more powerful than others and thus be
   associated with a higher gres/mps count.
   Another use case would be to prevent some GPUs from being used for MPS (i.e.
   they would have an MPS count of zero).
4. MPS configuration includes the *Name*, *Type* and *Count*
   parameters (no *File*): The *Count* is given to **every** GPU
   whose type matches the *Type* parameter (a case-insensitive substring of
   the GPU type; the most specific configuration wins). Unlike cases 1 and 2,
   the *Count* is per device, not a node total, so one line covers any
   number of GPUs of that model and one line per GPU type may be used to give
   different models different gres/mps counts. GPUs whose type matches no line
   get an MPS count of zero.
   With this form the *slurm.conf* "Gres=" specification should declare the
   gres/mps counts per type as node totals using the full GPU type names.
   An untyped total is accepted when it equals the sum of all the per-device
   counts.

Note that the *Cores* parameter for gres/mps is ignored, and the
*Type* parameter is ignored when *File* is also specified.
That information is copied from the gres/gpu configuration.

Note the *Count* parameter is translated to a percentage, so the value
would typically be a multiple of 100, or exactly 100 per device with the
per-type form of case 4.

Note that if NVIDIA's NVML library is installed, the GPU configuration
(i.e. *Type*, *File*, *Cores* and *Links* data) will be
automatically gathered from the library and need not be recorded in the
*gres.conf* file.

By default, job requests for MPS are required to fit on a single gpu on
each node. This can be overridden with a flag in the *slurm.conf*
configuration file. See [OPT\_MULTIPLE\_SHARING\_GRES\_PJ](slurm.conf.md#OPT_MULTIPLE_SHARING_GRES_PJ).

Note the same GPU can be allocated either as a GPU type of GRES or as
an MPS type of GRES, but not both.
In other words, once a GPU has been allocated as a gres/gpu resource it will
not be available as a gres/mps.
Likewise, once a GPU has been allocated as a gres/mps resource it will
not be available as a gres/gpu.
However the same GPU can be allocated as MPS generic resources to multiple jobs
belonging to multiple users, so long as the total count of MPS allocated to
jobs does not exceed the configured count.
Also, since shared GRES (MPS) cannot be allocated at the same time as a sharing
GRES (GPU) this option only allocates all sharing GRES and no underlying shared
GRES.
Some example configurations for Slurm's gres.conf file are shown below.

```
# Example 1 of gres.conf
# Configure four GPUs (with MPS)
AutoDetect=nvml
Name=gpu Type=gp100 File=/dev/nvidia0 Cores=0,1
Name=gpu Type=gp100 File=/dev/nvidia1 Cores=0,1
Name=gpu Type=p6000 File=/dev/nvidia2 Cores=2,3
Name=gpu Type=p6000 File=/dev/nvidia3 Cores=2,3
# Set gres/mps Count value to 100 on each of the 4 available GPUs
Name=mps Count=400
```

```
# Example 2 of gres.conf
# Configure four different GPU types (with MPS)
AutoDetect=nvml
Name=gpu Type=gtx1080 File=/dev/nvidia0 Cores=0,1
Name=gpu Type=gtx1070 File=/dev/nvidia1 Cores=0,1
Name=gpu Type=gtx1060 File=/dev/nvidia2 Cores=2,3
Name=gpu Type=gtx1050 File=/dev/nvidia3 Cores=2,3
Name=mps Count=1300   File=/dev/nvidia0
Name=mps Count=1200   File=/dev/nvidia1
Name=mps Count=1100   File=/dev/nvidia2
Name=mps Count=1000   File=/dev/nvidia3
```

**NOTE**: *gres/mps* requires the use of the *select/cons\_tres*
plugin.

Job requests for MPS will be processed the same as any other GRES except
that the request must be satisfied using only one GPU per node and only one
GPU per node may be configured for use with MPS.
For example, a job request for "--gres=mps:50" will not be satisfied by using
20 percent of one GPU and 30 percent of a second GPU on a single node.
Multiple jobs from different users can use MPS on a node at the same time.
Note that GRES types of GPU and MPS can not be requested within
a single job.
Also jobs requesting MPS resources can not specify a GPU frequency.

A prolog program should be used to start and stop MPS servers as needed.
A sample prolog script to do this is included with the Slurm distribution in
the location *etc/prolog.example*.
Its mode of operation is if a job is allocated gres/mps resources then the
Prolog will have the `CUDA_VISIBLE_DEVICES`,
`CUDA_MPS_ACTIVE_THREAD_PERCENTAGE`, and
`SLURM_JOB_UID` environment variables set.
The Prolog should then make sure that an MPS server is started for that GPU
and user (UID == User ID).
It also records the GPU device ID in a local file.
If a job is allocated gres/gpu resources then the Prolog will have the
`CUDA_VISIBLE_DEVICES` and
`SLURM_JOB_UID` environment variables set
(no `CUDA_MPS_ACTIVE_THREAD_PERCENTAGE`).
The Prolog should then terminate any MPS server associated with that GPU.
It may be necessary to modify this script as needed for the local environment.
For more information see the
[Prolog and Epilog Guide](prolog_epilog.md).

Jobs requesting MPS resources will have the
`CUDA_VISIBLE_DEVICES`
and `CUDA_DEVICE_ORDER` environment variables set.
The device ID is relative to those resources under MPS server control and will
always have a value of zero in the current implementation (only one GPU will be
usable in MPS mode per node).
The job will also have the
`CUDA_MPS_ACTIVE_THREAD_PERCENTAGE`
environment variable set to that job's percentage of MPS resources available on
the assigned GPU.
The percentage will be calculated based upon the portion of the configured
Count on the Gres is allocated to a job of step.
For example, a job requesting "--gres=mps:200" and using
[configuration example 2](#MPS_config_example_2) above would be
allocated  
15% of the gtx1080 (File=/dev/nvidia0, 200 x 100 / 1300 = 15), or  
16% of the gtx1070 (File=/dev/nvidia0, 200 x 100 / 1200 = 16), or  
18% of the gtx1060 (File=/dev/nvidia0, 200 x 100 / 1100 = 18), or  
20% of the gtx1050 (File=/dev/nvidia0, 200 x 100 / 1000 = 20).

An alternate mode of operation would be to permit jobs to be allocated whole
GPUs then trigger the starting of an MPS server based upon comments in the job.
For example, if a job is allocated whole GPUs then search for a comment of
"mps-per-gpu" or "mps-per-node" in the job (using the "scontrol show job"
command) and use that as a basis for starting one MPS daemon per GPU or across
all GPUs respectively.

Please consult the
[NVIDIA Multi-Process Service documentation](https://docs.nvidia.com/deploy/pdf/CUDA_Multi_Process_Service_Overview.pdf) for more information about MPS.

Note that a vulnerability exists in previous versions of the NVIDIA driver that
may affect users when sharing GPUs. More information can be found in
[CVE-2018-6260](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-6260) and in the
[Security Bulletin: NVIDIA GPU Display Driver - February 2019](https://nvidia.custhelp.com/app/answers/detail/a_id/4772).

NVIDIA MPS has a built-in limitation regarding GPU sharing among different
users. Only one user on a system may have an active MPS server, and the MPS
control daemon will queue MPS server activation requests from separate users,
leading to serialized exclusive access of the GPU between users (see
[Section 2.3.1.1 - Limitations](https://docs.nvidia.com/deploy/mps/index.html#topic_3_3_1_1) in the MPS docs). So different users cannot
truly run concurrently on the GPU with MPS; rather, the GPU will be time-sliced
between the users (for a diagram depicting this process, see
[Section 3.3 - Provisioning Sequence](https://docs.nvidia.com/deploy/mps/index.html#topic_4_3) in the MPS docs).

## MIG Management

Beginning in version 21.08, Slurm now supports NVIDIA
*Multi-Instance GPU* (MIG) devices. This feature allows some newer NVIDIA
GPUs (like the A100) to split up a GPU into up to seven separate, isolated GPU
instances. Slurm can treat these MIG instances as individual GPUs, complete with
cgroup isolation and task binding.

To configure MIGs in Slurm, specify
`AutoDetect=nvml` in *gres.conf* for the
nodes with MIGs, and specify `Gres`
in *slurm.conf* as if the MIGs were regular GPUs, like this:
`NodeName=tux[1-16] gres=gpu:2`. An optional
GRES type can be specified to distinguish MIGs of different sizes from each
other, as well as from other GPUs in the cluster. This type must be a substring
of the "MIG Profile" string as reported by the node in its slurmd log under the
`debug2` log level. Here is an example slurm.conf
for a system with 2 gpus, one of which is partitioned into 2 MIGs where the
"MIG Profile" is `nvidia_a100_3g.20gb`:

```
AccountingStorageTRES=gres/gpu,gres/gpu:a100,gres/gpu:a100_3g.20gb
GresTypes=gpu
NodeName=tux[1-16] gres=gpu:a100:1,gpu:a100_3g.20gb:2
```

The [MultipleFiles](gres.conf.md#OPT_MultipleFiles) parameter
allows you to specify multiple device files for the GPU card.

The sanity-check AutoDetect mode is not supported for MIGs.
Slurm expects MIG devices to already be partitioned, and does not support
dynamic MIG partitioning.

For more information on NVIDIA MIGs (including how to partition them), see
[the MIG user guide](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/index.html).

## Sharding

Sharding provides a generic mechanism where GPUs can be
shared by multiple jobs. While it does permit multiple jobs to run on a given
GPU, by default it does not fence the processes running on the GPU nor
constrain its device memory; it only allows the GPU to be shared. See
[Shard device memory enforcement](#shard_device_memory) for
opt-in memory limits.
Sharding, therefore, works best with homogeneous workflows. It is
recommended to limit the number of shards on a node to equal the max possible
jobs that can run simultaneously on the node (i.e. cores or memory).
The total count of shards available on a node should be configured in
the *slurm.conf* file (e.g. "NodeName=tux[1-16] Gres=gpu:2,shard:64").
Several options are available for configuring shards in the *gres.conf* file
as listed below with examples following that:

1. No Shard configuration: The count of gres/shard elements defined in the
   *slurm.conf* will be evenly distributed across all GPUs configured on the
   node. For example, "NodeName=tux[1-16] Gres=gpu:2,shard:64" will configure
   a count of 32 gres/shard resources on each of the two GPUs.
2. Shard configuration includes only the *Name* and *Count* parameters:
   The count of gres/shard elements will be evenly distributed across all GPUs
   configured on the node. This is similar to case 1, but places duplicate
   configuration in the gres.conf file.
3. Shard configuration includes the *Name*, *File* and *Count*
   parameters: Each *File* parameter should identify the device file path of a
   GPU and the *Count* should identify the number of gres/shard resources
   available for that specific GPU device.
   This may be useful in a heterogeneous environment.
   For example, some GPUs on a node may be more powerful than others and thus be
   associated with a higher gres/shard count.
   Another use case would be to prevent some GPUs from being used for sharding (i.e.
   they would have a shard count of zero).
4. Shard configuration includes the *Name*, *Type* and *Count*
   parameters (no *File*): The *Count* is given to **every** GPU
   whose type matches the *Type* parameter (a case-insensitive substring of
   the GPU type, like GPU type matching; the most specific configuration wins).
   Unlike cases 1 and 2, the *Count* is per device, not a node total, so
   one line covers any number of GPUs of that model. One line per GPU type may
   be used to give different models different shard counts, e.g.
   "Name=shard Type=a100 Count=32" and "Name=shard Type=l40s Count=16".
   GPUs whose type matches no line get a shard count of zero.
   With this form the *slurm.conf* "Gres=" specification should declare the
   shards per type as node totals using the full GPU type names, e.g.
   "Gres=gpu:a100:2,gpu:l40s:2,shard:a100:64,shard:l40s:32".
   An untyped total (e.g. "shard:96") is accepted when it equals the sum of all
   the per-device counts.

Note that the *Cores* parameter for gres/shard is ignored, and the
*Type* parameter is ignored when *File* is also specified.
That information is copied from the gres/gpu configuration.

Note that if NVIDIA's NVML library is installed, the GPU configuration
(i.e. *Type*, *File*, *Cores* and *Links* data) will be
automatically gathered from the library and need not be recorded in the
*gres.conf* file.

Note the same GPU can be allocated either as a GPU type of GRES or as
a shard type of GRES, but not both.
In other words, once a GPU has been allocated as a gres/gpu resource it will
not be available as a gres/shard.
Likewise, once a GPU has been allocated as a gres/shard resource it will
not be available as a gres/gpu.
However the same GPU can be allocated as shard generic resources to multiple jobs
belonging to multiple users, so long as the total count of SHARD allocated to
jobs does not exceed the configured count.

By default, job requests for shards are required to fit on a single gpu on
each node. This can be overridden with a flag in the *slurm.conf*
configuration file. See [OPT\_MULTIPLE\_SHARING\_GRES\_PJ](slurm.conf.md#OPT_MULTIPLE_SHARING_GRES_PJ).

In order for this to be correctly configured, the appropriate nodes need
to have the *shard* keyword added as a GRES for the relevant nodes as
well as being added to the *GresTypes* parameter. If you want the shards
to be tracked in accounting then *shard* also needs to be added to
*AccountingStorageTRES*.
See the relevant settings in an example slurm.conf:

```
AccountingStorageTRES=gres/gpu,gres/shard
GresTypes=gpu,shard
NodeName=tux[1-16] Gres=gpu:2,shard:64
```

Some example configurations for Slurm's gres.conf file are shown below.

```
# Example 1 of gres.conf
# Configure four GPUs (with Sharding)
AutoDetect=nvml
Name=gpu Type=gp100 File=/dev/nvidia0 Cores=0,1
Name=gpu Type=gp100 File=/dev/nvidia1 Cores=0,1
Name=gpu Type=p6000 File=/dev/nvidia2 Cores=2,3
Name=gpu Type=p6000 File=/dev/nvidia3 Cores=2,3
# Set gres/shard Count value to 8 on each of the 4 available GPUs
Name=shard Count=32
```

```
# Example 2 of gres.conf
# Configure four different GPU types (with Sharding)
AutoDetect=nvml
Name=gpu Type=gtx1080 File=/dev/nvidia0 Cores=0,1
Name=gpu Type=gtx1070 File=/dev/nvidia1 Cores=0,1
Name=gpu Type=gtx1060 File=/dev/nvidia2 Cores=2,3
Name=gpu Type=gtx1050 File=/dev/nvidia3 Cores=2,3
Name=shard Count=8    File=/dev/nvidia0
Name=shard Count=8    File=/dev/nvidia1
Name=shard Count=8    File=/dev/nvidia2
Name=shard Count=8    File=/dev/nvidia3
```

**NOTE**: *gres/shard* requires the use of the *select/cons\_tres*
plugin.

Job requests for shards can not specify a GPU frequency.

Jobs requesting shards resources will have the
`CUDA_VISIBLE_DEVICES`, `ROCR_VISIBLE_DEVICES`,
or `GPU_DEVICE_ORDINAL` environment variable set
which would be the same as if it were a GPU.

Steps with shards have`SLURM_SHARDS_ON_NODE`
set indicating the number of shards allocated.

### Shard device memory enforcement

By default sharding does not fence anything: a job with one shard can
allocate the whole memory of the GPU. When
[**ConstrainDeviceMemory**](cgroup.conf.md#OPT_ConstrainDeviceMemory) is enabled in *cgroup.conf*, every shard
implicitly carries a proportional slice of the device memory of its GPU: the
detected memory capacity of the device divided by the number of shards
configured on it. A job or step allocating *k* shards of a device is
limited to *k* slices of device memory (*dmem.max*), which are
also reserved for it (*dmem.min*), enforced by the kernel through
the dmem cgroup controller. There are no new request options and scheduling
is unaffected: the shard count is the memory accounting, so any placement
that fits its shards fits its memory by construction.

Requirements:

* Linux kernel 6.14 or later with cgroup/v2, and a device driver that
  registers dmem cgroup regions (amdgpu and xe since kernel 6.14, NVIDIA since
  driver release 610). This is detected automatically: a device without a
  usable region keeps today's unenforced behavior, reported once at slurmd
  startup.
* **TaskPlugin=task/cgroup** with **ConstrainDevices=yes**, since
  without the device access filter the memory limits could be evaded through
  devices not allocated to the job. Enabling **ConstrainDeviceMemory**
  without them is rejected at startup.
* The dmem controller enabled down to the Slurm cgroup, e.g. with
  **EnableControllers=yes** in *cgroup.conf* when systemd does not
  delegate it.

The slurmd logs one line per sharding device at startup showing the
detected region, capacity, and per-shard slice, and whether enforcement is
active, for example:

```
shard: /dev/nvidia0 shards=16 region=nvidia/0000:01:00/vidmem capacity=16013MiB slice=1000MiB dmem=enforced
```

Jobs with enforced shards have
`SLURM_SHARD_MEM_PER_GPU` set to a
comma-separated list of *pci\_addr*=*size*M pairs, one per allocated
device, so applications can budget their allocations (e.g. resolving the
device with `cudaDeviceGetByPCIBusId()`).
Exceeding the limit makes further device memory allocations of the job fail;
the exact error observed by the application depends on the vendor driver. The
*gres/gpumem* usage TRES is fed from the kernel counter on enforced
devices, extending GPU memory usage accounting to any vendor with dmem
regions.

A specific device can be excluded from enforcement with
**DmemRegion=off** on its *gres.conf* gpu record, and the region
autodetection can be overridden with
[**DmemRegion**](gres.conf.md#OPT_DmemRegion). The regions
available on the node are listed in
`/sys/fs/cgroup/dmem.capacity`.

Limitations:

* Unified/managed memory is not charged: allocations made through
  unified memory interfaces (e.g.
  `cudaMallocManaged()`) are handled by the
  NVIDIA UVM driver rather than the regular device memory allocator, so they
  do not count against the dmem limit and are effectively unconstrained.
* MIG instances stay unenforced: all instances carved out of a physical
  GPU share its single PCI device, so its dmem region is shared by every
  instance and cannot be attributed to one of them.
* Coherent platforms where GPU memory is exposed to the operating system
  as NUMA memory nodes are not reported by the dmem controller, as their
  GPU memory is managed as system memory, so this mechanism does not apply.

Example of a node with one 16 GB GPU split into 16 shards:

```
# slurm.conf
AccountingStorageTRES=gres/gpu,gres/shard,gres/gpumem
GresTypes=gpu,shard
NodeName=node1 Gres=gpu:1,shard:16
ProctrackType=proctrack/cgroup
TaskPlugin=task/cgroup,task/affinity

# gres.conf
AutoDetect=nvml
Name=shard Count=16

# cgroup.conf
ConstrainDevices=yes
ConstrainDeviceMemory=yes
EnableControllers=yes
```

At startup the slurmd logs the detected region and the resulting
per-shard slice for each sharding device:

```
shard: /dev/nvidia0 shards=16 region=nvidia/0000:01:00/vidmem capacity=16013MiB slice=1000MiB dmem=enforced
```

A job allocating three shards is limited to three slices. The limit is
exported to the application through the environment and written to the
dmem cgroup of the job and each of its steps (the job cgroup directory is
named after the job SLUID, or after the job id with
**CgroupJobIdPaths=yes**):

```
$ srun --gres=shard:3 sh -c 'echo $SLURM_SHARD_MEM_PER_GPU'
0000:01:00.0=3002M

$ srun --gres=shard:3 sh -c \
    'cat /sys/fs/cgroup/system.slice/slurmstepd.scope/$SLURM_JOB_SLUID/dmem.max'
nvidia/0000:01:00/vidmem 3148288512
```

Device memory allocations beyond the limit fail, while the rest of the
device memory remains available to the other jobs sharding the GPU
(`alloc_vram` here is a small test program
allocating the given number of MiB):

```
$ srun --gres=shard:3 ./alloc_vram 4000
cudaMalloc failed: out of memory (after 3002 of 4000 MiB)
```

The device memory used by the job is accounted in the
*gres/gpumem* TRES, visible while it runs and preserved after it
completes:

```
$ sstat -a -j 42 --format=JobID,TRESUsageInMax%70
JobID                                                                TRESUsageInMax
------------ ----------------------------------------------------------------------
42.extern                                                                  energy=0
42.batch     cpu=00:00:00,energy=0,fs/disk=87713,gres/gpumem=2128M,gres/gpuutil=1,+

$ sacct -j 42 --format=JobID,State,TRESUsageInTot%70
JobID             State                                                         TRESUsageInTot
------------ ---------- ----------------------------------------------------------------------
42            COMPLETED
42.batch      COMPLETED cpu=00:00:00,energy=0,fs/disk=87713,gres/gpumem=2128M,gres/gpuutil=1,+
42.extern     COMPLETED                                                               energy=0
```

Example of a node with three different GPU models from two vendors
(*cgroup.conf* as in the previous example):

```
# slurm.conf
GresTypes=gpu,shard
NodeName=node2 Gres=gpu:rtx_5090:1,gpu:rtx_5060_ti:1,gpu:amd_granite:1,shard:rtx_5090:16,shard:rtx_5060_ti:16,shard:amd_granite:4

# gres.conf
# nvml detects the two NVIDIA devices; the AMD one is configured explicitly
AutoDetect=nvml
Name=gpu Type=rtx_5060_ti File=/dev/nvidia1 DmemRegion=off
Name=gpu Type=amd_granite File=/dev/dri/renderD128
Name=shard Type=rtx_5090 Count=16
Name=shard Type=rtx_5060_ti Count=16
Name=shard Type=amd_granite Count=4
```

Each device gets its own slice from its own capacity and shard count.
The excluded device logs its region with *dmem=off*:

```
shard: /dev/nvidia0 shards=16 region=nvidia/0000:17:00/vidmem capacity=32607MiB slice=2037MiB dmem=enforced
shard: /dev/nvidia1 shards=16 region=nvidia/0000:b3:00/vidmem dmem=off
shard: /dev/dri/renderD128 shards=4 region=drm/0000:79:00.0/vram capacity=4080MiB slice=1020MiB dmem=enforced
```

A job sharding the RTX 5090 is limited using the RTX 5090 slice:

```
$ srun --gres=shard:rtx_5090:4 sh -c 'echo $SLURM_SHARD_MEM_PER_GPU'
0000:17:00.0=8151M
```

A job sharding the excluded RTX 5060 Ti behaves exactly as without
enforcement: no environment variable is set and no dmem limits are
written, while jobs on the other two devices of the node remain enforced:

```
$ srun --gres=shard:rtx_5060_ti:2 sh -c 'echo ${SLURM_SHARD_MEM_PER_GPU:-unset}'
unset
```

## Shared GRES Usage

Commands that display node GRES usage, such as `sinfo -O GresUsed`
and `scontrol show node -d`, list each allocated GRES.
Shared GRES entries (MPS and shards) show the total allocated count
followed by one entry per device (GPU):

```
$ sinfo -O NodeList:10,Gres:20,GresUsed:0
NODELIST  GRES                GRES_USED
node0     gpu:4,shard:20      gpu:1(IDX:0),shard:8(-/5,5/5,3/5,0/5)
```

In this example, the GRES\_USED column shows that 1 GPU and 8 shards are
allocated. Since shards are an alternate form of GPUs, both entries represent
usage of the same underlying GPU devices:

* `gpu:1(IDX:0)` shows that GPU 0 is allocated as a whole GPU.
* `shard:8(-/5,5/5,3/5,0/5)` shows that 8 shards are allocated
  across the four GPUs:
  + `-/5` means GPU 0 is unavailable for shards because it is
    allocated as a whole GPU.
  + `5/5` means GPU 1 has all 5 shards allocated.
  + `3/5` means GPU 2 has 3 of 5 shards allocated, and up to 2
    more shards can still be allocated.
  + `0/5` means GPU 3 has no shards allocated, and is available to be
    allocated as either a whole GPU or up to 5 shards.

A GPU that is drained takes no new shards,
and its entry starts with `d`. These forms are not in the example
above:

* `d/5` means the backing GPU is drained with no shards
  allocated.
* `d3/5` means the backing GPU is drained but still has 3 shards
  allocated from before the drain.