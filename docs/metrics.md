# Source: https://slurm.schedmd.com/metrics.html

# Metrics Guide

## Contents

* [Metrics Overview](#overview)
* [Configuration](#configuration)
* [HTTP Endpoints](#endpoints)
* [OpenMetrics Plugin](#openmetrics)
* [Metric Categories Provided by Slurm](#categories)
* [Security Considerations](#security)
* [Performance Impact](#performance)
* [Usage Examples](#examples)

## Metrics Overview

Slurm 25.11 introduced a comprehensive system for collecting and exposing
metrics related to cluster resources, job states, and scheduler performance.
The metrics system exposes real-time data about various Slurm entities through
HTTP endpoints provided by the slurmctld daemon.

The metrics feature enables integration with popular monitoring systems like
Prometheus, Grafana, and other observability tools.

## Configuration

### Prerequisites

The metrics feature requires specific configuration in *slurm.conf*:

* **PrivateData must not be set**: The metrics feature is disabled if any
  *PrivateData* parameter is configured in slurm.conf. This is a security
  requirement to prevent exposure of sensitive information through metrics.
* **MetricsType parameter**: Set the
  [MetricsType](slurm.conf.md#OPT_MetricsType) parameter to specify
  which metrics plugin to use. Currently, only the OpenMetrics plugin is
  supported:

  ```
  MetricsType=metrics/openmetrics
  ```

### Plugin Loading

The metrics plugin is automatically loaded by slurmctld when the
*MetricsType* parameter is configured.

## HTTP Endpoints

Slurm exposes metrics through HTTP GET endpoints on the slurmctld daemon's
listening port (default 6817). The following endpoints are available:

* **GET /metrics** - Print available metric endpoints
* **GET /metrics/jobs** - Job-related metrics including counts by state,
  resource allocation, and job statistics ([examples](#job_metrics))
* **GET /metrics/jobs-users-accts** - User- and account-specific job
  metrics ([examples](#ua_job_metrics))
* **GET /metrics/nodes** - Node-related metrics including resource counts,
  states, and utilization ([examples](#node_metrics))
* **GET /metrics/partitions** - Partition-related metrics including job
  counts per partition and resource allocation
  ([examples](#partition_metrics))
* **GET /metrics/scheduler** - Scheduler performance metrics including
  cycle times, backfill statistics, and queue lengths
  ([examples](#scheduler_metrics))

All endpoints return data in UTF-8 text format making them compatible with
Prometheus and other monitoring systems.

## OpenMetrics Plugin

The OpenMetrics plugin implements the [OpenMetrics 1.0](https://openmetrics.io/) specification, ensuring compatibility with Prometheus and
other monitoring systems that consume metrics in this format.

### Metric Format

Each metric follows the OpenMetrics format with the following components:

* **Metric name**: A descriptive name prefixed with "slurm\_"
* **Metric type**: Only "gauge" metrics are exposed
* **Metric value**: The actual numeric value
* **Labels**: Optional key-value pairs for additional context
* **Help text**: Human-readable description of the metric

## Metric Categories Provided by Slurm

Each endpoint provides a set of metrics related to the same general category.
Numerous metrics are provided so they are not all documented on this page.
A few examples are provided for each category in the following subsections.

### Job Metrics

Job metrics provide information about job states, resource allocation, and
job counts. Examples include:

* `slurm_jobs` - Total number of jobs
* `slurm_jobs_running` - Number of running jobs
* `slurm_jobs_pending` - Number of pending jobs (see note)
* `slurm_jobs_cpus_alloc` - Total CPUs allocated to jobs
* `slurm_jobs_memory_alloc` - Total memory allocated to jobs

**NOTE**: In Slurm, pending jobs include both jobs waiting for resources
and held jobs. Held jobs will not be scheduled until the hold is released.

### User- and Account-Specific Job Metrics

Job metrics for user and accounts provide a count of jobs in each state for
each active user and account in the system. It stores each entity under a
key-value pair. Remember that every unique key-value pair represents a new time
series, which can dramatically increase the amount of data stored.
Examples include:

* `slurm_user_jobs_pending{username="john"}`
  - Pending jobs for user "john"
* `slurm_account_jobs_pending{account="smith"}`
  - Pending jobs for account "smith"

### Node Metrics

Node metrics track resource availability, node states, and utilization.
Examples include:

* `slurm_nodes` - Total number of nodes
* `slurm_nodes_idle` - Number of idle nodes
* `slurm_nodes_alloc` - Number of allocated nodes
* `slurm_node_cpus{node="nodename"}` - CPUs on the specified node
* `slurm_node_memory_bytes{node="nodename"}`
  - Memory on the specified node (bytes)

### Partition Metrics

Partition metrics show job distribution and resource allocation across
partitions. Examples include:

* `slurm_partitions` - Total number of partitions
* `slurm_partition_jobs{partition="name"}`
  - Jobs on the specified partition
* `slurm_partition_nodes{partition="name"}`
  - Nodes on the specified partition

The following metrics might be useful for
[Slinky](https://slurm.schedmd.com/slinky.md) or other systems
which have an auto-scale feature. By knowing the maximum number of nodes that a
job requested in a partition, the decision to extend the nodes of the partition
by this number can be considered. Jobs which are held are not included in these
metrics.

* `slurm_partition_jobs_max_job_nodes_nohold`
  - Gives the maximum number of nodes requested by any job from all pending jobs
  that are not held in the partition.
* `slurm_partition_jobs_min_job_nodes_nohold`
  - Gives the maximum of the minimum number of nodes requested by any job from all
  pending jobs that are not held in the partition.

### Scheduler Metrics

Scheduler metrics provide insights into scheduling performance and behavior.
Examples include:

* `slurm_sched_cycle_cnt` - Scheduling cycle count
* `slurm_sched_cycle_last` - Last scheduling cycle time
* `slurm_bf_cycle_cnt` - Backfill cycle count
* `slurm_bf_active`
  - Whether the backfill scheduler is currently running

## Security Considerations

The metrics system has several important security implications:

* **No authentication**: There is no built-in authentication mechanism for
  metrics endpoints. Anyone with network access to the slurmctld port can query
  metrics.
* **PrivateData dependency**: The metrics feature is automatically disabled
  when any *PrivateData* parameter is set in slurm.conf to prevent exposure
  of sensitive information.
* **Network access**: Metrics are exposed through the slurmctld network
  interface. Consider firewall rules and network segmentation to control access.
* **Information disclosure**: Metrics may reveal information about cluster
  utilization, job patterns, and user activity that could be considered sensitive
  in some environments.

## Performance Impact

Metrics collection and exposition can impact slurmctld performance:

* **Lock contention**: Querying metrics requires acquiring various locks
  within slurmctld, which can impact scheduler performance during high-frequency
  queries.
* **Data collection overhead**: Metrics are collected in real-time from
  slurmctld's internal data structures, which adds computational overhead.
* **Data processing overhead in the external monitoring system**: We
  provide endpoints for unbounded entities like users and accounts metrics.
  A monitoring system may treat each entity as a new time series, which can
  dramatically increase the amount of data stored.
* **Network I/O**: Frequent metric queries generate network traffic and
  consume slurmctld's network I/O capacity, especially on systems with thousands
  of jobs, users or accounts.

To minimize performance impact:

* Configure appropriate scrape intervals in monitoring systems
  (e.g., 60-120 seconds)
* Use caching mechanisms in monitoring systems when possible
* Monitor slurmctld performance when enabling metrics
* Do not use unbounded metric endpoints like /metrics/jobs-users-accts to
  store data in your monitoring system

## Usage Examples

### Basic curl Examples

Query job metrics:

```
$ curl http://slurmctld.example.com:6817/metrics/jobs
# HELP slurm_jobs Total number of jobs
# TYPE slurm_jobs gauge
slurm_jobs 42
# HELP slurm_jobs_running Number of jobs in Running state
# TYPE slurm_jobs_running gauge
slurm_jobs_running 15
# HELP slurm_jobs_pending Number of jobs in Pending state
# TYPE slurm_jobs_pending gauge
slurm_jobs_pending 27
...
```

Query node metrics:

```
$ curl http://slurmctld.example.com:6817/metrics/nodes
# HELP slurm_nodes Total number of nodes
# TYPE slurm_nodes gauge
slurm_nodes 100
# HELP slurm_nodes_idle Number of nodes in Idle state
# TYPE slurm_nodes_idle gauge
slurm_nodes_idle 85
# HELP slurm_nodes_alloc Number of nodes in Allocated state
# TYPE slurm_nodes_alloc gauge
slurm_nodes_alloc 15
...
```

### Prometheus Configuration

Configure Prometheus to scrape Slurm metrics by adding the following to your
**prometheus.yml**:

```
scrape_configs:
  - job_name: 'slurm_jobs'
    static_configs:
      - targets: ['slurm.example.com:6817']
    metrics_path: '/metrics/jobs'

  - job_name: 'slurm_nodes'
    static_configs:
      - targets: ['slurm.example.com:6817']
    metrics_path: '/metrics/nodes'

  - job_name: 'slurm_partitions'
    static_configs:
      - targets: ['slurm.example.com:6817']
    metrics_path: '/metrics/partitions'

  - job_name: 'slurm_scheduler'
    static_configs:
      - targets: ['slurm.example.com:6817']
    metrics_path: '/metrics/scheduler'

  - job_name: 'slurm_useracct'
    static_configs:
      - targets: ['slurm.example.com:6817']
    metrics_path: '/metrics/jobs-users-accts'
```