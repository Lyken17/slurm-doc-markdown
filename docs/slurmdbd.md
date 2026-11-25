# Slurm Workload Manager - slurmdbd

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

# slurmdbd

Section: Slurm Daemon (8)  
Updated: Slurm Daemon  
[Index](#index)

## NAME

slurmdbd - Slurm Database Daemon.

## SYNOPSIS

**slurmdbd** [*OPTIONS*...]

## DESCRIPTION

**slurmdbd** provides a secure enterprise-wide interface to a database
for Slurm. This is particularly useful for archiving accounting records.

## OPTIONS

**-D**
:   Run **slurmdbd** in the foreground with logging copied to stdout.

    : **-h** : Help; print a brief summary of command options. : **-n <value>** : Set the daemon's nice value to the specified value, typically a negative number. : **-s** : Change working directory of slurmdbd to LogFile path if possible, or to /var/tmp otherwise. : **-u** : Only display the Slurm Database version and if conversion is needed and exit without taking control. If no conversion is needed 0 is returned, if conversion is needed 1 is returned. : **-v** : Verbose operation. Multiple **v**'s can be specified, with each '**v**' beyond the first increasing verbosity, up to 6 times (i.e. -vvvvvv). : **-V** : Print version information and exit.

## ENVIRONMENT VARIABLES

The following environment variables can be used to override settings
compiled into slurmdbd.

**ABORT\_ON\_FATAL**
:   When a fatal error is detected, use abort() instead of exit() to terminate the
    process. This allows backtraces to be captured without recompiling Slurm.

## HTTP server

The HTTP server shares the RPC listening sockets on **DbdPort**.
Set **CommunicationParameters**=**disable\_http** in
**[slurmdbd.conf](slurmdbd.conf.md)**(5) to disable HTTP without disabling RPC service.
Changes to **disable\_http** or **HttpAuthParameters** are not picked up
by **sacctmgr reconfigure**; they require a restart of **slurmdbd**.

Plain HTTP remains available even when **TLSType** requires TLS for RPCs.
HTTPS is available when TLS support and server certificates are configured.
Use HTTPS to protect authentication tokens in transit.

Configure **HttpAuthParameters** in **[slurmdbd.conf](slurmdbd.conf.md)**(5) for requests
that require authentication.
Supply a JWT using either **Authorization**: **Bearer** <*token*>
or **X-SLURM-USER-TOKEN**.
The optional **X-SLURM-USER-NAME** header supplies the user name.
Do not send both token headers in one request; such a request returns
HTTP 401.
HTTP and RPC authentication use independent keys; an RPC JWT is not
necessarily valid for HTTP.
When **HttpAuthParameters** is unset, requests requiring authentication
return HTTP 401, while public endpoints remain available.

Ordinary replies and unknown paths support HTTP/1.1 connection reuse.
A **Connection**: **close** request closes the connection after its reply.
Authentication and endpoint request failures may close the connection.

### Public endpoints

All endpoints use the GET method.

**GET /**
:   : Return the endpoint index with HTTP 200.

    : **GET /healthz** : Test whether the daemon is online. Return HTTP 200 with a body of **HEALTHY** on success, or HTTP 500 with an empty body on failure. : **GET /livez** : Test whether the daemon is online. Return HTTP 200 with a body of **LIVE** on success, or HTTP 500 with an empty body on failure. : **GET /readyz**[**?verbose**] : Test whether this daemon is the active **slurmdbd**, not a standby backup, and whether its readiness probes pass. Return HTTP 200 with a body of **READY** on success, or HTTP 500 with an empty body on failure. With **?verbose**, the body holds the probe details, if any, instead of **READY** on success or an empty body on failure. A verbose request requires authentication as root or **SlurmUser**. Missing credentials return HTTP 401; an authenticated user without the required privilege receives HTTP 403. The verbose output is intended for humans, not as a stable data format.

Unknown paths return HTTP 404.

### Versioned endpoints

Replace <*data\_parser*> with an installed parser version, such as
**v0.0.46**.
Successful replies use that parser's response schema and default to JSON.
Use the **Accept** header to select a supported serializer format, for
example **application/json**.
See **SerializerPlugins** in **[slurmdbd.conf](slurmdbd.conf.md)**(5).
These endpoints require HTTP authentication and return HTTP 200 on success.
Missing credentials or invalid tokens return HTTP 401; an authenticated
user without the required privilege receives HTTP 403.
Endpoint errors may return a plain-text explanation rather than JSON.

**GET /**<*data\_parser*>**/conf**
:   Return the responding daemon's configuration in the **slurmdbd\_conf**
    response field.
    Requires a <*data\_parser*> of **v0.0.45** or later; older parser
    versions return HTTP 404.
    Any authenticated user may request it.

    : **GET /**<*data\_parser*>**/diag** : Return the responding daemon's RPC and rollup statistics in the **statistics** response field. RPC and user counters include counts and total and average processing times in microseconds. Any installed <*data\_parser*> version may be used. Requires root, **SlurmUser**, or an accounting user with **AdminLevel**=**Administrator**.

### Standby operation

A newly started backup (**DbdBackupHost**) does not open its RPC/HTTP
listener until its first takeover, so connections to it, including
**/livez** and **/healthz**, are refused until then.
If it later returns to standby without restarting, the listener remains open.
Standby mode alone does not fail **/livez** or **/healthz**, but causes
**/readyz** to return HTTP 500.
HTTP responses describe the answering daemon; requests are not redirected
to the active peer.

## CORE FILE LOCATION

If slurmdbd is started with the **-D** option then the core file will be
written to the current working directory.
Otherwise if **LogFile** in "slurmdbd.conf" is a fully qualified
path name (starting with a slash), the core file will be written to
the same directory as the log file, provided SlurmUser has write
permission on the directory. Otherwise the core file will be written
to "/var/tmp/" as a last resort. If neither of the above directories
have write permission for SlurmUser, no core file will be produced.

## SIGNALS

**SIGTERM SIGINT SIGQUIT**
:   **slurmdbd** will shutdown cleanly, waiting for in-progress rollups to
    finish.

    : **SIGABRT** : **slurmdbd** will perform a core dump, then exit. In-progress operations are killed. : **SIGHUP** : Reloads the slurm configuration files, similar to 'scontrol reconfigure'. : **SIGTSTP** : Stop the process from a terminal. : **SIGUSR2** : Reread the log level from the configs, and then reopen the log file. This should be used when setting up **logrotate**(8). : **SIGCHLD SIGUSR1 SIGXCPU SIGPIPE SIGALRM** : These signals are explicitly ignored.

## NOTES

It may be useful to experiment with different **slurmctld** specific
configuration parameters using a distinct configuration file
(e.g. timeouts). However, this special configuration file will not be
used by the **slurmd** daemon or the Slurm programs, unless you
specifically tell each of them to use it. If you desire changing
communication ports, the location of the temporary file system, or
other parameters used by other Slurm components, change the common
configuration file, **slurm.conf**.

## COPYING

Copyright (C) 2008 Lawrence Livermore National Security.
Copyright (C) 2010-2022 SchedMD LLC.
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

## SEE ALSO

**[slurm.conf](slurm.conf.md)**(5), **[slurmdbd.conf](slurmdbd.conf.md)**(5), **[slurmctld](slurmctld.md)**(8)

---



## Index

[NAME](#lbAB): [SYNOPSIS](#lbAC): [DESCRIPTION](#lbAD): [OPTIONS](#lbAE): [ENVIRONMENT VARIABLES](#lbAF): [HTTP server](#lbAG): [Public endpoints](#lbAH): [Versioned endpoints](#lbAI): [Standby operation](#lbAJ) [CORE FILE LOCATION](#lbAK): [SIGNALS](#lbAL): [NOTES](#lbAM): [COPYING](#lbAN): [SEE ALSO](#lbAO)

---

This document was created by
*man2html* using the manual pages.  
Time: 20:23:17 GMT, November 24, 2026