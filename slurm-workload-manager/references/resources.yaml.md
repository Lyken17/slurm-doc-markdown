# Slurm Workload Manager - resources.yaml

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

# resources.yaml

Section: Slurm Configuration File (5)  
Updated: Slurm Configuration File  
[Index](#index)

## NAME

resources.yaml - Slurm configuration file for the Hierarchical Resources (HRES).

## DESCRIPTION

**resources.yaml** is a YAML-formatted configuration file that defines
Hierarchical Resources (HRES).
The file must be located in the same directory as **slurm.conf**. Any text
following a "#" in this file is treated as a comment through the end of that
line.

Additional details are available in
the Hierarchical Resource (HRES) Scheduling page:
<<https://slurm.schedmd.com/hres.html>>

## PARAMETERS

Each Hierarchical Resources definition is a YAML object containing the following
attributes:

**resource**
:   The unique name for the resource. This name will be used to identify it by
    slurmctld. This **must be the first** attribute in the object.

    : **mode** : The planning mode for the resource. Must be one of the following: : **MODE\_1** : Sufficient resources are required on **only one** layer that overlaps with the job's allocated nodes. **MODE\_2** : Sufficient resources must be available on **all** layers that overlap with the job's allocated nodes. **MODE\_3** : Resources are allocated on a per-node basis. The scheduler calculates total consumption from the most granular layer and sums it up into the successively higher layers, ensuring the **count** is not exceeded at any layer. This mode is designed for consumable resources like power and can be mapped to a block topology using the **topology** parameter. : **topology** : (Optional) Specifies the name of a **topology/block** definition to map to this resource. This parameter is **only** valid for **MODE\_3** resources. The HRes layers must have the same layout as the specified block topology. This enables the scheduler to simultaneously optimize both the HRes and block topology allocations. : **variables** : (Optional) A list of name/value pairs that map arbitrary text strings to administratively-defined resource counts. Users can then use these strings in job submissions (e.g., *--resources=power:full\_node*) instead of a numeric value. Each entry in the list contains: : **name** : The string alias for the value (e.g., "full\_node"). **value** : The numeric resource count (e.g., 1000). : **layers** : A list of layers that define the resource hierarchy. Each layer is a YAML object containing: : **nodes** : A list of node names or hostlist expressions that are part of this layer. : **count** : The total number of resources available in this specific layer. : **base** : (Optional) A list of name/value pairs describing non-job-related (static) resource consumption in this layer. This is particularly relevant for **MODE\_3**. Each entry contains: : **name** : The name of the static resource consumer (e.g., "storage", "network1"). **value** : The numeric resource count this consumer uses.

## EXAMPLE

```
---
- resource: flat
  mode: MODE_2
  layers:
    - nodes:                    # highest level
        - "node[01-32]"
      count: 24
    - nodes:                    # middle levels
        - "node[01-16]"
      count: 16
    - nodes:
        - "node[17-32]"
      count: 16
    - nodes:                    # lowest levels
        - "node[01-08]"
      count: 12
    - nodes:
        - "node[09-16]"
      count: 12
    - nodes:
        - "node[17-24]"
      count: 12
    - nodes:
        - "node[25-32]"
      count: 12
- resource: natural
  mode: MODE_1
  layers:
    - nodes:                    # highest level
        - "node[01-32]"
      count: 50
    - nodes:                    # lowest levels
        - "node[01-16]"
      count: 100
    - nodes:
        - "node[17-32]"
      count: 100
- resource: power
  mode: MODE_3
  topology: blok1
  variables:
    - name: full_node
      value: 1000
    - name: full_gpu_node
      value: 2000
  layers:
    - nodes:
        - "node[01-32]"
      count: 130000
      base:
        - name: acUnit1
          value: 10000
        - name: acUnit2
          value: 8000
    - nodes:
        - "node[01-16]"
      count: 60000
      base:
        - name: network1
          value: 3000
    - nodes:
        - "node[17-32]"
      count: 80000
      base:
        - name: network2
          value: 2000
    - nodes:
        - "node[01-08]"
      count: 40000
      base:
        - name: storage
          value: 5000
    - nodes:
        - "node[09-16]"
      count: 40000
    - nodes:
        - "node[17-24]"
      count: 40000
    - nodes:
        - "node[25-32]"
      count: 40000
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

**[slurm.conf](slurm.conf.md)**(5)

---



## Index

[NAME](#lbAB): [DESCRIPTION](#lbAC): [PARAMETERS](#lbAD): [EXAMPLE](#lbAE): [COPYING](#lbAF): [SEE ALSO](#lbAG)

---

This document was created by
*man2html* using the manual pages.  
Time: 20:36:11 GMT, January 15, 2026