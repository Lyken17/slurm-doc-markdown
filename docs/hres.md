# Slurm Workload Manager - Hierarchical Resource (HRES) Scheduling

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

# Hierarchical Resource (HRES) Scheduling

## Overview

Hierarchical Resources (HRES) were added in Slurm 25.05 in a **Beta**
state. While in beta, the configuration file format and other aspects of this
feature may undergo substantial changes in future versions and require major
changes to avoid errors. Sites that utilize this feature while in a beta state
should pay particularly close attention to changes noted in RELEASE\_NOTES and
the CHANGELOGs when [upgrading](upgrades.md).

Hierarchical Resources allow for [license](licenses.md)-like
resources to be defined as part of independent hierarchical topologies and
associated with specific nodes. Jobs may request any integer count of that
resource. Multiple resources may be defined in the configuration (in a
[resources.yaml](resources.yaml.md) file), and will use
independently defined hierarchies.

Although these hierarchical topologies have some similarities to
[network topologies](topology.md), the definitions for each are
completely separate.

## Planning Modes

Three modes of resource planning are provided. In either case, a layer may be
defined with a count of zero or infinite (`count: -1`) resources,
with the impact of this depending on the mode used. Every layer is identified by
a unique `layer_name`; `nodes` and `count` are
optional, and `count` defaults to zero.

### Mode 1

In **Mode 1**, sufficient resources are only required on one layer that
overlaps with job allocation. In many cases only a single level is needed.
However, multiple levels may be defined if some additional flexibility in where
resources are used is preferred, as described in the example below.

A layer with a **zero** count of a resource will have no impact on
scheduling. Since that layer will never satisfy the request, it will never alter
the calculated list of nodes eligible to run a given job. It would be
semantically equivalent to removing that layer definition.

A layer with an **infinite** count of a resource will the always allow a
new job allocation to succeed. Unless prevented due to other requirements, jobs
will be able to execute immediately.

For example, consider the **natural** resource defined in the example
[resources.yaml](#resources_yaml) file below. A job that requests
this resource and is allocated `node[01-04]` will pull from the pool
of 100 available to `node[01-16]`. With a count of 50 specified at
the higher level (`node[01-32]`), they can be allocated in addition
to the resources specified in each group of 16. That is, 100 each would be
available to each group of 16, and 50 more would be available on any of them,
for a total of 250 of this resource.

### Mode 2

In **Mode 2**, sufficient resources must be available on all layers on all
levels that overlap with job allocation. Note that scheduling stalls are
possible if higher levels do not make enough resources available.

A layer with a **zero** count of a resource will have a significant impact
on scheduling. All nodes underneath that layer would never be able to satisfy
the allocation constraints. This could be used to mark that resource unavailable
for a specific portion of the cluster, e.g., for hardware maintenance, without
altering the individual lower-layer resource counts.

A layer with an **infinite** count of a resource will have no impact on
scheduling. Since that layer will always satisfy the request, it will never
constrain execution and would be semantically equivalent to removing that layer
definition.

For example, consider the **flat** resource defined in the example
[resources.yaml](#resources_yaml) file below. A job that requests
this resource and is allocated `node[01-04]` will pull from all
levels that include those nodes. So it would pull from the 12 available on
`node[01-08]`, from the 16 available on `node[01-16]`, and
from the 24 available on `node[01-32]`. Since the highest level only
contains 24, that is the maximum that can be allocated, even though a larger
total is available on lower levels. This example allows a fixed set of resources
to have some flexibility in where they are used.

### Mode 3

In **Mode 3**, resources are allocated on a per-node basis,
with the total consumption being calculated from the most granular layer and
summed up into the successively higher layers.
This mode is specifically designed for consumable resources like power,
where the total usage at a higher level (e.g., cluster-wide)
is the sum of the usage of its components (e.g., chassis level,
then rack level summing multiple chassis, then datacenter row ).

The scheduler ensures that the total summed resources at every layer
in the hierarchy do not exceed that layer's defined count.

A job or reservation can request only one **Mode 3** resource, a request
for more is rejected.

**Important Note:** Layers defined under **Mode 3** must be able to be
represented as a **rooted uniform depth tree**. Every layer except the root
names its parent with `parent_name`, and `nodes` may only
be listed on leaf layers. Each parent inherits the union of its children's
nodes.

For example, consider the **power** resource defined in the example
[resources.yaml](#resources_yaml) file below. A job that requests
1000 of the **power** resource and is allocated `node[01-16]`
will pull from all levels that include those nodes.
So it would pull 8000 from `node[01-08]`,
8000 from `node[09-16]`, 16000 from `node[01-16]`, and
16000 from `node[01-32]`.

#### Preemption

A pending job can preempt lower-priority running jobs to reclaim a
**Mode 3** resource. Because per-node usage is summed into every layer above
it, a job holding the resource under a shared layer is a preemption candidate
even when it does not share any nodes with the preemptor.
Preemption is governed by the usual **PreemptType** and **PreemptMode**
configuration; only the **CANCEL** and **REQUEUE** preemption modes are
supported for **Mode 3** resources. Preemption to reclaim a hierarchical
resource is not supported for **Mode 1** or **Mode 2** resources.

## Plugins

An HRES plugin lets an external service take part in the life of the jobs
that use a resource, for example to reserve the resource when a job starts,
pass data to the job's nodes, release the resource when the job ends, and take
a layer out of service when the service reports a problem. A plugin is enabled
per resource with the `plugin` section of
[resources.yaml](resources.yaml.md). Currently only
**hres/lua** is available.

```
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
```

### Callbacks

When a job uses several resources with a plugin, the callbacks run in the
order the resources are defined in **resources.yaml**, and the epilogs run
in the reverse order. The pre-runs stop at the first failure, every other
callback of a kind runs even after one of them fails. A plugin may return
`ESLURM_HRES_REMOTE_FAIL` to report that the external service is
unavailable rather than broken.

The validate arguments, pre-run, revoke, and controller epilog callbacks
run while slurmctld holds its job lock, which stops scheduling and most
requests until they return. They must be quick. Slow work belongs in the
maintenance callback, or in the asynchronous pre-run of
[hres/lua](#hres_lua).

| Callback | Runs | On failure |
| --- | --- | --- |
| create context | slurmctld, for each resource with a plugin when the configuration is read. This is before the usage of running jobs is restored, so every layer is shown with nothing used | `ESLURM_HRES_MAINTENANCE_DISABLE` or `ESLURM_HRES_MAINTENANCE_DOWN` disable every layer of the resource, any other error is fatal |
| destroy context | slurmctld, before the configuration is read again | ignored |
| maintenance | slurmctld, every `maintenance_cycle` seconds, with the current state of each layer. The plugin may set or clear `disable_layer` of each layer, the same flag as `DisableLayer` of `scontrol update`, or mark a layer down to also requeue the running jobs that use it. A job that cannot be requeued is cancelled | logged |
| validate arguments | slurmctld, for each resource of a job's request, with the job's plugin arguments, if any, when the job is submitted or its licenses are updated, and for a pending job when slurmctld starts or reads its configuration again, or when the job is requeued | any error rejects the request, or holds a pending job |
| pre-run | slurmctld, once the job is scheduled and before its nodes are allocated. The plugin may attach a payload that is sent to the job's nodes | `ESLURM_HRES_REMOTE_FAIL` leaves the job pending, any other error holds it with the plugin's message as the reason, or rejects it at submission |
| revoke | slurmctld, when the job does not start after its pre-run succeeded, for example because the pre-run of another resource failed. The plugin must undo what its pre-run did | logged |
| controller epilog | slurmctld, once the epilogs of all the job's nodes are done and before its resources are returned | logged |
| job prolog | each node of the job where the **Prolog** runs, once, before it. That is every node with **PrologFlags=Alloc**, otherwise only the nodes that start a step | the job is requeued, or cancelled if it cannot be, for example when it was started by **srun** or **salloc**. The node is drained unless the error is `ESLURM_HRES_REMOTE_FAIL` |
| job epilog | each node of the job, once, after the **Epilog** script if one is configured, even when it failed | the node is drained unless the error is `ESLURM_HRES_REMOTE_FAIL` |
| task prolog | slurmstepd, in each task as root before it starts | the task fails |
| user task prolog | slurmstepd, in each task as the user, once its standard input and output are in place, just before it starts | the task fails |
| task epilog | slurmstepd, after each task exits | logged |

What the nodes receive about each resource is taken when the job starts:
the resource name, the plugin configuration, the job's plugin arguments, the
payload from the pre-run, and the layers the job holds, each with the amount
charged and the job's nodes under it. It does not change while the job runs,
even if the layers do. It travels in the credential of each job step, which
**srun** receives, so the job's user can read the plugin configuration, the
payload and the arguments. They must not hold secrets.

### Plugin Arguments

A job may pass arguments to the plugin of a resource at the end of its
request, after the count if one is given. Slurm does not interpret the
arguments. They are only handed to the plugin, which may reject them:

```
sbatch --license='qpu:1[mode=fast,shots=1000]' my_script.sh
```

Each argument needs both a name and a value, without whitespace, and a name
may be given only once. A resource takes one set of arguments. Arguments are
not allowed for a license that is not a hierarchical resource, or in the
licenses of a reservation. They are shown in the **Licenses** and
**LicensesAlloc** of the job.

### hres/lua

**hres/lua** runs a Lua script, given by the `path` entry of
the plugin `config`. The script must be available at the same path
on the controller and on the nodes, and be readable by every user running jobs
with the resource, because `hres_node_user_task_prolog` loads it as
the user. **WARNING**: Most of its functions run as root or as
**SlurmUser**, so the script and every directory on its path must be
writable only by root. It must define every function below except
`hres_validate_args` and
`hres_controller_job_async_prerun`, which are optional. Each function
returns a Slurm return code, such as `slurm.SUCCESS`,
`slurm.ERROR` or `slurm.ESLURM_HRES_REMOTE_FAIL`. A
missing or non-numeric return value means success. If the script cannot be
loaded, for example because a function is missing, the error is logged and the
callback fails. slurmctld does not start if the script cannot be loaded, and
later keeps using the last script it loaded, except for
`hres_controller_job_async_prerun`, which fails.

```
hres_create_context(ctx, layers)
hres_destroy_context(ctx)
hres_maintenance(ctx, layers)
hres_validate_args(ctx, args)                    -- optional
hres_controller_job_prerun(ctx, job, prep)       -- returns rc[, payload]
hres_controller_job_async_prerun(ctx, job, prep) -- optional, returns rc[, payload]
hres_controller_job_revoke(ctx, job, prep)
hres_controller_job_epilog(ctx, job, prep)
hres_node_job_prolog(prep, job)
hres_node_job_epilog(prep, job)
hres_node_task_prolog(prep, job, node_tid, global_tid, env)
hres_node_task_epilog(prep, job, node_tid, global_tid, env)
hres_node_user_task_prolog(prep, job, node_tid, global_tid, env)
```

The arguments are tables:

* `ctx`: `name` of the resource and `config`,
  the plugin configuration as a `name = value` table
* `layers`: an array of the resource's layers, each with
  `name`, `nodes`, `total`, `used` and
  `disable_layer`. `hres_maintenance` may set
  `disable_layer` on a layer to stop allocating from it, and clear it
  to enable the layer again. It may also set `down`, which is not
  passed in, to disable the layer and requeue its running jobs. This is done on
  every run that sets it, and the layer stays disabled until
  `disable_layer` is cleared
* `args`: the job's plugin arguments as a
  `name = value` table, empty when none are given. Without
  `hres_validate_args` every argument is accepted
* `job`: `job_id`, `sluid`,
  `user_id`, `user_name`, `group_id`,
  `account`, `partition`, `nodes` and
  `end_time`. `account` is nil when the job has none, and
  `user_name` may be nil, so use `user_id` to identify the
  user.
  `end_time` is the Unix time the job is expected to end, which is one
  year after its start when the job has no time limit.
  `hres_controller_job_revoke` gets the same expected end as the
  pre-run, although the job does not start.
  `hres_controller_job_epilog` and `hres_node_job_epilog`
  get the time the job ended, except that with **PrologFlags=RunInJob** the
  node job epilog gets the expected end as of the start of the job. The task
  functions get the value from the start of the step, not a later change of the
  time limit
* `env`: the environment of the task, looked up by name, as in
  `env.HOME`. It cannot be iterated, and setting a field does not
  change the environment. `hres_node_task_prolog` gets the step's
  environment, before task variables such as **SLURM\_PROCID** are set.
  `hres_node_user_task_prolog` gets the task's environment as it is
  before **TaskProlog** runs, and `hres_node_task_epilog` gets the
  same environment as **TaskEpilog**. Use `node_tid` and
  `global_tid` to identify the task. The user sets these values.
  **WARNING**: `hres_node_task_prolog` and
  `hres_node_task_epilog` run as root, so never use a value from
  `env` unchecked in a command or in a file path
* `prep`: what the nodes receive about the resource:
  `name`, `config`, `plugin_args` (a
  `name = value` table), `payload`,
  `async_running`, true in the revoke and controller epilog while
  the asynchronous pre-run has not stored its result, and `layers`,
  an array of the layers the job holds, each with `name`,
  `count` and `nodes`

A string returned as the second value of
`hres_controller_job_prerun` becomes the payload sent to the job's
nodes, as `prep.payload`. When
`hres_controller_job_async_prerun` is defined, it runs after the
pre-run in a separate thread, while the job stays in the **CONFIGURING**
state, and its payload, if any, replaces the one from the pre-run. If it fails,
the job is requeued, or cancelled if it cannot be requeued. If the job's
nodes are not allocated after all, its result is dropped and
`hres_controller_job_revoke` is called. The job is not scheduled
again until the asynchronous pre-run ends. As the revoke, and the controller
epilog of a job cancelled while it is **CONFIGURING**, can run while the
asynchronous pre-run of the same job is still running, the service must treat
them as final for that run of the job, identified by `job.job_id`
and `job.sluid`, and refuse or undo a later reservation from it.
If slurmctld stops without a clean shutdown, or a backup takes over, while the
asynchronous pre-run is running, its result is lost and the job is requeued,
or cancelled if it cannot be requeued.

The controller functions of a resource share one Lua state, except
`hres_maintenance`, which has a state of its own, and
`hres_controller_job_async_prerun`, which gets a new one for each
call. Globals set by the other functions are not visible to them. A state is
reloaded when the script changes, which drops its globals without calling
`hres_create_context` again. Each node function runs in a new Lua
state. `hres_node_task_prolog` and
`hres_node_user_task_prolog` run in the task's process, so the
latter may write to the task's output, flushing it before returning.
`hres_node_task_epilog` runs in slurmstepd after the task
exits.

A node function that runs longer than **PrologTimeout**, or
**EpilogTimeout** for the epilogs, fails with an error and is handled
like any other failure of that function (see the table above). Both default
to **PrologEpilogTimeout**, which is not set by default, so there is no
limit. The limit only stops Lua code: a function blocked in a command or a
read, as in `os.execute()` or `io.popen()`, is not
interrupted, so bound such calls in the script, for example with
`timeout(1)`.

```
function hres_controller_job_prerun(ctx, job, prep)
	slurm.log_info("reserving %s for JobId=%d", prep.name, job.job_id)
	return slurm.SUCCESS, "token=" .. job.job_id
end

function hres_node_job_prolog(prep, job)
	slurm.log_info("JobId=%d payload %s", job.job_id, prep.payload or "")
	return slurm.SUCCESS
end
```

## Limitations

* This implementation is in a **beta** state (see
  [overview](#overview))
* Resource names defined through the hierarchical resources configuration must
  not conflict with any cluster licenses
* The layer structure (layers, variables, and modes) is static. Changing it
  requires editing **resources.yaml** and restarting or reconfiguring
  (see [Runtime Updates](#updates))
* **PreemptParameters=reclaim\_licenses** in **slurm.conf** applies only
  to regular licenses, not to HRES. **Mode 3** resources are instead
  reclaimed by their own preemption path (see
  [Preemption](#mode3_preemption))
* Preemption to reclaim a **Mode 3** resource is only performed by the main
  scheduler, not during backfill scheduling
* The licenses of a running job that holds or requests an HRES cannot be
  changed with **scontrol update job**. Requeue the job and change them
  while it is pending
* A hierarchical resource cannot be requested with the `|` form
  of a license request

## Examples

After defining a resource hierarchy in **resources.yaml** (see below for
example), you can interact with these resources in several ways, using the
syntax already used for licenses:

* View HRES

  ```
  scontrol show license
  ```
* Reserve HRES

  ```
  scontrol create reservation account=root licenses=natural(low1):30,flat(low2):4,flat(low4):2
  ```

  Note that the layer must be named for each reserved HRES, using its
  `layer_name` from **resources.yaml**
* Request HRES on a job

  ```
  sbatch --license=flat:2,natural:1 my_script.sh
  ```

### resources.yaml

```
---
- resource: flat
  mode: MODE_2
  layers:
    - layer_name: top		# highest level
      nodes:
        - "node[01-32]"
      count: 24
    - layer_name: mid1		# middle levels
      nodes:
        - "node[01-16]"
      count: 16
    - layer_name: mid2
      nodes:
        - "node[17-32]"
      count: 16
    - layer_name: low1		# lowest levels
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
    - layer_name: top		# highest level
      nodes:
        - "node[01-32]"
      count: 50
    - layer_name: low1		# lowest levels
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
    - layer_name: rack1		# leaf layers list nodes
      parent_name: row1
      nodes:
        - "node[01-08]"
      count: 40000
      base:
        - name: storage
          value: 5000
    - layer_name: rack3
      parent_name: row2
      nodes:
        - "node[17-24]"
      count: 40000
    - layer_name: rack2
      parent_name: row1
      nodes:
        - "node[09-16]"
      count: 40000
    - layer_name: rack4
      parent_name: row2
      nodes:
        - "node[25-32]"
      count: 40000
    - layer_name: row1		# inherits node[01-16]
      parent_name: datacenter
      count: 60000
      base:
        - name: network1
          value: 3000
    - layer_name: row2		# inherits node[17-32]
      parent_name: datacenter
      count: 80000
      base:
        - name: network2
          value: 2000
    - layer_name: datacenter	# root, inherits node[01-32]
      count: 130000
      base:
        - name: acUnit1
          value: 10000
        - name: acUnit2
          value: 8000
```

## Runtime Updates

Administrators may change the nodes, count, base, and disabled state of an
existing layer with `scontrol update`. A plain `Nodes`
list replaces the layer's nodes, while a `+` or `-`
prefix adds or removes nodes. `Count` is absolute and must not be
lower than the layer's **BaseUsage**. `Base` replaces the whole
base list, and an empty `Base=` clears it. In **Mode 3**,
`Nodes` may only be changed on leaf layers. Node and base changes
are propagated to the ancestors. Running jobs are never affected, so lowering
a count below the current usage makes new jobs wait until usage drops.

A running job keeps the layers it was charged on, even when those layers
later gain or lose nodes. The job releases exactly what it took, so changing
the nodes of a layer under a running job does not distort the usage counts.
The layers a job holds are shown by the **LicensesAlloc** field of
`scontrol show job`, for example
`power(rack1*1000,row1*1000,datacenter*1000):1000`, each layer
followed by the amount charged on it. In **Mode 3** that amount grows with
the number of the job's nodes under the layer, as in `rack1*2000`
for two nodes.

```
scontrol update HRESName=power LayerName=rack2 Nodes=+node[33-36] Count=45000
scontrol update HRESName=power LayerName=rack1 Base=
```

The same operation is available through the REST API as
`POST /slurm/v0.0.46/hres/` with a JSON body containing
`hres_name`, `layer_name`, and any of `nodes`,
`count`, `base`, `disable_hres`, and
`disable_layer`.

The layers of a node can also be replaced all at once with
`scontrol update NodeName` and `HRES`. The node is removed
from every layer that is not listed, so it can be moved to another
**Mode 3** leaf with a single command. Every layer the node must stay in has
to be listed, including the layers of other resources. Run
`scontrol -d show node` first to see the current list in the same form.
`HRES='[]'` or an empty `HRES=` removes the node from
every layer. An invalid value is rejected and changes nothing. scontrol reports
invalid JSON, and other reasons are written to the slurmctld log.

With the [resources.yaml](#resources_yaml) example above, the
command below moves `node05` from `rack1` to
`rack2` of **power** and keeps its **flat** and **natural**
layers.

```
scontrol update NodeName=node05 HRES='[{"hres_name":"flat","layer_name":"top"},{"hres_name":"flat","layer_name":"mid1"},{"hres_name":"flat","layer_name":"low1"},{"hres_name":"natural","layer_name":"top"},{"hres_name":"natural","layer_name":"low1"},{"hres_name":"power","layer_name":"rack2"}]'
```

Changes to the nodes of a layer are saved in the slurmctld node state file
(in **StateSaveLocation**), and are recovered as follows when slurmctld
starts or is reconfigured:

* Dynamic nodes and cloud nodes keep their saved layers after a restart or
  `scontrol reconfigure`.
* Other nodes keep their saved layers only when slurmctld is started with
  `-R` or when a backup slurmctld takes control. A default restart or
  `scontrol reconfigure` returns them to the layers defined in
  **resources.yaml**. So when the primary slurmctld resumes control without
  `-R`, it returns these nodes to their configured layers, even though
  the backup kept their saved layers.
* When a node is powered down, or fails to resume within
  **ResumeTimeout**, it returns to its configured layers: those in
  **resources.yaml**, or for a dynamic node, those it was created with. A node
  that is powered down or powering down when slurmctld starts also uses its
  configured layers.
* When a node's saved layers are recovered, they replace its membership in
  every layer defined in **resources.yaml**. Edits to **resources.yaml** do
  not change that node's layers until it returns to its configured layers. If a
  saved layer no longer exists or is no longer a leaf layer, all of the node's
  saved changes are discarded and an error is logged.

Changes to the count, base, and disabled state are not saved.
**resources.yaml** is read again on the next reconfigure or restart, and
those changes are lost.

### Disabling a Resource

A resource or a single layer may be switched off without removing it from the
configuration. `DisableHRES` applies to every layer of the resource,
whether or not a layer is named, while `DisableLayer` applies only to
the named layer, so jobs may still be allocated resources from the other layers.
Both accept only `true` and `false`. Jobs may still
request a disabled resource, but they stay pending until it is enabled again.
A job that no enabled layer can serve pends with the reason
`HRESDisabled`.
Running jobs keep the resources that they already hold. The same fields may be
set in **resources.yaml** as `disable_hres` and
`disable_layer`.

```
scontrol update HRESName=power DisableHRES=true
scontrol update HRESName=power LayerName=rack1 DisableLayer=true
```

### Viewing a Resource

`scontrol show license` prints one entry per layer.

```
LicenseName=power
    Total=35000 Used=0 Free=35000 Reserved=0 Remote=no
    LayerName=rack1 ParentName=row1 Nodes=node[01-08] Mode=3 DisableHRES=false DisableLayer=false ConfTotal=40000 BaseUsage=5000
    Base=storage:5000
```

* **LayerName**, **ParentName**: the layer and, when it has one, its
  parent layer
* **Mode**: the planning mode of the resource
* **DisableHRES**, **DisableLayer**: whether the resource or the layer
  is disabled for scheduling
* **ConfTotal**: the count configured for the layer
* **BaseUsage**: the sum of the base values of the layer, plus, in
  **Mode 3**, the base usage propagated up from its children
* **Base**: the base name and value pairs, or `(null)`
* **Total**: what is left for jobs, the configured count minus the base
  usage

With the `-d` option, `scontrol show node` prints the
layers that contain a node in **HRES=**, a JSON list in the same form as the
**HRES=** node parameter.
For a **Mode 3** resource, only the leaf layer is listed, not its parent
layers. With the [resources.yaml](#resources_yaml) example above,
`node01` lists `rack1` of **power**, along with its
**flat** and **natural** layers, but not `row1` or
`datacenter`. A node that is in no layer has no **HRES=** line.
The same list is in the `hres` field of
`GET /slurm/v0.0.46/node/{node_name}`, as an array of objects with
`hres_name` and `layer_name`. The array is empty when the
node is in no layer.
The `hres` field of
`POST /slurm/v0.0.46/node/{node_name}` takes the same array and sets
the layers like `scontrol update NodeName HRES=`.
An empty array removes the node from every layer.
The node's layers do not change when the field is left out.

## Dynamic Nodes

Dynamic nodes are not listed in **resources.yaml**. They name their
layers when they are created, through the **HRES=** node parameter, which is
a JSON list of resource name and layer name pairs. In **Mode 3** only one
leaf layer per resource may be given.

```
scontrol create NodeName=node33 State=cloud HRES='[{"hres_name":"power","layer_name":"rack2"}]'
slurmd -Z --conf 'HRES=[{"hres_name":"power","layer_name":"rack2"}]'
```

The node is added to the listed layers and their parents when it is created,
and removed from all layers when it is deleted. An unknown or unsuitable layer
creates the node without HRES membership and logs an error. The parameter is
ignored for nodes defined in **slurm.conf**. Layers given at creation are
the node's configured layers. Runtime changes to them are kept across restarts
until the node is powered down, as described in
[Runtime Updates](#updates).