# Source: https://slurm.schedmd.com/sackd.html

# sackd

Section: Slurm Auth and Cred Kiosk Daemon (8)  
Updated: Slurm Auth and Cred Kiosk Daemon  
[Index](#index)

## NAME

sackd - Slurm Auth and Cred Kiosk Daemon.

## SYNOPSIS

**sackd** [*OPTIONS*...]

## DESCRIPTION

**sackd** is the Slurm Auth and Cred Kiosk Daemon. It can be used on login
nodes that are not running slurmd daemons to allow authentication to the
cluster. The program will run as the *SlurmUser*. When running in Slurm's
"configless" mode, in which case configuration files are retrieved and written
under the /run/slurm/conf directory (unless **RUNTIME\_DIRECTORY** is set).

## OPTIONS

**--ca-cert-file <file>**
:   Absolute path to CA certificate used for fetching configuration when running
    configless in a TLS enabled cluster.

    : **--conf-server host[:port]** : Retrieve configs from slurmctld running at *host[:port]*. Requires slurmctld support provided by setting **enable\_configless** in SlurmctldParameters. : **-D** : Run **sackd** in the foreground with logging copied to stderr. : **--disable-reconfig** : Fetch configurations in configless mode once, but do not register with slurmctld for further reconfiguration updates. : **-f config** : Read configuration from the specified file. : **-h** : Help; print a brief summary of command options. : **--jwks-file <file>** : Read auth/slurm JWKS information from the specified file. Default value is slurm.jwks located in the same directory as slurm.conf. : **--key-file <file>** : Read auth/slurm authentication key from the specified file. Default value is slurm.key located in the same directory as slurm.conf. : **--port number** : Port socket number to listen for reconfiguration updates. This can be useful when multiple sackds co-exist on the same login node. The default value is **SlurmdPort**. : **--systemd** : To be used when started from a systemd unit file. : **-v** : Verbose mode. Multiple -v's increase verbosity.

## ENVIRONMENT VARIABLES

The following environment variables can be used to override settings
compiled into sackd.

**ABORT\_ON\_FATAL**
:   When a fatal error is detected, use abort() instead of exit() to terminate the
    process. This allows backtraces to be captured without recompiling Slurm.

    : **RUNTIME\_DIRECTORY** : Absolute path governing the location for both the configuration cache sackd maintains, and the sack.socket unix socket used to provide authentication services. If multiple sackds need to be started on the same login node, the **RuntimeDirectory** systemd unit option should be set to **slurm-<clustername>**. Systemd v240+ automatically sets **RUNTIME\_DIRECTORY** to **/run/$RuntimeDirectory** for each sackd service, otherwise it requires manual setting (i.e. via **EnvironmentFile** unit option). If this is not set, the default value is **/run/slurm/**. : **SACKD\_DEBUG** : Set debug level explicitly for syslog and stderr. Valid values are 0-9, or the same string values as the debug options such as SlurmctldDebug in [slurm.conf](slurm.conf.md)(5). : **SACKD\_DISABLE\_RECONFIG** : Same as **--disable-reconfig**. : **SACKD\_PORT** : Same as **--port**. : **SACKD\_STDERR\_DEBUG** : Set debug level explicitly for stderr. Valid values are 0-9, or the same string values as the debug options such as SlurmctldDebug in [slurm.conf](slurm.conf.md)(5). : **SACKD\_SYSLOG\_DEBUG** : Set debug level explicitly for syslog. Valid values are 0-9, or the same string values as the debug options such as SlurmctldDebug in [slurm.conf](slurm.conf.md)(5). : **SLURM\_CONF** : The location of the Slurm configuration file. : **SLURM\_DEBUG\_FLAGS** : Specify debug flags for sackd to use. See DebugFlags in the **[slurm.conf](slurm.conf.md)**(5) man page for a full list of flags. The environment variable takes precedence over the setting in the slurm.conf.

## SIGNALS

**SIGINT**
:   **sackd** will shutdown cleanly.

    : **SIGHUP** : **sackd** will reconfigure. : **SIGUSR2 SIGPIPE** : This signal is explicitly ignored.

## COPYING

Copyright (C) SchedMD LLC.

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

**[slurm.conf](slurm.conf.md)**(5), **[slurmctld](slurmctld.md)**(8)

---



## Index

[NAME](#lbAB): [SYNOPSIS](#lbAC): [DESCRIPTION](#lbAD): [OPTIONS](#lbAE): [ENVIRONMENT VARIABLES](#lbAF): [SIGNALS](#lbAG): [COPYING](#lbAH): [SEE ALSO](#lbAI)

---

This document was created by
*man2html* using the manual pages.  
Time: 20:36:11 GMT, January 15, 2026