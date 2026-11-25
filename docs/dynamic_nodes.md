# Slurm Workload Manager - Dynamic Nodes

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

# Dynamic Nodes

## Overview

Starting in Slurm 22.05, nodes can be dynamically added and removed from
Slurm.

## Dynamic Node Communications

For regular, non-dynamically created nodes, Slurm knows how to communicate with
nodes by reading in the slurm.conf. This is why it is important for a
non-dynamic setup that the slurm.conf is synchronized across the cluster. For
dynamically created nodes, The controller automatically grabs the node's
**NodeAddr** and **NodeHostname** for dynamic slurmd registrations. The
controller then passes the node addresses to the clients so that they
communicate, and even fanout, to other nodes.

Starting in Slurm 26.11, set the **SlurmctldParameters** option
[dynamic\_node\_dns](slurm.conf.md#OPT_dynamic_node_dns)
to have each host resolve a dynamic node's **NodeName** through its own
system resolver instead of using the address the controller recorded. This
lets node-to-node traffic use a different network than the controller does.
Every host in the cluster, including login and submit hosts, must then be able
to resolve the **NodeName** of each node the option applies to. Slurm does
not fall back to the recorded address. See the option's description for which
nodes it applies to and how a failed lookup is logged.

## Slurm Configuration

**MaxNodeCount=#**: Set to the number of possible nodes that can be active in a system at a time. See the slurm.conf [man](slurm.conf.md#OPT_MaxNodeCount) page for more details. **SelectType=select/cons\_tres**: Dynamic nodes are only supported with cons\_tres.

### Partition Assignment

Dynamic nodes can be automatically assigned to partitions at creation by using
the partition's nodes [ALL](slurm.conf.md#OPT_Nodes_1) keyword or
[NodeSets](slurm.conf.md#SECTION_NODESET-CONFIGURATION) and
specifying a feature on the nodes.

e.g.

```
Nodeset=ns1 Feature=f1
Nodeset=ns2 Feature=f2

PartitionName=all  Nodes=ALL Default=yes
PartitionName=dyn1 Nodes=ns1
PartitionName=dyn2 Nodes=ns2
PartitionName=dyn3 Nodes=ns1,ns2
```

## Creating Nodes

Nodes can be created two ways:

1. **Dynamic slurmd registration**: Using the slurmd [-Z](slurmd.md#OPT_-Z) and [--conf](slurmd.md#OPT_conf-<node-parameters>) options a slurmd will register with the controller and will automatically be added to the system. e.g. ``` slurmd -Z --conf "RealMemory=80000 Gres=gpu:2 Feature=f1" ```
2. **scontrol create NodeName= ...**: Create nodes using scontrol by specifying the same **NodeName** line that you would define in the slurm.conf. See slurm.conf [man](slurm.conf.md#SECTION_NODE-CONFIGURATION) page for node options. Only **State=CLOUD**, **State=EXTERNAL** and **State=FUTURE** are supported. The node configuration should match what the slurmd will register with (e.g. slurmd -C) plus any additional attributes. Creation is all-or-nothing. If any node in the request cannot be created, the command fails, no node from the request is created, and every node that already existed — whether created dynamically or defined in slurm.conf — is left unchanged. e.g. ``` scontrol create NodeName=d[1-100] CPUs=16 Boards=1 SocketsPerBoard=1 CoresPerSocket=8 ThreadsPerCore=2 RealMemory=31848 Gres=gpu:2 Feature=f1 State=cloud ```

## Automatic GPU Detection

When a dynamic node is created with [slurmd -Z](slurmd.md#OPT_-Z),
the slurmd will automatically detect and register GPUs when:

* **--conf** does not specify any GPU GRES
* **gres.conf** does not contain explicit GPU GRES records for the node
* **gres.conf** does not contain **AutoDetect=off**

If [AutoDetect](gres.conf.md#OPT_AutoDetect) in
**gres.conf** specifies a particular detection mechanism (e.g.,
**NVML**, **NVIDIA**, **RSMI**, **AMD**, **oneAPI**, **NRT**),
it will use that mechanism to try to detect a GPU. Otherwise, **slurmd**
defaults to the [AutoDetect=full](gres.conf.md#OPT_full) GPU
detection method.

## Deleting Nodes

Nodes can be deleted using **scontrol delete nodename=<nodelist>**.
Only dynamic nodes that have no running jobs and that are not part of a
reservation can be deleted.

## Topology

Nodes can be dynamically added to and removed from topologies as described in
the [Topology Guide](topology.md).

## Hierarchical Resources

Dynamic nodes can join the layers of a
[Hierarchical Resource](hres.md) (HRES) with the **NodeName**
parameter [**HRES**](slurm.conf.md#OPT_HRES), a JSON list of
`hres_name` and `layer_name` pairs. It is accepted by both
creation methods:

```
scontrol create NodeName=d1 CPUs=16 RealMemory=31848 State=cloud HRES='[{"hres_name":"power","layer_name":"rack2"}]'
slurmd -Z --conf 'RealMemory=80000 HRES=[{"hres_name":"power","layer_name":"rack2"}]'
```

Malformed JSON rejects the node. Naming a layer that does not exist or cannot
accept the node creates the node without HRES membership and logs an error in
slurmctld. Deleting the node removes it from all layers.

## Limitations

1. Dynamic nodes are not sorted internally and when added to Slurm they will
   potentially be alphabetically out of order internally — leading to
   suboptimal job allocations if node names represent topology of the nodes.