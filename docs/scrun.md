# Slurm Workload Manager - scrun

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

# scrun

Section: Slurm Commands (1)  
Updated: Slurm Commands  
[Index](#index)

## NAME

**scrun** - an OCI runtime proxy for Slurm.

## SYNOPSIS

## Create Operation

:   **scrun** [*GLOBAL OPTIONS*...] *create* [*CREATE OPTIONS*] <*container-id*>

    : Prepares a new container with container-id in current working directory.

    ## Start Operation

    :   **scrun** [*GLOBAL OPTIONS*...] *start* <*container-id*>

        : Request to start and run container in job.

        ## Query State Operation

        :   **scrun** [*GLOBAL OPTIONS*...] *state* <*container-id*>

            : Output OCI defined JSON state of container.

            ## Kill Operation

            :   **scrun** [*GLOBAL OPTIONS*...] *kill* <*container-id*> [*signal*]

                : Send signal (default: SIGTERM) to container.

                ## Delete Operation

                :   **scrun** [*GLOBAL OPTIONS*...] *delete* [*DELETE OPTIONS*] <*container-id*>

                    : Release any resources held by container locally and remotely. Perform OCI runtime operations against *container-id* per: <https://github.com/opencontainers/runtime-spec/blob/main/runtime.md> **scrun** attempts to mimic the commandline behavior as closely as possible to **crun** and **runc** in order to maintain in place replacement compatibility with **DOCKER** and **podman**. All commandline arguments for **crun** and **runc** will be accepted for compatibility but may be ignored depending on their applicability.

                    ## DESCRIPTION

                    **scrun** is an OCI runtime proxy for Slurm. It acts as a common interface to
                    **DOCKER** or **podman** to allow container operations to be executed
                    under Slurm as jobs. **scrun** will accept all commands as an OCI compliant
                    runtime but will proxy the container and all STDIO to Slurm for scheduling and
                    execution. The containers will be executed remotely on Slurm compute nodes
                    according to settings in
                    **[oci.conf](oci.conf.md)**(5).

                    **scrun** requires all containers to be OCI image compliant per:
                      
                    <https://github.com/opencontainers/image-spec/blob/main/spec.md>

                    ## RETURN VALUE

                    On successful operation, **scrun** will return 0. For any other condition
                    **scrun** will return any non-zero number to denote a error.

                    ## GLOBAL OPTIONS

                    **--cgroup-manager**
                    :   Ignored.

                        : **--debug** : Activate debug level logging. : **-f** <*slurm\_conf\_path*> : Use specified slurm.conf for configuration. Default: sysconfdir from **configure** during compilation : **--usage** : Show quick help on how to call **scrun** : **--log-format**=<*json|text*> : Optional select format for logging. May be "json" or "text". Default: text : **--root**=<*root\_path*> : Path to spool directory to communication sockets and temporary directories and files. This should be a tmpfs and should be cleared on reboot. Default: /run/user/*{user\_id}*/scrun/ : **--rootless** : Ignored. All **scrun** commands are always rootless. : **--systemd-cgroup** : Ignored. : **-v** : Increase logging verbosity. Multiple -v's increase verbosity. : **-V**, **--version** : Print version information and exit.

                    ## CREATE OPTIONS

                    **-b** <*bundle\_path*>, **--bundle**=<*bundle\_path*>
                    :   Path to the root of the bundle directory.
                          
                        Default: caller's working directory

                        : **--console-socket**=<*console\_socket\_path*> : Optional path to an AF\_UNIX socket which will receive a file descriptor referencing the master end of the console's pseudoterminal. Default: *ignored* : **--no-pivot** : Ignored. : **--no-new-keyring** : Ignored. : **--pid-file**=<*pid\_file\_path*> : Specify the file to lock and populate with process ID. Default: *ignored* : **--preserve-fds** : Ignored.

                    ## DELETE OPTIONS

                    **--force**
                    :   Ignored. All delete requests are forced and will kill any running jobs.

                    ## INPUT ENVIRONMENT VARIABLES

                    **SCRUN\_DEBUG**=<quiet|fatal|error|info|verbose|debug|debug2|debug3|debug4|debug5>
                    :   Set logging level.

                        : **SCRUN\_STDERR\_DEBUG**=<quiet|fatal|error|info|verbose|debug|debug2|debug3|debug4|debug5> : Set logging level for standard error output only. : **SCRUN\_SYSLOG\_DEBUG**=<quiet|fatal|error|info|verbose|debug|debug2|debug3|debug4|debug5> : Set logging level for syslogging only. : **SCRUN\_FILE\_DEBUG**=<quiet|fatal|error|info|verbose|debug|debug2|debug3|debug4|debug5> : Set logging level for log file only.

                    ## JOB INPUT ENVIRONMENT VARIABLES

                    **SCRUN\_ACCOUNT**
                    :   See **SLURM\_ACCOUNT** from **[srun](srun.md)**(1).

                        : **SCRUN\_ACCTG\_FREQ** : See **SLURM\_ACCTG\_FREQ** from **[srun](srun.md)**(1). : **SCRUN\_BURST\_BUFFER** : See **SLURM\_BURST\_BUFFER** from **[srun](srun.md)**(1). : **SCRUN\_CLUSTER\_CONSTRAINT** : See **SLURM\_CLUSTER\_CONSTRAINT** from **[srun](srun.md)**(1). : **SCRUN\_CLUSTERS** : See **SLURM\_CLUSTERS** from **[srun](srun.md)**(1). : **SCRUN\_CONSTRAINT** : See **SLURM\_CONSTRAINT** from **[srun](srun.md)**(1). : **SLURM\_CORE\_SPEC** : See **SLURM\_ACCOUNT** from **[srun](srun.md)**(1). : **SCRUN\_CPU\_BIND** : See **SLURM\_CPU\_BIND** from **[srun](srun.md)**(1). : **SCRUN\_CPU\_FREQ\_REQ** : See **SLURM\_CPU\_FREQ\_REQ** from **[srun](srun.md)**(1). : **SCRUN\_CPUS\_PER\_GPU** : See **SLURM\_CPUS\_PER\_GPU** from **[srun](srun.md)**(1). : **SCRUN\_CPUS\_PER\_TASK** : See **SRUN\_CPUS\_PER\_TASK** from **[srun](srun.md)**(1). : **SCRUN\_DELAY\_BOOT** : See **SLURM\_DELAY\_BOOT** from **[srun](srun.md)**(1). : **SCRUN\_DEPENDENCY** : See **SLURM\_DEPENDENCY** from **[srun](srun.md)**(1). : **SCRUN\_DISTRIBUTION** : See **SLURM\_DISTRIBUTION** from **[srun](srun.md)**(1). : **SCRUN\_EPILOG** : See **SLURM\_EPILOG** from **[srun](srun.md)**(1). : **SCRUN\_EXACT** : See **SLURM\_EXACT** from **[srun](srun.md)**(1). : **SCRUN\_EXCLUSIVE** : See **SLURM\_EXCLUSIVE** from **[srun](srun.md)**(1). : **SCRUN\_GPU\_BIND** : See **SLURM\_GPU\_BIND** from **[srun](srun.md)**(1). : **SCRUN\_GPU\_FREQ** : See **SLURM\_GPU\_FREQ** from **[srun](srun.md)**(1). : **SCRUN\_GPUS** : See **SLURM\_GPUS** from **[srun](srun.md)**(1). : **SCRUN\_GPUS\_PER\_NODE** : See **SLURM\_GPUS\_PER\_NODE** from **[srun](srun.md)**(1). : **SCRUN\_GPUS\_PER\_SOCKET** : See **SLURM\_GPUS\_PER\_SOCKET** from **[salloc](salloc.md)**(1). : **SCRUN\_GPUS\_PER\_TASK** : See **SLURM\_GPUS\_PER\_TASK** from **[srun](srun.md)**(1). : **SCRUN\_GRES\_FLAGS** : See **SLURM\_GRES\_FLAGS** from **[srun](srun.md)**(1). : **SCRUN\_GRES** : See **SLURM\_GRES** from **[srun](srun.md)**(1). : **SCRUN\_HINT** : See **SLURM\_HIST** from **[srun](srun.md)**(1). : **SCRUN\_JOB\_NAME** : See **SLURM\_JOB\_NAME** from **[srun](srun.md)**(1). : **SCRUN\_JOB\_NODELIST** : See **SLURM\_JOB\_NODELIST** from **[srun](srun.md)**(1). : **SCRUN\_JOB\_NUM\_NODES** : See **SLURM\_JOB\_NUM\_NODES** from **[srun](srun.md)**(1). : **SCRUN\_LABELIO** : See **SLURM\_LABELIO** from **[srun](srun.md)**(1). : **SCRUN\_MEM\_BIND** : See **SLURM\_MEM\_BIND** from **[srun](srun.md)**(1). : **SCRUN\_MEM\_PER\_CPU** : See **SLURM\_MEM\_PER\_CPU** from **[srun](srun.md)**(1). : **SCRUN\_MEM\_PER\_GPU** : See **SLURM\_MEM\_PER\_GPU** from **[srun](srun.md)**(1). : **SCRUN\_MEM\_PER\_NODE** : See **SLURM\_MEM\_PER\_NODE** from **[srun](srun.md)**(1). : **SCRUN\_MPI\_TYPE** : See **SLURM\_MPI\_TYPE** from **[srun](srun.md)**(1). : **SCRUN\_NCORES\_PER\_SOCKET** : See **SLURM\_NCORES\_PER\_SOCKET** from **[srun](srun.md)**(1). : **SCRUN\_NETWORK** : See **SLURM\_NETWORK** from **[srun](srun.md)**(1). : **SCRUN\_NSOCKETS\_PER\_NODE** : See **SLURM\_NSOCKETS\_PER\_NODE** from **[srun](srun.md)**(1). : **SCRUN\_NTASKS** : See **SLURM\_NTASKS** from **[srun](srun.md)**(1). : **SCRUN\_NTASKS\_PER\_CORE** : See **SLURM\_NTASKS\_PER\_CORE** from **[srun](srun.md)**(1). : **SCRUN\_NTASKS\_PER\_GPU** : See **SLURM\_NTASKS\_PER\_GPU** from **[srun](srun.md)**(1). : **SCRUN\_NTASKS\_PER\_NODE** : See **SLURM\_NTASKS\_PER\_NODE** from **[srun](srun.md)**(1). : **SCRUN\_NTASKS\_PER\_TRES** : See **SLURM\_NTASKS\_PER\_TRES** from **[srun](srun.md)**(1). : **SCRUN\_OPEN\_MODE** : See **SLURM\_MODE** from **[srun](srun.md)**(1). : **SCRUN\_OVERCOMMIT** : See **SLURM\_OVERCOMMIT** from **[srun](srun.md)**(1). : **SCRUN\_OVERLAP** : See **SLURM\_OVERLAP** from **[srun](srun.md)**(1). : **SCRUN\_PARTITION** : See **SLURM\_PARTITION** from **[srun](srun.md)**(1). : **SCRUN\_POWER** : See **SLURM\_POWER** from **[srun](srun.md)**(1). : **SCRUN\_PROFILE** : See **SLURM\_PROFILE** from **[srun](srun.md)**(1). : **SCRUN\_PROLOG** : See **SLURM\_PROLOG** from **[srun](srun.md)**(1). : **SCRUN\_QOS** : See **SLURM\_QOS** from **[srun](srun.md)**(1). : **SCRUN\_REMOTE\_CWD** : See **SLURM\_REMOTE\_CWD** from **[srun](srun.md)**(1). : **SCRUN\_REQ\_SWITCH** : See **SLURM\_REQ\_SWITCH** from **[srun](srun.md)**(1). : **SCRUN\_RESERVATION** : See **SLURM\_RESERVATION** from **[srun](srun.md)**(1). : **SCRUN\_SIGNAL** : See **SLURM\_SIGNAL** from **[srun](srun.md)**(1). : **SCRUN\_SLURMD\_DEBUG** : See **SLURMD\_DEBUG** from **[srun](srun.md)**(1). : **SCRUN\_SPREAD\_JOB** : See **SLURM\_SPREAD\_JOB** from **[srun](srun.md)**(1). : **SCRUN\_TASK\_EPILOG** : See **SLURM\_TASK\_EPILOG** from **[srun](srun.md)**(1). : **SCRUN\_TASK\_PROLOG** : See **SLURM\_TASK\_PROLOG** from **[srun](srun.md)**(1). : **SCRUN\_THREAD\_SPEC** : See **SLURM\_THREAD\_SPEC** from **[srun](srun.md)**(1). : **SCRUN\_THREADS\_PER\_CORE** : See **SLURM\_THREADS\_PER\_CORE** from **[srun](srun.md)**(1). : **SCRUN\_THREADS** : See **SLURM\_THREADS** from **[srun](srun.md)**(1). : **SCRUN\_TIMELIMIT** : See **SLURM\_TIMELIMIT** from **[srun](srun.md)**(1). : **SCRUN\_TRES\_BIND** : Same as **--tres-bind** : **SCRUN\_TRES\_PER\_TASK** : See **SLURM\_TRES\_PER\_TASK** from **[srun](srun.md)**(1). : **SCRUN\_UNBUFFEREDIO** : See **SLURM\_UNBUFFEREDIO** from **[srun](srun.md)**(1). : **SCRUN\_USE\_MIN\_NODES** : See **SLURM\_USE\_MIN\_NODES** from **[srun](srun.md)**(1). : **SCRUN\_WAIT4SWITCH** : See **SLURM\_WAIT4SWITCH** from **[srun](srun.md)**(1). : **SCRUN\_WCKEY** : See **SLURM\_WCKEY** from **[srun](srun.md)**(1). : **SCRUN\_WORKING\_DIR** : See **SLURM\_WORKING\_DIR** from **[srun](srun.md)**(1).

                    ## OUTPUT ENVIRONMENT VARIABLES

                    **SCRUN\_OCI\_VERSION**
                    :   Advertised version of OCI compliance of container.

                        : **SCRUN\_CONTAINER\_ID** : Value based as *container\_id* during create operation. : **SCRUN\_PID** : PID of process used to monitor and control container on allocation node. : **SCRUN\_BUNDLE** : Path to container bundle directory. : **SCRUN\_SUBMISSION\_BUNDLE** : Path to container bundle directory before modification by Lua script. : **SCRUN\_ANNOTATION\_\*** : List of annotations from container's config.json. : **SCRUN\_PID\_FILE** : Path to pid file that is locked and populated with PID of scrun. : **SCRUN\_SOCKET** : Path to control socket for scrun. : **SCRUN\_SPOOL\_DIR** : Path to workspace for all temporary files for current container. Purged by deletion operation. : **SCRUN\_SUBMISSION\_CONFIG\_FILE** : Path to container's config.json file at time of submission. : **SCRUN\_USER** : Name of user that called create operation. : **SCRUN\_USER\_ID** : Numeric ID of user that called create operation. : **SCRUN\_GROUP** : Name of user's primary group that called create operation. : **SCRUN\_GROUP\_ID** : Numeric ID of user primary group that called create operation. : **SCRUN\_ROOT** : See **--root**. : **SCRUN\_ROOTFS\_PATH** : Path to container's root directory. : **SCRUN\_SUBMISSION\_ROOTFS\_PATH** : Path to container's root directory at submission time. : **SCRUN\_LOG\_FILE** : Path to scrun's log file during create operation. : **SCRUN\_LOG\_FORMAT** : Log format type during create operation.

                    ## JOB OUTPUT ENVIRONMENT VARIABLES

                    **SLURM\_\*\_HET\_GROUP\_#**
                    :   For a heterogeneous job allocation, the environment variables are set separately
                        for each component.

                        : **SLURM\_CLUSTER\_NAME** : Name of the cluster on which the job is executing. : **SLURM\_CONTAINER** : OCI Bundle for job. : **SLURM\_CONTAINER\_ID** : OCI id for job. : **SLURM\_CPUS\_PER\_GPU** : Number of CPUs requested per allocated GPU. : **SLURM\_CPUS\_PER\_TASK** : Number of CPUs requested per task. : **SLURM\_DIST\_PLANESIZE** : Plane distribution size. Only set for plane distributions. : **SLURM\_DISTRIBUTION** : Distribution type for the allocated jobs. : **SLURM\_GPU\_BIND** : Requested binding of tasks to GPU. : **SLURM\_GPU\_FREQ** : Requested GPU frequency. : **SLURM\_GPUS** : Number of GPUs requested. : **SLURM\_GPUS\_PER\_NODE** : Requested GPU count per allocated node. : **SLURM\_GPUS\_PER\_SOCKET** : Requested GPU count per allocated socket. : **SLURM\_GPUS\_PER\_TASK** : Requested GPU count per allocated task. : **SLURM\_HET\_SIZE** : Set to count of components in heterogeneous job. : **SLURM\_JOB\_ACCOUNT** : Account name associated of the job allocation. : **SLURM\_JOB\_CPUS\_PER\_NODE** : Count of CPUs available to the job on the nodes in the allocation, using the format *CPU\_count*[(x*number\_of\_nodes*)][,*CPU\_count* [(x*number\_of\_nodes*)] ...]. For example: SLURM\_JOB\_CPUS\_PER\_NODE='72(x2),36' indicates that on the first and second nodes (as listed by SLURM\_JOB\_NODELIST) the allocation has 72 CPUs, while the third node has 36 CPUs. **NOTE**: The **select/linear** plugin allocates entire nodes to jobs, so the value indicates the total count of CPUs on allocated nodes. The **select/cons\_tres** plugin allocates individual CPUs to jobs, so this number indicates the number of CPUs allocated to the job. : **SLURM\_JOB\_END\_TIME** : The UNIX timestamp for a job's projected end time. : **SLURM\_JOB\_GPUS** : The global GPU IDs of the GPUs allocated to this job. The GPU IDs are not relative to any device cgroup, even if devices are constrained with task/cgroup. Only set in batch and interactive jobs. : **SLURM\_JOB\_ID** : The ID of the job allocation. : **SLURM\_JOB\_NODELIST** : List of nodes allocated to the job. : **SLURM\_JOB\_NUM\_NODES** : Total number of nodes in the job allocation. : **SLURM\_JOB\_PARTITION** : Name of the partition in which the job is running. : **SLURM\_JOB\_QOS** : Quality Of Service (QOS) of the job allocation. : **SLURM\_JOB\_RESERVATION** : Advanced reservation containing the job allocation, if any. : **SLURM\_JOB\_START\_TIME** : UNIX timestamp for a job's start time. : **SLURM\_MEM\_BIND** : Bind tasks to memory. : **SLURM\_MEM\_BIND\_LIST** : Set to bit mask used for memory binding. : **SLURM\_MEM\_BIND\_PREFER** : Set to "prefer" if the **SLURM\_MEM\_BIND** option includes the prefer option. : **SLURM\_MEM\_BIND\_TYPE** : Set to the memory binding type specified with the **SLURM\_MEM\_BIND** option. Possible values are "none", "rank", "map\_mem:", "mask\_mem:" and "local". : **SLURM\_MEM\_BIND\_VERBOSE** : Set to "verbose" if the **SLURM\_MEM\_BIND** option includes the verbose option. Set to "quiet" otherwise. : **SLURM\_MEM\_PER\_CPU** : Minimum memory required per usable allocated CPU. : **SLURM\_MEM\_PER\_GPU** : Requested memory per allocated GPU. : **SLURM\_MEM\_PER\_NODE** : Specify the real memory required per node. : **SLURM\_NTASKS** : Specify the number of tasks to run. : **SLURM\_NTASKS\_PER\_CORE** : Request the maximum *ntasks* be invoked on each core. : **SLURM\_NTASKS\_PER\_GPU** : Request that there are *ntasks* tasks invoked for every GPU. : **SLURM\_NTASKS\_PER\_NODE** : Request that *ntasks* be invoked on each node. : **SLURM\_NTASKS\_PER\_SOCKET** : Request the maximum *ntasks* be invoked on each socket. : **SLURM\_OVERCOMMIT** : Overcommit resources. : **SLURM\_PROFILE** : Enables detailed data collection by the acct\_gather\_profile plugin. : **SLURM\_SHARDS\_ON\_NODE** : Number of GPU Shards available to the step on this node. : **SLURM\_SUBMIT\_HOST** : The hostname of the computer from which **scrun** was invoked. : **SLURM\_TASKS\_PER\_NODE** : Number of tasks to be initiated on each node. Values are comma separated and in the same order as SLURM\_JOB\_NODELIST. If two or more consecutive nodes are to have the same task count, that count is followed by "(x#)" where "#" is the repetition count. For example, "SLURM\_TASKS\_PER\_NODE=2(x3),1" indicates that the first three nodes will each execute two tasks and the fourth node will execute one task. : **SLURM\_THREADS\_PER\_CORE** : This is only set if **--threads-per-core** or **SCRUN\_THREADS\_PER\_CORE** were specified. The value will be set to the value specified by **--threads-per-core** or **SCRUN\_THREADS\_PER\_CORE**. This is used by subsequent srun calls within the job allocation. : **SLURM\_TRES\_PER\_TASK** : Set to the value of **--tres-per-task**. If **--cpus-per-task** or **--gpus-per-task** is specified, it is also set in **SLURM\_TRES\_PER\_TASK** as if it were specified in **--tres-per-task**.

                    ## SCRUN.LUA

                    /etc/slurm/**scrun.lua** must be present on any node
                    where **scrun** will be invoked. **scrun.lua** must be a compliant
                    **lua** script.

                    ### Required functions

                    The following functions must be defined.

                    • function **slurm\_scrun\_stage\_in**(**id**, **bundle**, **spool\_dir**, **config\_file**, **job\_id**, **user\_id**, **group\_id**, **job\_env**): Called right after job allocation to stage container into job node(s). Must return *SLURM.success* or job will be cancelled. It is required that function will prepare the container for execution on job node(s) as required to run as configured in **[oci.conf](oci.conf.md)**(1). The function may block as long as required until container has been fully prepared (up to the job's max wall time). : **id** : Container ID **bundle** : OCI bundle path **spool\_dir** : Temporary working directory for container **config\_file** : Path to config.json for container **job\_id** : *jobid* of job allocation **user\_id** : Resolved numeric user id of job allocation. It is generally expected that the lua script will be executed inside of a user namespace running under the *root(0)* user. **group\_id** : Resolved numeric group id of job allocation. It is generally expected that the lua script will be executed inside of a user namespace running under the *root(0)* group. **job\_env** : Table with each entry of Key=Value or Value of each environment variable of the job. • function **slurm\_scrun\_stage\_out**(**id**, **bundle**, **orig\_bundle**, **root\_path**, **orig\_root\_path**, **spool\_dir**, **config\_file**, **jobid**, **user\_id**, **group\_id**): Called right after container step completes to stage out files from job nodes. Must return *SLURM.success* or job will be cancelled. It is required that function will pull back any changes and cleanup the container on job node(s). The function may block as long as required until container has been fully prepared (up to the job's max wall time). : **id** : Container ID **bundle** : OCI bundle path **orig\_bundle** : Originally submitted OCI bundle path before modification by **set\_bundle\_path**(). **root\_path** : Path to directory root of container contents. **orig\_root\_path** : Original path to directory root of container contents before modification by **set\_root\_path**(). **spool\_dir** : Temporary working directory for container **config\_file** : Path to config.json for container **job\_id** : *jobid* of job allocation **user\_id** : Resolved numeric user id of job allocation. It is generally expected that the lua script will be executed inside of a user namespace running under the *root(0)* user. **group\_id** : Resolved numeric group id of job allocation. It is generally expected that the lua script will be executed inside of a user namespace running under the *root(0)* group.

                    ### Provided functions

                    The following functions are provided for any Lua function to call as needed.

                    • **slurm.set\_bundle\_path**(*PATH*): Called to notify **scrun** to use *PATH* as new OCI container bundle path. Depending on the filesystem layout, cloning the container bundle may be required to allow execution on job nodes. • **slurm.set\_root\_path**(*PATH*): Called to notify **scrun** to use *PATH* as new container root filesystem path. Depending on the filesystem layout, cloning the container bundle may be required to allow execution on job nodes. Script must also update #/root/path in config.json when changing root path. • *STATUS*,*OUTPUT* = **slurm.remote\_command**(*SCRIPT*): Run *SCRIPT* in new job step on all job nodes. Returns numeric job status as *STATUS* and job stdio as *OUTPUT*. Blocks until *SCRIPT* exits. • *STATUS*,*OUTPUT* = **slurm.allocator\_command**(*SCRIPT*): Run *SCRIPT* as forked child process of **scrun**. Returns numeric job status as *STATUS* and job stdio as *OUTPUT*. Blocks until *SCRIPT* exits. • **slurm.log**(*MSG*, *LEVEL*): Log *MSG* at log *LEVEL*. Valid range of values for *LEVEL* is [0, 4]. • **slurm.error**(*MSG*): Log error *MSG*. • **slurm.log\_error**(*MSG*): Log error *MSG*. • **slurm.log\_info**(*MSG*): Log *MSG* at log level INFO. • **slurm.log\_verbose**(*MSG*): Log *MSG* at log level VERBOSE. • **slurm.log\_verbose**(*MSG*): Log *MSG* at log level VERBOSE. • **slurm.log\_debug**(*MSG*): Log *MSG* at log level DEBUG. • **slurm.log\_debug2**(*MSG*): Log *MSG* at log level DEBUG2. • **slurm.log\_debug3**(*MSG*): Log *MSG* at log level DEBUG3. • **slurm.log\_debug4**(*MSG*): Log *MSG* at log level DEBUG4. • *MINUTES* = **slurm.time\_str2mins**(*TIME\_STRING*): Parse *TIME\_STRING* into number of minutes as *MINUTES*. Valid formats: : • days-[hours[:minutes[:seconds]]]: • hours:minutes:seconds: • minutes[:seconds]: • -1: • INFINITE: • UNLIMITED

                    ### Example **scrun.lua** scripts

                    Full Container staging example using rsync:: This full example will stage a container as given by **docker** or **podman**. The container's config.json is modified to remove unwanted functions that may cause the container run to under **crun** or **runc**. The script uses **rsync** to move the container to a shared filesystem under the *scratch\_path* variable. **NOTE**: Support for JSON in liblua must generally be installed before Slurm is compiled. scrun.lua's syntax and ability to load JSON support should be tested by directly calling the script using **lua** outside of Slurm. ``` local json = require 'json' local open = io.open local scratch_path = "/run/user/" local function read_file(path) local file = open(path, "rb") if not file then return nil end local content = file:read "*all" file:close() return content end local function write_file(path, contents) local file = open(path, "wb") if not file then return nil end file:write(contents) file:close() return end function slurm_scrun_stage_in(id, bundle, spool_dir, config_file, job_id, user_id, group_id, job_env) slurm.log_debug(string.format("stage_in(%s, %s, %s, %s, %d, %d, %d)", id, bundle, spool_dir, config_file, job_id, user_id, group_id)) local status, output, user, rc local config = json.decode(read_file(config_file)) local src_rootfs = config["root"]["path"] rc, user = slurm.allocator_command(string.format("id -un %d", user_id)) user = string.gsub(user, "%s+", "") local root = scratch_path..math.floor(user_id).."/slurm/scrun/" local dst_bundle = root.."/"..id.."/" local dst_config = root.."/"..id.."/config.json" local dst_rootfs = root.."/"..id.."/rootfs/" if string.sub(src_rootfs, 1, 1) ~= "/" then -- always use absolute path src_rootfs = string.format("%s/%s", bundle, src_rootfs) end status, output = slurm.allocator_command("mkdir -p "..dst_rootfs) if (status ~= 0) then slurm.log_info(string.format("mkdir(%s) failed %u: %s", dst_rootfs, status, output)) return slurm.ERROR end status, output = slurm.allocator_command(string.format("/usr/bin/env rsync --exclude sys --exclude proc --numeric-ids --delete-after --ignore-errors --stats -a -- %s/ %s/", src_rootfs, dst_rootfs)) if (status ~= 0) then -- rsync can fail due to permissions which may not matter slurm.log_info(string.format("WARNING: rsync failed: %s", output)) end slurm.set_bundle_path(dst_bundle) slurm.set_root_path(dst_rootfs) config["root"]["path"] = dst_rootfs -- Always force user namespace support in container or runc will reject local process_user_id = 0 local process_group_id = 0 if ((config["process"] ~= nil) and (config["process"]["user"] ~= nil)) then -- resolve out user in the container if (config["process"]["user"]["uid"] ~= nil) then process_user_id=config["process"]["user"]["uid"] else process_user_id=0 end -- resolve out group in the container if (config["process"]["user"]["gid"] ~= nil) then process_group_id=config["process"]["user"]["gid"] else process_group_id=0 end -- purge additionalGids as they are not supported in rootless if (config["process"]["user"]["additionalGids"] ~= nil) then config["process"]["user"]["additionalGids"] = nil end end if (config["linux"] ~= nil) then -- force user namespace to always be defined for rootless mode local found = false if (config["linux"]["namespaces"] == nil) then config["linux"]["namespaces"] = {} else for _, namespace in ipairs(config["linux"]["namespaces"]) do if (namespace["type"] == "user") then found=true break end end end if (found == false) then table.insert(config["linux"]["namespaces"], {type= "user"}) end -- Provide default user map as root if one not provided if (true or config["linux"]["uidMappings"] == nil) then config["linux"]["uidMappings"] = {{containerID=process_user_id, hostID=math.floor(user_id), size=1}} end -- Provide default group map as root if one not provided -- mappings fail with build??? if (true or config["linux"]["gidMappings"] == nil) then config["linux"]["gidMappings"] = {{containerID=process_group_id, hostID=math.floor(group_id), size=1}} end -- disable trying to use a specific cgroup config["linux"]["cgroupsPath"] = nil end if (config["mounts"] ~= nil) then -- Find and remove any user/group settings in mounts for _, mount in ipairs(config["mounts"]) do local opts = {} if (mount["options"] ~= nil) then for _, opt in ipairs(mount["options"]) do if ((string.sub(opt, 1, 4) ~= "gid=") and (string.sub(opt, 1, 4) ~= "uid=")) then table.insert(opts, opt) end end end if (opts ~= nil and #opts > 0) then mount["options"] = opts else mount["options"] = nil end end -- Remove all bind mounts by copying files into rootfs local mounts = {} for i, mount in ipairs(config["mounts"]) do if ((mount["type"] ~= nil) and (mount["type"] == "bind") and (string.sub(mount["source"], 1, 4) ~= "/sys") and (string.sub(mount["source"], 1, 5) ~= "/proc")) then status, output = slurm.allocator_command(string.format("/usr/bin/env rsync --numeric-ids --ignore-errors --stats -a -- %s %s", mount["source"], dst_rootfs..mount["destination"])) if (status ~= 0) then -- rsync can fail due to permissions which may not matter slurm.log_info("rsync failed") end else table.insert(mounts, mount) end end config["mounts"] = mounts end -- Force version to one compatible with older runc/crun at risk of new features silently failing config["ociVersion"] = "1.0.0" -- Merge in Job environment into container -- this is optional! if (config["process"]["env"] == nil) then config["process"]["env"] = {} end for _, env in ipairs(job_env) do table.insert(config["process"]["env"], env) end -- Remove all prestart hooks to squash any networking attempts if ((config["hooks"] ~= nil) and (config["hooks"]["prestart"] ~= nil)) then config["hooks"]["prestart"] = nil end -- Remove all rlimits if ((config["process"] ~= nil) and (config["process"]["rlimits"] ~= nil)) then config["process"]["rlimits"] = nil end write_file(dst_config, json.encode(config)) slurm.log_info("created: "..dst_config) return slurm.SUCCESS end function slurm_scrun_stage_out(id, bundle, orig_bundle, root_path, orig_root_path, spool_dir, config_file, jobid, user_id, group_id) if (root_path == nil) then root_path = "" end slurm.log_debug(string.format("stage_out(%s, %s, %s, %s, %s, %s, %s, %d, %d, %d)", id, bundle, orig_bundle, root_path, orig_root_path, spool_dir, config_file, jobid, user_id, group_id)) if (bundle == orig_bundle) then slurm.log_info(string.format("skipping stage_out as bundle=orig_bundle=%s", bundle)) return slurm.SUCCESS end status, output = slurm.allocator_command(string.format("/usr/bin/env rsync --numeric-ids --delete-after --ignore-errors --stats -a -- %s/ %s/", root_path, orig_root_path)) if (status ~= 0) then -- rsync can fail due to permissions which may not matter slurm.log_info("rsync failed") else -- cleanup temporary after they have been synced backed to source slurm.allocator_command(string.format("/usr/bin/rm --preserve-root=all --one-file-system -dr -- %s", bundle)) end return slurm.SUCCESS end slurm.log_info("initialized scrun.lua") return slurm.SUCCESS ```

                    ## SIGNALS

                    **SIGINT**
                    :   Attempt to gracefully cancel any related jobs (if any) and cleanup.

                        : **SIGCHLD** : Wait for all children, cleanup anchor and gracefully shutdown.

                    ## COPYING

                    Copyright (C) 2023 SchedMD LLC.

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

                    **[slurm](slurm.md)**(1), **[oci.conf](oci.conf.md)**(5), **[srun](srun.md)**(1), **crun**, **runc**,
                    **DOCKER** and **podman**

                    ---



                    ## Index

                    [NAME](#lbAB): [SYNOPSIS](#lbAC): [Create Operation](#lbAD): [Start Operation](#lbAE): [Query State Operation](#lbAF): [Kill Operation](#lbAG): [Delete Operation](#lbAH): [DESCRIPTION](#lbAI): [RETURN VALUE](#lbAJ): [GLOBAL OPTIONS](#lbAK): [CREATE OPTIONS](#lbAL): [DELETE OPTIONS](#lbAM): [INPUT ENVIRONMENT VARIABLES](#lbAN): [JOB INPUT ENVIRONMENT VARIABLES](#lbAO): [OUTPUT ENVIRONMENT VARIABLES](#lbAP): [JOB OUTPUT ENVIRONMENT VARIABLES](#lbAQ): [SCRUN.LUA](#lbAR): [Required functions](#lbAS): [Provided functions](#lbAT): [Example **scrun.lua** scripts](#lbAU) [SIGNALS](#lbAV): [COPYING](#lbAW): [SEE ALSO](#lbAX)

                    ---

                    This document was created by
                    *man2html* using the manual pages.  
                    Time: 21:24:25 GMT, February 19, 2026