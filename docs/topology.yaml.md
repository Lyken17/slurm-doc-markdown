# Slurm Workload Manager - topology.yaml

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

# topology.yaml

Section: Slurm Configuration File (5)  
Updated: Slurm Configuration File  
[Index](#index)

## NAME

topology.yaml - Slurm configuration file for the topology plugins

## DESCRIPTION

**topology.yaml** is a YAML-formatted configuration file that defines
multiple network topologies for optimizing job resource allocation in Slurm.
The file must be located in the same directory as **slurm.conf**. Any text
following a "#" in this file is treated as a comment through the end of that
line.

Additional details are available in **[topology.conf](topology.conf.md)**(5) and in the
Topology Guide: <<https://slurm.schedmd.com/topology.html>>

**NOTE**: Slurm will first check for topology.yaml.
If this file exists, topology.conf will be ignored.

## PARAMETERS

Each topology contains the following attributes:

**topology**
:   Unique name of the topology, will be used to identify it on partition
    configurations. Must be the first attribute.

    : **cluster\_default** : The first topology defined with **cluster\_default: true** will be used for partitions without an explicitly specified topology and cluster-wide operations not tied to a partition (e.g., slurmctld-to-slurmd communication). Defaults to **false**.

Each topology must also define exactly one of the following topology types:

: **block** : This topology will use the **topology/block** plugin. Must contain additional fields, see below. : **flat** : If set to **true**, this topology will use the **topology/flat** plugin, which is the default if no TopologyPlugin or topology.yaml is specified. May also be set to a dictionary of options, see "Flat definitions" below. : **ring** : This topology will use the **topology/ring** plugin. Must contain additional fields, see below. : **torus3d** : This topology will use the **topology/torus3d** plugin. Must contain additional fields, see below. : **tree** : This topology will use the **topology/tree** plugin. Must contain additional fields, see below.

### Block definitions

Each block topology contains the following attributes:

**block\_sizes**
:   List of the planning base block size, alongside any
    higher-level block sizes that would be enforced.
    Successive **BlockSizes** must be a power of two larger than the prior values.

    : **blocks** : List of blocks available in this topology. Each block contains the following attributes: : **block** : The name of a block. This name is internal to Slurm and arbitrary. Each block should have a unique name. This field must be specified. : **nodes** : Child nodes of the named block.

### Tree definitions

Each tree topology contains the following attribute:

**switches**
:   List of switches available in this topology. Each switch contains the following
    attributes:

    : **switch** : The name of a switch. This name is internal to Slurm and arbitrary. Each switch should have a unique name. This field must be specified and cannot be longer than 64 characters. : **children** : Child switches of the named switch. : **nodes** : Child nodes of the named leaf switch.

### Ring definitions

Each ring topology contains the following attribute:

**rings**
:   List of rings available in this topology. Each ring contains the following
    attributes:

    : **ring** : The name of a ring. This name is internal to Slurm and arbitrary. Each ring should have a unique name. This field must be specified. : **nodes** : Ordered list of child nodes in the ring. A maximum of 16 nodes can be specified per ring.

### Torus3d definitions

Each torus3d topology contains the following attribute:

**toruses**
:   List of 3D torus definitions. Each torus contains the following attributes:

    : **name** : The name of the torus. This name is internal to Slurm and arbitrary. Each torus should have a unique name. This field must be specified. : **dims** : The dimensions of the torus as an object with **x**, **y**, and **z** fields (each a positive integer). The product x\*y\*z defines the total number of coordinate cells in the torus. : **nodes** : Child nodes of the torus. Nodes are mapped to coordinates in x-major order (x varies fastest). Mutually exclusive with **regions**. : **regions** : List of regions within the torus that map subsets of coordinates to nodes. Mutually exclusive with **nodes**. Each region contains the following attributes: : **anchor** : Starting coordinate of the region as an object with **x**, **y**, and **z** fields. : **dims** : Size of the region as an object with **x**, **y**, and **z** fields. The region covers coordinates from **anchor** to **anchor** + **dims** - 1. The region must fit within the torus dimensions (no wrap-around). : **nodes** : Nodes to place in the region, mapped in x-major order within the region's coordinate range. : **placements** : List of allowed placement shapes for this torus. Jobs requesting a number of nodes matching a placement size will be allocated as a contiguous sub-cube that may wrap around torus boundaries. Jobs that don't match any placement size will not receive an allocation. Each placement contains the following attributes: : **dims** : Dimensions of the placement shape as an object with **x**, **y**, and **z** fields. The product x\*y\*z defines the placement size (number of nodes). : **anchor\_seed** : Optional starting coordinate offset for the anchor grid as an object with **x**, **y**, and **z** fields. Shifts the entire anchor grid by the given offset. Defaults to {0, 0, 0}. : **anchor\_spacing** : Optional spacing between placement anchors as an object with **x**, **y**, and **z** fields. Controls how anchor positions are generated across the torus. Defaults to the placement **dims** if not specified.

### Flat definitions

Each flat topology may contain the following attribute:

**alpha\_step\_rank**
:   If set to **true**, sort the job's allocated nodes alphabetically by name
    when picking step nodes and laying out tasks. By default the order follows
    the internal node table index, which for dynamically registered nodes
    reflects registration order rather than name order.

## EXAMPLE

```
---
- topology: topo1
  cluster_default: true
  tree:
    switches:
      - switch: sw_root
        children: s[1-2]
      - switch: s1
        nodes: node[01-02]
      - switch: s2
        nodes: node[03-04]
- topology: topo2
  cluster_default: false
  block:
    block_sizes:
      - 4
      - 16
    blocks:
      - block: b1
        nodes: node[01-04]
      - block: b2
        nodes: node[05-08]
      - block: b3
        nodes: node[09-12]
      - block: b4
        nodes: node[13-16]
- topology: topo3
  cluster_default: false
  flat: true
- topology: topo3a
  cluster_default: false
  flat:
    alpha_step_rank: true
- topology: topo4
  cluster_default: false
  ring:
    rings:
      - ring: ring0
        nodes: node[01-08]
      - ring: ring1
        nodes: node[09-16]
- topology: topo5
  cluster_default: false
  torus3d:
    toruses:
      - name: pod1
        dims:
          x: 4
          y: 4
          z: 2
        nodes: node[01-32]
        placements:
          - dims:
              x: 2
              y: 2
              z: 1
          - dims:
              x: 2
              y: 2
              z: 2
          - dims:
              x: 4
              y: 4
              z: 2
```

## COPYING

Copyright (C) 2025 SchedMD LLC.

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

**[slurm.conf](slurm.conf.md)**(5), **[topology.conf](topology.conf.md)**(5)

---



## Index

[NAME](#lbAB): [DESCRIPTION](#lbAC): [PARAMETERS](#lbAD): [Block definitions](#lbAE): [Tree definitions](#lbAF): [Ring definitions](#lbAG): [Torus3d definitions](#lbAH): [Flat definitions](#lbAI) [EXAMPLE](#lbAJ): [COPYING](#lbAK): [SEE ALSO](#lbAL)

---

This document was created by
*man2html* using the manual pages.  
Time: 20:52:42 GMT, May 26, 2026