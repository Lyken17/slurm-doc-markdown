# Slurm Workload Manager - Slurm Priority Site Factor Plugin API

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

# Slurm Priority Site Factor Plugin API

## Overview

This document describes Slurm site\_factor plugins and the API that defines
them. It is intended as a resource to programmers wishing to write their own
Slurm site\_factor plugins.

Slurm site\_factor plugins are Slurm plugins that implement the Slurm
site\_factor API described herein. They are designed to provide the site a
way to build a custom [multifactor priority](priority_multifactor.md)
factor, and will only be loaded and operated alongside
PriorityType=priority/multifactor.

The plugins are meant to set and update the
site\_factor value in the
job\_record\_t corresponding to a given job.
Note that the site\_factor itself is an
unsigned integer, but uses NICE\_OFFSET as
an offset to allow the value to be positive or negative. The plugin itself
must add NICE\_OFFSET to the value stored to
site\_factor for proper operation, otherwise
the value itself will be extremely negative, and the job priority will likely
drop to 1. (The lowest value that does not correspond to a held job.)

Plugins must conform to the Slurm Plugin API with the following
specifications:

const char plugin\_type[]="*major/minor*"  
The major type must be "site\_factor" The minor type can be any
recognizable abbreviation for the specific plugin.

const char plugin\_name[]  
Some descriptive name for the plugin.
There is no requirement with respect to its format.

const uint32\_t plugin\_version  
If specified, identifies the version of Slurm used to build this plugin and
any attempt to load the plugin from a different version of Slurm will result
in an error.
If not specified, then the plugin may be loaded by Slurm commands and
daemons from any version, however this may result in difficult to diagnose
failures due to changes in the arguments to plugin functions or changes
in other Slurm functions used by the plugin.

## API Functions

The following functions must appear. Functions which are not implemented
must be stubbed, or the plugin will fail to load.

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

void site\_factor\_p\_reconfig(void)

**Description**: Refresh the plugin's
configuration. Called whenever slurmctld is reconfigured.

**Returns**: void

void site\_factor\_p\_set(job\_record\_t \*job\_ptr)

**Description**: Sets the site\_priority of the job, if desired.

**Arguments**:  
job\_ptr (input) pointer to the job record.

**Returns**: void

void site\_factor\_p\_update(void)

**Description**: Handle periodic updates to
all site\_priority values in the job\_list. Called every

**Returns**: void

## Parameters

These parameters can be used in the slurm.conf to configure the
plugin and the frequency at which to gather information about running jobs.

PrioritySiteFactorParameters
:   Optional parameters for the site\_factor plugin. Interpretation of any
    value is left to the site\_factor plugin itself.

PrioritySiteFactorPlugin
:   Specifies which plugin should be used.

PriorityCalcPeriod
:   Interval between calls to
    site\_factor\_p\_update()