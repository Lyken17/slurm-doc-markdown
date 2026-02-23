---
name: slurm-workload-manager
description: Comprehensive guide and documentation for Slurm Workload Manager. Use when submitting jobs, managing queues, configuring Slurm, or troubleshooting Slurm-managed clusters.
---

# Slurm Workload Manager

This skill provides a complete reference for interacting with and managing a Slurm-based HPC cluster. It includes detailed command guides, job submission templates, and extensive configuration references.

## Core Workflows

### 1. Job Submission and Management
Submit and monitor your computational tasks.
- **Submit a batch script**: Use `sbatch`. See [sbatch.md](references/sbatch.md) for full options.
- **Run interactive tasks**: Use `srun`. See [srun.md](references/srun.md).
- **Check job status**: Use `squeue`. See [squeue.md](references/squeue.md).
- **Cancel jobs**: Use `scancel`. See [scancel.md](references/scancel.md).

### 2. Monitoring Cluster State
View nodes, partitions, and resource availability.
- **Cluster overview**: Use `sinfo`. See [sinfo.md](references/sinfo.md).
- **Node/Job details**: Use `scontrol show [node|job] <id>`. See [scontrol.md](references/scontrol.md).
- **Accounting & history**: Use `sacct`. See [sacct.md](references/sacct.md).

### 3. Cluster Administration
Manage Slurm configuration, users, and accounts.
- **Manage accounts/users**: Use `sacctmgr`. See [sacctmgr.md](references/sacctmgr.md).
- **Configuration files**: The primary configuration is [slurm.conf.md](references/slurm.conf.md).
- **Generic Resources (GRES)**: Configure GPUs and other resources in [gres.conf.md](references/gres.conf.md).

---

## Command Reference Library

Detailed documentation for all Slurm utilities:

| Command | Description | Reference |
| :--- | :--- | :--- |
| `sbatch` | Submit a batch script | [sbatch.md](references/sbatch.md) |
| `squeue` | View job queue | [squeue.md](references/squeue.md) |
| `srun` | Submit/run job steps | [srun.md](references/srun.md) |
| `scancel` | Cancel jobs | [scancel.md](references/scancel.md) |
| `sinfo` | View cluster state | [sinfo.md](references/sinfo.md) |
| `scontrol` | View/modify state | [scontrol.md](references/scontrol.md) |
| `sacct` | View job accounting | [sacct.md](references/sacct.md) |
| `sacctmgr` | Manage accounting | [sacctmgr.md](references/sacctmgr.md) |
| `salloc` | Allocate resources | [salloc.md](references/salloc.md) |
| `sreport` | Generate reports | [sreport.md](references/sreport.md) |

## Configuration Reference

Documentation for Slurm configuration files:

- **Main Config**: [slurm.conf.md](references/slurm.conf.md)
- **Database Config**: [slurmdbd.conf.md](references/slurmdbd.conf.md)
- **GRES (GPU) Config**: [gres.conf.md](references/gres.conf.md)
- **Cgroup Config**: [cgroup.conf.md](references/cgroup.conf.md)
- **Topology Config**: [topology.conf.md](references/topology.conf.md)

## Specialized Guides

- **Job Arrays**: [job_array.md](references/job_array.md)
- **QoS (Quality of Service)**: [qos.md](references/qos.md)
- **Reservations**: [reservations.md](references/reservations.md)
- **REST API**: [rest_api.md](references/rest_api.md)
- **Troubleshooting**: [troubleshoot.md](references/troubleshoot.md)
- **FAQs**: [faq.md](references/faq.md)

For any topic not listed above, use `grep` to search the `references/` directory for specific keywords.
