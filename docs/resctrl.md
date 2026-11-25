# Slurm Workload Manager - Resctrl Task Plugin

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

# Resctrl Task Plugin

## Overview

On non-exclusive jobs, the **task/resctrl** plugin confines the
processes of every step to a Linux resource control (resctrl) group. Resctrl
is the kernel interface to
Arm MPAM (Memory System Resource Partitioning and Monitoring), Intel RDT
(Resource Director Technology), and AMD PQoS (Platform Quality of Service),
which partition memory bandwidth and cache capacity among groups of tasks. It
is exposed as a filesystem mounted on `/sys/fs/resctrl`, where
every directory is a group whose `schemata` file holds the limits
applied to the tasks listed in its `tasks` file.

The use case is a node shared between GPU jobs and CPU-only jobs, where the
CPU-only jobs must not consume the memory bandwidth the GPU jobs depend on.
The administrator sets the limits of three fixed groups in
[resctrl.yaml](resctrl.yaml.md), slurmd creates them on the
nodes, and slurmstepd places each step in the group matching the resources
of its job on that node. Users have no control over the placement, and no
option or environment variable exposes it. This plugin is experimental.

## Requirements

* A kernel with resctrl support for the hardware. Arm MPAM is exposed through
  resctrl starting with Linux 7.1 (`CONFIG_ARM64_MPAM` together with
  `CONFIG_RESCTRL_FS`); Intel RDT and AMD PQoS have been supported for
  many releases (`CONFIG_X86_CPU_RESCTRL`). The filesystem type must
  appear in `/proc/filesystems`.
* The **serializer/yaml** plugin, which requires libyaml at build time,
  to read `resctrl.yaml`.
* GPUs with device files (**File**) and CPU affinity (**Cores**) in
  [gres.conf](gres.conf.md), or found by **AutoDetect**, so that
  the plugin can tell which socket each is attached to. The sockets are those
  slurmd detects, whatever the node definition in `slurm.conf`
  says.
* Tasks bound to the CPUs of their GPUs, with **task/cgroup** or
  **task/affinity** and cores allocated near the GPUs, so that the traffic of
  a job reaches the memory domain its group was sized for.

## Configuration

Add **task/resctrl** to
[TaskPlugin](slurm.conf.md#OPT_TaskPlugin) in
`slurm.conf`, for example
`TaskPlugin=task/cgroup,task/affinity,task/resctrl`, then set the
limits of the three groups in `resctrl.yaml`, in the same directory
as `slurm.conf`. In [configless](configless_slurm.md)
mode the file is kept on the slurmctld host, which sends it to the nodes with
`slurm.conf`, and deleting it there deletes it from the nodes on
their next reconfigure. This example is for nodes whose
`/sys/fs/resctrl/schemata` lists the `MB` domains 0 and
1:

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

All three groups must be defined and no other name is accepted. On every
start, including the re-execution triggered by `scontrol
reconfigure`, slurmd mounts the filesystem when it is not already
mounted, creates the group directories under `/sys/fs/resctrl`,
and writes their `schemata`. Slurm never unmounts the filesystem,
so a changed `mount_options` takes effect only once
`/sys/fs/resctrl` has been unmounted while no jobs run, for example
by rebooting the node. Directories that already exist are
reused, and Slurm never removes a group; to stop confining steps, remove
**task/resctrl** from **TaskPlugin** or delete `resctrl.yaml`.
The three groups, the root group, and any group created outside Slurm must fit
in the smallest `/sys/fs/resctrl/info/*/num_closids`, or slurmd
refuses to start. The attributes of the file are described in
[resctrl.yaml](resctrl.yaml.md).

On a node without kernel support for resctrl, without
`resctrl.yaml`, or where the filesystem cannot be mounted on
`/sys/fs/resctrl`, slurmd does not manage the groups, so
**TaskPlugin** can be set cluster-wide.

**NOTE**: A changed `schemata` applies immediately to the
jobs already running in the group. The groups are written in the order of the
file, so when the `schemata` of one is rejected, the groups before
it already have their new limits. A slurmd that fails to reconfigure keeps
running only when it runs as a daemon or under systemd; in the foreground it
exits. Either way it refuses to start again until the file is fixed. Testing
changes on a single node before applying them cluster-wide is
recommended.

### Schemata values

Slurm writes the `schemata` exactly as configured, so the
values must follow the conventions of the hardware. They are documented in the
kernel resctrl documentation and discoverable in
`/sys/fs/resctrl/schemata` and under
`/sys/fs/resctrl/info`. In particular:

* The memory bandwidth resource (`MB`) takes one value per memory
  domain. It is a percentage on Intel and Arm MPAM systems, rounded up to a
  multiple of `info/MB/bandwidth_gran`. A value below
  `info/MB/min_bandwidth` is rejected, not raised, and the rejected
  `schemata` is fatal to slurmd. On AMD systems the value is
  expressed in units of 1/8 GB/s rather than as a percentage. The
  `mba_MBps` mount option, where the kernel supports it, changes the
  unit to MiBps.
* A value is a limit for the group, not a reservation and not per job. On
  Intel without `mba_MBps` it throttles each core, so more jobs in a
  group draw more bandwidth. The values of all groups may add up to more than
  100 percent.
* A write only changes the resources and domains it lists: a line or domain
  left out keeps its previous limit, and a resource or domain the node does not
  have is rejected, so the file must match every node that reads it. A node with
  resctrl for cache allocation but no memory bandwidth control rejects an
  `MB` line, for example.
* Cache portion masks (`L3`, `L2`) may overlap between
  groups.

## Group selection

The group is chosen per job and node when a step starts, and depends on the
GPUs the job was allocated on that node and the sockets they are attached to:

| Job on the node | Group |
| --- | --- |
| Owns the whole node (`--exclusive`, `--exclusive=topo`, **Exclusive=NODE**, or **Exclusive=TOPO**) | none; the step stays in the group of slurmd, normally the root group |
| No GPU | `cpu_only` |
| At most one GPU on any socket | `gpu_one_per_socket` |
| Two or more GPUs on one socket | `gpu_two_per_socket` |

So on a node with two sockets and two GPUs each, a two-GPU job goes to
`gpu_two_per_socket` when both GPUs share a socket, and to
`gpu_one_per_socket` when they do not. A three- or four-GPU
job always goes to `gpu_two_per_socket`. On a given node, every step
of the job uses the same group, including the batch script and the external
step, whatever the step itself requests.

Jobs with `--exclusive=user` or `--exclusive=mcs` share
the node and are placed like the others. So are `--exclusive` jobs
in a partition with **OverSubscribe=FORCE** and a count above 1 (the default
is 4), since that partition shares every node whatever the job requests.
Shards and MPS slices count as the GPU
they are carved out of, once per physical device. A GPU whose CPUs span several
sockets counts on each of them, and a GPU without **File** or known CPUs
counts on all.

The slurmstepd thread that forks the tasks joins the group first, so the
tasks inherit the membership. Processes that
[pam\_slurm\_adopt](pam_slurm_adopt.md) places in the external step
are moved when they are adopted. Every placement is
logged in the slurmd log file with the group, the number of GPUs, and the most
GPUs on one socket.

## Limitations

* CPU-only jobs are limited to the `cpu_only` value even when no
  GPU job runs on the node.
* A job with GPUs on several sockets is placed by its busiest socket, and
  the same limits apply on the other sockets.
* Only traffic issued by the CPUs is limited. Memory accesses initiated by
  the GPUs themselves are not tagged with the group of the job.
* Slurm does not collect monitoring data. The counters of a group in
  `/sys/fs/resctrl/<group>/mon_data` can be read by hand and
  cover all the jobs of the group together. Per-job monitoring, per-job groups,
  and the `cpus` file of the groups are not supported.
* Steps launched by an **srun** older than 26.05 are placed as if the
  job were not exclusive, because their credential does not carry the
  exclusivity of the job.