# Source: https://slurm.schedmd.com/rest_quickstart.html

# REST API Quick Start Guide

Slurm provides a [REST API](https://restfulapi.net/) through the
slurmrestd daemon, using [JSON Web Tokens](jwt.html) for
authentication. This daemon is designed to allow clients to communicate with
Slurm via a REST API (in addition to the command line interface (CLI) or C API).
This page provides a brief tutorial for setting up these components.

See also:

* [REST API Details](rest.html)
* [REST API Methods and Models](rest_api.html)
* [slurmrestd man page](slurmrestd.html)
* [OpenAPI Plugin Release Notes](openapi_release_notes.html)
* [REST API Client Guide](rest_clients.html)

## Contents

* [Prerequisites](#prereq)
* [Quick Start](#quick_start)
  + [Running with systemd](#systemd)
  + [Customizing slurmrestd.service](#customization)
* [Basic Usage](#basic_usage)
  + [Token management](#tokens)
* [Advanced Usage](#advanced_usage)
* [Common Issues](#common_issues)
  + [Unable to bind socket](#bind_socket)
  + [Connection refused](#connection_refused)
  + [Protocol authentication error (HTTP 500)](#authentication_error)
  + [Unable to find requested URL (HTTP 404)](#invalid_url)
  + [Rejecting thread config token (HTTP 401)](#rejected_token)
  + [Unexpected URL character (HTTP 400)](#unexpected_character)
  + [Other Slurm commands not working](#slurm_commands)

## Prerequisites

The following development libraries are required at compile time
in order for slurmrestd to be compiled (minimum versions are on the related
software page linked below):

* [HTTP Parser](related_software.html#httpparser)
* [JSON-C](related_software.html#json)

The following development libraries are optional; if present at compile time
the related functionality will be available:

* [YAML](related_software.html#yaml) (YAML support)
* [JWT](related_software.html#jwt)
  (authentication for socket-based clients)
* [s2n](tls.html#s2n) (TLS communications)

It is generally recommended that you have
[slurmdbd](slurmdbd.html) set up for
[accounting](accounting.html). Without slurmdbd you may need to
start slurmrestd with the [-s](slurmrestd.html#OPT_-s-<plugin>)
flag to tell it not to load the slurmdbd plugin.

## Quick Start

This may be done on a dedicated REST API machine or
your existing 'slurmctld' machine, depending on demand.
If you have multiple clusters, you will need a unique instance of
**slurmrestd** for each cluster.

1. Install components for slurmrestd
   * DEB: `slurm-smd slurm-smd-slurmrestd`
   * RPM: `slurm slurm-slurmrestd` (requires
     `--with slurmrestd` at build time)
2. Set up [JSON Web Tokens](jwt.html) for authentication
3. Ensure `/etc/slurm/slurm.conf` is present and correct for your
   cluster (see [Quick Start Admin Guide](quickstart_admin.html) and
   [slurm.conf man page](slurm.conf.html))
4. Run **slurmrestd** (see [below](#systemd) for systemd
   instructions) on your preferred [HOST]:PORT combination
   (':6820' is the default for production)

   ```
   export SLURM_JWT=daemon
   export SLURMRESTD_DEBUG=debug
   slurmrestd <host>:<port>
   ```

   Adjust SLURMRESTD\_DEBUG to the desired level of output (as described on the
   [man page](slurmrestd.html#OPT_SLURMRESTD_DEBUG))

### Running with systemd

Slurm ships with a **slurmrestd** service unit for systemd,
however, it might require some additional setup to run properly.
This section assumes you have either installed slurmrestd using DEB/RPM packages
or built it manually such that the files are in the same places.
  
**Note** the versions associated with certain steps in the instructions
below; these steps should be ignored on other versions.

1. Create a local service account and group of `slurmrestd` to
   run the slurmrestd daemon. To prevent privilege escalation, the user account
   should be:
   * Not root or SlurmUser
   * Not used by real users or for any other functions
   * Not granted any special permissions

   ```
   sudo useradd -M -r -s /usr/sbin/nologin -U slurmrestd
   ```
2. If needed, sites can run `systemctl edit slurmrestd` to
   override the default User and Group to the site specific user and group:

   ```
   [Service]
     User=slurmrestd
     Group=slurmrestd
   ```
3. (Slurm **24.05** and newer) Optional: Customize the socket for
   slurmrestd. By default it will listen only on TCP port 6820. You may change
   this behavior by changing `SLURMRESTD_LISTEN`
   (see [Customizing slurmrestd.service](#customization)).
4. (Slurm **23.11** and earlier) Configure the socket for slurmrestd. This
   may be accomplished by creating/changing permissions on the parent directory
   and/or changing the path to the socket in the service file.
   * **Permissions**: The user running the service must have write+execute
     permissions on the directory that will contain the UNIX socket
   * **Changing socket**: On Slurm 23.11, the way to change or disable the
     socket is to modify the 'ExecStart' line of the service
     1. Run `systemctl edit slurmrestd`
     2. Add the following contents to the `[Service]` section:

        ```
        ExecStart=
        ExecStart=/usr/sbin/slurmrestd $SLURMRESTD_OPTIONS
        Environment=SLURMRESTD_LISTEN=:6820
        ```
     3. Adjust the assignment of SLURMRESTD\_LISTEN to contain the socket(s) you want
        the daemon to listen on.
     4. After a future upgrade to Slurm 24.05+, the 'ExecStart' overrides will be
        unnecessary but will not conflict with the newer version.

### Customizing slurmrestd.service

The Slurm 24.05 release changes the operation of
the default service file and may break existing overrides. If you have
overridden `ExecStart=` to contain any TCP/UNIX sockets directly, it
will cause the service to fail if it duplicates any sockets contained in
SLURMRESTD\_LISTEN. These overrides will need to be changed after upgrading.

The default `slurmrestd.service` file has two intended ways of
customizing its operation:

1. **Environment files**:
   The service will read environment variables from two files:
   `/etc/default/slurmrestd` and `/etc/sysconfig/slurmrestd`.
   You may set any environment variables recognized by
   [slurmrestd](slurmrestd.html#SECTION_ENVIRONMENT-VARIABLES),
   but the following are particularly relevant:
   * **SLURMRESTD\_OPTIONS**: CLI options to add to the slurmrestd command
     (see [slurmrestd](slurmrestd.html))
   * **SLURMRESTD\_LISTEN**: Comma-delimited list of host:port pairs or
     unix:$SOCKET\_PATH sockets to listen on
       
     **NOTE**: If this duplicates what is already set in the
     'ExecStart' line in the service file, it will fail. Starting in Slurm 24.05,
     the default service file contains no sockets in 'ExecStart' and fully relies on
     this variable to contain the desired sockets.
2. **Service editing**: Systemd has a built in way to edit services
   by running `systemctl edit slurmrestd`.
   * This will create an override file in '/etc/systemd/' containing directives
     that will add to or replace directives in the default unit in '/lib/systemd/'.
   * The override file must have the appropriate section declaration(s)
     for the directives you use (e.g., `[Service]`).
   * Environment variables may be set with `Environment=NAME=value`
     (refer to systemd documentation for more details)
   * Changes may be reverted by running `systemctl revert slurmrestd`

## Basic Usage

1. Find the latest supported API version

   ```
   slurmrestd -d list
   ```
2. Get an authentication token for JWT

   ```
   unset SLURM_JWT; export $(scontrol token)
   ```

   * This ensures an old token doesn't prevent a new one from being issued
   * By default, tokens will expire after 1800 seconds (30 minutes).
     Add `lifespan=SECONDS` to the 'scontrol' command to change this.
3. Run a basic curl command to hit the API when listening on a TCP host:port

   ```
   curl -s -o "/tmp/curl.log" -k -vvvv \
   -H X-SLURM-USER-TOKEN:$SLURM_JWT \
   -X GET 'http://<server>:<port>/slurm/v0.0.<api-version>/diag'
   ```

   * Replace the **server**, **port**, and **api-version**
     with the appropriate values.
   * Examine the output to ensure the response was **200 OK**,
     and examine **/tmp/curl.log** for a valid JSON response.
   * Try other endpoints described in the [API Methods
     and Models](rest_api.html). Change **GET** to the correct method for the endpoint.
4. Alternate command to use the UNIX socket instead

   ```
   curl -s -o "/tmp/curl.log" -k -vvvv \
   -H X-SLURM-USER-TOKEN:$SLURM_JWT \
   --unix-socket /path/to/slurmrestd.socket \
   'http://<server>/slurm/v0.0.<api-version>/diag'
   ```

   * Replace the **path**, **server**, and **api-version**
     with the appropriate values.
   * Examine the output to ensure the response was **200 OK**,
     and examine **/tmp/curl.log** for a valid JSON response.

### Token management

This guide provides a simple overview using `scontrol` to
obtain tokens. This is a basic introductory approach that in many cases
should be disabled in favor of more sophisticated token management.
Refer to the [JWT page](jwt.html) for more details.

## Advanced Usage

Information about ways to further customize and configure slurmrestd,
including authentication methods, run modes, plugins, high availability, proxies,
and Python client is found on the [REST API Details](rest.html) page.

## Common Issues

In general, look out for these things:

1. Validity of authentication token in `SLURM_JWT`
2. Hostname and port number
3. API version and endpoint
4. Log output of slurmrestd

### Unable to bind socket

This may be due to a permissions issue while attempting to set up the socket.
Check the log output from slurmrestd for the path to the socket.
Ensure that the user running the slurmrestd service has permissions to the
parent directory of the configured socket path, or change/remove the socket path
as [described above](#systemd).

If it says "**Address already in use**", check the command being run
and the contents of "SLURMRESTD\_LISTEN" for duplicates of the same TCP or UNIX
socket.

### Connection refused

Verify that slurmrestd is running and listening on the port you are
attempting to connect to.

### Protocol authentication error (HTTP 500)

One common authentication problem is an expired token. Request a new one:

```
unset SLURM_JWT; export $(scontrol token)
```

This solution also applies to an HTTP 401 error caused by no authentication
token being sent at all. This may appear in the slurmrestd logs as
"Authentication does not apply to request."

Otherwise, consult the logs on the **slurmctld** and **slurmdbd**.

### Unable to find requested URL (HTTP 404)

Check the [API Methods and Models](rest_api.html) page to ensure
you're using a valid URL and the correct method for it. Pay attention to the
path as there are different endpoints for **slurm** and **slurmdbd**.

### Rejecting thread config token (HTTP 401)

Check that slurmrestd has loaded the **auth/jwt** plugin.
You should see a debug message like this:

```
slurmrestd: debug:  auth/jwt: init: JWT authentication plugin loaded
```

If it didn't load jwt, run this in the terminal you're using for slurmrestd:

```
export SLURM_JWT=daemon
```

### Unexpected URL character (HTTP 400)

Check the request URL and slurmrestd logs for characters that may be causing
the URL to be parsed incorrectly. Use the appropriate URL encoding sequence in
place of the problematic character (e.g., **/** = **%2F**).

```
... -X GET "localhost:8080/slurmdb/v0.0.40/jobs?submit_time=02/28/24"
### 400 BAD REQUEST
... -X GET "localhost:8080/slurmdb/v0.0.40/jobs?submit_time=02%2F28%2F24"
### 200 OK
```

### Other slurm commands not working

If SLURM\_JWT is set, other slurm commands will attempt to use JWT
authentication, causing failures. This can be fixed by clearing the variable:

```
unset SLURM_JWT
```