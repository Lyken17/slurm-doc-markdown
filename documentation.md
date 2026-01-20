# Source: https://slurm.schedmd.com/documentation.html

# Documentation

**NOTE: This documentation is for Slurm version 25.11.  
Documentation for older versions of Slurm are distributed with the source, or
may be found in the [archive](https://slurm.schedmd.com/archive/).**

## Slurm Users

* [Quick Start User Guide](quickstart.html)
* [Command/option Summary (two pages)](pdfs/summary.pdf)
* [Man Pages](man_index.html)
* [Rosetta Stone of Workload Managers](rosetta.html)
* [Job Array Support](job_array.html)
* [Heterogeneous Job Support](heterogeneous_jobs.html)
* [CPU Management User and Administrator Guide](cpu_management.html)
* [MPI and UPC Users Guide](mpi_guide.html)
* [Support for Multi-core/Multi-threaded Architectures](mc_support.html)
* [Multi-Cluster Operation](multi_cluster.html)
* [Profiling Using HDF5 User Guide](hdf5_profile_user_guide.html)
* [Job Reason Codes](job_reason_codes.html)
* [Job State Codes](job_state_codes.html)
* [Job Exit Codes](job_exit_code.html)
* [Resource Binding](resource_binding.html)

## Slurm Administrators

* [Quick Start Administrator Guide](quickstart_admin.html)
* [Upgrade Guide](upgrades.html)
* [Accounting](accounting.html)
* [Advanced Resource Reservation Guide](reservations.html)
* [Authentication Plugins](authentication.html)
* [Burst Buffer Guide](burst_buffer.html)
* [Cgroups Guide](cgroups.html)
* ["Configless" Slurm Operation](configless_slurm.html)
* [Configuration Tool (Full version)](configurator.html)
* [Configuration Tool (Simplified version)](configurator.easy.html)
* [Containers](containers.html)
* [CPU Management User and Administrator Guide](cpu_management.html)
* [Dynamic Nodes](dynamic_nodes.html)
* [Elasticsearch Guide](elasticsearch.html)
* [Job Completion Kafka plugin Guide](jobcomp_kafka.html)
* [namespace/tmpfs - Job Specific Temporary File Management](namespace_tmpfs.html)
* [JSON Web Tokens Authentication](jwt.html)
* [Federated Scheduling Guide](federation.html)
* [Job Containment (SSH Session Control) with pam\_slurm\_adopt](pam_slurm_adopt.html)
* [Kubernetes Guide](kubernetes.html)
* [Large Cluster Administration Guide](big_sys.html)
* [License Management](licenses.html)
* [Hierarchical Resources (HRES)](hres.html) (in Beta)
* [Multi-Category Security (MCS) Guide](mcs.html)
* [Name Service Caching Through NSS Slurm](nss_slurm.html)
* [Network Configuration Guide](network.html)
* [OpenAPI Plugin Release Notes](openapi_release_notes.html)
* [Power Saving Guide (power down idle nodes)](power_save.html)
* [Prolog and Epilog Guide](prolog_epilog.html)
* Slurm REST API
  + [Quick Start Guide](rest_quickstart.html)
  + [API Details](rest.html)
  + [API Methods and Models](rest_api.html)
  + [Client Guide](rest_clients.html)
* [Slurm SELinux Context Management](selinux.html)
* [Troubleshooting Guide](troubleshoot.html)
* [User Permissions](user_permissions.html)
* [WCKey Management](wckey.html)
* Workload Prioritization
  + [Multifactor Job Priority](priority_multifactor.html)
  + [Classic Fairshare Algorithm](classic_fair_share.html)
  + [Depth-Oblivious Fair-share Factor](priority_multifactor3.html)
  + [Fair Tree Fairshare Algorithm](fair_tree.html)
* Slurm Scheduling
  + [Scheduling Configuration Guide](sched_config.html)
  + [Consumable Resources Guide](cons_tres.html)
  + [Core Specialization](core_spec.html)
  + [Gang Scheduling](gang_scheduling.html)
  + [Generic Resource (GRES) Scheduling](gres.html)
  + [High Throughput Computing Guide](high_throughput.html)
  + [Preemption](preempt.html)
  + [Quality of Service (QOS)](qos.html)
  + [Resource Limits](resource_limits.html)
  + [Resource Reservation Guide](reservations.html)
  + [Sharing Consumable Resources](cons_tres_share.html)
  + [Topology](topology.html)
  + [Trackable Resources (TRES)](tres.html)
* Cloud
  + [Cloud Scheduling Guide](power_save.html)
  + [Slurm on Google Cloud Platform](https://github.com/schedmd/slurm-gcp)
  + [Deploying Slurm on AWS Parallel Computing Service](https://aws.amazon.com/pcs/)
  + [Slurm on Microsoft Azure and CycleCloud](https://github.com/Azure/cyclecloud-slurm)

## Slurm Developers

* [Contributor Guide](contributor.html)
* [Programmer Guide](programmer_guide.html)
* [Application Programmer Interface (API) Guide](api.html)
* [Adding Files or Plugins to Slurm](add.html)
* Design Information
  + [Generic Resource (GRES) Design Guide](gres_design.html)
  + [Job Launch Design Guide](job_launch.html)
  + [Select Plugin Design Guide](select_design.html)
* [Plugin Programmer Guide](plugins.html)
* Plugin Interface Details
  + [Command Line Filter Plugin Programmer Guide](cli_filter_plugins.html)
  + [Job Submission Plugin Programmer Guide](job_submit_plugins.html)
  + [PrEp Plugin Programmer Guide](prep_plugins.html)
  + [Site Factor (Priority) Plugin Programmer Guide](site_factor.html)