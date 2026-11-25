# Slurm Workload Manager - resources.yaml

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

    : **mode** : The planning mode for the resource. Must be one of the following: : **MODE\_1** : Sufficient resources are required on **only one** layer that overlaps with the job's allocated nodes. **MODE\_2** : Sufficient resources must be available on **all** layers that overlap with the job's allocated nodes. **MODE\_3** : Resources are allocated on a per-node basis. The scheduler calculates total consumption from the most granular layer and sums it up into the successively higher layers, ensuring the **count** is not exceeded at any layer. This mode is designed for consumable resources like power and can be mapped to a block topology using the **topology** parameter. : **topology** : (Optional) Specifies the name of a **topology/block** definition to map to this resource. This parameter is **only** valid for **MODE\_3** resources. The HRes layers must have the same layout as the specified block topology. This enables the scheduler to simultaneously optimize both the HRes and block topology allocations. : **variables** : (Optional) A list of name/value pairs that map arbitrary text strings to administratively-defined resource counts. Users can then use these strings in job submissions (e.g., *--resources=power:full\_node*) instead of a numeric value. Each entry in the list contains: : **name** : The string alias for the value (e.g., "full\_node"). **value** : The numeric resource count (e.g., 1000). : **disable\_hres** : (Optional) If true, no job is allocated resources from any layer of this resource. Jobs may still request the resource, but they stay pending until it is enabled again, with reason **HRESDisabled**. Running jobs keep the resources that they already hold. Defaults to false. : **plugin** : (Optional) An HRES plugin that takes part in the life of the jobs using this resource, for example to reserve it on an external service when a job starts. slurmctld creates one context of the plugin for each resource that defines one. The plugin also runs on the nodes of those jobs. Contains: : **type** : The plugin to use. Currently only **hres/lua** is available. : **config** : (Optional) A list of name/value pairs handed to the plugin as they are. Slurm does not interpret them. **hres/lua** requires **path**, the path of its Lua script, which must be the same on the controller and on the nodes, and writable only by root. : **name** : The name of the entry. **value** : Its value, as a string. : **maintenance\_cycle** : (Optional) Seconds between calls to the maintenance callback of the plugin, which may set or clear **disable\_layer** of each layer. The cycles are checked every 5 seconds, so a cycle is rounded up to the next multiple of 5 seconds. Defaults to 0, no maintenance. : **maintenance\_timeout** : (Optional) Seconds after which a maintenance call is logged as taking too long, at the verbose level. The call is not interrupted. Defaults to 3. : **layers** : A list of layers that define the resource hierarchy. Each layer is a YAML object containing: : **layer\_name** : The name of the layer, unique within the resource (case-insensitive). The name identifies the layer in the licenses of jobs and reservations, so it may not contain whitespace or any of the characters **, ; | : = ( ) \***. : **parent\_name** : The **layer\_name** of the parent layer. Only valid for **MODE\_3**, where it is required for every layer except the root. : **nodes** : (Optional) A list of node names or hostlist expressions that are part of this layer. Defaults to no nodes. In **MODE\_3**, nodes may only be listed on leaf layers; each parent layer is automatically assigned the nodes of its children. : **count** : (Optional) The total number of resources available in this specific layer. Defaults to 0. A value of -1 means infinite. : **disable\_layer** : (Optional) If true, no job is allocated resources from this layer. Jobs may still be allocated resources from the other layers of the same resource. Defaults to false. : **base** : (Optional) A list of name/value pairs describing non-job-related (static) resource consumption in this layer. This is particularly relevant for **MODE\_3**. Each entry contains: : **name** : The name of the static resource consumer (e.g., "storage", "network1"). **value** : The numeric resource count this consumer uses.

The **nodes**, **count**, **base**, and **disable\_layer** of a layer,
and the **disable\_hres** of a resource, can be changed at runtime with the
**update HRESName** command of **[scontrol](scontrol.md)**(1). The layers of a node can
be replaced at once with the **HRES** option of **update NodeName**.
Runtime changes to
**nodes** are saved in the slurmctld node state file. Dynamic and cloud
nodes keep them across **scontrol reconfigure** and slurmctld restarts, while
other nodes keep them only when slurmctld is started with **-R** or a backup
slurmctld takes control. A node that is powered
down returns to the layers defined in this file, or to the layers a dynamic
node was created with. Other changes are lost when this file is read again on
the next reconfigure or restart.

## EXAMPLE

```
---
- resource: flat
  mode: MODE_2
  layers:
    - layer_name: top   # highest level
      nodes:
        - "node[01-32]"
      count: 24
    - layer_name: mid1  # middle levels
      nodes:
        - "node[01-16]"
      count: 16
    - layer_name: mid2
      nodes:
        - "node[17-32]"
      count: 16
    - layer_name: low1  # lowest levels
      nodes:
        - "node[01-08]"
      count: 12
    - layer_name: low2
      nodes:
        - "node[09-16]"
      count: 12
    - layer_name: low3
      nodes:
        - "node[17-24]"
      count: 12
    - layer_name: low4
      nodes:
        - "node[25-32]"
      count: 12
- resource: natural
  mode: MODE_1
  layers:
    - layer_name: top   # highest level
      nodes:
        - "node[01-32]"
      count: 50
    - layer_name: low1  # lowest levels
      nodes:
        - "node[01-16]"
      count: 100
    - layer_name: low2
      nodes:
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
    - layer_name: site  # root, nodes inherited from children
      count: 130000
      base:
        - name: acUnit1
          value: 10000
        - name: acUnit2
          value: 8000
    - layer_name: row1
      parent_name: site
      count: 60000
      base:
        - name: network1
          value: 3000
    - layer_name: row2
      parent_name: site
      count: 80000
      base:
        - name: network2
          value: 2000
    - layer_name: rack1 # leaf layers
      parent_name: row1
      nodes:
        - "node[01-08]"
      count: 40000
      base:
        - name: storage
          value: 5000
    - layer_name: rack2
      parent_name: row1
      nodes:
        - "node[09-16]"
      count: 40000
    - layer_name: rack3
      parent_name: row2
      nodes:
        - "node[17-24]"
      count: 40000
    - layer_name: rack4
      parent_name: row2
      nodes:
        - "node[25-32]"
      count: 40000
- resource: qpu
  mode: MODE_1
  plugin:
    type: hres/lua
    config:
      - name: path
        value: /etc/slurm/hres_qpu.lua
    maintenance_cycle: 60
    maintenance_timeout: 10
  layers:
    - layer_name: qpu1
      nodes:
        - "node[01-16]"
      count: 1
    - layer_name: qpu2
      nodes:
        - "node[17-32]"
      count: 1
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

**[scontrol](scontrol.md)**(1), **[slurm.conf](slurm.conf.md)**(5)

---



## Index

[NAME](#lbAB): [DESCRIPTION](#lbAC): [PARAMETERS](#lbAD): [EXAMPLE](#lbAE): [COPYING](#lbAF): [SEE ALSO](#lbAG)

---

This document was created by
*man2html* using the manual pages.  
Time: 20:23:17 GMT, November 24, 2026