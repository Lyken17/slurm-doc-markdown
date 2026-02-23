# Slurm System Configuration Tool

# Slurm Version 25.11 Configuration Tool

This form can be used to create a Slurm configuration file with
you controlling many of the important configuration parameters.

This is the full version of the Slurm configuration tool. This version
has all the configuration options to create a Slurm configuration file. There
is a simplified version of the Slurm configuration tool available at
<configurator.easy.html>.

**This tool supports Slurm version 25.11 only.**
Configuration files for other versions of Slurm should be built
using the tool distributed with it in *doc/html/configurator.html*.
Some parameters will be set to default values, but you can
manually edit the resulting *slurm.conf* as desired
for greater flexibility. See *man slurm.conf* for more
details about the configuration parameters.

Note the while Slurm daemons create log files and other files as needed,
it treats the lack of parent directories as a fatal error.
This prevents the daemons from running if critical file systems are
not mounted and will minimize the risk of cold-starting (starting
without preserving jobs).

Note that this configuration file must be installed on all nodes
in your cluster.

After you have filled in the fields of interest, use the
"Submit" button on the bottom of the page to build the *slurm.conf*
file. It will appear on your web browser. Save the file in text format
as *slurm.conf* for use by Slurm.

For more information about Slurm, see
<https://slurm.schedmd.com/slurm.html>

## Cluster Name

 **ClusterName**:
The name of your cluster. Using different names for each of your clusters is
important when using a single database to record information from multiple
Slurm-managed clusters.

## Control Machines

Define the hostname of the computer on which the Slurm controller and
optional backup controller will execute.
Hostname values should not be the fully qualified domain
name (e.g. use *tux* rather than *tux.abc.com*).

**SlurmctldHost**:
Primary Controller Hostname

**BackupController**: Backup
Controller Hostname (optional)

## Compute Machines

Define the machines on which user applications can run.
You can also specify addresses of these computers if desired
(defaults to their hostnames).
Only a few of the possible parameters associated with the nodes will
be set by this tool, but many others are available.
Executing the command *slurmd -C* on each compute node will print its
physical configuration (sockets, cores, real memory size, etc.), which
can be used in constructing the *slurm.conf* file.
All of the nodes will be placed into a single partition (or queue)
with global access. Many options are available to group nodes into
partitions with a wide variety of configuration parameters.
Manually edit the *slurm.conf* produced to exercise these options.
Node names and addresses may be specified using a numeric range specification.

**NodeName**:
Compute nodes

**NodeAddr**: Compute node addresses
(optional)

**PartitionName**:
Name of the one partition to be created

**MaxTime**:
Maximum time limit of jobs in minutes or INFINITE

The following parameters describe a node's configuration.
Set a value for **CPUs**.
The other parameters are optional, but provide more control over scheduled resources:

**CPUs**: Count of processors
on each compute node.
If CPUs is omitted, it will be inferred from:
Sockets, CoresPerSocket, and ThreadsPerCore.

**Sockets**:
Number of physical processor sockets/chips on the node.
If Sockets is omitted, it will be inferred from:
CPUs, CoresPerSocket, and ThreadsPerCore.

**CoresPerSocket**:
Number of cores in a single physical processor socket.
The CoresPerSocket value describes physical cores, not
the logical number of processors per socket.

**ThreadsPerCore**:
Number of logical threads in a single physical core.

**RealMemory**: Amount
of real memory. This parameter is required when specifying Memory as a
consumable resource with the select/cons\_tres plug-in. See below
under Resource Selection.

## Slurm User

The Slurm controller (slurmctld) can run without elevated privileges,
so it is recommended that a user "slurm" be created for it. For testing
purposes any user name can be used.

**SlurmUser**

## Slurm Port Numbers

The Slurm controller (slurmctld) requires a unique port for communications
as do the Slurm compute node daemons (slurmd). If not set, slurm ports
are set by checking for an entry in */etc/services* and if that
fails by using an interval default set at Slurm build time.

**SlurmctldPort**

**SlurmdPort**

## State Preservation

Define the location of a directory where the slurmctld daemon saves its state.
This should be a fully qualified pathname which can be read and written to
by the Slurm user on both the control machine and backup controller (if configured).
The location of a directory where slurmd saves state should also be defined.
This must be a unique directory on each compute server (local disk).
The use of a highly reliable file system (e.g. RAID) is recommended.

**StateSaveLocation**: Slurmctld state save directory
**Must be writable by all SlurmctldHost nodes**

**SlurmdSpoolDir**: Slurmd state save directory

Define when a non-responding (DOWN) node is returned to service.  
Select one value for **ReturnToService**:  

**0**: When explicitly restored to service by an administrator.  

**1**:Upon registration with a valid configuration only if it was set DOWN
due to being non-responsive.  

**2**:Upon registration with a valid configuration.  

## Scheduling

Define the mechanism to be used for controlling job ordering.  
Select one value for **SchedulerType**:  
 **Backfill**:
FIFO with backfill  
 **Builtin**: First-In
First-Out (FIFO)  

## Interconnect

Define the node interconnect used.  
Select one value for **SwitchType**:  
 **HPE
Slingshot**: HPE Slingshot proprietary interconnect  
 **None**: No special

## Default MPI Type

Specify the type of MPI to be used by default. Slurm will configure environment
variables accordingly. Users can over-ride this specification with an srun option.  
Select one value for **MpiDefault**:  
 **MPI-PMI2**
(For PMI2-supporting MPI implementations)  
 **MPI-PMIx**
(Exascale PMI implementation)  
 **None**:
This works for most other MPI types.  

## Process Tracking

Define the algorithm used to identify which processes are associated with a
given job. This is used signal, kill, and account for the processes associated
with a job step.  
Select one value for **ProctrackType**:  
 **Cgroup**: Use
Linux *cgroup* to create a job container and track processes.
Build a *cgroup.conf* file as well  
 **LinuxProc**: Use
parent process ID records, processes can escape from Slurm control  
 **Pgid**: Use Unix
Process Group ID, processes changing their process group ID can escape from Slurm
control  

## Resource Selection

Define resource (node) selection algorithm to be used.  
Select one value for **SelectType**:  

**cons\_tres**: Allocate individual processors, memory, GPUs, and other
trackable resources  

**Linear**: Node-base
resource allocation, does not manage individual processor allocation