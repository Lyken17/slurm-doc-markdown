# Slurm Workload Manager - tpu.yaml

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

# tpu.yaml

Section: Slurm Configuration File (5)  
Updated: Slurm Configuration File  
[Index](#index)

## NAME

tpu.yaml - Slurm configuration file for TPU accelerator families.

## DESCRIPTION

**tpu.yaml** describes the TPU accelerator families present on a cluster.
It is read by the **job\_submit/tpu** plugin, which validates **--layout**
requests against it, and by the **gres/tpu** plugin, which uses it to detect
accelerator chips on a compute node.

The file is located in the same directory as **slurm.conf**.
It is only required on clusters that enable one of those plugins.
In configless mode it is sent to the compute nodes along with
**slurm.conf**.

The file is parsed as YAML.
Changes take effect on **scontrol reconfigure** or daemon restart.

Each **type**, and each pair of **vendor\_id** and **pci\_device\_id**,
may appear only once.
If the file is missing, cannot be parsed, or has an invalid entry, slurmctld
logs an error and **job\_submit/tpu** rejects every **--layout** request
for TPUs.
In the same cases slurmd detects no chips, and reports it only at the debug
log level.
Keys that this page does not describe are ignored and also reported only at
the debug log level, so a misspelled key is not applied and causes no error.

## CONFIGURATION

To use TPUs, set the following in **slurm.conf**:

•: **GresTypes=tpu**, so the nodes can report their chips. •: **JobSubmitPlugins=tpu**, so jobs can request chips with **--layout**. •: **Gres=tpu:***type***:***count* on each node, where *type* is the **type** of its family in this file. *count* is the number of chips on the node, which is the product of the components of the family's **shape\_per\_node**, for example 4 for **"2x2x1"**. A chip counts once even when it presents several PCI functions, as tpu7x chips do.

To allocate multi-node layouts as contiguous blocks of the fabric, also use
**TopologyPlugin=topology/block**, with blocks that match the segments
described here.
Make each base block the nodes of the smallest multi-node geometry of the
family, and give block sizes that double up to the number of nodes in a
segment.
For the tpu7x family in the example below, a base block is the 2 nodes of a
*2x2x2* geometry and a segment is 16 nodes, so the block sizes are 2, 4, 8
and 16.
See **[topology.yaml](topology.yaml.md)**(5).

## PARAMETERS

The file contains a single top-level key.

**tpu\_types**
:   A list of accelerator family descriptions.
    Each entry accepts the following keys.

    : **type** : : The canonical family name, for example **tpu7x** or **v6e**. This is the name users give to **--layout**, and the GRES type of the family's chips. Names are matched exactly; there are no aliases or abbreviations. Required. : **shape\_per\_node** : The chip geometry attached to a single node, as a <*x*>x<*y*>[x<*z*>] string, for example **"2x2x1"**. The number of components, 2 or 3, determines the fabric's dimensionality, and therefore how many components a **--layout** geometry for this family must have. Required. : A requested geometry must be a whole multiple of this shape along every axis, not merely a multiple of its chip count. On a family whose nodes are **"2x2x1"**, a request of *1x2x4* is eight chips (two nodes), but its first axis is not a multiple of 2, so it is rejected. : **shape\_per\_segment** : The chip geometry of one segment (the scale beyond which an optical circuit switch (OCS) is used), for example **"4x4x4"**. Must be a whole multiple of **shape\_per\_node** along every axis and have the same number of components. Required. : Requests that fit within one segment must divide this shape evenly along every axis and have their largest dimension at most twice their smallest. Larger requests are stitched together from whole segments over an OCS, where supported, and so must be a whole multiple of this shape along every axis. : **nodes\_per\_pod** : The pod limit: the largest allocation this family can serve, counted in nodes. A request larger than this is rejected at submit time. Must be a whole number of segments. For a family with no OCS tier this is the size of a single segment. Required. : **vendor\_id** : The PCI vendor ID of these chips, as the zero-padded hexadecimal string that */sys/bus/pci/devices/\*/vendor* shows, for example **"0x1ae0"**. Optional; defaults to **"0x1ae0"** if omitted. : **pci\_device\_id** : The PCI device ID of these chips, as the zero-padded hexadecimal string that */sys/bus/pci/devices/\*/device* shows, for example **"0x0076"**. The comparison is case insensitive but otherwise exact, so **"0x76"** does not match. Used together with **vendor\_id**. Optional; chips of the family are not detected if omitted.

## DETECTION

The **gres/tpu** plugin finds a node's chips in sysfs by the
**vendor\_id** and **pci\_device\_id** of each family.
Detection runs unless **gres.conf** sets **AutoDetect=off**.
**AutoDetect=tpu** is accepted and has the same effect as leaving
**AutoDetect** unset.

When chips are detected, they replace every **Name=tpu** line for the node
in **gres.conf**.
Lines for other GRES are kept.

Each chip is handed to a job through VFIO, so the node must boot with an IOMMU
enabled, and the chips must be bound to the **vfio-pci** driver.
A chip that has no IOMMU group is logged and ignored.
VFIO hands out an IOMMU group as a whole, so each chip needs a group of its
own.
Chips that share a group, as happens when the PCI bridge above them does not
have ACS enabled, are also logged and ignored, and the node reports fewer
chips.
Run **slurmd -G** on a node to see the chips it detects.

The chips of a node are numbered from zero in the order of their lowest IOMMU
group.
A job is given the numbers of its chips on the node in **SLURM\_JOB\_TPUS**,
and the tasks of a step in **SLURM\_STEP\_TPUS**.

## USING --layout

A job requests chips with
**--layout**=*type*=*geometry*, for example
**--layout=tpu7x=2x2x4**.
The **job\_submit/tpu** plugin then:

•: checks the geometry against the rules above; •: sets the job's node count to the number of nodes the geometry covers, and refuses a **-N** that asks for a different count; •: adds **gres/tpu:***type***:***chips* to the job's per-node GRES, where *chips* is the number of chips on one node, keeping any other GRES the job requests; •: refuses a job that also requests TPUs with **--gres** or **--tres-per-task**.

The value of **--layout** is a comma-separated list of
*key*=*value* pairs.
Only one pair may request TPUs: one whose key is a family **type**, or whose
value is a geometry.
Other pairs are passed through to other plugins unchanged.

The layout of a job can be changed with **scontrol update** only while the
job is pending.
A pending job that has a TPU layout keeps its TPUs when its GRES is changed,
and refuses a node count that its layout does not need.

Removing the TPU pair from the layout of a job removes its TPUs, but the node
count of the job is the one the layout set, and the count requested before it
is not kept.
So the same update must give the new node count, for example
**scontrol update JobId=***id* **Layout= NumNodes=1**.
Without **NumNodes**, the update is refused.

## NOTES

The number of chips on a node, the fabric's dimensionality, and the number of
nodes in a segment are all derived from **shape\_per\_node** and
**shape\_per\_segment**, and are not configured separately.
A count cannot express a shape: on the family in the example below, 256 chips
is 64 nodes, which could be *4x4x16* or *4x8x8*.
Distinguishing the two is the purpose of **--layout**.

Dimensions are never reordered.
A multi-node geometry whose dimensions are not in non-decreasing order (for
example, *4x2x2* instead of *2x2x4*) is rejected rather than sorted.

## EXAMPLE

```
tpu_types:
  - type: tpu7x
    shape_per_node: "2x2x1"
    shape_per_segment: "4x4x4"
    nodes_per_pod: 2304
    vendor_id: "0x1ae0"
    pci_device_id: "0x0076"

  - type: v6e
    shape_per_node: "2x2"
    shape_per_segment: "16x16"
    nodes_per_pod: 64
    vendor_id: "0x1ae0"
    pci_device_id: "0x006f"
```

## COPYING

Copyright (C) 2026 Google LLC.

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

**[slurm.conf](slurm.conf.md)**(5), **[gres.conf](gres.conf.md)**(5), **[topology.yaml](topology.yaml.md)**(5),
**[sbatch](sbatch.md)**(1), **[salloc](salloc.md)**(1), **[srun](srun.md)**(1), **[slurmd](slurmd.md)**(8)

---



## Index

[NAME](#lbAB): [DESCRIPTION](#lbAC): [CONFIGURATION](#lbAD): [PARAMETERS](#lbAE): [DETECTION](#lbAF): [USING --layout](#lbAG): [NOTES](#lbAH): [EXAMPLE](#lbAI): [COPYING](#lbAJ): [SEE ALSO](#lbAK)

---

This document was created by
*man2html* using the manual pages.  
Time: 20:23:17 GMT, November 24, 2026