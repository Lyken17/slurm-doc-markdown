# Slurm Workload Manager - switch/lua Plugin

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

# switch/lua Plugin

## Contents

* [Overview](#overview)
* [Quick start](#quickstart)
* [slurm.conf settings](#conf)
* [switch/lua API](#luafunc)
* [Script environment](#script)
* [Restarts](#restart)
* [Example script](#example)

## Overview

This document describes the Slurm switch/lua plugin API and integration
requirements. It is intended as a resource to programmers building a custom
interconnect interface for Slurm. The switch/lua interface is provided to allow
a developer to build forward-support for new networking capabilities ahead of
the development of a more established C implementation of a switch plugin.

The purpose of the switch plugin API is to allow Slurm to integrate with
the interconnect of an HPC system, with the intent of allowing a scheduled set
of nodes to be configured at job start, and have that configuration torn down
at job end. The switch/lua plugin interface is designed with accessing a remote
interface in mind (e.g., configuring switches, accessing a REST API or similar)
and as such, the two job functions run by slurmctld,
`slurm_switch_job_start()` and
`slurm_switch_job_complete()`, are each run in a process of their
own, started by slurmscriptd, to avoid blocking Slurm RPC processing during
potentially slow operations. A call that is still running when
**switch\_timeout** runs out is killed.
They are only run for jobs that request `--network`.

Asynchronous communication with remote resources has some inherent risks
that the plugin developer needs to be aware of. slurmctld cannot know what a
call that fails, never returns, or is lost to a restart of slurmctld has left
behind on the interconnect. It therefore treats a setup that fails or times out
as a reason to fail the job (it is requeued if possible, cancelled if not, see
[below](#job_start)), and a teardown that fails or times out as a
reason to drain the nodes of the job, so that corrective action can be taken
before the nodes are used again.

The script, *switch.lua*, may define any of the following functions.
A function that is not defined is not an error: the plugin simply does nothing
at that point.

Run by slurmctld:

* [`slurm_switch_job_start(job)`](#job_start)
* [`slurm_switch_job_complete(job, jobinfo)`](#job_complete)
* [`slurm_switch_block_job_complete()`](#block_job_complete)
* [`slurm_switch_setup_special_steps()`](#special_steps)

Run by slurmstepd, on each node of a step:

* [`slurm_switch_step_preinit(step, stepinfo)`](#step_preinit)
* [`slurm_switch_step_init(step, stepinfo)`](#step_init)
* [`slurm_switch_step_postfini(step, stepinfo)`](#step_postfini)

## Quick start

To try switch/lua on a test cluster with the example script:

1. Copy `etc/switch.lua.example` from the Slurm source to
   *switch.lua* in the directory that holds
   *slurm.conf*. Install it on every slurmctld host and,
   unless [configless](configless_slurm.md) mode is
   used, on every compute node. **SlurmUser** must be able to
   read it.
2. Add **SwitchType=switch/lua** to *slurm.conf*.
3. Restart every slurmctld, backups included, and the slurmd on
   every node.
4. Check that the slurmctld log has the line "switchlua: script
   loaded". If slurmctld stopped instead, see
   [slurm.conf settings](#conf) for what the log
   says.
5. Submit a job that requests a network, for example
   sbatch --network=test --wrap
   true. The slurmctld log shows a line with
   "switchlua: job\_start(): JobId=" when the job starts, and
   one with "switchlua: job\_complete(): JobId=" when it
   ends.
6. Replace the example with a script for your interconnect.

## slurm.conf settings

[**SwitchType=switch/lua**](slurm.conf.md#OPT_SwitchType)
  
Basic configuration to enable the switch/lua plugin. switch/lua is only
built if Lua is found when Slurm is built (see the
[Lua API](quickstart_admin.md#prereqs) prerequisite).
The plugin reads
*switch.lua* from the same directory as *slurm.conf*. The script
is used by slurmctld as well as by slurmstepd, so it must exist on every
slurmctld host, backups included, as well as on all compute nodes. If
[configless](configless_slurm.md) mode is used, switch.lua is
automatically populated on compute nodes. Ensure that any custom Lua packages
needed by the script are installed in all locations that use the script
(installing them is outside the purview of Slurm).

To enable switch/lua, or to change **SwitchType** later, restart every
slurmctld, backups included, and the slurmd on every node. The change can
affect running jobs, so read the
[SwitchType](slurm.conf.md#OPT_SwitchType) entry in slurm.conf
first.

slurmctld and slurmstepd load the script when they start, and a script that
cannot be loaded stops them: slurmctld will not start, and a slurmstepd cannot
run a step. A script cannot be loaded if it is missing, has a syntax error,
raises an error when its top level runs, or if its top level returns a number
other than `slurm.SUCCESS` (returning nothing is fine). The log of
the daemon has an "error: switch/lua:" line that says which (for example
"Unable to stat" the file, or "returned N on load"), followed by "fatal: Can't
find plugin for switch/lua". If there is no "error: switch/lua:" line before
the fatal line, the plugin itself could not be loaded. Either it was not built
or not installed on that host, or the Lua library it was built against is
missing. In that last case, an error line before the fatal line names the
library: "plugin\_load\_from\_file: dlopen(<PluginDir>/switch\_lua.so):
<Lua library>: cannot open shared object file: No such file or
directory".

Each call of `slurm_switch_job_start()` and
`slurm_switch_job_complete()` runs on a Lua state that is loaded
from switch.lua for that call alone. An edit to the script on the controller is
therefore picked up by the next call without restarting anything, and so is a
mistake: a script that no longer loads fails those calls. A failed
`slurm_switch_job_start()` requeues or cancels the job, and a failed
`slurm_switch_job_complete()` drains its nodes. Check a change
before installing it on a live system: `luac -p switch.lua` finds a
syntax error, but not an error raised when the top level runs, and the script
can be tried out on a test cluster. Compute nodes only see an edit once the
file has been copied to them (in configless mode, after
scontrol reconfigure or a restart of slurmd).
slurmctld asks `slurm_switch_block_job_complete()` and
`slurm_switch_setup_special_steps()` again only when it starts or is
reconfigured, and a backup controller keeps the answers it got when it started,
even after it takes over. Each slurmstepd asks them when it starts, so change
them for the controllers and the nodes together. Because each call has a Lua
state of its own, global variables are not shared between calls, nor with the
functions run by slurmstepd. Keep whatever must survive in the interconnect
itself. The
dictionary returned by `slurm_switch_job_start()` reaches the
slurmstepd functions, as `stepinfo`, and
`slurm_switch_job_complete()`, as `jobinfo`.

[**SlurmctldParameters**](slurm.conf.md#OPT_SlurmctldParameters)
  
These options of **SlurmctldParameters** change how the
controller treats what the script reports. Their entries in
[slurm.conf](slurm.conf.md) give the details.

* [**switch\_timeout**](slurm.conf.md#OPT_switch_timeout): how long slurmctld waits for a
  call to report, and when the call is killed.
* [**switch\_retries**](slurm.conf.md#OPT_switch_retries): how many times a teardown that
  returns `slurm.EAGAIN` is called again.
* [**switch\_drain\_on\_failure**](slurm.conf.md#OPT_switch_drain_on_failure): whether a failed
  teardown drains the nodes of the job.

**NOTE**: Because a failed `slurm_switch_job_complete()`
drains the job's nodes by default, it is recommended you enable
**SchedulerParameters=disable\_job\_shrink**. The nodes that are held
and drained are those the job has when it ends, so the mechanism will miss
nodes released early.

## switch/lua API

### slurm\_switch\_job\_start(job)

Function run asynchronously at job beginning by slurmctld, immediately after
node selection and allocation. The job is held in the CONFIGURING state, as
it is for **PrologSlurmctld**, and does not start until the function has
reported. It is not called when slurmctld is only testing whether a job could
start. The only argument is the job description (see
`_lua_job_info_field()` in `src/lua/slurm_lua.c` for an
extensive list of all the fields that can be queried and used). It is a
snapshot taken when the call is made, and changes to it are not seen by
slurmctld.

It is only called for a job whose allocation requests `--network`
with a non-empty value, which the script reads as `job.network`
(`--network` given to an srun
inside an existing allocation only applies to that step). A job without it is
not set up or torn down, and the slurmstepd functions do not run for its steps.
The same holds for a job that `slurm_switch_job_start()` declined by
returning `nil`. A site chooses which jobs are set up
with a [job\_submit](job_submit_plugins.md) plugin, which can
set, clear or reject `job_desc.network`.

There is an expectation that the plugin is purely implemented in Lua. Use
LuaSocket or Lua-cURL to reach external services. Each call runs in a process
of its own, whose standard input, output and error are `/dev/null`:
whatever the script, or a program it starts, writes to them is discarded. Log
with the `slurm.log_*()` functions (see
[Script environment](#script)). Starting another program (e.g.,
with `os.execute()`) adds to the cost of every call. When the call
ends, whether it returned or was killed, slurmscriptd kills its process group,
so a program the script started that is still running is killed as well,
unless it has left that process group. The functions run by slurmctld run as
**SlurmUser**, so any file or Lua module that the script needs on the
controller (a token, a CA file) must be readable by that user. Do not put a
secret in switch.lua itself: in configless mode it is copied to the compute
nodes, where every user can read it. The dictionary returned by
`slurm_switch_job_start()` is carried in the credential of each
step, which the job's own **srun** receives, so treat it as readable by the
owner of the job.

#### Return values

slurm\_switch\_job\_start() has two return values, the first being a numeric
indicator of success (e.g., slurm.SUCCESS or slurm.ERROR), and the second is a
dictionary (a table) containing state for the plugin describing the
interconnect state with respect to the job at hand.

* **slurm.SUCCESS** - indicates switch setup succeeded, job can
  start.
* **Any other number** (e.g., **slurm.ERROR**), a return value
  that is not a number, or a Lua error - indicates switch setup
  failed.

If the plugin determines the job should be managed by the plugin, return a
dictionary with appropriate data (even empty if none is required). It is stored
on the job record, saved with the job state, copied into every step of the
job as the `stepinfo` that is passed to the
[slurmstepd functions](#step_preinit), and passed to
[`slurm_switch_job_complete()`](#job_complete) as its
`jobinfo`. Keep it to strings, numbers,
booleans and nested tables. It is saved and sent with every step, so keep it
small: at most 32768 entries, counting the entries of every nested table, and
at most 16 levels of tables. A larger dictionary fails the setup as described
under **Failure**, after the function has already done its work, which is
then torn down. A table with a few entries for each node of a very large
allocation can reach the limit, so have the dictionary refer to the
interconnect state and keep the state itself elsewhere. If the plugin will
*not* manage the job, return `nil` for the data return: the
job then has no stepinfo, and `slurm_switch_job_complete()` is not
called for it. A dictionary returned together with a failure is discarded.

**Failure** - when the setup fails, the job is requeued if possible, or
cancelled with the reason "switch setup failed" if not. Only a batch job that
can be requeued (see **JobRequeue** in
[slurm.conf](slurm.conf.md), and the **--requeue** and
**--no-requeue** options of sbatch) is requeued, and its setup is tried
again when it next runs, with no limit on the number of attempts. Any other
job, **salloc** and **srun** allocations included, is cancelled. The
nodes are not drained. `slurm_switch_job_complete()` is not called
for the job, so the function has to undo whatever it had already done before it
returns a failure. A Lua error that escapes the function does not give it that
chance, so wrap the work that has to be undone in `pcall()`, undo
it on an error, and return `slurm.ERROR`. The exception is a function
that returned `slurm.SUCCESS` with a dictionary slurmctld refused,
because it could not be read or is too large to be saved. That function has done
its work and could not have undone it, so
[`slurm_switch_job_complete()`](#job_complete) is called
for the job when it ends, as for an abandoned setup. The same is done for a
call that exits without a result, for example because the script called
`os.exit()` or a function that stops the process. A call that dies
on a signal is treated as timed out.

**Timeout** - if the function has not reported within
**switch\_timeout**, the job is failed in the same way, with the reason
"switch setup timed out". The setup is abandoned: the call is killed, and
slurmctld stops waiting for it. Since slurmctld cannot say what an abandoned
setup left behind, `slurm_switch_job_complete()` is called for the
job to find out and clean up. slurmscriptd counts **switch\_timeout** from
when it starts the call, which can be after slurmctld made it, so in rare cases
a setup still reports after slurmctld stopped waiting for it. If such a setup
returns `slurm.SUCCESS` with a dictionary, even one slurmctld would
refuse, or exits without a result, `slurm_switch_job_complete()` is
called once more for it, with the job as it was when the setup started and
that dictionary as `jobinfo`, or `nil` for a refused
dictionary or a call that exited without a result. By then a requeued job may
be running again on the same nodes, so key what the script creates by the
job's `sluid`. The result of that call is only
logged, in a slurmctld line that contains "late setup of JobId=". The nodes
are not held or drained for it, and `slurm.EAGAIN` is not retried.
A job that ends while the function is still running is described under
[`slurm_switch_job_complete()`](#job_complete).

**Repeated calls** - slurm\_switch\_job\_start() is called again for a job
whose setup was still outstanding when slurmctld restarted (see
[Restarts](#restart)), and for each run of a job that is requeued.
The controller does not say that the call is a repeat, so the function must
judge from the interconnect what already exists and must be safe to repeat.

Example:

```
function slurm_switch_job_start(job)
    if job.num_nodes == 1 then
        return slurm.SUCCESS, nil
    end

    -- _setup_switch() is your site's own code that sets up the interconnect.
    local context = _setup_switch(job.nodes)
    if context.rc ~= 0 then
        slurm.log_error("Failed to set up switch for job " .. job.job_id)
        return slurm.ERROR, nil
    end

    return slurm.SUCCESS, { state = context }
end
```

### slurm\_switch\_job\_complete(job, jobinfo)

Function run asynchronously at job end by slurmctld, as it starts to release
the nodes of the job. The first argument is the job description, as for
`slurm_switch_job_start()`. The second, `jobinfo`, is a
copy of the dictionary that `slurm_switch_job_start()` returned for
the job, or `nil` if there is none. Check it for `nil`
before indexing it, as a Lua error fails the teardown. The function is called
for:

* a job for which `slurm_switch_job_start()` returned a
  dictionary;
* a job whose setup was abandoned because it did not report within
  **switch\_timeout**, exited without a result, or returned
  `slurm.SUCCESS` with a dictionary that slurmctld
  refused (see
  [Return values](#job_start_rc)). Such a setup has no
  dictionary to say what it left behind, so `jobinfo`
  is `nil` and the function must work out from the
  interconnect whether anything needs to be undone.

It is not called for a job that did not request `--network`, or
that `slurm_switch_job_start()` declined (returned `nil`)
or failed by returning an error, which has to undo its work first. Undoing what
an abandoned setup left behind is up to the function; slurmctld calls it and
acts on its result as for any other teardown. In rare cases a timed-out setup
still reports before it is killed. If it returns `slurm.SUCCESS`
with a dictionary, or exits without a result, the function is called once more
for it, possibly while the first call is still running (see
[`slurm_switch_job_start()`](#job_start)).

A job that ends while `slurm_switch_job_start()` is still running
keeps its nodes held until that call reports, or until the time allowed for the
setup (**switch\_timeout**, counted from when it started) has run out. If
the call reports a dictionary,
`slurm_switch_job_complete()` is called with it as above. If it
reports a failure or declines the job, there is nothing to tear down, unless
the failure is a refused dictionary or a call that exited without a result,
which are torn down as above. If the time passes first, the setup is
abandoned as described above and `slurm_switch_job_complete()` is
called, in rare cases before the setup has been killed.

**Repeated calls** - slurm\_switch\_job\_complete() is called again for a
job whose teardown was holding its nodes when slurmctld restarted (see
[Restarts](#restart)), with the nodes still held and the same
`jobinfo`. The controller does not say that the call is a repeat, so
the function must judge from the interconnect what is left to undo and must be
safe to repeat.

A teardown that does not hold its nodes can still be running when a
requeued batch job starts again, and so when its next
`slurm_switch_job_start()` runs. Key what the script creates by
the job's `sluid`, which changes on each run.

#### Return values

slurm\_switch\_job\_complete() has a single numeric return value:

* **slurm.SUCCESS** - the teardown is done, the nodes of the job go
  back to service.
* **slurm.EAGAIN** - not yet. The nodes stay held and nothing is
  drained. The function is called again for the same job, with
  the same `jobinfo`, at the next periodic check (see
  **switch\_timeout** above), up to
  **switch\_retries** times, after which the nodes are
  drained like any failure. This only takes effect when
  [`slurm_switch_block_job_complete()`](#block_job_complete) returns
  true, because a retry needs the nodes held, or for a job that
  ended while its setup was still running or whose teardown is
  run again after a restart (see [Restarts](#restart)),
  whose nodes are held whatever that returns. Otherwise it is a
  failure. Be ready to
  be called again after a partial attempt.
* **A negative number** (e.g., **slurm.ERROR**), or a Lua
  error - the teardown failed. The nodes of the job are drained,
  unless **switch\_drain\_on\_failure=no**.
* **Any other positive number** - logged as an error but not
  enforced, as for the slurmstepd functions.
  `slurm_switch_job_start()` is different: any
  number other than `slurm.SUCCESS` fails the
  setup.

A return value that is not a number is logged and taken as success. A call
that does not report within **switch\_timeout** is a failure, and its
report is ignored when it comes.

When a teardown fails, its nodes are drained (unless
**switch\_drain\_on\_failure=no**) with the reason "Switch job complete
failed", which sinfo -R lists. The slurmctld
log says what failed, in an error line that contains one of:

* "switch teardown failed for": the function failed.
* "switch completion did not report within": the function did not
  report within **switch\_timeout**.
* "switch teardown still not done after": the function still returned
  `slurm.EAGAIN` after **switch\_retries**
  retries.
* "had unresolved switch cleanup": the teardown was holding its nodes
  when slurmctld restarted, and could not be run again (see
  [Restarts](#restart)).

Then a line that contains "drained <nodes> after a failed switch
teardown" names the nodes. Once the interconnect is fixed, return the nodes to
service with scontrol update nodename=<nodes>
state=RESUME.

Whether the nodes of the job are held while the function runs is decided by
[`slurm_switch_block_job_complete()`](#block_job_complete).

### slurm\_switch\_block\_job\_complete()

Function run by slurmctld, without arguments, once when it loads the plugin
(when slurmctld is started or reconfigured). It returns a boolean. If it
returns true, the nodes of a job stay in the COMPLETING state, and so are not
given to another job, until `slurm_switch_job_complete()` has
reported. If it returns false, is not defined, or raises an error, the nodes
are returned to service while `slurm_switch_job_complete()` runs,
and `slurm.EAGAIN` is treated as a failure. The exception is a job
that ended while its setup was still running: its nodes are held for the
report of the setup, and for the teardown that follows, whatever this returns.
So are the nodes of a teardown run again after a restart (see
[Restarts](#restart)).
slurmstepd calls this
function as well when it loads the plugin, and ignores the answer, so it should
not have side effects.

### slurm\_switch\_setup\_special\_steps()

Function run by slurmctld and slurmstepd, without arguments, once when each
loads the plugin (for slurmctld, when it is started or reconfigured). It
returns a boolean. By default, only the normal job steps go through the
slurmstepd functions below. If it returns true,
`slurm_switch_step_init()` is
also called for the batch step and for the interactive step of a job that the
plugin manages, and these carry the stepinfo as well, which allows the script to
set environment variables for the batch job, for example.
`slurm_switch_step_preinit()` and
`slurm_switch_step_postfini()` are only ever called for normal steps,
whatever this returns. The extern step runs none of the step functions. Like
every slurmstepd, it still loads the script and calls this function and
`slurm_switch_block_job_complete()` when it starts, so neither should
have side effects. A function that raises an error, or is not defined, counts
as false.

### slurm\_switch\_step\_preinit(step, stepinfo)

Function run by slurmstepd, synchronously, once on each node for every normal
step of a job that the plugin manages, as root and before the container of the
step is created. Anything it starts is outside of the container and will not be
cleaned up for you. It is paired with [`slurm_switch_step_postfini()`](#step_postfini).

`step` is a table with the fields `job_id`,
`partition` (which may be `nil`) and `sluid`.
`stepinfo` is a copy of the dictionary that
`slurm_switch_job_start()` returned, or `nil` if it could
not be passed in, which is logged. The function is not called for a job that
the plugin does not manage. Return a number:

* **slurm.SUCCESS** - success.
* **A negative number** - the step fails with "Error configuring
  interconnect".
* **A positive number** - logged, the step proceeds.

A Lua error is logged and the step proceeds: unlike the functions run by
slurmctld, those run by slurmstepd fail open, so that a bug in the script does
not fail every step on the cluster. Only an explicit negative return value is
enforced.

### slurm\_switch\_step\_init(step, stepinfo)

Function run by slurmstepd, synchronously, once on each node for every normal
step of a job that the plugin manages (and its batch and interactive steps, if
[`slurm_switch_setup_special_steps()`](#special_steps)
returns true). It runs as root, after the container of the step has been
created and the SPANK plugins are initialized, and before the tasks are
forked. It is the only function that can set the environment of the whole
step. The arguments are as for `slurm_switch_step_preinit()`.

It returns a return code as for `slurm_switch_step_preinit()`
(a negative number fails the step) and a table of environment variables, which
may be omitted:

* `FOO = "bar"` sets FOO=bar
* `FOO = 42` sets FOO=42 (numbers are converted to
  strings)
* `FOO = true` sets FOO=1
* `FOO = false` unsets FOO

Any other type of value, and any name that is not a string, is skipped and
logged. Slurm sets its own SLURM\_\* variables after this function has run.

### slurm\_switch\_step\_postfini(step, stepinfo)

Function run by slurmstepd, synchronously, once on each node for every normal
step of a job that the plugin manages, as root, after every task of the step is
dead and its container has been killed. It is the teardown mirror of
`slurm_switch_step_preinit()`: the last chance to release whatever it
took. The arguments are as for `slurm_switch_step_preinit()`. Return
a number:

* **slurm.SUCCESS** - success.
* **A negative number** - the node is drained, with the reason
  "switch\_g\_job\_postfini failed".
* **A positive number** - logged only.

A Lua error is logged and the node is not drained.

## Script environment

The script has the following available through the `slurm`
table:

* `slurm.SUCCESS` (0), `slurm.ERROR` and
  `slurm.FAILURE` (both -1) and
  `slurm.EAGAIN`.
* `slurm.log_info(fmt, ...)`,
  `slurm.log_error(fmt, ...)`,
  `slurm.log_verbose(fmt, ...)` and
  `slurm.log_debug(fmt, ...)` (also
  `slurm.log_debug2` to `slurm.log_debug4`)
  take a format as for `string.format()`.
  `slurm.log(level, msg)` and
  `slurm.error(msg)` take a message. The output of
  `print()` is logged at the info level. A line goes to
  the log of the daemon running the function, prefixed with
  "switch/lua:" and the name of the function. For
  `slurm_switch_job_start()` and
  `slurm_switch_job_complete()`, the process that runs
  the call writes it to **SlurmctldLogFile**, or to syslog if
  that is not set, never to the terminal of
  slurmctld -D. With
  **SlurmctldLogFile** set to `/dev/stdout` or
  `/dev/stderr`, those lines never reach slurmctld's
  output, as the standard output and error of that process are
  `/dev/null`.
* `slurm.to_json()`, `slurm.from_json()`,
  `slurm.to_yaml()` and `slurm.from_yaml()`
  convert between tables and text. The YAML pair needs Slurm built
  with libyaml and, where slurmctld itself runs the script (its
  top level, `slurm_switch_block_job_complete()` and
  `slurm_switch_setup_special_steps()`), yaml listed in
  **SerializerPlugins** if that is set. Without that, calling
  either stops the process running the script, which
  `pcall()` cannot catch: a call of
  `slurm_switch_job_start()` exits without a result,
  `slurm_switch_job_complete()` fails, and any other
  function stops slurmctld or slurmstepd.

## Restarts

When slurmctld restarts, the calls of
`slurm_switch_job_start()` and
`slurm_switch_job_complete()` that were running are killed, and
their answers are lost. Nothing asks the script what became of them, and
slurmctld cannot undo what they did. What slurmctld has is the state
it saved for each job.
(scontrol reconfigure starts a new slurmctld
process that recovers its state the way a restart does, so the following
applies to it too. It also applies to a backup slurmctld that takes over,
which recovers the saved state the same way.)

* A setup that was still outstanding for a job that had not
  ended is not torn down but run again, as there is no record of
  its answer. The job stays in the
  CONFIGURING state until that call reports, and it is given a new
  **switch\_timeout**. This is why
  `slurm_switch_job_start()` must be safe to repeat.
  A setup that had already reported is not run again, whether it
  returned a dictionary or declined the job.
* A job that was running with a dictionary from
  `slurm_switch_job_start()` keeps it, and
  `slurm_switch_job_complete()` is called with it when
  it ends.
* A teardown that was holding its nodes (see
  `slurm_switch_block_job_complete()`) is run again
  from the start, as there is no record of how far it got. That
  includes one waiting to be tried again, and one waiting for a
  setup that had not reported, which is then torn down as an
  abandoned setup. The nodes stay held until that call reports,
  and it is given a new **switch\_timeout** and
  **switch\_retries**. This is why
  `slurm_switch_job_complete()` must be safe to
  repeat. A teardown that cannot be run again is treated as
  failed.
* A teardown that was not holding its nodes is neither run again
  nor treated as failed. Its nodes are already back in
  service.

slurmctld kills the calls that are still running when it shuts down,
restarts or is reconfigured, part way through if need be, and a report that
arrives after slurmctld has stopped taking them is dropped. That is why an
outstanding setup, and a teardown that holds its nodes, are run again. A
backup slurmctld that gives control back kills its calls the same way.
slurmctld can wait for a call started while it is stopping, until the call
ends or is killed at **switch\_timeout**.

Two things follow for
scontrol reconfigure:

* The old slurmctld kills its calls before it starts the new one,
  so a setup or teardown that is run again does not overlap the
  call it repeats.
* When slurmctld is daemonized or runs under systemd and the
  reconfigure fails, slurmctld carries on in the same process,
  and nothing runs the killed calls again. A setup that was
  running is then treated as one that timed out, and a teardown
  that was running is treated as failed once
  **switch\_timeout** has run out, so its nodes are drained
  whether or not it was holding them.

## Example script

The file `etc/switch.lua.example` in the Slurm source is a
manual-test harness that exercises every function above and the main ways each
of them can answer. It logs each call. On a test cluster, set
`ALLOW_DIRECTIVES` at the top of the file to true to drive it from
the `--network` option of the job
(e.g., `--network=switchlua:defer`); it is off by default because the
directives let any user fail setups and drain nodes. A directive
that fails the setup (`defer`, `start_crash`) requeues a
batch job that can be requeued, which then fails again on each run. Submit
those with `sbatch --no-requeue`, or run them with
**srun**.