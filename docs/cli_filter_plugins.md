# Source: https://slurm.schedmd.com/cli_filter_plugins.html

# cli\_filter Plugin API

## Overview

This document describes Slurm cli\_filter plugins and the API that
defines them. It is intended as a resource to programmers wishing to write
their own Slurm cli\_filter plugins.

The purpose of the cli\_filter plugins is to provide programmatic hooks
during the execution of the **salloc**, **sbatch**, and **srun**
command line interface (CLI) programs. Three hooks are defined:

* **cli\_filter\_p\_setup\_defaults** —
  Called before any option processing is done,
  *per job component*, allowing a plugin to replace default option
  values.
* **cli\_filter\_p\_pre\_submit** —
  Called after option processing *per job
  component* but before any communication
  is made with the slurm controller. This location
  is ideal for policy enforcement because the plugin can read all the options
  supplied by the user (as well as the environment) - thus invalid job requests
  can be stopped before they ever reach the slurmctld.
* **cli\_filter\_p\_post\_submit** —
  Called after the jobid (and, in the case of
  **srun**, after the stepid) is generated, and typically before or in
  parallel with job execution. In combination with data collected in the
  cli\_filter\_p\_pre\_submit() hook, this is an ideal location for logging
  activity.

cli\_filter plugins vary from the [job\_submit
plugin](job_submit_plugins.html) as it is entirely executed client-side, whereas job\_submit is
processed server-side (within the slurm controller). The benefit of the
cli\_filter is that it has access to all command line options in a simple and
consistent interface as well as being safer to run disruptive operations
(e.g., quota checks or other long running operations you might want to use
for integrating policy decisions), which can be problematic if run from the
controller. The disadvantage of the cli\_filter is that it must not be relied
upon for security purposes as an enterprising user can circumvent it simply
by providing an alternate slurm.conf with the CliFilterPlugins option
disabled. If you plan to use the cli\_filter for managing policies, you should
also configure a job\_submit plugin to reinforce those policies.

Slurm cli\_filter plugins must conform to the
Slurm Plugin API with the following specifications:

const char
plugin\_name[]="*full text name*"

A free-formatted ASCII text string that identifies the plugin.

const char
plugin\_type[]="*major/minor*"  

The major type must be "cli\_filter."
The minor type can be any suitable name for the type of job submission package.
We include samples in the Slurm distribution for

* **none** — An empty plugin with no actions taken, a useful starting
  template for a new plugin.

const uint32\_t plugin\_version  
If specified, identifies the version of Slurm used to build this plugin and
any attempt to load the plugin from a different version of Slurm will result
in an error.
If not specified, then the plugin may be loaded by Slurm commands and
daemons from any version, however this may result in difficult to diagnose
failures due to changes in the arguments to plugin functions or changes
in other Slurm functions used by the plugin.

Slurm can be configured to use multiple cli\_filter plugins if desired,
however the lua plugin will only execute one lua script named "cli\_filter.lua"
located in the default script directory (typically the subdirectory "etc" of
the installation directory).

## API Functions

All of the following functions are required. Functions which are not
implemented must be stubbed.

int init(void)

**Description**:  
Called when the plugin is loaded, before any other functions are
called. Put global initialization here.

**Returns**:   
SLURM\_SUCCESS on success, or  
SLURM\_ERROR on failure.

void fini(void)

**Description**:  
Called when the plugin is removed. Clear any allocated storage here.

**Returns**: None.

**Note**: These init and fini functions are not the same as those
described in the dlopen (3) system library.
The C run-time system co-opts those symbols for its own initialization.
The system \_init() is called before the Slurm
init(), and the Slurm
fini() is called before the system's
\_fini().

int cli\_filter\_p\_setup\_defaults(slurm\_opt\_t \*options, bool early)

**Description**:  
This function is called by the salloc, sbatch, or srun command line interface
(CLI) programs shortly before processing any options from the environment,
command line, or script (#SBATCH). The hook may be run multiple times per job
component, once for an early pass (if implemented by the CLI), and again for
the main pass.
Note that this call is skipped for any srun command run within an existing job
allocation to prevent settings from overriding the set of options that have been
populated for the job based on the job environment.
The options and early arguments are meant to be passed to **slurm\_option\_set()**
which will set the option if it is in the appropriate pass. Failures to set
an option may be a symptom of trying to set the option on the wrong pass. Given
that you should not return SLURM\_ERROR simply because of a failure to set an option.

**Arguments**:   
options
(input) slurm option data structure; meant to be passed to the slurm\_option\_\* API
within *src/common/slurm\_opt.h*.  
early
(input) boolean indicating if this is the early pass or not; meant to be passed to
the slurm\_option\_\* API within *src/common/slurm\_opt.h*.  

**Returns**:   
SLURM\_SUCCESS on success, or  
SLURM\_ERROR on failure, will terminate execution
of the CLI.

int cli\_filter\_p\_pre\_submit(slurm\_opt\_t \*options, int offset)

**Description**:  
This function is called by the CLI after option processing but before any
communication with the slurmctld is made. This is after all
cli\_filter\_p\_setup\_defaults()
hooks are executed (for the current job component), environment variables
processed, command line options and #SBATCH directives interpreted.
cli\_filter\_p\_pre\_submit() is called before any parts of
the data structure are rewritten, so it is safe to
both read and write or unset any options from the plugin that you desire.
Note that cli\_filter\_p\_post\_submit() cannot safely read (or write) the options,
so you should save any state for logging in cli\_filter\_p\_post\_submit() during
cli\_filter\_p\_pre\_submit(). This function is called once per job component.

**Arguments**:   
options
(input/output) the job allocation request specifications.  
offset
(input) integer value for the current hetjob offset; should be used as a key when
storing data for communication between cli\_filter\_p\_pre\_submit() and
cli\_filter\_p\_post\_submit().  

**Returns**:   
SLURM\_SUCCESS on success, or  
SLURM\_ERROR on failure, will terminate execution
of the CLI.

void cli\_filter\_p\_post\_submit(int offset, uint32\_t jobid, uint32\_t stepid)

**Description**:  
This function is called by the CLI after a jobid (and, if srun, a stepid) has
been assigned by the controller. It is no longer safe to read or write to the
options data structure, so it has been removed from this function. You should
save any state you need in cli\_filter\_p\_pre\_submit() using het\_job\_offset as a
key, since the function is called separately for every job component, and access
it here.

**Arguments**:   
offset
(input) integer value for the current hetjob offset; should be used as a key
when storing data for communication between cli\_filter\_p\_pre\_submit() and
cli\_filter\_p\_post\_submit().  
jobid
(input) job id of the job  
stepid
(input) step id of the job if appropriate, NO\_VAL otherwise  

## LUA Interface

Setting **CliFilterPlugins=cli\_filter/lua** in slurm.conf will allow
you to implement the API functions mentioned using Lua language. Unless
otherwise specified via
[CliFilterParameters=cli\_filter\_lua\_path](slurm.conf.html#OPT_cli_filter_lua_path),
the file must be named "cli\_filter.lua" and, similar to the job\_submit plugin,
it must be located in the default configuration directory (typically the
subdirectory "etc" of the installation).
An example is provided within the source code
[here](https://github.com/SchedMD/slurm/blob/master/etc/cli_filter.lua.example).

If explicitly configuring a path for "cli\_filter.lua" the configured
directory containing the cli\_filter.lua script should have 755 permissions,
the script itself 644 and both be owned by SlurmdUser.

**NOTE**: Although available options are defined in the struct
slurm\_opt\_t within
*src/common/slurm\_opt.h*, some options might be renamed. The provided
example shows a way of displaying the configured options by using
slurm.json\_cli\_options(options).

## User Defaults

Setting **CliFilterPlugins=cli\_filter/user\_defaults** in slurm.conf will
allow users to define their own defaults for jobs submitted from the machine(s)
with the configured file. The plugin looks for the definition file in
`$HOME/.slurm/defaults`. It will read each line as a
`component=value` pair, where `component` is any of the
job submission options available to salloc, sbatch, or srun and
`value` is a default value defined by the user. The following
example would configure each job to have a default name, time limit, amount
of memory, and error and output files:

```
job-name=default_name
time=10:00
mem=256
error = slurm-%j.errfile
output = slurm-%j.logfile
```

You can also specify different default settings for jobs based on the
command being used to submit the job and/or the cluster being submitted to.
The syntax for this would be:  
`<command>:<cluster>:<component>`

`<command>` could be one of:

* **salloc**: Jobs submitted with the salloc command.
* **sbatch**: Jobs submitted with the sbatch command.
* **srun**: Jobs submitted with the srun command.
* **\***: Jobs submitted with any submission command.

`<cluster>` could be any defined cluster on your system,
or **\*** to have it match any cluster.

`<component>` is any of the job submission options
available to salloc, sbatch, or srun.

The following example would assign different default partitions based on
the command used to submit the job. It would also assign different partitions
for jobs submitted with salloc, depending on the cluster being used:

```
salloc:cluster1:partition = interactive
salloc:cluster2:partition = member
sbatch:*:partition = high
srun:*:partition = short
```