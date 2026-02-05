---
name: Slurm Workload Manager Skill
description: Instructions and templates for interacting with the Slurm Workload Manager to submit, monitor, and manage jobs.
---

# Slurm Workload Manager Skill

This skill provides a comprehensive guide for interacting with the Slurm Workload Manager. It covers job submission, monitoring, and management using core Slurm commands.

## Core Commands

The following commands are essential for working with Slurm:

*   **`sbatch`**: Submits a batch script to Slurm.
*   **`squeue`**: View information about jobs located in the Slurm scheduling queue.
*   **`scancel`**: Signals or cancels jobs, job arrays, or job steps.
*   **`sinfo`**: View information about Slurm nodes and partitions.
*   **`scontrol`**: View or modify Slurm configuration and state (e.g., job details).

## Job Submission (`sbatch`)

The primary way to run jobs on Slurm is by submitting a batch script using `sbatch`. A batch script is a shell script containing `#SBATCH` directives that define resource requirements and job attributes.

### Common `#SBATCH` Directives

| Directive | Description | Example |
| :--- | :--- | :--- |
| `-A, --account=<account>` | Charge resources to this account. | `#SBATCH --account=mygroup` |
| `-p, --partition=<partition>` | Request a specific partition. | `#SBATCH --partition=gpu` |
| `-t, --time=<time>` | Set a time limit for the job. | `#SBATCH --time=01:00:00` (1 hour) |
| `-N, --nodes=<minnodes>` | Request a minimum number of nodes. | `#SBATCH --nodes=1` |
| `-n, --ntasks=<number>` | Request a specific number of tasks (often maps to MPI processes). | `#SBATCH --ntasks=4` |
| `-c, --cpus-per-task=<ncpus>` | Request CPUs per task (useful for multi-threaded jobs). | `#SBATCH --cpus-per-task=4` |
| `--gres=<list>` | Request generic resources (e.g., GPUs). | `#SBATCH --gres=gpu:1` |
| `--mem=<size>` | Request real memory per node. | `#SBATCH --mem=16G` |
| `-o, --output=<filename>` | File for standard output. | `#SBATCH --output=slurm-%j.out` |
| `-e, --error=<filename>` | File for standard error. | `#SBATCH --error=slurm-%j.err` |
| `-J, --job-name=<name>` | Specify a name for the job. | `#SBATCH --job-name=my_job` |
| `--mail-type=<type>` | Notify on state change (BEGIN, END, FAIL, ALL). | `#SBATCH --mail-type=END,FAIL` |
| `--mail-user=<email>` | User to receive email notification. | `#SBATCH --mail-user=user@example.com` |

### Environment Variables

Slurm exports environment variables to the job script, starting with `SLURM_` or `SBATCH_`. Common ones include:
*   `SLURM_JOB_ID`: The ID of the job.
*   `SLURM_SUBMIT_DIR`: The directory from which `sbatch` was invoked.
*   `SLURM_JOB_NODELIST`: List of nodes allocated to the job.
*   `SLURM_ARRAY_TASK_ID`: Task ID for a job array.

## Monitoring and Management

### Viewing Queue (`squeue`)

*   **List all jobs**: `squeue`
*   **List jobs for a specific user**: `squeue -u <username>`
*   **Format output**: `squeue -o "%.18i %.9P %.8j %.8u %.2t %.10M %.6D %R"` (Custom format)
*   **Long format**: `squeue -l`

### Cancelling Jobs (`scancel`)

*   **Cancel a specific job**: `scancel <job_id>`
*   **Cancel all jobs for a user**: `scancel -u <username>`
*   **Cancel a specific job step**: `scancel <job_id>.<step_id>`

### Viewing Job Details (`scontrol`)

*   **Show details of a running/pending job**: `scontrol show job <job_id>`
*   **Show node details**: `scontrol show node <node_name>`

### Viewing Node/Partition State (`sinfo`)

*   **View all partitions and node states**: `sinfo`
*   **View summary**: `sinfo -s`
*   **View long format with node details**: `sinfo -N -l`

## Templates

### Basic Job Script

```bash
#!/bin/bash
#SBATCH --job-name=basic_job
#SBATCH --output=result_%j.out
#SBATCH --error=result_%j.err
#SBATCH --time=00:10:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=4G

echo "Starting job on $(hostname)"
srun echo "Hello from Slurm"
echo "Job finished"
```

### GPU Job Script

```bash
#!/bin/bash
#SBATCH --job-name=gpu_job
#SBATCH --partition=gpu
#SBATCH --gres=gpu:1
#SBATCH --time=01:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G
#SBATCH --output=gpu_job_%j.out

module load cuda/11.0  # Example module load
echo "Running on $(hostname) with GPU"
nvidia-smi
python train.py
```

### Array Job Script

```bash
#!/bin/bash
#SBATCH --job-name=array_job
#SBATCH --array=1-10
#SBATCH --output=array_%A_%a.out
#SBATCH --time=00:30:00
#SBATCH --ntasks=1
#SBATCH --mem=2G

echo "Processing task ID: $SLURM_ARRAY_TASK_ID"
python process_data.py --task-id $SLURM_ARRAY_TASK_ID
```

## Best Practices

1.  **Always specify a time limit**: Prevent jobs from hanging indefinitely and blocking resources.
2.  **Request appropriate memory**: Too little triggers OOM kills; too much wastes resources.
3.  **Use `srun` inside scripts**: Launch parallel steps with `srun` to utilize Slurm's process management and resource accounting.
4.  **Check output/error files**: Debug failures by inspecting the files defined by `--output` and `--error`.
5.  **Clean up**: Cancel jobs that are no longer needed or are behaving incorrectly.
