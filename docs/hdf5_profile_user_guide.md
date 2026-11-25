# Slurm Workload Manager - Profiling Using HDF5 User Guide

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

# Profiling Using HDF5 User Guide

## Contents

* [Overview](#Overview)
* [Administration](#Administration)
* [Profiling Jobs](#Profiling)
* [HDF5](#HDF5)
* [Data Structure](#DataSeries)

## Overview

The acct\_gather\_profile/hdf5 plugin allows Slurm to coordinate collecting
data on jobs it runs on a cluster that is more detailed than is practical to
include in its database. The data comes from periodically sampling various
performance data either collected by Slurm, the operating system, or
component software. The plugin will record the data from each source
as a **Time Series**. Totals for each statistic can be computed from the
time series with [sh5util](sh5util.md).

Time Series are energy data collected by an acct\_gather\_energy plugin,
I/O data from a network interface collected by an acct\_gather\_interconnect
plugin, I/O data from parallel file systems such as Lustre collected by an
acct\_gather\_filesystem plugin, and task performance data such as local disk I/O,
cpu consumption, and memory use from a jobacct\_gather plugin.
Data from other sources may be added in the future.

The data is collected into a file on a shared file system for each step on
each allocated node of a job and then merged into an HDF5 file.
This shared file system architecture was chosen because it is possible
that the data is voluminous. Solutions that pass data to the Slurm control
daemon via RPC may not scale to very large clusters or jobs with
many allocated nodes.

## Administration

### Shared File System

The HDF5 Profile Plugin requires a common shared file system on all
the compute nodes. While a job is running, the plugin writes a
file into this file system for each step of the job on each node. When
the job ends, the merge process is launched and the node-step files
are combined into one HDF5 file for the job.

The root of the directory structure is declared in the **ProfileHDF5Dir**
option in the acct\_gather.conf file. The directory will be created by
Slurm if it doesn't exist. Each user will have
their own directory created in the ProfileHDF5Dir which contains
the HDF5 files. All the directories and files are created by the
SlurmdUser which is usually root. The user specific directories, as well
as the files inside, are chowned to the user running the job so they
can access the files. Since user root is usually creating these
files/directories a root squashed file system will not work for
the ProfileHDF5Dir.

Each user that creates a profile will have a subdirectory in the profile
directory that has read/write permission only for the user.

  

### Configuration parameters

The profile plugin is enabled in the
[slurm.conf](slurm.conf.md) file and it is internally
configured in the
[acct\_gather.conf](acct_gather.conf.md) file.

### slurm.conf parameters

**AcctGatherProfileType**=acct\_gather\_profile/hdf5
:   Enables the HDF5 plugin.

**JobAcctGatherFrequency**=<freq>
:   Sets the sampling frequency for data types, e.g.
    `task=sec,energy=sec,filesystem=sec,network=sec`.

### acct\_gather.conf parameters

These parameters are directly used by the HDF5 Profile Plugin.

**ProfileHDF5Dir**=<path>
:   This parameter is the path to the shared folder into which the
    acct\_gather\_profile plugin will write detailed data as an HDF5 file.
    The directory is assumed to be on a file system shared by the controller and
    all compute nodes. This is a required parameter.

**ProfileHDF5Default**=[options]
:   A comma-delimited list of data types to be collected for each job
    submission. Use this option with caution. A node-step file will be created on
    every node for every step of every job. They will not automatically be merged
    into job files. (Even job files for large numbers of small jobs would fill the
    file system.) This option is intended for test environments where you
    might want to profile a series of jobs but do not want to have to
    add the --profile option to the launch scripts.
    The options are described below and in the man pages for acct\_gather.conf,
    srun, salloc and sbatch commands.

### Time Series Control Parameters

Other plugins add time series data to the HDF5 collection. The HDF5
profile plugin stores samples produced by the corresponding accounting gather
plugin configured in slurm.conf: AcctGatherEnergyType,
AcctGatherFilesystemType, AcctGatherInterconnectType, or JobAcctGatherType.
They typically have a default polling frequency specified in slurm.conf in the
JobAcctGatherFrequency parameter. The polling frequency can be overridden
using the --acctg-freq [srun](srun.md) parameter.
Both parameters use the form task=sec,energy=sec,filesystem=sec,network=sec.

The acct\_gather\_energy/ipmi plugin also needs the EnergyIPMIFrequency value
set in the acct\_gather.conf file. This sets the rate at which that plugin
samples the external sensors. This value should be the same as the energy=sec in
either JobAcctGatherFrequency or --acctg-freq.

Note that the IPMI and profile sampling are not synchronous.
The profile sample simply takes the last available IPMI sample value.
If the profile energy sample is more frequent than the IPMI sample rate,
the IPMI value will be repeated. If the profile energy sample is greater
than the IPMI rate, IPMI values will be lost.

Also note that smallest effective IPMI (EnergyIPMIFrequency) sample rate
for 2013 era Intel processors is 3 seconds.

## Profiling Jobs

### Data Collection

The --profile option on salloc|sbatch|srun controls whether data is
collected and what type of data is collected. If --profile is not specified
no data is collected unless the **ProfileHDF5Default**
option is used in acct\_gather.conf. --profile on the command line overrides
any value specified in the configuration file.

**--profile**=<all|none|[energy[,|task[,|filesystem[,|network]]]]>
:   Enables detailed data collection by the acct\_gather\_profile plugin.
    Detailed data is typically a time series stored in an HDF5 file for the job.
:   **All**
    :   All data types are collected. (Cannot be combined with other values.)

    **None**
    :   No data types are collected. This is the default. (Cannot be
        combined with other values.)

    **Energy**
    :   Energy data is collected.

    **Filesystem**
    :   Filesystem data is collected. Currently only
        Lustre filesystem is supported.

    **Network**
    :   Network data is collected.

    **Task**
    :   Task (I/O, Memory, ...) data is collected.

  

### Data Consolidation

The node-step files are merged into one HDF5 file for the job using the
[sh5util](sh5util.md).

If the job is started with sbatch, the command line may be added to the
normal launch script. For example:

```
sbatch -n1 -d$SLURM_JOB_ID --wrap="sh5util -j $SLURM_JOB_ID"
```

### Data Extraction

The [sh5util](sh5util.md) program can also be used to extract
specific data from the HDF5 file and write it in *comma separated value (csv)*
form for importation into other analysis tools such as spreadsheets.

## HDF5

HDF5 is a well known structured data set that allows heterogeneous but
related data to be stored in one file
(e.g. sections for energy statistics, network I/O, task data, etc.).
Its internal structure resembles a
file system with **groups** being similar to *directories* and
**data sets** being similar to *files*. It also allows **attributes**
to be attached to groups to store application defined properties.

There are commodity programs, notably
[HDFView](https://www.hdfgroup.org/download-hdfview/), for viewing and manipulating these files.

## Data Structure

In the merged job file, the top-level **Steps** group contains a group
for each **step** of the job, named by step ID (**batch** for the batch
step). Within each step, there will be a **Nodes** group. Each node
group contains the node-level time series datasets for the configured
accounting gather plugins and a **Tasks** group for per-task data.
For example, step 0 of a job with energy, filesystem, network, and task
profiling enabled and two tasks on node1 contains:

```
/Steps/0/Nodes/node1/Energy
/Steps/0/Nodes/node1/Filesystem
/Steps/0/Nodes/node1/Network
/Steps/0/Nodes/node1/Tasks/0
/Steps/0/Nodes/node1/Tasks/1
```

* The **Nodes** group will have a group for each node in the step allocation.
  For each node group, node-level series such as Energy, Filesystem, and
  Network are stored as HDF5 datasets.
  + Each dataset contains an **ElapsedTime** field for seconds since the step
    started and an **EpochTime** field for the sample's UNIX timestamp, followed
    by the fields defined by the accounting gather plugin that produced the
    samples.
  + The [sh5util](sh5util.md) command can aggregate time series data
    when extracting totals.
  + The **Tasks** group contains one dataset for each task that ran on the node,
    named by task ID.

  

### Energy Data

An **AcctGatherEnergyType** plugin is required in slurm.conf
to collect energy data.
Appropriately set energy=freq in either JobAcctGatherFrequency in slurm.conf
or in --acctg-freq on the command line.
Also set EnergyIPMIFrequency in acct\_gather.conf when using
**acct\_gather\_energy/ipmi**.

Each Energy sample contains **ElapsedTime** and **EpochTime**.
Additional data items are defined by the configured energy plugin and may vary
by hardware. The [sh5util](sh5util.md) command can list the
fields present in a job file.

**acct\_gather\_energy/rapl**, **acct\_gather\_energy/ibmaem**, **acct\_gather\_energy/pm\_counters**
:   **Power**

**acct\_gather\_energy/ipmi**
:   **<label>Power**, where label comes from
    EnergyIPMIPowerSensors; the default label is **Node**.

**acct\_gather\_energy/gpu**
:   **GPU0Power**, **GPU1Power**, ...

**acct\_gather\_energy/xcc**
:   **Energy**, **CurrPower**

### Filesystem Data

An **AcctGatherFilesystemType** plugin is required in slurm.conf
to collect filesystem data.
Appropriately set filesystem=freq in either JobAcctGatherFrequency in slurm.conf
or in --acctg-freq on the command line.

Each Filesystem sample contains **ElapsedTime** and **EpochTime**.
The Lustre plugin adds the following data items.

**Reads**
:   Number of read operations.

**ReadMB**
:   Number of megabytes read.

**Writes**
:   Number of write operations.

**WriteMB**
:   Number of megabytes written.

### Network Data

An **AcctGatherInterconnectType** plugin is required in slurm.conf
to collect interconnect data.
Appropriately set network=freq in either JobAcctGatherFrequency in slurm.conf
or in --acctg-freq on the command line.

Each Network sample contains **ElapsedTime** and **EpochTime**
in addition to the following data items.

**PacketsIn**
:   Number of packets coming in.

**PacketsOut**
:   Number of packets going out.

**InMB**
:   Number of megabytes coming in through the interface.

**OutMB**
:   Number of megabytes going out through the interface.

### Task Data

A **JobAcctGatherType** plugin is required in slurm.conf
to collect task data.
Appropriately set task=freq in either JobAcctGatherFrequency in slurm.conf
or in --acctg-freq on the command line.

Each Task sample contains **ElapsedTime** and **EpochTime**.
The job accounting gather plugins add the following data items.

**CPUFrequency**
:   CPU Frequency at time of sample.

**CPUTime**
:   Seconds of CPU time used during the sample.

**CPUUtilization**
:   CPU Utilization during the interval.

**GPUMemMB**
:   GPU memory used, in megabytes.

**GPUUtilization**
:   GPU utilization during the interval.

**RSS**
:   Value of RSS at time of sample.

**VMSize**
:   Value of VM Size at time of sample.

**Pages**
:   Pages used in sample.

**ReadMB**
:   Number of megabytes read from local disk.

**WriteMB**
:   Number of megabytes written to local disk.