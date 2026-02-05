# Slurm Workload Manager - PrEp Plugin API

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

# PrEp Plugin API

## Overview

This document describes the Slurm PrEp — short for "Pr"olog and
"Ep"ilog — plugins API. It is intended as a resource to programmers
wishing to write their own Slurm prep plugins.

The purpose of the prep plugin APIs to provide a native C interface to the
same hooks traditionally used by the *Prolog*, *Epilog*,
*PrologSlurmctld*, and *EpilogSlurmctld* scripts. Those interfaces
are now implemented through the *prep/script* plugin, and that plugin
serves as a good example of how to approach development of additional
plugins.

Slurm PrEp plugins must conform to the Slurm Plugin API with the following
specifications:

const char plugin\_name[]="*full text name*"

A free-formatted ASCII text string that identifies the plugin.

const char plugin\_type[]="*major/minor*"

The major type must be "prep".
The minor type can be any suitable name for the type of prep plugin.

const uint32\_t plugin\_version

If specified, identifies the version of Slurm used to build this plugin and
any attempt to load the plugin from a different version of Slurm will result
in an error.
If not specified, then the plugin may be loaded by Slurm commands and
daemons from any version, however this may result in difficult to diagnose
failures due to changes in the arguments to plugin functions or changes
in other Slurm functions used by the plugin.

Slurm can be configured to use multiple prep plugins if desired through the
PrEpPlugins configuration option. Additional plugins should be comma-separated.
Note that, by default, the *prep/script* plugin is loaded if that option
is not set, but will not be loaded if an explicit setting has been made. Thus,
if you do set that option, and intend to still use the *Prolog*,
*Epilog*, *PrologSlurmctld*, and/or *EpilogSlurmctld* options
you will need to ensure both your additional plugin and *prep/script* are
set.

Special care must be used when developing against the
prep\_p\_prolog\_slurmctld() or
prep\_p\_epilog\_slurmctld() interfaces. These
functions are called while the slurmctld holds a number of internal locks,
and need to return quickly otherwise slurmctld responsiveness and system
throughput will be impacted. For simple logging, this is not required, and
the "async" option can be left to false. But, especially for anything
communicating with an external API or spawning additional processes, it is
highly recommended to first make a local copy of any job record details
required, and then spawn a separate processing thread — which, by default,
will not have inherited any slurmctld locks — to continue processing.
You must set the async return value to true, and call the corresponding
prolog\_slurmctld\_callback() or
epilog\_slurmctld\_callback() function before
the thread exits. These callbacks are provided as function pointers when the
slurmctld starts through
prep\_p\_register\_callbacks() call, and these
function pointers should be cached locally in your plugin.

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

void prep\_p\_register\_callbacks(prep\_callbacks\_t \*callbacks)

**Description**:  
This function is called by the slurmctld to pass function pointer addresses
used with asynchronous operation with the prep\_p\_prolog\_slurmctld() and
prep\_p\_epilog\_slurmctld() interfaces. These pointers must be saved if
asynchronous operation is used, otherwise this function can be an empty stub.

**Arguments**:   
callbacks
(input) contains function pointers for use with asynchronous operation within the slurmctld

**Returns**: None.

int prep\_p\_prolog(job\_env\_t \*job\_env, slurm\_cred\_t \*cred)

**Description**:  
Called within the slurmd as root before the first step of a job starts on the
compute node.

**Arguments**:   
job\_env
(input) details from the step launch request  
cred
(input) launch credential with additional verifiable launch details signed by
the slurmctld