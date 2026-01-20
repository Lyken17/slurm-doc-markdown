# Source: https://slurm.schedmd.com/spank.html

# SPANK

Section: Slurm Component (8)  
Updated: Slurm Component  
[Index](#index)

## NAME

**SPANK** - Slurm Plug-in Architecture for Node and job (K)control

## DESCRIPTION

This manual briefly describes the capabilities of the Slurm Plug-in
Architecture for Node and job Kontrol (**SPANK**) as well as the **SPANK**
configuration file: (By default: **plugstack.conf**.)

**SPANK** provides a very generic interface for stackable plug-ins
which may be used to dynamically modify the job launch code in
Slurm. **SPANK** plugins may be built without access to Slurm source
code. They need only be compiled against Slurm's **spank.h** header file,
added to the **SPANK** config file **plugstack.conf**,
and they will be loaded at runtime during the next job launch. Thus,
the **SPANK** infrastructure provides administrators and other developers
a low cost, low effort ability to dynamically modify the runtime
behavior of Slurm job launch.

**NOTE**: All **SPANK** plugins should be recompiled when upgrading Slurm
to a new major release. The **SPANK** API is not guaranteed to be ABI
compatible between major releases. Any **SPANK** plugin linking to any of the
Slurm libraries should be carefully checked as the Slurm APIs and headers
can change between major releases.

## SPANK PLUGINS

**SPANK** plugins are loaded in up to five separate contexts during a
**Slurm** job. Briefly, the five contexts are:

**local**
:   In **local** context, the plugin is loaded by **srun**. (i.e. the "local"
    part of a parallel job).

    : **remote** : In **remote** context, the plugin is loaded by **slurmstepd**. (i.e. the "remote" part of a parallel job). : **allocator** : In **allocator** context, the plugin is loaded in one of the job allocation utilities **salloc**, **sbatch** or **scrontab**. : **slurmd** : In **slurmd** context, the plugin is loaded in the **slurmd** daemon itself. **NOTE**: Plugins loaded in slurmd context persist for the entire time slurmd is running, so if configuration is changed or plugins are updated, slurmd must be restarted for the changes to take effect. : **job\_script** : In the **job\_script** context, plugins are loaded in the context of the job prolog or epilog. **NOTE**: Plugins are loaded in **job\_script** context on each run on the job prolog or epilog, in a separate address space from plugins in **slurmd** context. This means there is no state shared between this context and other contexts, or even between one call to **slurm\_spank\_job\_prolog** or **slurm\_spank\_job\_epilog** and subsequent calls.

In local context, only the **init**, **exit**, **init\_post\_opt**, and
**local\_user\_init** functions are called. In allocator context, only the
**init**, **exit**, and **init\_post\_opt** functions are called.
Similarly, in slurmd context, only the **init** and **slurmd\_exit**
callbacks are active, and in the job\_script context, only the **job\_prolog**
and **job\_epilog** callbacks are used.
Plugins may query the context in which they are running with the
**spank\_context** and **spank\_remote** functions defined in
**spank.h**.

**SPANK** plugins may be called from multiple points during the Slurm job
launch. A plugin may define the following functions:

**slurm\_spank\_init**
:   Called just after plugins are loaded. In remote context, this is just
    after job step is initialized. This function is called before any plugin
    option processing.

    : **slurm\_spank\_job\_prolog** : Called at the same time as the job prolog. If this function returns a non-zero value and the **SPANK** plugin that contains it is required in the **plugstack.conf**, the node that this is run on will be drained. : **slurm\_spank\_init\_post\_opt** : Called at the same point as **slurm\_spank\_init**, but after all user options to the plugin have been processed. The reason that the **init** and **init\_post\_opt** callbacks are separated is so that plugins can process system-wide options specified in plugstack.conf in the **init** callback, then process user options, and finally take some action in **slurm\_spank\_init\_post\_opt** if necessary. In the case of a heterogeneous job, **slurm\_spank\_init** is invoked once per job component. : **slurm\_spank\_local\_user\_init** : Called in local (**srun**) context only after all options have been processed. This is called after the job ID and step IDs are available. This happens in **srun** after the allocation is made, but before tasks are launched. : **slurm\_spank\_user\_init** : Called after privileges are temporarily dropped. (remote context only) : **slurm\_spank\_task\_init\_privileged** : Called for each task just after fork, but before all elevated privileges are dropped. This can run in parallel with **slurm\_spank\_task\_post\_fork**. (remote context only) : **slurm\_spank\_task\_init** : Called for each task just before execve (2). If you are restricting memory with cgroups, memory allocated here will be in the job's cgroup. (remote context only) : **slurm\_spank\_task\_post\_fork** : Called for each task from parent process after fork (2) is complete. Due to the fact that **slurmd** does not exec any tasks until all tasks have completed fork (2), this call is guaranteed to run before the user task is executed. This can run in parallel with **slurm\_spank\_task\_init\_privileged**. (remote context only) : **slurm\_spank\_task\_exit** : Called for each task as its exit status is collected by Slurm. (remote context only) : **slurm\_spank\_exit** : Called once just before **slurmstepd** exits in remote context. In local context, called before **srun** exits. : **slurm\_spank\_job\_epilog** : Called at the same time as the job epilog. If this function returns a non-zero value and the **SPANK** plugin that contains it is required in the **plugstack.conf**, the node that this is run on will be drained. : **slurm\_spank\_slurmd\_exit** : Called in slurmd when the daemon is shut down.

All of these functions have the same prototype, for example:

```
   int slurm_spank_init (spank_t spank, int ac, char *argv[])
```

Where **spank** is the **SPANK** handle which must be passed back to
Slurm when the plugin calls functions like **spank\_get\_item** and
**spank\_getenv**. Configured arguments (See **CONFIGURATION**
below) are passed in the argument vector **argv** with argument
count **ac**.

A plugin may also define the following variables that will be used by Slurm:

**slurm\_spank\_init\_failure\_mode**
:   When a slurm\_spank\_init call fails, change how that failure is handled by Slurm.
    Recognized values are:

    : : **ESPANK\_NODE\_FAILURE** : Slurm considers the node to be at fault and marks it as drained. The job may be requeued. This is the default. : **ESPANK\_JOB\_FAILURE** : Slurm considers the job to be at fault and marks it as failed (not to be requeued). The node will not be drained.

**SPANK** plugins can query the current list of supported slurm\_spank
symbols to determine if the current version supports a given plugin hook.
This may be useful because the list of plugin symbols may grow in the
future. The query is done using the **spank\_symbol\_supported** function,
which has the following prototype:

```
    int spank_symbol_supported (const char *sym);
```

The return value is 1 if the symbol is supported, 0 if not.

**SPANK** plugins do not have direct access to internally defined Slurm
data structures. Instead, information about the currently executing
job is obtained via the **spank\_get\_item** function call.

```
  spank_err_t spank_get_item (spank_t spank, spank_item_t item, ...);
```

The **spank\_get\_item** call must be passed the current **SPANK**
handle as well as the item requested, which is defined by the
passed **spank\_item\_t**. A variable number of pointer arguments are also
passed, depending on which item was requested by the plugin. A
list of the valid values for **item** is kept in the **spank.h** header
file. Some examples are:

**S\_JOB\_UID**
:   User id for running job. (uid\_t \*) is third arg of **spank\_get\_item**

    : **S\_JOB\_STEPID** : Job step id for running job. (uint32\_t \*) is third arg of **spank\_get\_item**. : **S\_TASK\_EXIT\_STATUS** : Exit status for exited task. Only valid from **slurm\_spank\_task\_exit**. (int \*) is third arg of **spank\_get\_item**. : **S\_JOB\_ARGV** : Complete job command line. Third and fourth args to **spank\_get\_item** are (int \*, char \*\*\*).

See **spank.h** for more details.

**SPANK** functions in the **local and allocator** environment should
use the **getenv**, **setenv**, and **unsetenv** functions to view and
modify the job's environment.
**SPANK** functions in the **remote** environment should use the
**spank\_getenv**, **spank\_setenv**, and **spank\_unsetenv** functions to
view and modify the job's environment. **spank\_getenv**
searches the job's environment for the environment variable
*var* and copies the current value into a buffer *buf*
of length *len*. **spank\_setenv** allows a **SPANK**
plugin to set or overwrite a variable in the job's environment,
and **spank\_unsetenv** unsets an environment variable in
the job's environment. The prototypes are:

```
 spank_err_t spank_getenv (spank_t spank, const char *var,
                           char *buf, int len);
 spank_err_t spank_setenv (spank_t spank, const char *var,
                           const char *val, int overwrite);
 spank_err_t spank_unsetenv (spank_t spank, const char *var);
```

These are only necessary in remote context since modifications of
the standard process environment using **setenv** (3), **getenv** (3),
and **unsetenv** (3) may be used in local context.

Functions are also available from within the **SPANK** plugins to
establish environment variables to be exported to the Slurm
**PrologSlurmctld**, **Prolog**, **Epilog** and **EpilogSlurmctld**
programs (the so-called **job control** environment).
The name of environment variables established by these calls will be prepended
with the string *SPANK\_* in order to avoid any security implications
of arbitrary environment variable control. (After all, the job control
scripts do run as root or the Slurm user.).

These functions are available from **local** context only.

```
  spank_err_t spank_job_control_getenv(spank_t spank, const char *var,
                             char *buf, int len);
  spank_err_t spank_job_control_setenv(spank_t spank, const char *var,
                             const char *val, int overwrite);
  spank_err_t spank_job_control_unsetenv(spank_t spank, const char *var);
```

See **spank.h** for more information.

Many of the described **SPANK** functions available to plugins return
errors via the **spank\_err\_t** error type. On success, the return value
will be set to **ESPANK\_SUCCESS**, while on failure, the return value
will be set to one of many error values defined in **spank.h**. The
**SPANK** interface provides a simple function

```
  const char * spank_strerror(spank_err_t err);
```

which may be used to translate a **spank\_err\_t** value into its
string representation.

The **slurm\_spank\_log** function can be used to print messages back to the
user at an error level. This is to keep users from having to rely on the
**slurm\_error** function, which can be confusing because it prepends
"**error:**" to every message.

## SPANK OPTIONS

SPANK plugins also have an interface through which they may define
and implement extra job options. These options are made available to
the user through Slurm commands such as **[srun](srun.html)**(1), **[salloc](salloc.html)**(1),
and **[sbatch](sbatch.html)**(1). If the option is specified by the user, its value is
forwarded and registered with the plugin in slurmd when the job is run.
In this way, **SPANK** plugins may dynamically provide new options and
functionality to Slurm.

Each option registered by a plugin to Slurm takes the form of
a **struct spank\_option** which is declared in **spank.h** as

```
   struct spank_option {
      char *         name;
      char *         arginfo;
      char *         usage;
      int            has_arg;
      int            val;
      spank_opt_cb_f cb;
   };
```

Where

*name*
:   :   is the name of the option. Its length is limited to **SPANK\_OPTION\_MAXLEN**
        defined in **spank.h**.

        : *arginfo* : : is a description of the argument to the option, if the option does take an argument. : *usage* : : is a short description of the option suitable for --help output. : *has\_arg* : : 0 if option takes no argument, 1 if option takes an argument, and 2 if the option takes an optional argument. (See **getopt\_long** (3)). : *val* : : A plugin-local value to return to the option callback function. : *cb* : : A callback function that is invoked when the plugin option is registered with Slurm. **spank\_opt\_cb\_f** is typedef'd in **spank.h** as : ``` typedef int (*spank_opt_cb_f) (int val, const char *optarg, int remote); ``` Where *val* is the value of the *val* field in the **spank\_option** struct, *optarg* is the supplied argument if applicable, and *remote* is 0 if the function is being called from the "local" host (e.g. host where **srun** or **sbatch/salloc** are invoked) or 1 from the "remote" host (host where slurmd/slurmstepd run) but only executed by **slurmstepd** (remote context) if the option was registered for such context.

Plugin options may be registered with Slurm using
the **spank\_option\_register** function. This function is only valid
when called from the plugin's **slurm\_spank\_init** handler, and
registers one option at a time. The prototype is

```
   spank_err_t spank_option_register (spank_t sp,
                   struct spank_option *opt);
```

This function will return **ESPANK\_SUCCESS** on successful registration
of an option, or **ESPANK\_BAD\_ARG** for errors including invalid spank\_t
handle, or when the function is not called from the **slurm\_spank\_init**
function. All options need to be registered from all contexts in which
they will be used. For instance, if an option is only used in local (srun)
and remote (slurmd) contexts, then **spank\_option\_register**
should only be called from within those contexts. For example:

```
   if (spank_context() != S_CTX_ALLOCATOR)
      spank_option_register (sp, opt);
```

If, however, the option is used in all contexts, the **spank\_option\_register**
needs to be called everywhere.

In addition to **spank\_option\_register**, plugins may also export options
to Slurm by defining a table of **struct spank\_option** with the
symbol name **spank\_options**. This method, however, is not supported
for use with **sbatch** and **salloc** (allocator context), thus
the use of **spank\_option\_register** is preferred. When using the
**spank\_options** table, the final element in the array must be
filled with zeros. A **SPANK\_OPTIONS\_TABLE\_END** macro is provided
in **spank.h** for this purpose.

When an option is provided by the user on the local side, either by command line
options or by environment variables, **Slurm** will immediately invoke the
option's callback with *remote*=0. This is meant for the plugin to do local
sanity checking of the option before the value is sent to the remote side during
job launch. If the argument the user specified is invalid, the plugin should
issue an error and issue a non-zero return code from the callback. The plugin
should be able to handle cases where the spank option is set multiple times
through environment variables and command line options. Environment variables
are processed before command line options.

On the remote side, options and their arguments are registered just
after **SPANK** plugins are loaded and before the **spank\_init**
handler is called. This allows plugins to modify behavior of all plugin
functionality based on the value of user-provided options.

As an alternative to use of an option callback and global variable,
plugins can use the **spank\_option\_getopt** option to check for
supplied options after option processing. This function has the prototype:

```
   spank_err_t spank_option_getopt(spank_t sp,
       struct spank_option *opt, char **optargp);
```

This function returns **ESPANK\_SUCCESS** if the option defined in the
struct spank\_option *opt* has been used by the user. If *optargp*
is non-NULL then it is set to any option argument passed (if the option
takes an argument). The use of this method is *required* to process
options in **job\_script** context (**slurm\_spank\_job\_prolog** and
**slurm\_spank\_job\_epilog**). This function is valid in the following contexts:
slurm\_spank\_job\_prolog, slurm\_spank\_local\_user\_init, slurm\_spank\_user\_init,
slurm\_spank\_task\_init\_privileged, slurm\_spank\_task\_init, slurm\_spank\_task\_exit,
and slurm\_spank\_job\_epilog.

## CONFIGURATION

The default **SPANK** plug-in stack configuration file is
**plugstack.conf** in the same directory as **[slurm.conf](slurm.conf.html)**(5),
though this may be changed via the Slurm config parameter
*PlugStackConfig*. Normally the **plugstack.conf** file
should be identical on all nodes of the cluster.
The config file lists **SPANK** plugins,
one per line, along with whether the plugin is *required* or
*optional*, and any global arguments that are to be passed to
the plugin for runtime configuration. Comments are preceded with '#'
and extend to the end of the line. If the configuration file
is missing or empty, it will simply be ignored.

**NOTE**: The **SPANK** plugins need to be installed on the machines that
execute slurmd (compute nodes) as well as on the machines that execute job
allocation utilities such as salloc, sbatch, etc (login nodes).

The format of each non-comment line in the configuration file is:

```
  required/optional   plugin   arguments
```

For example:

```
  optional /usr/lib/slurm/test.so
```

Tells **slurmd** to load the plugin **test.so** passing no arguments.
If a **SPANK** plugin is *required*, then failure of any of the
plugin's functions will cause **slurmd**, or the job allocator command to
terminate the job, while *optional* plugins only cause a warning.

If a fully-qualified path is not specified for a plugin, then the
currently configured *PluginDir* in **[slurm.conf](slurm.conf.html)**(5) is searched.

**SPANK** plugins are stackable, meaning that more than one plugin may
be placed into the config file. The plugins will simply be called
in order, one after the other, and appropriate action taken on
failure given that state of the plugin's *optional* flag.

Additional config files or directories of config files may be included
in **plugstack.conf** with the **include** keyword. The **include**
keyword must appear on its own line, and takes a glob as its parameter,
so multiple files may be included from one **include** line. For
example, the following syntax will load all config files in the
/etc/slurm/plugstack.conf.d directory, in local collation order:

```
  include /etc/slurm/plugstack.conf.d/*
```

which might be considered a more flexible method for building up
a spank plugin stack.

The **SPANK** config file is re-read on each job launch, so editing
the config file will not affect running jobs. However care should
be taken so that a partially edited config file is not read by a
launching job.

## Errors

When SPANK plugin results in a non-zero result, the following changes will result:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Command | Function | Context | Exitcode | Drains Node | Fails job |
| srun | slurm\_spank\_init | local | 1 | no | yes |
| srun | slurm\_spank\_init\_post\_opt | local | 1 | no | yes |
| srun | slurm\_spank\_local\_user\_init | local | 1 | no | yes |
| srun | slurm\_spank\_init | remote | 1 | no | no |
| srun | slurm\_spank\_user\_init | remote | 0 | no | no |
| srun | slurm\_spank\_task\_init\_privileged | remote | 1 | no | yes |
| srun | slurm\_spank\_task\_post\_fork | remote | 0 | no | no |
| srun | slurm\_spank\_task\_init | remote | 1 | no | yes |
| srun | slurm\_spank\_task\_exit | remote | 0 | no | no |
| srun | slurm\_spank\_exit | local | 0 | no | yes |
| ---  --- | | | | | |
| salloc | slurm\_spank\_init | allocator | 1 | no | yes |
| salloc | slurm\_spank\_init\_post\_opt | allocator | 1 | no | yes |
| salloc | slurm\_spank\_init | remote | 1 | no | no |
| salloc | slurm\_spank\_user\_init | remote | 1 | no | yes |
| salloc | slurm\_spank\_task\_init\_privileged | remote | 1 | no | yes |
| salloc | slurm\_spank\_task\_post\_fork | remote | 1 | no | yes |
| salloc | slurm\_spank\_task\_init | remote | 1 | no | yes |
| salloc | slurm\_spank\_task\_exit | remote | 0 | no | no |
| salloc | slurm\_spank\_exit | allocator | 0 | no | yes |
| ---  --- | | | | | |
| sbatch | slurm\_spank\_init | allocator | 1 | no | yes |
| sbatch | slurm\_spank\_init\_post\_opt | allocator | 1 | no | yes |
| sbatch | slurm\_spank\_init | remote | 1 | yes | no |
| sbatch | slurm\_spank\_user\_init | remote | 1 | yes | yes |
| sbatch | slurm\_spank\_task\_init\_privileged | remote | 1 | no | yes |
| sbatch | slurm\_spank\_task\_post\_fork | remote | 1 | yes | yes |
| sbatch | slurm\_spank\_task\_init | remote | 1 | no | yes |
| sbatch | slurm\_spank\_task\_exit | remote | 0 | no | no |
| sbatch | slurm\_spank\_exit | allocator | 0 | no | no |
| ---  --- | | | | | |
| scrontab | slurm\_spank\_init | allocator | 1 | no | no |
| scrontab | slurm\_spank\_exit | allocator | 0 | no | no |

**NOTE**: The behavior for **ProctrackType=proctrack/pgid** may result in
timeouts for **slurm\_spank\_task\_post\_fork** with **remote** context on
failure.

## COPYING

Portions copyright (C) 2010-2022 SchedMD LLC.
Copyright (C) 2006 The Regents of the University of California.
Produced at Lawrence Livermore National Laboratory (cf, DISCLAIMER).
CODE-OCEC-09-009. All rights reserved.

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

## FILES

**/etc/slurm/slurm.conf** - Slurm configuration file.
  
**/etc/slurm/plugstack.conf** - SPANK configuration file.
  
**/usr/include/slurm/spank.h** - SPANK header file.

## SEE ALSO

**[srun](srun.html)**(1), **[slurm.conf](slurm.conf.html)**(5)

---



## Index

[NAME](#lbAB): [DESCRIPTION](#lbAC): [SPANK PLUGINS](#lbAD): [SPANK OPTIONS](#lbAE): [CONFIGURATION](#lbAF): [Errors](#lbAG): [COPYING](#lbAH): [FILES](#lbAI): [SEE ALSO](#lbAJ)

---

This document was created by
*man2html* using the manual pages.  
Time: 20:36:11 GMT, January 15, 2026