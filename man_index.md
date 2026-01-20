# Source: https://slurm.schedmd.com/man_index.html

# Man Pages

**NOTE: This documentation is for Slurm version 25.11.  
Documentation for other versions of Slurm is distributed with the code**

Refer to [this page](slurm.html) for an overview of Slurm.

## Commands

|  |  |
| --- | --- |
| [sacct](sacct.html) | Displays accounting data for all jobs and job steps in the Slurm job accounting log or Slurm database. |
| [sacctmgr](sacctmgr.html) | Used to view and modify Slurm account information. |
| [salloc](salloc.html) | Obtain a Slurm job allocation (a set of nodes), execute a command, and then release the allocation when the command is finished. |
| [sattach](sattach.html) | Attach to a Slurm job step. |
| [sbatch](sbatch.html) | Submit a batch script to Slurm. |
| [sbcast](sbcast.html) | Transmit a file to the nodes allocated to a Slurm job. |
| [scancel](scancel.html) | Used to signal jobs or job steps that are under the control of Slurm. |
| [scontrol](scontrol.html) | View or modify Slurm configuration and state. |
| [scrontab](scrontab.html) | Manage Slurm crontab files. |
| [scrun](scrun.html) | An OCI runtime proxy for slurm. |
| [sdiag](sdiag.html) | Scheduling diagnostic tool. |
| [sh5util](sh5util.html) | Merge utility for acct\_gather\_profile plugin. |
| [sinfo](sinfo.html) | View information about Slurm nodes and partitions. |
| [sprio](sprio.html) | View the factors that comprise a job's scheduling priority. |
| [squeue](squeue.html) | View information about jobs located in the Slurm scheduling queue. |
| [sreport](sreport.html) | Generate reports from the slurm accounting data. |
| [srun](srun.html) | Run parallel jobs. |
| [sshare](sshare.html) | Tool for listing the shares of associations to a cluster. |
| [sstat](sstat.html) | Display the status information of a running job/step. |
| [strigger](strigger.html) | Used to set, get or clear Slurm trigger information. |
| [sview](sview.html) | Graphical user interface to view and modify Slurm state. |

## Configuration Files

|  |  |
| --- | --- |
| [acct\_gather.conf](acct_gather.conf.html) | Slurm configuration file for the acct\_gather plugins. |
| [burst\_buffer.conf](burst_buffer.conf.html) | Slurm burst buffer configuration. |
| [cgroup.conf](cgroup.conf.html) | Slurm configuration file for the cgroup support. |
| [gres.conf](gres.conf.html) | Slurm configuration file for generic resource management. |
| [helpers.conf](helpers.conf.html) | Slurm configuration file for the node\_features/helpers plugin. |
| [job\_container.conf](job_container.conf.html) | Slurm configuration file for configuring the tmpfs job container plugin. |
| [mpi.conf](mpi.conf.html) | Slurm configuration file to allow the configuration of MPI plugins. |
| [namespace.yaml](namespace.yaml.html) | Slurm configuration file for the namespace/linux plugin. |
| [oci.conf](oci.conf.html) | Slurm configuration file for OCI Containers. |
| [plugstack.conf](spank.html#SECTION_CONFIGURATION) | Slurm configuration file for SPANK plug-in stack. |
| [slurm.conf](slurm.conf.html) | Slurm configuration file. |
| [slurmdbd.conf](slurmdbd.conf.html) | Slurm Database Daemon (SlurmDBD) configuration file. |
| [topology.conf](topology.conf.html) | Slurm configuration file for defining the network topology. |
| [topology.yaml](topology.yaml.html) | Slurm configuration file for defining multiple network topologies. |

## Daemons and Other

|  |  |
| --- | --- |
| [sackd](sackd.html) | Slurm Auth and Cred Kiosk Daemon. |
| [slurmctld](slurmctld.html) | The central management daemon of Slurm. |
| [slurmd](slurmd.html) | The compute node daemon for Slurm. |
| [slurmdbd](slurmdbd.html) | Slurm Database Daemon. |
| [slurmrestd](slurmrestd.html) | The Slurm REST API daemon. |
| [slurmstepd](slurmstepd.html) | The job step manager for Slurm. |
| [SPANK](spank.html) | Slurm Plug-in Architecture for Node and job (K)control. |