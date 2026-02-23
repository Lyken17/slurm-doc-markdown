# Slurm Workload Manager - 

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

# Slurm REST API

API to access and control Slurm

More information: <https://www.schedmd.com/>

Contact Info: <sales@schedmd.com>

Version: Slurm-25.11.3

BasePath:

Apache 2.0

https://www.apache.org/licenses/LICENSE-2.0.html

## Access

1. APIKey KeyParamName:X-SLURM-USER-NAME KeyInQuery:false KeyInHeader:true
2. APIKey KeyParamName:X-SLURM-USER-TOKEN KeyInQuery:false KeyInHeader:true
3. HTTP Basic Authentication

## Methods

[ Jump to [Models](#__Models) ]

### Table of Contents

#### [Slurm](#Slurm)

* [`delete /slurm/v0.0.44/job/{job_id}`](#slurmV0044DeleteJob)
* [`delete /slurm/v0.0.44/jobs/`](#slurmV0044DeleteJobs)
* [`delete /slurm/v0.0.44/node/{node_name}`](#slurmV0044DeleteNode)
* [`delete /slurm/v0.0.44/reservation/{reservation_name}`](#slurmV0044DeleteReservation)
* [`get /slurm/v0.0.44/diag/`](#slurmV0044GetDiag)
* [`get /slurm/v0.0.44/job/{job_id}`](#slurmV0044GetJob)
* [`get /slurm/v0.0.44/jobs/`](#slurmV0044GetJobs)
* [`get /slurm/v0.0.44/jobs/state/`](#slurmV0044GetJobsState)
* [`get /slurm/v0.0.44/licenses/`](#slurmV0044GetLicenses)
* [`get /slurm/v0.0.44/node/{node_name}`](#slurmV0044GetNode)
* [`get /slurm/v0.0.44/nodes/`](#slurmV0044GetNodes)
* [`get /slurm/v0.0.44/partition/{partition_name}`](#slurmV0044GetPartition)
* [`get /slurm/v0.0.44/partitions/`](#slurmV0044GetPartitions)
* [`get /slurm/v0.0.44/ping/`](#slurmV0044GetPing)
* [`get /slurm/v0.0.44/reconfigure/`](#slurmV0044GetReconfigure)
* [`get /slurm/v0.0.44/reservation/{reservation_name}`](#slurmV0044GetReservation)
* [`get /slurm/v0.0.44/reservations/`](#slurmV0044GetReservations)
* [`get /slurm/v0.0.44/resources/{job_id}`](#slurmV0044GetResources)
* [`get /slurm/v0.0.44/shares`](#slurmV0044GetShares)
* [`post /slurm/v0.0.44/job/{job_id}`](#slurmV0044PostJob)
* [`post /slurm/v0.0.44/job/allocate`](#slurmV0044PostJobAllocate)
* [`post /slurm/v0.0.44/job/submit`](#slurmV0044PostJobSubmit)
* [`post /slurm/v0.0.44/new/node/`](#slurmV0044PostNewNode)
* [`post /slurm/v0.0.44/node/{node_name}`](#slurmV0044PostNode)
* [`post /slurm/v0.0.44/nodes/`](#slurmV0044PostNodes)
* [`post /slurm/v0.0.44/reservation`](#slurmV0044PostReservation)
* [`post /slurm/v0.0.44/reservations/`](#slurmV0044PostReservations)

#### [Slurmdb](#Slurmdb)

* [`delete /slurmdb/v0.0.44/account/{account_name}`](#slurmdbV0044DeleteAccount)
* [`delete /slurmdb/v0.0.44/association/`](#slurmdbV0044DeleteAssociation)
* [`delete /slurmdb/v0.0.44/associations/`](#slurmdbV0044DeleteAssociations)
* [`delete /slurmdb/v0.0.44/cluster/{cluster_name}`](#slurmdbV0044DeleteCluster)
* [`delete /slurmdb/v0.0.44/qos/{qos}`](#slurmdbV0044DeleteSingleQos)
* [`delete /slurmdb/v0.0.44/user/{name}`](#slurmdbV0044DeleteUser)
* [`delete /slurmdb/v0.0.44/wckey/{id}`](#slurmdbV0044DeleteWckey)
* [`get /slurmdb/v0.0.44/account/{account_name}`](#slurmdbV0044GetAccount)
* [`get /slurmdb/v0.0.44/accounts/`](#slurmdbV0044GetAccounts)
* [`get /slurmdb/v0.0.44/association/`](#slurmdbV0044GetAssociation)
* [`get /slurmdb/v0.0.44/associations/`](#slurmdbV0044GetAssociations)
* [`get /slurmdb/v0.0.44/cluster/{cluster_name}`](#slurmdbV0044GetCluster)
* [`get /slurmdb/v0.0.44/clusters/`](#slurmdbV0044GetClusters)
* [`get /slurmdb/v0.0.44/config`](#slurmdbV0044GetConfig)
* [`get /slurmdb/v0.0.44/diag/`](#slurmdbV0044GetDiag)
* [`get /slurmdb/v0.0.44/instance/`](#slurmdbV0044GetInstance)
* [`get /slurmdb/v0.0.44/instances/`](#slurmdbV0044GetInstances)
* [`get /slurmdb/v0.0.44/job/{job_id}`](#slurmdbV0044GetJob)
* [`get /slurmdb/v0.0.44/jobs/`](#slurmdbV0044GetJobs)
* [`get /slurmdb/v0.0.44/ping/`](#slurmdbV0044GetPing)
* [`get /slurmdb/v0.0.44/qos/`](#slurmdbV0044GetQos)
* [`get /slurmdb/v0.0.44/qos/{qos}`](#slurmdbV0044GetSingleQos)
* [`get /slurmdb/v0.0.44/tres/`](#slurmdbV0044GetTres)
* [`get /slurmdb/v0.0.44/user/{name}`](#slurmdbV0044GetUser)
* [`get /slurmdb/v0.0.44/users/`](#slurmdbV0044GetUsers)
* [`get /slurmdb/v0.0.44/wckey/{id}`](#slurmdbV0044GetWckey)
* [`get /slurmdb/v0.0.44/wckeys/`](#slurmdbV0044GetWckeys)
* [`post /slurmdb/v0.0.44/accounts/`](#slurmdbV0044PostAccounts)
* [`post /slurmdb/v0.0.44/accounts_association/`](#slurmdbV0044PostAccountsAssociation)
* [`post /slurmdb/v0.0.44/associations/`](#slurmdbV0044PostAssociations)
* [`post /slurmdb/v0.0.44/clusters/`](#slurmdbV0044PostClusters)
* [`post /slurmdb/v0.0.44/config`](#slurmdbV0044PostConfig)
* [`post /slurmdb/v0.0.44/job/{job_id}`](#slurmdbV0044PostJob)
* [`post /slurmdb/v0.0.44/jobs/`](#slurmdbV0044PostJobs)
* [`post /slurmdb/v0.0.44/qos/`](#slurmdbV0044PostQos)
* [`post /slurmdb/v0.0.44/tres/`](#slurmdbV0044PostTres)
* [`post /slurmdb/v0.0.44/users/`](#slurmdbV0044PostUsers)
* [`post /slurmdb/v0.0.44/users_association/`](#slurmdbV0044PostUsersAssociation)
* [`post /slurmdb/v0.0.44/wckeys/`](#slurmdbV0044PostWckeys)

# Slurm

[Up](#__Methods)

```
delete /slurm/v0.0.44/job/{job_id}
```

cancel or signal job (slurmV0044DeleteJob)

### Path parameters

job\_id (required)

Path Parameter — Job ID default: null

### Query parameters

signal (optional)

Query Parameter — Signal to send to Job default: null

flags (optional)

Query Parameter — Signalling flags default: null

### Return type

[v0.0.44\_openapi\_kill\_job\_resp](#v0.0.44_openapi_kill_job_resp)

### Example data

Content-Type: application/json

```
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ],
  "status" : [ {
    "federation" : {
      "sibling" : "sibling"
    },
    "job_id" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "error" : {
      "code" : 0,
      "string" : "string",
      "message" : "message"
    },
    "step_id" : "step_id"
  }, {
    "federation" : {
      "sibling" : "sibling"
    },
    "job_id" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "error" : {
      "code" : 0,
      "string" : "string",
      "message" : "message"
    },
    "step_id" : "step_id"
  } ]
}
```

### Produces

This API call produces the following media types according to the Accept request header;
the media type will be conveyed by the Content-Type response header.

* `application/json`

### Responses

#### 200

job signal result
[v0.0.44\_openapi\_kill\_job\_resp](#v0.0.44_openapi_kill_job_resp)

#### default

job signal result
[v0.0.44\_openapi\_kill\_job\_resp](#v0.0.44_openapi_kill_job_resp)



---

[Up](#__Methods)

```
delete /slurm/v0.0.44/jobs/
```

send signal to list of jobs (slurmV0044DeleteJobs)

### Consumes

This API call consumes the following media types via the Content-Type request header:

* `application/json`

### Request body

v0.0.44\_kill\_jobs\_msg [v0.0.44\_kill\_jobs\_msg](#v0.0.44_kill_jobs_msg) (optional)

Body Parameter —

### Return type

[v0.0.44\_openapi\_kill\_jobs\_resp](#v0.0.44_openapi_kill_jobs_resp)

### Example data

Content-Type: application/json

```
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ],
  "status" : [ {
    "federation" : {
      "sibling" : "sibling"
    },
    "job_id" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "error" : {
      "code" : 0,
      "string" : "string",
      "message" : "message"
    },
    "step_id" : "step_id"
  }, {
    "federation" : {
      "sibling" : "sibling"
    },
    "job_id" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "error" : {
      "code" : 0,
      "string" : "string",
      "message" : "message"
    },
    "step_id" : "step_id"
  } ]
}
```

### Produces

This API call produces the following media types according to the Accept request header;
the media type will be conveyed by the Content-Type response header.

* `application/json`

### Responses

#### 200

description of jobs to signal
[v0.0.44\_openapi\_kill\_jobs\_resp](#v0.0.44_openapi_kill_jobs_resp)

#### default

description of jobs to signal
[v0.0.44\_openapi\_kill\_jobs\_resp](#v0.0.44_openapi_kill_jobs_resp)



---

[Up](#__Methods)

```
delete /slurm/v0.0.44/node/{node_name}
```

delete node (slurmV0044DeleteNode)

### Path parameters

node\_name (required)

Path Parameter — Node name default: null

### Return type

[v0.0.44\_openapi\_resp](#v0.0.44_openapi_resp)

### Example data

Content-Type: application/json

```
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces

This API call produces the following media types according to the Accept request header;
the media type will be conveyed by the Content-Type response header.

* `application/json`

### Responses

#### 200

node delete request result
[v0.0.44\_openapi\_resp](#v0.0.44_openapi_resp)

#### default

node delete request result
[v0.0.44\_openapi\_resp](#v0.0.44_openapi_resp)



---

[Up](#__Methods)

```
delete /slurm/v0.0.44/reservation/{reservation_name}
```

delete a reservation (slurmV0044DeleteReservation)

### Path parameters

reservation\_name (required)

Path Parameter — Reservation name default: null

### Return type

[v0.0.44\_openapi\_resp](#v0.0.44_openapi_resp)

### Example data

Content-Type: application/json

```
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces

This API call produces the following media types according to the Accept request header;
the media type will be conveyed by the Content-Type response header.

* `application/json`

### Responses

#### 200

reservation delete request result
[v0.0.44\_openapi\_resp](#v0.0.44_openapi_resp)

#### default

reservation delete request result
[v0.0.44\_openapi\_resp](#v0.0.44_openapi_resp)



---

[Up](#__Methods)

```
get /slurm/v0.0.44/diag/
```

get diagnostics (slurmV0044GetDiag)

### Return type

[v0.0.44\_openapi\_diag\_resp](#v0.0.44_openapi_diag_resp)

### Example data

Content-Type: application/json

```
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ],
  "statistics" : {
    "bf_cycle_max" : 7,
    "rpcs_by_message_type" : [ {
      "cycle_last" : 0,
      "average_time" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "type_id" : 7,
      "queued" : 0,
      "count" : 9,
      "dropped" : 9,
      "message_type" : "message_type",
      "total_time" : 5,
      "cycle_max" : 7
    }, {
      "cycle_last" : 0,
      "average_time" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "type_id" : 7,
      "queued" : 0,
      "count" : 9,
      "dropped" : 9,
      "message_type" : "message_type",
      "total_time" : 5,
      "cycle_max" : 7
    } ],
    "bf_backfilled_het_jobs" : 6,
    "bf_table_size" : 4,
    "schedule_cycle_depth" : 1,
    "bf_depth_sum" : 5,
    "job_states_ts" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "bf_queue_len" : 4,
    "jobs_started" : 8,
    "schedule_cycle_max" : 9,
    "server_thread_count" : 6,
    "bf_queue_len_sum" : 6,
    "bf_cycle_last" : 0,
    "bf_exit" : {
      "state_changed" : 3,
      "bf_max_time" : 8,
      "bf_max_job_start" : 0,
      "bf_node_space_size" : 7,
      "end_job_queue" : 6,
      "bf_max_job_test" : 4
    },
    "agent_thread_count" : 5,
    "jobs_completed" : 9,
    "bf_depth_mean" : 3,
    "bf_depth_try_sum" : 3,
    "schedule_cycle_mean" : 7,
    "bf_table_size_sum" : 1,
    "agent_queue_size" : 1,
    "jobs_failed" : 3,
    "bf_last_depth_try" : 7,
    "req_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "bf_cycle_counter" : 5,
    "schedule_queue_length" : 9,
    "bf_queue_len_mean" : 0,
    "schedule_exit" : {
      "max_sched_time" : 5,
      "licenses" : 9,
      "default_queue_depth" : 7,
      "max_job_start" : 1,
      "max_rpc_cnt" : 4,
      "end_job_queue" : 6
    },
    "jobs_canceled" : 6,
    "schedule_cycle_sum" : 2,
    "jobs_submitted" : 6,
    "schedule_cycle_mean_depth" : 1,
    "schedule_cycle_per_minute" : 1,
    "req_time_start" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "jobs_running" : 1,
    "bf_last_backfilled_jobs" : 6,
    "bf_last_depth" : 3,
    "bf_backfilled_jobs" : 2,
    "rpcs_by_user" : [ {
      "average_time" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "user_id" : 4,
      "count" : 6,
      "total_time" : 8,
      "user" : "user"
    }, {
      "average_time" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "user_id" : 4,
      "count" : 6,
      "total_time" : 8,
      "user" : "user"
    } ],
    "bf_cycle_mean" : 6,
    "pending_rpcs_by_hostlist" : [ {
      "type_id" : 0,
      "count" : [ "count", "count" ],
      "message_type" : "message_type"
    }, {
      "type_id" : 0,
      "count" : [ "count", "count" ],
      "message_type" : "message_type"
    } ],
    "dbd_agent_queue_size" : 2,
    "bf_table_size_mean" : 4,
    "jobs_pending" : 6,
    "agent_count" : 5,
    "bf_cycle_sum" : 7,
    "parts_packed" : 0,
    "bf_active" : true,
    "bf_depth_mean_try" : 3,
    "gettimeofday_latency" : 7,
    "pending_rpcs" : [ {
      "type_id" : 4,
      "count" : 3,
      "message_type" : "message_type"
    }, {
      "type_id" : 4,
      "count" : 3,
      "message_type" : "message_type"
    } ],
    "schedule_cycle_total" : 4,
    "bf_when_last_cycle" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "schedule_cycle_last" : 3
  }
}
```

### Produces

This API call produces the following media types according to the Accept request header;
the media type will be conveyed by the Content-Type response header.

* `application/json`

### Responses

#### 200

diagnostic results
[v0.0.44\_openapi\_diag\_resp](#v0.0.44_openapi_diag_resp)

#### default

diagnostic results
[v0.0.44\_openapi\_diag\_resp](#v0.0.44_openapi_diag_resp)



---

[Up](#__Methods)

```
get /slurm/v0.0.44/job/{job_id}
```

get job info (slurmV0044GetJob)

### Path parameters

job\_id (required)

Path Parameter — Job ID default: null

### Query parameters

update\_time (optional)

Query Parameter — Query jobs updated more recently than this time (UNIX timestamp) default: null

flags (optional)

Query Parameter — Query flags default: null

### Return type

[v0.0.44\_openapi\_job\_info\_resp](#v0.0.44_openapi_job_info_resp)

### Example data

Content-Type: application/json

```
{
  "last_backfill" : {
    "number" : 2,
    "set" : true,
    "infinite" : true
  },
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "jobs" : [ {
    "container" : "container",
    "cluster" : "cluster",
    "stdin_expanded" : "stdin_expanded",
    "time_minimum" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "memory_per_tres" : "memory_per_tres",
    "scheduled_nodes" : "scheduled_nodes",
    "qos" : "qos",
    "resize_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "eligible_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "cpus_per_tres" : "cpus_per_tres",
    "preemptable_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "tasks" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "system_comment" : "system_comment",
    "federation_siblings_active" : "federation_siblings_active",
    "tasks_per_tres" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "tasks_per_core" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "accrue_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "dependency" : "dependency",
    "group_name" : "group_name",
    "profile" : [ "NOT_SET", "NOT_SET" ],
    "priority" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "tres_per_job" : "tres_per_job",
    "failed_node" : "failed_node",
    "derived_exit_code" : {
      "return_code" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "signal" : {
        "name" : "name",
        "id" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        }
      },
      "status" : [ "INVALID", "INVALID" ]
    },
    "priority_by_partition" : [ {
      "partition" : "partition",
      "priority" : 6
    }, {
      "partition" : "partition",
      "priority" : 6
    } ],
    "maximum_switch_wait_time" : 9,
    "core_spec" : 6,
    "mcs_label" : "mcs_label",
    "required_nodes" : "required_nodes",
    "tres_bind" : "tres_bind",
    "user_id" : 9,
    "selinux_context" : "selinux_context",
    "exit_code" : {
      "return_code" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "signal" : {
        "name" : "name",
        "id" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        }
      },
      "status" : [ "INVALID", "INVALID" ]
    },
    "federation_origin" : "federation_origin",
    "container_id" : "container_id",
    "shared" : [ "none", "none" ],
    "tasks_per_board" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "user_name" : "user_name",
    "stderr_expanded" : "stderr_expanded",
    "flags" : [ "KILL_INVALID_DEPENDENCY", "KILL_INVALID_DEPENDENCY" ],
    "standard_input" : "standard_input",
    "admin_comment" : "admin_comment",
    "cores_per_socket" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "step_id" : {
      "sluid" : "sluid",
      "job_id" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "step_het_component" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "step_id" : "step_id"
    },
    "job_state" : [ "PENDING", "PENDING" ],
    "tasks_per_node" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "current_working_directory" : "current_working_directory",
    "standard_error" : "standard_error",
    "array_job_id" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "cluster_features" : "cluster_features",
    "partition" : "partition",
    "segment_size" : 4,
    "threads_per_core" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "tres_alloc_str" : "tres_alloc_str",
    "memory_per_cpu" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "cpu_frequency_minimum" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "node_count" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "power" : {
      "flags" : [ "", "" ]
    },
    "deadline" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "mail_type" : [ "BEGIN", "BEGIN" ],
    "memory_per_node" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "state_reason" : "state_reason",
    "het_job_offset" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "end_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "sockets_per_board" : 5,
    "nice" : 1,
    "last_sched_evaluation" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "tres_per_node" : "tres_per_node",
    "burst_buffer" : "burst_buffer",
    "licenses" : "licenses",
    "excluded_nodes" : "excluded_nodes",
    "array_max_tasks" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "het_job_id" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "sockets_per_node" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "prefer" : "prefer",
    "time_limit" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "minimum_cpus_per_node" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "tasks_per_socket" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "batch_host" : "batch_host",
    "max_cpus" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "job_size_str" : [ "job_size_str", "job_size_str" ],
    "hold" : true,
    "cpu_frequency_maximum" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "features" : "features",
    "het_job_id_set" : "het_job_id_set",
    "state_description" : "state_description",
    "submit_line" : "submit_line",
    "array_task_id" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "licenses_allocated" : "licenses_allocated",
    "minimum_tmp_disk_per_node" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "tres_req_str" : "tres_req_str",
    "burst_buffer_state" : "burst_buffer_state",
    "cron" : "cron",
    "allocating_node" : "allocating_node",
    "tres_per_socket" : "tres_per_socket",
    "array_task_string" : "array_task_string",
    "submit_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "wckey" : "wckey",
    "max_nodes" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "batch_flag" : true,
    "start_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "name" : "name",
    "preempt_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "contiguous" : true,
    "job_resources" : {
      "nodes" : {
        "allocation" : [ {
          "memory" : {
            "used" : 2,
            "allocated" : 4
          },
          "cpus" : {
            "count" : 9,
            "used" : 3
          },
          "name" : "name",
          "index" : 7,
          "sockets" : [ {
            "cores" : [ {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            }, {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            } ],
            "index" : 7
          }, {
            "cores" : [ {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            }, {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            } ],
            "index" : 7
          } ]
        }, {
          "memory" : {
            "used" : 2,
            "allocated" : 4
          },
          "cpus" : {
            "count" : 9,
            "used" : 3
          },
          "name" : "name",
          "index" : 7,
          "sockets" : [ {
            "cores" : [ {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            }, {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            } ],
            "index" : 7
          }, {
            "cores" : [ {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            }, {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            } ],
            "index" : 7
          } ]
        } ],
        "count" : 2,
        "select_type" : [ "AVAILABLE", "AVAILABLE" ],
        "whole" : true,
        "list" : "list"
      },
      "threads_per_core" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "cpus" : 1,
      "select_type" : [ "CPU", "CPU" ]
    },
    "billable_tres" : {
      "number" : 4.145608029883936,
      "set" : true,
      "infinite" : true
    },
    "federation_siblings_viable" : "federation_siblings_viable",
    "cpus_per_task" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "batch_features" : "batch_features",
    "thread_spec" : 1,
    "cpu_frequency_governor" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "gres_detail" : [ "gres_detail", "gres_detail" ],
    "stdout_expanded" : "stdout_expanded",
    "network" : "network",
    "restart_cnt" : 1,
    "resv_name" : "resv_name",
    "extra" : "extra",
    "delay_boot" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "reboot" : true,
    "cpus" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "standard_output" : "standard_output",
    "pre_sus_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "suspend_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "association_id" : 0,
    "command" : "command",
    "tres_freq" : "tres_freq",
    "requeue" : true,
    "tres_per_task" : "tres_per_task",
    "mail_user" : "mail_user",
    "nodes" : "nodes",
    "group_id" : 5,
    "job_id" : 5,
    "comment" : "comment",
    "account" : "account",
    "required_switches" : 7
  }, {
    "container" : "container",
    "cluster" : "cluster",
    "stdin_expanded" : "stdin_expanded",
    "time_minimum" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "memory_per_tres" : "memory_per_tres",
    "scheduled_nodes" : "scheduled_nodes",
    "qos" : "qos",
    "resize_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "eligible_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "cpus_per_tres" : "cpus_per_tres",
    "preemptable_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "tasks" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "system_comment" : "system_comment",
    "federation_siblings_active" : "federation_siblings_active",
    "tasks_per_tres" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "tasks_per_core" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "accrue_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "dependency" : "dependency",
    "group_name" : "group_name",
    "profile" : [ "NOT_SET", "NOT_SET" ],
    "priority" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "tres_per_job" : "tres_per_job",
    "failed_node" : "failed_node",
    "derived_exit_code" : {
      "return_code" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "signal" : {
        "name" : "name",
        "id" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        }
      },
      "status" : [ "INVALID", "INVALID" ]
    },
    "priority_by_partition" : [ {
      "partition" : "partition",
      "priority" : 6
    }, {
      "partition" : "partition",
      "priority" : 6
    } ],
    "maximum_switch_wait_time" : 9,
    "core_spec" : 6,
    "mcs_label" : "mcs_label",
    "required_nodes" : "required_nodes",
    "tres_bind" : "tres_bind",
    "user_id" : 9,
    "selinux_context" : "selinux_context",
    "exit_code" : {
      "return_code" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "signal" : {
        "name" : "name",
        "id" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        }
      },
      "status" : [ "INVALID", "INVALID" ]
    },
    "federation_origin" : "federation_origin",
    "container_id" : "container_id",
    "shared" : [ "none", "none" ],
    "tasks_per_board" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "user_name" : "user_name",
    "stderr_expanded" : "stderr_expanded",
    "flags" : [ "KILL_INVALID_DEPENDENCY", "KILL_INVALID_DEPENDENCY" ],
    "standard_input" : "standard_input",
    "admin_comment" : "admin_comment",
    "cores_per_socket" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "step_id" : {
      "sluid" : "sluid",
      "job_id" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "step_het_component" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "step_id" : "step_id"
    },
    "job_state" : [ "PENDING", "PENDING" ],
    "tasks_per_node" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "current_working_directory" : "current_working_directory",
    "standard_error" : "standard_error",
    "array_job_id" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "cluster_features" : "cluster_features",
    "partition" : "partition",
    "segment_size" : 4,
    "threads_per_core" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "tres_alloc_str" : "tres_alloc_str",
    "memory_per_cpu" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "cpu_frequency_minimum" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "node_count" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "power" : {
      "flags" : [ "", "" ]
    },
    "deadline" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "mail_type" : [ "BEGIN", "BEGIN" ],
    "memory_per_node" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "state_reason" : "state_reason",
    "het_job_offset" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "end_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "sockets_per_board" : 5,
    "nice" : 1,
    "last_sched_evaluation" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "tres_per_node" : "tres_per_node",
    "burst_buffer" : "burst_buffer",
    "licenses" : "licenses",
    "excluded_nodes" : "excluded_nodes",
    "array_max_tasks" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "het_job_id" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "sockets_per_node" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "prefer" : "prefer",
    "time_limit" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "minimum_cpus_per_node" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "tasks_per_socket" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "batch_host" : "batch_host",
    "max_cpus" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "job_size_str" : [ "job_size_str", "job_size_str" ],
    "hold" : true,
    "cpu_frequency_maximum" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "features" : "features",
    "het_job_id_set" : "het_job_id_set",
    "state_description" : "state_description",
    "submit_line" : "submit_line",
    "array_task_id" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "licenses_allocated" : "licenses_allocated",
    "minimum_tmp_disk_per_node" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "tres_req_str" : "tres_req_str",
    "burst_buffer_state" : "burst_buffer_state",
    "cron" : "cron",
    "allocating_node" : "allocating_node",
    "tres_per_socket" : "tres_per_socket",
    "array_task_string" : "array_task_string",
    "submit_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "wckey" : "wckey",
    "max_nodes" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "batch_flag" : true,
    "start_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "name" : "name",
    "preempt_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "contiguous" : true,
    "job_resources" : {
      "nodes" : {
        "allocation" : [ {
          "memory" : {
            "used" : 2,
            "allocated" : 4
          },
          "cpus" : {
            "count" : 9,
            "used" : 3
          },
          "name" : "name",
          "index" : 7,
          "sockets" : [ {
            "cores" : [ {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            }, {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            } ],
            "index" : 7
          }, {
            "cores" : [ {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            }, {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            } ],
            "index" : 7
          } ]
        }, {
          "memory" : {
            "used" : 2,
            "allocated" : 4
          },
          "cpus" : {
            "count" : 9,
            "used" : 3
          },
          "name" : "name",
          "index" : 7,
          "sockets" : [ {
            "cores" : [ {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            }, {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            } ],
            "index" : 7
          }, {
            "cores" : [ {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            }, {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            } ],
            "index" : 7
          } ]
        } ],
        "count" : 2,
        "select_type" : [ "AVAILABLE", "AVAILABLE" ],
        "whole" : true,
        "list" : "list"
      },
      "threads_per_core" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "cpus" : 1,
      "select_type" : [ "CPU", "CPU" ]
    },
    "billable_tres" : {
      "number" : 4.145608029883936,
      "set" : true,
      "infinite" : true
    },
    "federation_siblings_viable" : "federation_siblings_viable",
    "cpus_per_task" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "batch_features" : "batch_features",
    "thread_spec" : 1,
    "cpu_frequency_governor" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "gres_detail" : [ "gres_detail", "gres_detail" ],
    "stdout_expanded" : "stdout_expanded",
    "network" : "network",
    "restart_cnt" : 1,
    "resv_name" : "resv_name",
    "extra" : "extra",
    "delay_boot" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "reboot" : true,
    "cpus" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "standard_output" : "standard_output",
    "pre_sus_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "suspend_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "association_id" : 0,
    "command" : "command",
    "tres_freq" : "tres_freq",
    "requeue" : true,
    "tres_per_task" : "tres_per_task",
    "mail_user" : "mail_user",
    "nodes" : "nodes",
    "group_id" : 5,
    "job_id" : 5,
    "comment" : "comment",
    "account" : "account",
    "required_switches" : 7
  } ],
  "last_update" : {
    "number" : 2,
    "set" : true,
    "infinite" : true
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces

This API call produces the following media types according to the Accept request header;
the media type will be conveyed by the Content-Type response header.

* `application/json`

### Responses

#### 200

job(s) information
[v0.0.44\_openapi\_job\_info\_resp](#v0.0.44_openapi_job_info_resp)

#### default

job(s) information
[v0.0.44\_openapi\_job\_info\_resp](#v0.0.44_openapi_job_info_resp)



---

[Up](#__Methods)

```
get /slurm/v0.0.44/jobs/
```

get list of jobs (slurmV0044GetJobs)

### Query parameters

update\_time (optional)

Query Parameter — Query jobs updated more recently than this time (UNIX timestamp) default: null

flags (optional)

Query Parameter — Query flags default: null

### Return type

[v0.0.44\_openapi\_job\_info\_resp](#v0.0.44_openapi_job_info_resp)

### Example data

Content-Type: application/json

```
{
  "last_backfill" : {
    "number" : 2,
    "set" : true,
    "infinite" : true
  },
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "jobs" : [ {
    "container" : "container",
    "cluster" : "cluster",
    "stdin_expanded" : "stdin_expanded",
    "time_minimum" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "memory_per_tres" : "memory_per_tres",
    "scheduled_nodes" : "scheduled_nodes",
    "qos" : "qos",
    "resize_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "eligible_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "cpus_per_tres" : "cpus_per_tres",
    "preemptable_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "tasks" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "system_comment" : "system_comment",
    "federation_siblings_active" : "federation_siblings_active",
    "tasks_per_tres" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "tasks_per_core" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "accrue_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "dependency" : "dependency",
    "group_name" : "group_name",
    "profile" : [ "NOT_SET", "NOT_SET" ],
    "priority" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "tres_per_job" : "tres_per_job",
    "failed_node" : "failed_node",
    "derived_exit_code" : {
      "return_code" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "signal" : {
        "name" : "name",
        "id" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        }
      },
      "status" : [ "INVALID", "INVALID" ]
    },
    "priority_by_partition" : [ {
      "partition" : "partition",
      "priority" : 6
    }, {
      "partition" : "partition",
      "priority" : 6
    } ],
    "maximum_switch_wait_time" : 9,
    "core_spec" : 6,
    "mcs_label" : "mcs_label",
    "required_nodes" : "required_nodes",
    "tres_bind" : "tres_bind",
    "user_id" : 9,
    "selinux_context" : "selinux_context",
    "exit_code" : {
      "return_code" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "signal" : {
        "name" : "name",
        "id" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        }
      },
      "status" : [ "INVALID", "INVALID" ]
    },
    "federation_origin" : "federation_origin",
    "container_id" : "container_id",
    "shared" : [ "none", "none" ],
    "tasks_per_board" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "user_name" : "user_name",
    "stderr_expanded" : "stderr_expanded",
    "flags" : [ "KILL_INVALID_DEPENDENCY", "KILL_INVALID_DEPENDENCY" ],
    "standard_input" : "standard_input",
    "admin_comment" : "admin_comment",
    "cores_per_socket" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "step_id" : {
      "sluid" : "sluid",
      "job_id" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "step_het_component" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "step_id" : "step_id"
    },
    "job_state" : [ "PENDING", "PENDING" ],
    "tasks_per_node" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "current_working_directory" : "current_working_directory",
    "standard_error" : "standard_error",
    "array_job_id" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "cluster_features" : "cluster_features",
    "partition" : "partition",
    "segment_size" : 4,
    "threads_per_core" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "tres_alloc_str" : "tres_alloc_str",
    "memory_per_cpu" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "cpu_frequency_minimum" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "node_count" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "power" : {
      "flags" : [ "", "" ]
    },
    "deadline" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "mail_type" : [ "BEGIN", "BEGIN" ],
    "memory_per_node" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "state_reason" : "state_reason",
    "het_job_offset" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "end_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "sockets_per_board" : 5,
    "nice" : 1,
    "last_sched_evaluation" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "tres_per_node" : "tres_per_node",
    "burst_buffer" : "burst_buffer",
    "licenses" : "licenses",
    "excluded_nodes" : "excluded_nodes",
    "array_max_tasks" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "het_job_id" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "sockets_per_node" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "prefer" : "prefer",
    "time_limit" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "minimum_cpus_per_node" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "tasks_per_socket" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "batch_host" : "batch_host",
    "max_cpus" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "job_size_str" : [ "job_size_str", "job_size_str" ],
    "hold" : true,
    "cpu_frequency_maximum" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "features" : "features",
    "het_job_id_set" : "het_job_id_set",
    "state_description" : "state_description",
    "submit_line" : "submit_line",
    "array_task_id" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "licenses_allocated" : "licenses_allocated",
    "minimum_tmp_disk_per_node" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "tres_req_str" : "tres_req_str",
    "burst_buffer_state" : "burst_buffer_state",
    "cron" : "cron",
    "allocating_node" : "allocating_node",
    "tres_per_socket" : "tres_per_socket",
    "array_task_string" : "array_task_string",
    "submit_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "wckey" : "wckey",
    "max_nodes" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "batch_flag" : true,
    "start_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "name" : "name",
    "preempt_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "contiguous" : true,
    "job_resources" : {
      "nodes" : {
        "allocation" : [ {
          "memory" : {
            "used" : 2,
            "allocated" : 4
          },
          "cpus" : {
            "count" : 9,
            "used" : 3
          },
          "name" : "name",
          "index" : 7,
          "sockets" : [ {
            "cores" : [ {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            }, {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            } ],
            "index" : 7
          }, {
            "cores" : [ {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            }, {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            } ],
            "index" : 7
          } ]
        }, {
          "memory" : {
            "used" : 2,
            "allocated" : 4
          },
          "cpus" : {
            "count" : 9,
            "used" : 3
          },
          "name" : "name",
          "index" : 7,
          "sockets" : [ {
            "cores" : [ {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            }, {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            } ],
            "index" : 7
          }, {
            "cores" : [ {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            }, {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            } ],
            "index" : 7
          } ]
        } ],
        "count" : 2,
        "select_type" : [ "AVAILABLE", "AVAILABLE" ],
        "whole" : true,
        "list" : "list"
      },
      "threads_per_core" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "cpus" : 1,
      "select_type" : [ "CPU", "CPU" ]
    },
    "billable_tres" : {
      "number" : 4.145608029883936,
      "set" : true,
      "infinite" : true
    },
    "federation_siblings_viable" : "federation_siblings_viable",
    "cpus_per_task" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "batch_features" : "batch_features",
    "thread_spec" : 1,
    "cpu_frequency_governor" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "gres_detail" : [ "gres_detail", "gres_detail" ],
    "stdout_expanded" : "stdout_expanded",
    "network" : "network",
    "restart_cnt" : 1,
    "resv_name" : "resv_name",
    "extra" : "extra",
    "delay_boot" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "reboot" : true,
    "cpus" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "standard_output" : "standard_output",
    "pre_sus_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "suspend_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "association_id" : 0,
    "command" : "command",
    "tres_freq" : "tres_freq",
    "requeue" : true,
    "tres_per_task" : "tres_per_task",
    "mail_user" : "mail_user",
    "nodes" : "nodes",
    "group_id" : 5,
    "job_id" : 5,
    "comment" : "comment",
    "account" : "account",
    "required_switches" : 7
  }, {
    "container" : "container",
    "cluster" : "cluster",
    "stdin_expanded" : "stdin_expanded",
    "time_minimum" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "memory_per_tres" : "memory_per_tres",
    "scheduled_nodes" : "scheduled_nodes",
    "qos" : "qos",
    "resize_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "eligible_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "cpus_per_tres" : "cpus_per_tres",
    "preemptable_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "tasks" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "system_comment" : "system_comment",
    "federation_siblings_active" : "federation_siblings_active",
    "tasks_per_tres" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "tasks_per_core" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "accrue_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "dependency" : "dependency",
    "group_name" : "group_name",
    "profile" : [ "NOT_SET", "NOT_SET" ],
    "priority" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "tres_per_job" : "tres_per_job",
    "failed_node" : "failed_node",
    "derived_exit_code" : {
      "return_code" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "signal" : {
        "name" : "name",
        "id" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        }
      },
      "status" : [ "INVALID", "INVALID" ]
    },
    "priority_by_partition" : [ {
      "partition" : "partition",
      "priority" : 6
    }, {
      "partition" : "partition",
      "priority" : 6
    } ],
    "maximum_switch_wait_time" : 9,
    "core_spec" : 6,
    "mcs_label" : "mcs_label",
    "required_nodes" : "required_nodes",
    "tres_bind" : "tres_bind",
    "user_id" : 9,
    "selinux_context" : "selinux_context",
    "exit_code" : {
      "return_code" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "signal" : {
        "name" : "name",
        "id" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        }
      },
      "status" : [ "INVALID", "INVALID" ]
    },
    "federation_origin" : "federation_origin",
    "container_id" : "container_id",
    "shared" : [ "none", "none" ],
    "tasks_per_board" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "user_name" : "user_name",
    "stderr_expanded" : "stderr_expanded",
    "flags" : [ "KILL_INVALID_DEPENDENCY", "KILL_INVALID_DEPENDENCY" ],
    "standard_input" : "standard_input",
    "admin_comment" : "admin_comment",
    "cores_per_socket" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "step_id" : {
      "sluid" : "sluid",
      "job_id" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "step_het_component" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "step_id" : "step_id"
    },
    "job_state" : [ "PENDING", "PENDING" ],
    "tasks_per_node" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "current_working_directory" : "current_working_directory",
    "standard_error" : "standard_error",
    "array_job_id" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "cluster_features" : "cluster_features",
    "partition" : "partition",
    "segment_size" : 4,
    "threads_per_core" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "tres_alloc_str" : "tres_alloc_str",
    "memory_per_cpu" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "cpu_frequency_minimum" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "node_count" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "power" : {
      "flags" : [ "", "" ]
    },
    "deadline" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "mail_type" : [ "BEGIN", "BEGIN" ],
    "memory_per_node" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "state_reason" : "state_reason",
    "het_job_offset" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "end_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "sockets_per_board" : 5,
    "nice" : 1,
    "last_sched_evaluation" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "tres_per_node" : "tres_per_node",
    "burst_buffer" : "burst_buffer",
    "licenses" : "licenses",
    "excluded_nodes" : "excluded_nodes",
    "array_max_tasks" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "het_job_id" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "sockets_per_node" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "prefer" : "prefer",
    "time_limit" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "minimum_cpus_per_node" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "tasks_per_socket" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "batch_host" : "batch_host",
    "max_cpus" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "job_size_str" : [ "job_size_str", "job_size_str" ],
    "hold" : true,
    "cpu_frequency_maximum" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "features" : "features",
    "het_job_id_set" : "het_job_id_set",
    "state_description" : "state_description",
    "submit_line" : "submit_line",
    "array_task_id" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "licenses_allocated" : "licenses_allocated",
    "minimum_tmp_disk_per_node" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "tres_req_str" : "tres_req_str",
    "burst_buffer_state" : "burst_buffer_state",
    "cron" : "cron",
    "allocating_node" : "allocating_node",
    "tres_per_socket" : "tres_per_socket",
    "array_task_string" : "array_task_string",
    "submit_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "wckey" : "wckey",
    "max_nodes" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "batch_flag" : true,
    "start_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "name" : "name",
    "preempt_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "contiguous" : true,
    "job_resources" : {
      "nodes" : {
        "allocation" : [ {
          "memory" : {
            "used" : 2,
            "allocated" : 4
          },
          "cpus" : {
            "count" : 9,
            "used" : 3
          },
          "name" : "name",
          "index" : 7,
          "sockets" : [ {
            "cores" : [ {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            }, {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            } ],
            "index" : 7
          }, {
            "cores" : [ {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            }, {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            } ],
            "index" : 7
          } ]
        }, {
          "memory" : {
            "used" : 2,
            "allocated" : 4
          },
          "cpus" : {
            "count" : 9,
            "used" : 3
          },
          "name" : "name",
          "index" : 7,
          "sockets" : [ {
            "cores" : [ {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            }, {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            } ],
            "index" : 7
          }, {
            "cores" : [ {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            }, {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            } ],
            "index" : 7
          } ]
        } ],
        "count" : 2,
        "select_type" : [ "AVAILABLE", "AVAILABLE" ],
        "whole" : true,
        "list" : "list"
      },
      "threads_per_core" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "cpus" : 1,
      "select_type" : [ "CPU", "CPU" ]
    },
    "billable_tres" : {
      "number" : 4.145608029883936,
      "set" : true,
      "infinite" : true
    },
    "federation_siblings_viable" : "federation_siblings_viable",
    "cpus_per_task" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "batch_features" : "batch_features",
    "thread_spec" : 1,
    "cpu_frequency_governor" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "gres_detail" : [ "gres_detail", "gres_detail" ],
    "stdout_expanded" : "stdout_expanded",
    "network" : "network",
    "restart_cnt" : 1,
    "resv_name" : "resv_name",
    "extra" : "extra",
    "delay_boot" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "reboot" : true,
    "cpus" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "standard_output" : "standard_output",
    "pre_sus_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "suspend_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "association_id" : 0,
    "command" : "command",
    "tres_freq" : "tres_freq",
    "requeue" : true,
    "tres_per_task" : "tres_per_task",
    "mail_user" : "mail_user",
    "nodes" : "nodes",
    "group_id" : 5,
    "job_id" : 5,
    "comment" : "comment",
    "account" : "account",
    "required_switches" : 7
  } ],
  "last_update" : {
    "number" : 2,
    "set" : true,
    "infinite" : true
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces

This API call produces the following media types according to the Accept request header;
the media type will be conveyed by the Content-Type response header.

* `application/json`

### Responses

#### 200

job(s) information
[v0.0.44\_openapi\_job\_info\_resp](#v0.0.44_openapi_job_info_resp)

#### default

job(s) information
[v0.0.44\_openapi\_job\_info\_resp](#v0.0.44_openapi_job_info_resp)



---

[Up](#__Methods)

```
get /slurm/v0.0.44/jobs/state/
```

get list of job states (slurmV0044GetJobsState)

### Query parameters

job\_id (optional)

Query Parameter — CSV list of Job IDs to search for default: null

### Return type

[v0.0.44\_openapi\_job\_info\_resp](#v0.0.44_openapi_job_info_resp)

### Example data

Content-Type: application/json

```
{
  "last_backfill" : {
    "number" : 2,
    "set" : true,
    "infinite" : true
  },
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "jobs" : [ {
    "container" : "container",
    "cluster" : "cluster",
    "stdin_expanded" : "stdin_expanded",
    "time_minimum" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "memory_per_tres" : "memory_per_tres",
    "scheduled_nodes" : "scheduled_nodes",
    "qos" : "qos",
    "resize_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "eligible_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "cpus_per_tres" : "cpus_per_tres",
    "preemptable_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "tasks" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "system_comment" : "system_comment",
    "federation_siblings_active" : "federation_siblings_active",
    "tasks_per_tres" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "tasks_per_core" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "accrue_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "dependency" : "dependency",
    "group_name" : "group_name",
    "profile" : [ "NOT_SET", "NOT_SET" ],
    "priority" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "tres_per_job" : "tres_per_job",
    "failed_node" : "failed_node",
    "derived_exit_code" : {
      "return_code" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "signal" : {
        "name" : "name",
        "id" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        }
      },
      "status" : [ "INVALID", "INVALID" ]
    },
    "priority_by_partition" : [ {
      "partition" : "partition",
      "priority" : 6
    }, {
      "partition" : "partition",
      "priority" : 6
    } ],
    "maximum_switch_wait_time" : 9,
    "core_spec" : 6,
    "mcs_label" : "mcs_label",
    "required_nodes" : "required_nodes",
    "tres_bind" : "tres_bind",
    "user_id" : 9,
    "selinux_context" : "selinux_context",
    "exit_code" : {
      "return_code" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "signal" : {
        "name" : "name",
        "id" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        }
      },
      "status" : [ "INVALID", "INVALID" ]
    },
    "federation_origin" : "federation_origin",
    "container_id" : "container_id",
    "shared" : [ "none", "none" ],
    "tasks_per_board" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "user_name" : "user_name",
    "stderr_expanded" : "stderr_expanded",
    "flags" : [ "KILL_INVALID_DEPENDENCY", "KILL_INVALID_DEPENDENCY" ],
    "standard_input" : "standard_input",
    "admin_comment" : "admin_comment",
    "cores_per_socket" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "step_id" : {
      "sluid" : "sluid",
      "job_id" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "step_het_component" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "step_id" : "step_id"
    },
    "job_state" : [ "PENDING", "PENDING" ],
    "tasks_per_node" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "current_working_directory" : "current_working_directory",
    "standard_error" : "standard_error",
    "array_job_id" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "cluster_features" : "cluster_features",
    "partition" : "partition",
    "segment_size" : 4,
    "threads_per_core" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "tres_alloc_str" : "tres_alloc_str",
    "memory_per_cpu" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "cpu_frequency_minimum" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "node_count" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "power" : {
      "flags" : [ "", "" ]
    },
    "deadline" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "mail_type" : [ "BEGIN", "BEGIN" ],
    "memory_per_node" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "state_reason" : "state_reason",
    "het_job_offset" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "end_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "sockets_per_board" : 5,
    "nice" : 1,
    "last_sched_evaluation" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "tres_per_node" : "tres_per_node",
    "burst_buffer" : "burst_buffer",
    "licenses" : "licenses",
    "excluded_nodes" : "excluded_nodes",
    "array_max_tasks" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "het_job_id" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "sockets_per_node" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "prefer" : "prefer",
    "time_limit" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "minimum_cpus_per_node" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "tasks_per_socket" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "batch_host" : "batch_host",
    "max_cpus" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "job_size_str" : [ "job_size_str", "job_size_str" ],
    "hold" : true,
    "cpu_frequency_maximum" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "features" : "features",
    "het_job_id_set" : "het_job_id_set",
    "state_description" : "state_description",
    "submit_line" : "submit_line",
    "array_task_id" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "licenses_allocated" : "licenses_allocated",
    "minimum_tmp_disk_per_node" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "tres_req_str" : "tres_req_str",
    "burst_buffer_state" : "burst_buffer_state",
    "cron" : "cron",
    "allocating_node" : "allocating_node",
    "tres_per_socket" : "tres_per_socket",
    "array_task_string" : "array_task_string",
    "submit_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "wckey" : "wckey",
    "max_nodes" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "batch_flag" : true,
    "start_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "name" : "name",
    "preempt_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "contiguous" : true,
    "job_resources" : {
      "nodes" : {
        "allocation" : [ {
          "memory" : {
            "used" : 2,
            "allocated" : 4
          },
          "cpus" : {
            "count" : 9,
            "used" : 3
          },
          "name" : "name",
          "index" : 7,
          "sockets" : [ {
            "cores" : [ {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            }, {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            } ],
            "index" : 7
          }, {
            "cores" : [ {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            }, {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            } ],
            "index" : 7
          } ]
        }, {
          "memory" : {
            "used" : 2,
            "allocated" : 4
          },
          "cpus" : {
            "count" : 9,
            "used" : 3
          },
          "name" : "name",
          "index" : 7,
          "sockets" : [ {
            "cores" : [ {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            }, {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            } ],
            "index" : 7
          }, {
            "cores" : [ {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            }, {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            } ],
            "index" : 7
          } ]
        } ],
        "count" : 2,
        "select_type" : [ "AVAILABLE", "AVAILABLE" ],
        "whole" : true,
        "list" : "list"
      },
      "threads_per_core" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "cpus" : 1,
      "select_type" : [ "CPU", "CPU" ]
    },
    "billable_tres" : {
      "number" : 4.145608029883936,
      "set" : true,
      "infinite" : true
    },
    "federation_siblings_viable" : "federation_siblings_viable",
    "cpus_per_task" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "batch_features" : "batch_features",
    "thread_spec" : 1,
    "cpu_frequency_governor" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "gres_detail" : [ "gres_detail", "gres_detail" ],
    "stdout_expanded" : "stdout_expanded",
    "network" : "network",
    "restart_cnt" : 1,
    "resv_name" : "resv_name",
    "extra" : "extra",
    "delay_boot" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "reboot" : true,
    "cpus" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "standard_output" : "standard_output",
    "pre_sus_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "suspend_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "association_id" : 0,
    "command" : "command",
    "tres_freq" : "tres_freq",
    "requeue" : true,
    "tres_per_task" : "tres_per_task",
    "mail_user" : "mail_user",
    "nodes" : "nodes",
    "group_id" : 5,
    "job_id" : 5,
    "comment" : "comment",
    "account" : "account",
    "required_switches" : 7
  }, {
    "container" : "container",
    "cluster" : "cluster",
    "stdin_expanded" : "stdin_expanded",
    "time_minimum" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "memory_per_tres" : "memory_per_tres",
    "scheduled_nodes" : "scheduled_nodes",
    "qos" : "qos",
    "resize_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "eligible_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "cpus_per_tres" : "cpus_per_tres",
    "preemptable_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "tasks" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "system_comment" : "system_comment",
    "federation_siblings_active" : "federation_siblings_active",
    "tasks_per_tres" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "tasks_per_core" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "accrue_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "dependency" : "dependency",
    "group_name" : "group_name",
    "profile" : [ "NOT_SET", "NOT_SET" ],
    "priority" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "tres_per_job" : "tres_per_job",
    "failed_node" : "failed_node",
    "derived_exit_code" : {
      "return_code" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "signal" : {
        "name" : "name",
        "id" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        }
      },
      "status" : [ "INVALID", "INVALID" ]
    },
    "priority_by_partition" : [ {
      "partition" : "partition",
      "priority" : 6
    }, {
      "partition" : "partition",
      "priority" : 6
    } ],
    "maximum_switch_wait_time" : 9,
    "core_spec" : 6,
    "mcs_label" : "mcs_label",
    "required_nodes" : "required_nodes",
    "tres_bind" : "tres_bind",
    "user_id" : 9,
    "selinux_context" : "selinux_context",
    "exit_code" : {
      "return_code" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "signal" : {
        "name" : "name",
        "id" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        }
      },
      "status" : [ "INVALID", "INVALID" ]
    },
    "federation_origin" : "federation_origin",
    "container_id" : "container_id",
    "shared" : [ "none", "none" ],
    "tasks_per_board" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "user_name" : "user_name",
    "stderr_expanded" : "stderr_expanded",
    "flags" : [ "KILL_INVALID_DEPENDENCY", "KILL_INVALID_DEPENDENCY" ],
    "standard_input" : "standard_input",
    "admin_comment" : "admin_comment",
    "cores_per_socket" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "step_id" : {
      "sluid" : "sluid",
      "job_id" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "step_het_component" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "step_id" : "step_id"
    },
    "job_state" : [ "PENDING", "PENDING" ],
    "tasks_per_node" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "current_working_directory" : "current_working_directory",
    "standard_error" : "standard_error",
    "array_job_id" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "cluster_features" : "cluster_features",
    "partition" : "partition",
    "segment_size" : 4,
    "threads_per_core" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "tres_alloc_str" : "tres_alloc_str",
    "memory_per_cpu" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "cpu_frequency_minimum" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "node_count" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "power" : {
      "flags" : [ "", "" ]
    },
    "deadline" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "mail_type" : [ "BEGIN", "BEGIN" ],
    "memory_per_node" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "state_reason" : "state_reason",
    "het_job_offset" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "end_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "sockets_per_board" : 5,
    "nice" : 1,
    "last_sched_evaluation" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "tres_per_node" : "tres_per_node",
    "burst_buffer" : "burst_buffer",
    "licenses" : "licenses",
    "excluded_nodes" : "excluded_nodes",
    "array_max_tasks" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "het_job_id" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "sockets_per_node" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "prefer" : "prefer",
    "time_limit" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "minimum_cpus_per_node" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "tasks_per_socket" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "batch_host" : "batch_host",
    "max_cpus" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "job_size_str" : [ "job_size_str", "job_size_str" ],
    "hold" : true,
    "cpu_frequency_maximum" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "features" : "features",
    "het_job_id_set" : "het_job_id_set",
    "state_description" : "state_description",
    "submit_line" : "submit_line",
    "array_task_id" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "licenses_allocated" : "licenses_allocated",
    "minimum_tmp_disk_per_node" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "tres_req_str" : "tres_req_str",
    "burst_buffer_state" : "burst_buffer_state",
    "cron" : "cron",
    "allocating_node" : "allocating_node",
    "tres_per_socket" : "tres_per_socket",
    "array_task_string" : "array_task_string",
    "submit_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "wckey" : "wckey",
    "max_nodes" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "batch_flag" : true,
    "start_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "name" : "name",
    "preempt_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "contiguous" : true,
    "job_resources" : {
      "nodes" : {
        "allocation" : [ {
          "memory" : {
            "used" : 2,
            "allocated" : 4
          },
          "cpus" : {
            "count" : 9,
            "used" : 3
          },
          "name" : "name",
          "index" : 7,
          "sockets" : [ {
            "cores" : [ {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            }, {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            } ],
            "index" : 7
          }, {
            "cores" : [ {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            }, {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            } ],
            "index" : 7
          } ]
        }, {
          "memory" : {
            "used" : 2,
            "allocated" : 4
          },
          "cpus" : {
            "count" : 9,
            "used" : 3
          },
          "name" : "name",
          "index" : 7,
          "sockets" : [ {
            "cores" : [ {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            }, {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            } ],
            "index" : 7
          }, {
            "cores" : [ {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            }, {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            } ],
            "index" : 7
          } ]
        } ],
        "count" : 2,
        "select_type" : [ "AVAILABLE", "AVAILABLE" ],
        "whole" : true,
        "list" : "list"
      },
      "threads_per_core" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "cpus" : 1,
      "select_type" : [ "CPU", "CPU" ]
    },
    "billable_tres" : {
      "number" : 4.145608029883936,
      "set" : true,
      "infinite" : true
    },
    "federation_siblings_viable" : "federation_siblings_viable",
    "cpus_per_task" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "batch_features" : "batch_features",
    "thread_spec" : 1,
    "cpu_frequency_governor" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "gres_detail" : [ "gres_detail", "gres_detail" ],
    "stdout_expanded" : "stdout_expanded",
    "network" : "network",
    "restart_cnt" : 1,
    "resv_name" : "resv_name",
    "extra" : "extra",
    "delay_boot" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "reboot" : true,
    "cpus" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "standard_output" : "standard_output",
    "pre_sus_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "suspend_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "association_id" : 0,
    "command" : "command",
    "tres_freq" : "tres_freq",
    "requeue" : true,
    "tres_per_task" : "tres_per_task",
    "mail_user" : "mail_user",
    "nodes" : "nodes",
    "group_id" : 5,
    "job_id" : 5,
    "comment" : "comment",
    "account" : "account",
    "required_switches" : 7
  } ],
  "last_update" : {
    "number" : 2,
    "set" : true,
    "infinite" : true
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces

This API call produces the following media types according to the Accept request header;
the media type will be conveyed by the Content-Type response header.

* `application/json`

### Responses

#### 200

job(s) state information
[v0.0.44\_openapi\_job\_info\_resp](#v0.0.44_openapi_job_info_resp)

#### default

job(s) state information
[v0.0.44\_openapi\_job\_info\_resp](#v0.0.44_openapi_job_info_resp)



---

[Up](#__Methods)

```
get /slurm/v0.0.44/licenses/
```

get all Slurm tracked license info (slurmV0044GetLicenses)

### Return type

[v0.0.44\_openapi\_licenses\_resp](#v0.0.44_openapi_licenses_resp)

### Example data

Content-Type: application/json

```
{
  "licenses" : [ {
    "Used" : 6,
    "LastUpdate" : 7,
    "Total" : 0,
    "Remote" : true,
    "LastConsumed" : 5,
    "LastDeficit" : 2,
    "LicenseName" : "LicenseName",
    "Free" : 1,
    "Nodes" : "Nodes",
    "Reserved" : 5
  }, {
    "Used" : 6,
    "LastUpdate" : 7,
    "Total" : 0,
    "Remote" : true,
    "LastConsumed" : 5,
    "LastDeficit" : 2,
    "LicenseName" : "LicenseName",
    "Free" : 1,
    "Nodes" : "Nodes",
    "Reserved" : 5
  } ],
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "last_update" : {
    "number" : 2,
    "set" : true,
    "infinite" : true
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces

This API call produces the following media types according to the Accept request header;
the media type will be conveyed by the Content-Type response header.

* `application/json`

### Responses

#### 200

results of get all licenses
[v0.0.44\_openapi\_licenses\_resp](#v0.0.44_openapi_licenses_resp)

#### default

results of get all licenses
[v0.0.44\_openapi\_licenses\_resp](#v0.0.44_openapi_licenses_resp)



---

[Up](#__Methods)

```
get /slurm/v0.0.44/node/{node_name}
```

get node info (slurmV0044GetNode)

### Path parameters

node\_name (required)

Path Parameter — Node name default: null

### Query parameters

update\_time (optional)

Query Parameter — Query jobs updated more recently than this time (UNIX timestamp) default: null

flags (optional)

Query Parameter — Query flags default: null

### Return type

[v0.0.44\_openapi\_nodes\_resp](#v0.0.44_openapi_nodes_resp)

### Example data

Content-Type: application/json

```
{
  "nodes" : [ {
    "reason" : "reason",
    "gpu_spec" : "gpu_spec",
    "slurmd_start_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "features" : [ "features", "features" ],
    "hostname" : "hostname",
    "cores" : 6,
    "reason_changed_at" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "reservation" : "reservation",
    "tres" : "tres",
    "cpu_binding" : 5,
    "state" : [ "INVALID", "INVALID" ],
    "sockets" : 9,
    "energy" : {
      "current_watts" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "base_consumed_energy" : 3,
      "last_collected" : 7,
      "consumed_energy" : 2,
      "previous_consumed_energy" : 4,
      "average_watts" : 9
    },
    "partitions" : [ "partitions", "partitions" ],
    "topology" : "topology",
    "gres_drained" : "gres_drained",
    "weight" : 8,
    "version" : "version",
    "gres_used" : "gres_used",
    "mcs_label" : "mcs_label",
    "real_memory" : 1,
    "instance_id" : "instance_id",
    "burstbuffer_network_address" : "burstbuffer_network_address",
    "port" : 1,
    "name" : "name",
    "resume_after" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "temporary_disk" : 6,
    "tres_used" : "tres_used",
    "effective_cpus" : 7,
    "instance_type" : "instance_type",
    "external_sensors" : "{}",
    "cert_flags" : [ "TOKEN_SET", "TOKEN_SET" ],
    "res_cores_per_gpu" : 6,
    "boards" : 0,
    "alloc_cpus" : 1,
    "active_features" : [ "active_features", "active_features" ],
    "reason_set_by_user" : "reason_set_by_user",
    "free_mem" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "alloc_idle_cpus" : 4,
    "extra" : "extra",
    "operating_system" : "operating_system",
    "power" : "{}",
    "tls_cert_last_renewal" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "architecture" : "architecture",
    "owner" : "owner",
    "cluster_name" : "cluster_name",
    "address" : "address",
    "cpus" : 2,
    "tres_weighted" : 5.025004791520295,
    "gres" : "gres",
    "threads" : 9,
    "boot_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "alloc_memory" : 7,
    "specialized_memory" : 1,
    "specialized_cpus" : "specialized_cpus",
    "specialized_cores" : 1,
    "last_busy" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "comment" : "comment",
    "next_state_after_reboot" : [ "INVALID", "INVALID" ],
    "cpu_load" : 5
  }, {
    "reason" : "reason",
    "gpu_spec" : "gpu_spec",
    "slurmd_start_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "features" : [ "features", "features" ],
    "hostname" : "hostname",
    "cores" : 6,
    "reason_changed_at" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "reservation" : "reservation",
    "tres" : "tres",
    "cpu_binding" : 5,
    "state" : [ "INVALID", "INVALID" ],
    "sockets" : 9,
    "energy" : {
      "current_watts" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "base_consumed_energy" : 3,
      "last_collected" : 7,
      "consumed_energy" : 2,
      "previous_consumed_energy" : 4,
      "average_watts" : 9
    },
    "partitions" : [ "partitions", "partitions" ],
    "topology" : "topology",
    "gres_drained" : "gres_drained",
    "weight" : 8,
    "version" : "version",
    "gres_used" : "gres_used",
    "mcs_label" : "mcs_label",
    "real_memory" : 1,
    "instance_id" : "instance_id",
    "burstbuffer_network_address" : "burstbuffer_network_address",
    "port" : 1,
    "name" : "name",
    "resume_after" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "temporary_disk" : 6,
    "tres_used" : "tres_used",
    "effective_cpus" : 7,
    "instance_type" : "instance_type",
    "external_sensors" : "{}",
    "cert_flags" : [ "TOKEN_SET", "TOKEN_SET" ],
    "res_cores_per_gpu" : 6,
    "boards" : 0,
    "alloc_cpus" : 1,
    "active_features" : [ "active_features", "active_features" ],
    "reason_set_by_user" : "reason_set_by_user",
    "free_mem" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "alloc_idle_cpus" : 4,
    "extra" : "extra",
    "operating_system" : "operating_system",
    "power" : "{}",
    "tls_cert_last_renewal" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "architecture" : "architecture",
    "owner" : "owner",
    "cluster_name" : "cluster_name",
    "address" : "address",
    "cpus" : 2,
    "tres_weighted" : 5.025004791520295,
    "gres" : "gres",
    "threads" : 9,
    "boot_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "alloc_memory" : 7,
    "specialized_memory" : 1,
    "specialized_cpus" : "specialized_cpus",
    "specialized_cores" : 1,
    "last_busy" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "comment" : "comment",
    "next_state_after_reboot" : [ "INVALID", "INVALID" ],
    "cpu_load" : 5
  } ],
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "last_update" : {
    "number" : 2,
    "set" : true,
    "infinite" : true
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces

This API call produces the following media types according to the Accept request header;
the media type will be conveyed by the Content-Type response header.

* `application/json`

### Responses

#### 200

node information
[v0.0.44\_openapi\_nodes\_resp](#v0.0.44_openapi_nodes_resp)

#### default

node information
[v0.0.44\_openapi\_nodes\_resp](#v0.0.44_openapi_nodes_resp)



---

[Up](#__Methods)

```
get /slurm/v0.0.44/nodes/
```

get node(s) info (slurmV0044GetNodes)

### Query parameters

update\_time (optional)

Query Parameter — Query jobs updated more recently than this time (UNIX timestamp) default: null

flags (optional)

Query Parameter — Query flags default: null

### Return type

[v0.0.44\_openapi\_nodes\_resp](#v0.0.44_openapi_nodes_resp)

### Example data

Content-Type: application/json

```
{
  "nodes" : [ {
    "reason" : "reason",
    "gpu_spec" : "gpu_spec",
    "slurmd_start_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "features" : [ "features", "features" ],
    "hostname" : "hostname",
    "cores" : 6,
    "reason_changed_at" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "reservation" : "reservation",
    "tres" : "tres",
    "cpu_binding" : 5,
    "state" : [ "INVALID", "INVALID" ],
    "sockets" : 9,
    "energy" : {
      "current_watts" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "base_consumed_energy" : 3,
      "last_collected" : 7,
      "consumed_energy" : 2,
      "previous_consumed_energy" : 4,
      "average_watts" : 9
    },
    "partitions" : [ "partitions", "partitions" ],
    "topology" : "topology",
    "gres_drained" : "gres_drained",
    "weight" : 8,
    "version" : "version",
    "gres_used" : "gres_used",
    "mcs_label" : "mcs_label",
    "real_memory" : 1,
    "instance_id" : "instance_id",
    "burstbuffer_network_address" : "burstbuffer_network_address",
    "port" : 1,
    "name" : "name",
    "resume_after" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "temporary_disk" : 6,
    "tres_used" : "tres_used",
    "effective_cpus" : 7,
    "instance_type" : "instance_type",
    "external_sensors" : "{}",
    "cert_flags" : [ "TOKEN_SET", "TOKEN_SET" ],
    "res_cores_per_gpu" : 6,
    "boards" : 0,
    "alloc_cpus" : 1,
    "active_features" : [ "active_features", "active_features" ],
    "reason_set_by_user" : "reason_set_by_user",
    "free_mem" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "alloc_idle_cpus" : 4,
    "extra" : "extra",
    "operating_system" : "operating_system",
    "power" : "{}",
    "tls_cert_last_renewal" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "architecture" : "architecture",
    "owner" : "owner",
    "cluster_name" : "cluster_name",
    "address" : "address",
    "cpus" : 2,
    "tres_weighted" : 5.025004791520295,
    "gres" : "gres",
    "threads" : 9,
    "boot_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "alloc_memory" : 7,
    "specialized_memory" : 1,
    "specialized_cpus" : "specialized_cpus",
    "specialized_cores" : 1,
    "last_busy" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "comment" : "comment",
    "next_state_after_reboot" : [ "INVALID", "INVALID" ],
    "cpu_load" : 5
  }, {
    "reason" : "reason",
    "gpu_spec" : "gpu_spec",
    "slurmd_start_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "features" : [ "features", "features" ],
    "hostname" : "hostname",
    "cores" : 6,
    "reason_changed_at" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "reservation" : "reservation",
    "tres" : "tres",
    "cpu_binding" : 5,
    "state" : [ "INVALID", "INVALID" ],
    "sockets" : 9,
    "energy" : {
      "current_watts" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "base_consumed_energy" : 3,
      "last_collected" : 7,
      "consumed_energy" : 2,
      "previous_consumed_energy" : 4,
      "average_watts" : 9
    },
    "partitions" : [ "partitions", "partitions" ],
    "topology" : "topology",
    "gres_drained" : "gres_drained",
    "weight" : 8,
    "version" : "version",
    "gres_used" : "gres_used",
    "mcs_label" : "mcs_label",
    "real_memory" : 1,
    "instance_id" : "instance_id",
    "burstbuffer_network_address" : "burstbuffer_network_address",
    "port" : 1,
    "name" : "name",
    "resume_after" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "temporary_disk" : 6,
    "tres_used" : "tres_used",
    "effective_cpus" : 7,
    "instance_type" : "instance_type",
    "external_sensors" : "{}",
    "cert_flags" : [ "TOKEN_SET", "TOKEN_SET" ],
    "res_cores_per_gpu" : 6,
    "boards" : 0,
    "alloc_cpus" : 1,
    "active_features" : [ "active_features", "active_features" ],
    "reason_set_by_user" : "reason_set_by_user",
    "free_mem" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "alloc_idle_cpus" : 4,
    "extra" : "extra",
    "operating_system" : "operating_system",
    "power" : "{}",
    "tls_cert_last_renewal" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "architecture" : "architecture",
    "owner" : "owner",
    "cluster_name" : "cluster_name",
    "address" : "address",
    "cpus" : 2,
    "tres_weighted" : 5.025004791520295,
    "gres" : "gres",
    "threads" : 9,
    "boot_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "alloc_memory" : 7,
    "specialized_memory" : 1,
    "specialized_cpus" : "specialized_cpus",
    "specialized_cores" : 1,
    "last_busy" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "comment" : "comment",
    "next_state_after_reboot" : [ "INVALID", "INVALID" ],
    "cpu_load" : 5
  } ],
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "last_update" : {
    "number" : 2,
    "set" : true,
    "infinite" : true
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces

This API call produces the following media types according to the Accept request header;
the media type will be conveyed by the Content-Type response header.

* `application/json`

### Responses

#### 200

node(s) information
[v0.0.44\_openapi\_nodes\_resp](#v0.0.44_openapi_nodes_resp)

#### default

node(s) information
[v0.0.44\_openapi\_nodes\_resp](#v0.0.44_openapi_nodes_resp)



---

[Up](#__Methods)

```
get /slurm/v0.0.44/partition/{partition_name}
```

get partition info (slurmV0044GetPartition)

### Path parameters

partition\_name (required)

Path Parameter — Partition name default: null

### Query parameters

update\_time (optional)

Query Parameter — Query partitions updated more recently than this time (UNIX timestamp) default: null

flags (optional)

Query Parameter — Query flags default: null

### Return type

[v0.0.44\_openapi\_partition\_resp](#v0.0.44_openapi_partition_resp)

### Example data

Content-Type: application/json

```
{
  "partitions" : [ {
    "cluster" : "cluster",
    "cpus" : {
      "task_binding" : 6,
      "total" : 1
    },
    "topology" : "topology",
    "timeouts" : {
      "resume" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "suspend" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      }
    },
    "groups" : {
      "allowed" : "allowed"
    },
    "alternate" : "alternate",
    "select_type" : [ "CPU", "CPU" ],
    "suspend_time" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "priority" : {
      "tier" : 4,
      "job_factor" : 2
    },
    "node_sets" : "node_sets",
    "maximums" : {
      "shares" : 7,
      "nodes" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "over_time_limit" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "cpus_per_node" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "cpus_per_socket" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "partition_memory_per_node" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "oversubscribe" : {
        "jobs" : 9,
        "flags" : [ "force", "force" ]
      },
      "memory_per_cpu" : 2,
      "time" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "partition_memory_per_cpu" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      }
    },
    "nodes" : {
      "configured" : "configured",
      "total" : 0,
      "allowed_allocation" : "allowed_allocation"
    },
    "partition" : {
      "state" : [ "INACTIVE", "INACTIVE" ]
    },
    "qos" : {
      "deny" : "deny",
      "allowed" : "allowed",
      "assigned" : "assigned"
    },
    "defaults" : {
      "partition_memory_per_node" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "memory_per_cpu" : 5,
      "time" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "job" : "job",
      "partition_memory_per_cpu" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      }
    },
    "name" : "name",
    "tres" : {
      "configured" : "configured",
      "billing_weights" : "billing_weights"
    },
    "accounts" : {
      "deny" : "deny",
      "allowed" : "allowed"
    },
    "minimums" : {
      "nodes" : 3
    },
    "grace_time" : 5
  }, {
    "cluster" : "cluster",
    "cpus" : {
      "task_binding" : 6,
      "total" : 1
    },
    "topology" : "topology",
    "timeouts" : {
      "resume" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "suspend" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      }
    },
    "groups" : {
      "allowed" : "allowed"
    },
    "alternate" : "alternate",
    "select_type" : [ "CPU", "CPU" ],
    "suspend_time" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "priority" : {
      "tier" : 4,
      "job_factor" : 2
    },
    "node_sets" : "node_sets",
    "maximums" : {
      "shares" : 7,
      "nodes" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "over_time_limit" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "cpus_per_node" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "cpus_per_socket" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "partition_memory_per_node" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "oversubscribe" : {
        "jobs" : 9,
        "flags" : [ "force", "force" ]
      },
      "memory_per_cpu" : 2,
      "time" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "partition_memory_per_cpu" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      }
    },
    "nodes" : {
      "configured" : "configured",
      "total" : 0,
      "allowed_allocation" : "allowed_allocation"
    },
    "partition" : {
      "state" : [ "INACTIVE", "INACTIVE" ]
    },
    "qos" : {
      "deny" : "deny",
      "allowed" : "allowed",
      "assigned" : "assigned"
    },
    "defaults" : {
      "partition_memory_per_node" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "memory_per_cpu" : 5,
      "time" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "job" : "job",
      "partition_memory_per_cpu" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      }
    },
    "name" : "name",
    "tres" : {
      "configured" : "configured",
      "billing_weights" : "billing_weights"
    },
    "accounts" : {
      "deny" : "deny",
      "allowed" : "allowed"
    },
    "minimums" : {
      "nodes" : 3
    },
    "grace_time" : 5
  } ],
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "last_update" : {
    "number" : 2,
    "set" : true,
    "infinite" : true
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces

This API call produces the following media types according to the Accept request header;
the media type will be conveyed by the Content-Type response header.

* `application/json`

### Responses

#### 200

partition information
[v0.0.44\_openapi\_partition\_resp](#v0.0.44_openapi_partition_resp)

#### default

partition information
[v0.0.44\_openapi\_partition\_resp](#v0.0.44_openapi_partition_resp)



---

[Up](#__Methods)

```
get /slurm/v0.0.44/partitions/
```

get all partition info (slurmV0044GetPartitions)

### Query parameters

update\_time (optional)

Query Parameter — Query partitions updated more recently than this time (UNIX timestamp) default: null

flags (optional)

Query Parameter — Query flags default: null

### Return type

[v0.0.44\_openapi\_partition\_resp](#v0.0.44_openapi_partition_resp)

### Example data

Content-Type: application/json

```
{
  "partitions" : [ {
    "cluster" : "cluster",
    "cpus" : {
      "task_binding" : 6,
      "total" : 1
    },
    "topology" : "topology",
    "timeouts" : {
      "resume" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "suspend" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      }
    },
    "groups" : {
      "allowed" : "allowed"
    },
    "alternate" : "alternate",
    "select_type" : [ "CPU", "CPU" ],
    "suspend_time" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "priority" : {
      "tier" : 4,
      "job_factor" : 2
    },
    "node_sets" : "node_sets",
    "maximums" : {
      "shares" : 7,
      "nodes" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "over_time_limit" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "cpus_per_node" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "cpus_per_socket" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "partition_memory_per_node" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "oversubscribe" : {
        "jobs" : 9,
        "flags" : [ "force", "force" ]
      },
      "memory_per_cpu" : 2,
      "time" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "partition_memory_per_cpu" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      }
    },
    "nodes" : {
      "configured" : "configured",
      "total" : 0,
      "allowed_allocation" : "allowed_allocation"
    },
    "partition" : {
      "state" : [ "INACTIVE", "INACTIVE" ]
    },
    "qos" : {
      "deny" : "deny",
      "allowed" : "allowed",
      "assigned" : "assigned"
    },
    "defaults" : {
      "partition_memory_per_node" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "memory_per_cpu" : 5,
      "time" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "job" : "job",
      "partition_memory_per_cpu" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      }
    },
    "name" : "name",
    "tres" : {
      "configured" : "configured",
      "billing_weights" : "billing_weights"
    },
    "accounts" : {
      "deny" : "deny",
      "allowed" : "allowed"
    },
    "minimums" : {
      "nodes" : 3
    },
    "grace_time" : 5
  }, {
    "cluster" : "cluster",
    "cpus" : {
      "task_binding" : 6,
      "total" : 1
    },
    "topology" : "topology",
    "timeouts" : {
      "resume" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "suspend" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      }
    },
    "groups" : {
      "allowed" : "allowed"
    },
    "alternate" : "alternate",
    "select_type" : [ "CPU", "CPU" ],
    "suspend_time" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "priority" : {
      "tier" : 4,
      "job_factor" : 2
    },
    "node_sets" : "node_sets",
    "maximums" : {
      "shares" : 7,
      "nodes" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "over_time_limit" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "cpus_per_node" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "cpus_per_socket" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "partition_memory_per_node" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "oversubscribe" : {
        "jobs" : 9,
        "flags" : [ "force", "force" ]
      },
      "memory_per_cpu" : 2,
      "time" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "partition_memory_per_cpu" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      }
    },
    "nodes" : {
      "configured" : "configured",
      "total" : 0,
      "allowed_allocation" : "allowed_allocation"
    },
    "partition" : {
      "state" : [ "INACTIVE", "INACTIVE" ]
    },
    "qos" : {
      "deny" : "deny",
      "allowed" : "allowed",
      "assigned" : "assigned"
    },
    "defaults" : {
      "partition_memory_per_node" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "memory_per_cpu" : 5,
      "time" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "job" : "job",
      "partition_memory_per_cpu" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      }
    },
    "name" : "name",
    "tres" : {
      "configured" : "configured",
      "billing_weights" : "billing_weights"
    },
    "accounts" : {
      "deny" : "deny",
      "allowed" : "allowed"
    },
    "minimums" : {
      "nodes" : 3
    },
    "grace_time" : 5
  } ],
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "last_update" : {
    "number" : 2,
    "set" : true,
    "infinite" : true
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces

This API call produces the following media types according to the Accept request header;
the media type will be conveyed by the Content-Type response header.

* `application/json`

### Responses

#### 200

partition information
[v0.0.44\_openapi\_partition\_resp](#v0.0.44_openapi_partition_resp)

#### default

partition information
[v0.0.44\_openapi\_partition\_resp](#v0.0.44_openapi_partition_resp)



---

[Up](#__Methods)

```
get /slurm/v0.0.44/ping/
```

ping test (slurmV0044GetPing)

### Return type

[v0.0.44\_openapi\_ping\_array\_resp](#v0.0.44_openapi_ping_array_resp)

### Example data

Content-Type: application/json

```
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "pings" : [ {
    "mode" : "mode",
    "responding" : true,
    "hostname" : "hostname",
    "latency" : 0,
    "pinged" : "pinged",
    "primary" : true
  }, {
    "mode" : "mode",
    "responding" : true,
    "hostname" : "hostname",
    "latency" : 0,
    "pinged" : "pinged",
    "primary" : true
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces

This API call produces the following media types according to the Accept request header;
the media type will be conveyed by the Content-Type response header.

* `application/json`

### Responses

#### 200

results of ping test
[v0.0.44\_openapi\_ping\_array\_resp](#v0.0.44_openapi_ping_array_resp)

#### default

results of ping test
[v0.0.44\_openapi\_ping\_array\_resp](#v0.0.44_openapi_ping_array_resp)



---

[Up](#__Methods)

```
get /slurm/v0.0.44/reconfigure/
```

request slurmctld reconfigure (slurmV0044GetReconfigure)

### Return type

[v0.0.44\_openapi\_resp](#v0.0.44_openapi_resp)

### Example data

Content-Type: application/json

```
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces

This API call produces the following media types according to the Accept request header;
the media type will be conveyed by the Content-Type response header.

* `application/json`

### Responses

#### 200

reconfigure request result
[v0.0.44\_openapi\_resp](#v0.0.44_openapi_resp)

#### default

reconfigure request result
[v0.0.44\_openapi\_resp](#v0.0.44_openapi_resp)



---

[Up](#__Methods)

```
get /slurm/v0.0.44/reservation/{reservation_name}
```

get reservation info (slurmV0044GetReservation)

### Path parameters

reservation\_name (required)

Path Parameter — Reservation name default: null

### Query parameters

update\_time (optional)

Query Parameter — Query reservations updated more recently than this time (UNIX timestamp) default: null

### Return type

[v0.0.44\_openapi\_reservation\_resp](#v0.0.44_openapi_reservation_resp)

### Example data

Content-Type: application/json

```
{
  "reservations" : [ {
    "end_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "flags" : [ "MAINT", "MAINT" ],
    "groups" : "groups",
    "users" : "users",
    "max_start_delay" : 6,
    "features" : "features",
    "start_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "burst_buffer" : "burst_buffer",
    "licenses" : "licenses",
    "partition" : "partition",
    "watts" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "core_specializations" : [ {
      "node" : "node",
      "core" : "core"
    }, {
      "node" : "node",
      "core" : "core"
    } ],
    "name" : "name",
    "tres" : "tres",
    "accounts" : "accounts",
    "node_count" : 1,
    "node_list" : "node_list",
    "purge_completed" : {
      "time" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      }
    },
    "core_count" : 0
  }, {
    "end_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "flags" : [ "MAINT", "MAINT" ],
    "groups" : "groups",
    "users" : "users",
    "max_start_delay" : 6,
    "features" : "features",
    "start_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "burst_buffer" : "burst_buffer",
    "licenses" : "licenses",
    "partition" : "partition",
    "watts" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "core_specializations" : [ {
      "node" : "node",
      "core" : "core"
    }, {
      "node" : "node",
      "core" : "core"
    } ],
    "name" : "name",
    "tres" : "tres",
    "accounts" : "accounts",
    "node_count" : 1,
    "node_list" : "node_list",
    "purge_completed" : {
      "time" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      }
    },
    "core_count" : 0
  } ],
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "last_update" : {
    "number" : 2,
    "set" : true,
    "infinite" : true
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces

This API call produces the following media types according to the Accept request header;
the media type will be conveyed by the Content-Type response header.

* `application/json`

### Responses

#### 200

reservation information
[v0.0.44\_openapi\_reservation\_resp](#v0.0.44_openapi_reservation_resp)

#### default

reservation information
[v0.0.44\_openapi\_reservation\_resp](#v0.0.44_openapi_reservation_resp)



---

[Up](#__Methods)

```
get /slurm/v0.0.44/reservations/
```

get all reservation info (slurmV0044GetReservations)

### Query parameters

update\_time (optional)

Query Parameter — Query reservations updated more recently than this time (UNIX timestamp) default: null

### Return type

[v0.0.44\_openapi\_reservation\_resp](#v0.0.44_openapi_reservation_resp)

### Example data

Content-Type: application/json

```
{
  "reservations" : [ {
    "end_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "flags" : [ "MAINT", "MAINT" ],
    "groups" : "groups",
    "users" : "users",
    "max_start_delay" : 6,
    "features" : "features",
    "start_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "burst_buffer" : "burst_buffer",
    "licenses" : "licenses",
    "partition" : "partition",
    "watts" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "core_specializations" : [ {
      "node" : "node",
      "core" : "core"
    }, {
      "node" : "node",
      "core" : "core"
    } ],
    "name" : "name",
    "tres" : "tres",
    "accounts" : "accounts",
    "node_count" : 1,
    "node_list" : "node_list",
    "purge_completed" : {
      "time" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      }
    },
    "core_count" : 0
  }, {
    "end_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "flags" : [ "MAINT", "MAINT" ],
    "groups" : "groups",
    "users" : "users",
    "max_start_delay" : 6,
    "features" : "features",
    "start_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "burst_buffer" : "burst_buffer",
    "licenses" : "licenses",
    "partition" : "partition",
    "watts" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "core_specializations" : [ {
      "node" : "node",
      "core" : "core"
    }, {
      "node" : "node",
      "core" : "core"
    } ],
    "name" : "name",
    "tres" : "tres",
    "accounts" : "accounts",
    "node_count" : 1,
    "node_list" : "node_list",
    "purge_completed" : {
      "time" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      }
    },
    "core_count" : 0
  } ],
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "last_update" : {
    "number" : 2,
    "set" : true,
    "infinite" : true
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces

This API call produces the following media types according to the Accept request header;
the media type will be conveyed by the Content-Type response header.

* `application/json`

### Responses

#### 200

reservation information
[v0.0.44\_openapi\_reservation\_resp](#v0.0.44_openapi_reservation_resp)

#### default

reservation information
[v0.0.44\_openapi\_reservation\_resp](#v0.0.44_openapi_reservation_resp)



---

[Up](#__Methods)

```
get /slurm/v0.0.44/resources/{job_id}
```

get resource layout info (slurmV0044GetResources)

### Path parameters

job\_id (required)

Path Parameter — Job ID default: null

### Return type

[v0.0.44\_openapi\_resource\_layout\_resp](#v0.0.44_openapi_resource_layout_resp)

### Example data

Content-Type: application/json

```
{
  "nodes" : [ {
    "node" : "node",
    "channel" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "gres" : [ {
      "name" : "name",
      "count" : 5,
      "index" : "index",
      "type" : "type"
    }, {
      "name" : "name",
      "count" : 5,
      "index" : "index",
      "type" : "type"
    } ],
    "cores_per_socket" : 6,
    "mem_alloc" : 1,
    "core_bitmap" : "core_bitmap",
    "sockets_per_node" : 0
  }, {
    "node" : "node",
    "channel" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "gres" : [ {
      "name" : "name",
      "count" : 5,
      "index" : "index",
      "type" : "type"
    }, {
      "name" : "name",
      "count" : 5,
      "index" : "index",
      "type" : "type"
    } ],
    "cores_per_socket" : 6,
    "mem_alloc" : 1,
    "core_bitmap" : "core_bitmap",
    "sockets_per_node" : 0
  } ],
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces

This API call produces the following media types according to the Accept request header;
the media type will be conveyed by the Content-Type response header.

* `application/json`

### Responses

#### 200

resource layout information
[v0.0.44\_openapi\_resource\_layout\_resp](#v0.0.44_openapi_resource_layout_resp)

#### default

resource layout information
[v0.0.44\_openapi\_resource\_layout\_resp](#v0.0.44_openapi_resource_layout_resp)



---

[Up](#__Methods)

```
get /slurm/v0.0.44/shares
```

get fairshare info (slurmV0044GetShares)

### Query parameters

accounts (optional)

Query Parameter — Accounts to query default: null

users (optional)

Query Parameter — Users to query default: null

### Return type

[v0.0.44\_openapi\_shares\_resp](#v0.0.44_openapi_shares_resp)

### Example data

Content-Type: application/json

```
{
  "shares" : {
    "shares" : [ {
      "cluster" : "cluster",
      "parent" : "parent",
      "shares_normalized" : {
        "number" : 4.145608029883936,
        "set" : true,
        "infinite" : true
      },
      "usage" : 1,
      "fairshare" : {
        "level" : {
          "number" : 4.145608029883936,
          "set" : true,
          "infinite" : true
        },
        "factor" : {
          "number" : 4.145608029883936,
          "set" : true,
          "infinite" : true
        }
      },
      "type" : [ "USER", "USER" ],
      "effective_usage" : {
        "number" : 4.145608029883936,
        "set" : true,
        "infinite" : true
      },
      "shares" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "partition" : "partition",
      "usage_normalized" : {
        "number" : 4.145608029883936,
        "set" : true,
        "infinite" : true
      },
      "name" : "name",
      "tres" : {
        "run_seconds" : [ {
          "name" : "name",
          "value" : {
            "number" : 2,
            "set" : true,
            "infinite" : true
          }
        }, {
          "name" : "name",
          "value" : {
            "number" : 2,
            "set" : true,
            "infinite" : true
          }
        } ],
        "usage" : [ {
          "name" : "name",
          "value" : 6.027456183070403
        }, {
          "name" : "name",
          "value" : 6.027456183070403
        } ],
        "group_minutes" : [ {
          "name" : "name",
          "value" : {
            "number" : 2,
            "set" : true,
            "infinite" : true
          }
        }, {
          "name" : "name",
          "value" : {
            "number" : 2,
            "set" : true,
            "infinite" : true
          }
        } ]
      },
      "id" : 0
    }, {
      "cluster" : "cluster",
      "parent" : "parent",
      "shares_normalized" : {
        "number" : 4.145608029883936,
        "set" : true,
        "infinite" : true
      },
      "usage" : 1,
      "fairshare" : {
        "level" : {
          "number" : 4.145608029883936,
          "set" : true,
          "infinite" : true
        },
        "factor" : {
          "number" : 4.145608029883936,
          "set" : true,
          "infinite" : true
        }
      },
      "type" : [ "USER", "USER" ],
      "effective_usage" : {
        "number" : 4.145608029883936,
        "set" : true,
        "infinite" : true
      },
      "shares" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "partition" : "partition",
      "usage_normalized" : {
        "number" : 4.145608029883936,
        "set" : true,
        "infinite" : true
      },
      "name" : "name",
      "tres" : {
        "run_seconds" : [ {
          "name" : "name",
          "value" : {
            "number" : 2,
            "set" : true,
            "infinite" : true
          }
        }, {
          "name" : "name",
          "value" : {
            "number" : 2,
            "set" : true,
            "infinite" : true
          }
        } ],
        "usage" : [ {
          "name" : "name",
          "value" : 6.027456183070403
        }, {
          "name" : "name",
          "value" : 6.027456183070403
        } ],
        "group_minutes" : [ {
          "name" : "name",
          "value" : {
            "number" : 2,
            "set" : true,
            "infinite" : true
          }
        }, {
          "name" : "name",
          "value" : {
            "number" : 2,
            "set" : true,
            "infinite" : true
          }
        } ]
      },
      "id" : 0
    } ],
    "total_shares" : 5
  },
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces

This API call produces the following media types according to the Accept request header;
the media type will be conveyed by the Content-Type response header.

* `application/json`

### Responses

#### 200

shares information
[v0.0.44\_openapi\_shares\_resp](#v0.0.44_openapi_shares_resp)

#### default

shares information
[v0.0.44\_openapi\_shares\_resp](#v0.0.44_openapi_shares_resp)



---

[Up](#__Methods)

```
post /slurm/v0.0.44/job/{job_id}
```

update job (slurmV0044PostJob)

### Path parameters

job\_id (required)

Path Parameter — Job ID default: null

### Consumes

This API call consumes the following media types via the Content-Type request header:

* `application/json`

### Request body

v0.0.44\_job\_desc\_msg [v0.0.44\_job\_desc\_msg](#v0.0.44_job_desc_msg) (optional)

Body Parameter —

### Return type

[v0.0.44\_openapi\_job\_post\_response](#v0.0.44_openapi_job_post_response)

### Example data

Content-Type: application/json

```
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "results" : [ {
    "job_id" : 0,
    "why" : "why",
    "error_code" : 6,
    "step_id" : "step_id",
    "error" : "error"
  }, {
    "job_id" : 0,
    "why" : "why",
    "error_code" : 6,
    "step_id" : "step_id",
    "error" : "error"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces

This API call produces the following media types according to the Accept request header;
the media type will be conveyed by the Content-Type response header.

* `application/json`

### Responses

#### 200

job update result
[v0.0.44\_openapi\_job\_post\_response](#v0.0.44_openapi_job_post_response)

#### default

job update result
[v0.0.44\_openapi\_job\_post\_response](#v0.0.44_openapi_job_post_response)



---

[Up](#__Methods)

```
post /slurm/v0.0.44/job/allocate
```

submit new job allocation without any steps that must be signaled to stop (slurmV0044PostJobAllocate)

### Consumes

This API call consumes the following media types via the Content-Type request header:

* `application/json`

### Request body

v0.0.44\_job\_alloc\_req [v0.0.44\_job\_alloc\_req](#v0.0.44_job_alloc_req) (optional)

Body Parameter —

### Return type

[v0.0.44\_openapi\_job\_alloc\_resp](#v0.0.44_openapi_job_alloc_resp)

### Example data

Content-Type: application/json

```
{
  "job_id" : 0,
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "job_submit_user_msg" : "job_submit_user_msg",
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces

This API call produces the following media types according to the Accept request header;
the media type will be conveyed by the Content-Type response header.

* `application/json`

### Responses

#### 200

job allocation response
[v0.0.44\_openapi\_job\_alloc\_resp](#v0.0.44_openapi_job_alloc_resp)

#### default

job allocation response
[v0.0.44\_openapi\_job\_alloc\_resp](#v0.0.44_openapi_job_alloc_resp)



---

[Up](#__Methods)

```
post /slurm/v0.0.44/job/submit
```

submit new job (slurmV0044PostJobSubmit)

### Consumes

This API call consumes the following media types via the Content-Type request header:

* `application/json`

### Request body

v0.0.44\_job\_submit\_req [v0.0.44\_job\_submit\_req](#v0.0.44_job_submit_req) (optional)

Body Parameter —

### Return type

[v0.0.44\_openapi\_job\_submit\_response](#v0.0.44_openapi_job_submit_response)

### Example data

Content-Type: application/json

```
{
  "job_id" : 0,
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "step_id" : "step_id",
  "job_submit_user_msg" : "job_submit_user_msg",
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces

This API call produces the following media types according to the Accept request header;
the media type will be conveyed by the Content-Type response header.

* `application/json`

### Responses

#### 200

job submission response
[v0.0.44\_openapi\_job\_submit\_response](#v0.0.44_openapi_job_submit_response)

#### default

job submission response
[v0.0.44\_openapi\_job\_submit\_response](#v0.0.44_openapi_job_submit_response)



---

[Up](#__Methods)

```
post /slurm/v0.0.44/new/node/
```

create node (slurmV0044PostNewNode)

### Consumes

This API call consumes the following media types via the Content-Type request header:

* `application/json`

### Request body

v0.0.44\_openapi\_create\_node\_req [v0.0.44\_openapi\_create\_node\_req](#v0.0.44_openapi_create_node_req) (optional)

Body Parameter —

### Return type

[v0.0.44\_openapi\_resp](#v0.0.44_openapi_resp)

### Example data

Content-Type: application/json

```
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces

This API call produces the following media types according to the Accept request header;
the media type will be conveyed by the Content-Type response header.

* `application/json`

### Responses

#### 200

node create request result
[v0.0.44\_openapi\_resp](#v0.0.44_openapi_resp)

#### default

node create request result
[v0.0.44\_openapi\_resp](#v0.0.44_openapi_resp)



---

[Up](#__Methods)

```
post /slurm/v0.0.44/node/{node_name}
```

update node properties (slurmV0044PostNode)

### Path parameters

node\_name (required)

Path Parameter — Node name default: null

### Consumes

This API call consumes the following media types via the Content-Type request header:

* `application/json`

### Request body

v0.0.44\_update\_node\_msg [v0.0.44\_update\_node\_msg](#v0.0.44_update_node_msg) (optional)

Body Parameter —

### Return type

[v0.0.44\_openapi\_resp](#v0.0.44_openapi_resp)

### Example data

Content-Type: application/json

```
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces

This API call produces the following media types according to the Accept request header;
the media type will be conveyed by the Content-Type response header.

* `application/json`

### Responses

#### 200

node update request result
[v0.0.44\_openapi\_resp](#v0.0.44_openapi_resp)

#### default

node update request result
[v0.0.44\_openapi\_resp](#v0.0.44_openapi_resp)



---

[Up](#__Methods)

```
post /slurm/v0.0.44/nodes/
```

batch update node(s) (slurmV0044PostNodes)

### Consumes

This API call consumes the following media types via the Content-Type request header:

* `application/json`

### Request body

v0.0.44\_update\_node\_msg [v0.0.44\_update\_node\_msg](#v0.0.44_update_node_msg) (optional)

Body Parameter —

### Return type

[v0.0.44\_openapi\_resp](#v0.0.44_openapi_resp)

### Example data

Content-Type: application/json

```
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces

This API call produces the following media types according to the Accept request header;
the media type will be conveyed by the Content-Type response header.

* `application/json`

### Responses

#### 200

batch node update request result
[v0.0.44\_openapi\_resp](#v0.0.44_openapi_resp)

#### default

batch node update request result
[v0.0.44\_openapi\_resp](#v0.0.44_openapi_resp)



---

[Up](#__Methods)

```
post /slurm/v0.0.44/reservation
```

create or update a reservation (slurmV0044PostReservation)

### Consumes

This API call consumes the following media types via the Content-Type request header:

* `application/json`

### Request body

v0.0.44\_reservation\_desc\_msg [v0.0.44\_reservation\_desc\_msg](#v0.0.44_reservation_desc_msg) (optional)

Body Parameter —

### Return type

[v0.0.44\_openapi\_reservation\_mod\_resp](#v0.0.44_openapi_reservation_mod_resp)

### Example data

Content-Type: application/json

```
{
  "reservations" : [ {
    "end_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "flags" : [ "MAINT", "MAINT" ],
    "groups" : [ "groups", "groups" ],
    "users" : [ "users", "users" ],
    "max_start_delay" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "duration" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "features" : "features",
    "start_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "burst_buffer" : "burst_buffer",
    "licenses" : [ "licenses", "licenses" ],
    "partition" : "partition",
    "name" : "name",
    "comment" : "comment",
    "tres" : [ {
      "name" : "name",
      "count" : 0,
      "id" : 7,
      "type" : "type"
    }, {
      "name" : "name",
      "count" : 0,
      "id" : 7,
      "type" : "type"
    } ],
    "accounts" : [ "accounts", "accounts" ],
    "node_count" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "node_list" : [ "node_list", "node_list" ],
    "purge_completed" : {
      "time" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      }
    },
    "core_count" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    }
  }, {
    "end_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "flags" : [ "MAINT", "MAINT" ],
    "groups" : [ "groups", "groups" ],
    "users" : [ "users", "users" ],
    "max_start_delay" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "duration" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "features" : "features",
    "start_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "burst_buffer" : "burst_buffer",
    "licenses" : [ "licenses", "licenses" ],
    "partition" : "partition",
    "name" : "name",
    "comment" : "comment",
    "tres" : [ {
      "name" : "name",
      "count" : 0,
      "id" : 7,
      "type" : "type"
    }, {
      "name" : "name",
      "count" : 0,
      "id" : 7,
      "type" : "type"
    } ],
    "accounts" : [ "accounts", "accounts" ],
    "node_count" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "node_list" : [ "node_list", "node_list" ],
    "purge_completed" : {
      "time" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      }
    },
    "core_count" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    }
  } ],
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces

This API call produces the following media types according to the Accept request header;
the media type will be conveyed by the Content-Type response header.

* `application/json`

### Responses

#### 200

reservation description
[v0.0.44\_openapi\_reservation\_mod\_resp](#v0.0.44_openapi_reservation_mod_resp)

#### default

reservation description
[v0.0.44\_openapi\_reservation\_mod\_resp](#v0.0.44_openapi_reservation_mod_resp)



---

[Up](#__Methods)

```
post /slurm/v0.0.44/reservations/
```

create or update reservations (slurmV0044PostReservations)

### Consumes

This API call consumes the following media types via the Content-Type request header:

* `application/json`

### Request body

v0.0.44\_reservation\_mod\_req [v0.0.44\_reservation\_mod\_req](#v0.0.44_reservation_mod_req) (optional)

Body Parameter —

### Return type

[v0.0.44\_openapi\_reservation\_mod\_resp](#v0.0.44_openapi_reservation_mod_resp)

### Example data

Content-Type: application/json

```
{
  "reservations" : [ {
    "end_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "flags" : [ "MAINT", "MAINT" ],
    "groups" : [ "groups", "groups" ],
    "users" : [ "users", "users" ],
    "max_start_delay" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "duration" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "features" : "features",
    "start_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "burst_buffer" : "burst_buffer",
    "licenses" : [ "licenses", "licenses" ],
    "partition" : "partition",
    "name" : "name",
    "comment" : "comment",
    "tres" : [ {
      "name" : "name",
      "count" : 0,
      "id" : 7,
      "type" : "type"
    }, {
      "name" : "name",
      "count" : 0,
      "id" : 7,
      "type" : "type"
    } ],
    "accounts" : [ "accounts", "accounts" ],
    "node_count" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "node_list" : [ "node_list", "node_list" ],
    "purge_completed" : {
      "time" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      }
    },
    "core_count" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    }
  }, {
    "end_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "flags" : [ "MAINT", "MAINT" ],
    "groups" : [ "groups", "groups" ],
    "users" : [ "users", "users" ],
    "max_start_delay" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "duration" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "features" : "features",
    "start_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "burst_buffer" : "burst_buffer",
    "licenses" : [ "licenses", "licenses" ],
    "partition" : "partition",
    "name" : "name",
    "comment" : "comment",
    "tres" : [ {
      "name" : "name",
      "count" : 0,
      "id" : 7,
      "type" : "type"
    }, {
      "name" : "name",
      "count" : 0,
      "id" : 7,
      "type" : "type"
    } ],
    "accounts" : [ "accounts", "accounts" ],
    "node_count" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "node_list" : [ "node_list", "node_list" ],
    "purge_completed" : {
      "time" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      }
    },
    "core_count" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    }
  } ],
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces

This API call produces the following media types according to the Accept request header;
the media type will be conveyed by the Content-Type response header.

* `application/json`

### Responses

#### 200

reservation descriptions
[v0.0.44\_openapi\_reservation\_mod\_resp](#v0.0.44_openapi_reservation_mod_resp)

#### default

reservation descriptions
[v0.0.44\_openapi\_reservation\_mod\_resp](#v0.0.44_openapi_reservation_mod_resp)



---

# Slurmdb

[Up](#__Methods)

```
delete /slurmdb/v0.0.44/account/{account_name}
```

Delete account (slurmdbV0044DeleteAccount)

### Path parameters

account\_name (required)

Path Parameter — Account name default: null

### Return type

[v0.0.44\_openapi\_accounts\_removed\_resp](#v0.0.44_openapi_accounts_removed_resp)

### Example data

Content-Type: application/json

```
{
  "removed_accounts" : [ "removed_accounts", "removed_accounts" ],
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces

This API call produces the following media types according to the Accept request header;
the media type will be conveyed by the Content-Type response header.

* `application/json`

### Responses

#### 200

Status of account deletion request
[v0.0.44\_openapi\_accounts\_removed\_resp](#v0.0.44_openapi_accounts_removed_resp)

#### default

Status of account deletion request
[v0.0.44\_openapi\_accounts\_removed\_resp](#v0.0.44_openapi_accounts_removed_resp)



---

[Up](#__Methods)

```
delete /slurmdb/v0.0.44/association/
```

Delete association (slurmdbV0044DeleteAssociation)

### Query parameters

account (optional)

Query Parameter — CSV accounts list default: null

cluster (optional)

Query Parameter — CSV clusters list default: null

default\_qos (optional)

Query Parameter — CSV QOS list default: null

Include deleted associations (optional)

Query Parameter — default: null

Include usage (optional)

Query Parameter — default: null

Filter to only defaults (optional)

Query Parameter — default: null

Include the raw QOS or delta\_qos (optional)

Query Parameter — default: null

Include sub acct information (optional)

Query Parameter — default: null

Exclude parent id/name (optional)

Query Parameter — default: null

Exclude limits from parents (optional)

Query Parameter — default: null

format (optional)

Query Parameter — Ignored; process JSON manually to control output format default: null

id (optional)

Query Parameter — CSV ID list default: null

parent\_account (optional)

Query Parameter — CSV names of parent account default: null

partition (optional)

Query Parameter — CSV partition name list default: null

qos (optional)

Query Parameter — CSV QOS list default: null

usage\_end (optional)

Query Parameter — Usage end (UNIX timestamp) default: null

usage\_start (optional)

Query Parameter — Usage start (UNIX timestamp) default: null

user (optional)

Query Parameter — CSV user list default: null

### Return type

[v0.0.44\_openapi\_assocs\_removed\_resp](#v0.0.44_openapi_assocs_removed_resp)

### Example data

Content-Type: application/json

```
{
  "removed_associations" : [ "removed_associations", "removed_associations" ],
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces

This API call produces the following media types according to the Accept request header;
the media type will be conveyed by the Content-Type response header.

* `application/json`

### Responses

#### 200

Status of associations delete request
[v0.0.44\_openapi\_assocs\_removed\_resp](#v0.0.44_openapi_assocs_removed_resp)

#### default

Status of associations delete request
[v0.0.44\_openapi\_assocs\_removed\_resp](#v0.0.44_openapi_assocs_removed_resp)



---

[Up](#__Methods)

```
delete /slurmdb/v0.0.44/associations/
```

Delete associations (slurmdbV0044DeleteAssociations)

### Query parameters

account (optional)

Query Parameter — CSV accounts list default: null

cluster (optional)

Query Parameter — CSV clusters list default: null

default\_qos (optional)

Query Parameter — CSV QOS list default: null

Include deleted associations (optional)

Query Parameter — default: null

Include usage (optional)

Query Parameter — default: null

Filter to only defaults (optional)

Query Parameter — default: null

Include the raw QOS or delta\_qos (optional)

Query Parameter — default: null

Include sub acct information (optional)

Query Parameter — default: null

Exclude parent id/name (optional)

Query Parameter — default: null

Exclude limits from parents (optional)

Query Parameter — default: null

format (optional)

Query Parameter — Ignored; process JSON manually to control output format default: null

id (optional)

Query Parameter — CSV ID list default: null

parent\_account (optional)

Query Parameter — CSV names of parent account default: null

partition (optional)

Query Parameter — CSV partition name list default: null

qos (optional)

Query Parameter — CSV QOS list default: null

usage\_end (optional)

Query Parameter — Usage end (UNIX timestamp) default: null

usage\_start (optional)

Query Parameter — Usage start (UNIX timestamp) default: null

user (optional)

Query Parameter — CSV user list default: null

### Return type

[v0.0.44\_openapi\_assocs\_removed\_resp](#v0.0.44_openapi_assocs_removed_resp)

### Example data

Content-Type: application/json

```
{
  "removed_associations" : [ "removed_associations", "removed_associations" ],
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces

This API call produces the following media types according to the Accept request header;
the media type will be conveyed by the Content-Type response header.

* `application/json`

### Responses

#### 200

List of associations deleted
[v0.0.44\_openapi\_assocs\_removed\_resp](#v0.0.44_openapi_assocs_removed_resp)

#### default

List of associations deleted
[v0.0.44\_openapi\_assocs\_removed\_resp](#v0.0.44_openapi_assocs_removed_resp)



---

[Up](#__Methods)

```
delete /slurmdb/v0.0.44/cluster/{cluster_name}
```

Delete cluster (slurmdbV0044DeleteCluster)

### Path parameters

cluster\_name (required)

Path Parameter — Cluster name default: null

### Query parameters

classification (optional)

Query Parameter — Type of machine default: null

cluster (optional)

Query Parameter — CSV cluster list default: null

federation (optional)

Query Parameter — CSV federation list default: null

flags (optional)

Query Parameter — Query flags default: null

format (optional)

Query Parameter — Ignored; process JSON manually to control output format default: null

rpc\_version (optional)

Query Parameter — CSV RPC version list default: null

usage\_end (optional)

Query Parameter — Usage end (UNIX timestamp) default: null

usage\_start (optional)

Query Parameter — Usage start (UNIX timestamp) default: null

with\_deleted (optional)

Query Parameter — Include deleted clusters default: null

with\_usage (optional)

Query Parameter — Include usage default: null

### Return type

[v0.0.44\_openapi\_clusters\_removed\_resp](#v0.0.44_openapi_clusters_removed_resp)

### Example data

Content-Type: application/json

```
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "deleted_clusters" : [ "deleted_clusters", "deleted_clusters" ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces

This API call produces the following media types according to the Accept request header;
the media type will be conveyed by the Content-Type response header.

* `application/json`

### Responses

#### 200

Result of delete cluster request
[v0.0.44\_openapi\_clusters\_removed\_resp](#v0.0.44_openapi_clusters_removed_resp)

#### default

Result of delete cluster request
[v0.0.44\_openapi\_clusters\_removed\_resp](#v0.0.44_openapi_clusters_removed_resp)



---

[Up](#__Methods)

```
delete /slurmdb/v0.0.44/qos/{qos}
```

Delete QOS (slurmdbV0044DeleteSingleQos)

### Path parameters

qos (required)

Path Parameter — QOS name default: null

### Return type

[v0.0.44\_openapi\_slurmdbd\_qos\_removed\_resp](#v0.0.44_openapi_slurmdbd_qos_removed_resp)

### Example data

Content-Type: application/json

```
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "removed_qos" : [ "removed_qos", "removed_qos" ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces

This API call produces the following media types according to the Accept request header;
the media type will be conveyed by the Content-Type response header.

* `application/json`

### Responses

#### 200

results of ping test
[v0.0.44\_openapi\_slurmdbd\_qos\_removed\_resp](#v0.0.44_openapi_slurmdbd_qos_removed_resp)

#### default

results of ping test
[v0.0.44\_openapi\_slurmdbd\_qos\_removed\_resp](#v0.0.44_openapi_slurmdbd_qos_removed_resp)



---

[Up](#__Methods)

```
delete /slurmdb/v0.0.44/user/{name}
```

Delete user (slurmdbV0044DeleteUser)

### Path parameters

name (required)

Path Parameter — User name default: null

### Return type

[v0.0.44\_openapi\_resp](#v0.0.44_openapi_resp)

### Example data

Content-Type: application/json

```
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces

This API call produces the following media types according to the Accept request header;
the media type will be conveyed by the Content-Type response header.

* `application/json`

### Responses

#### 200

Result of user delete request
[v0.0.44\_openapi\_resp](#v0.0.44_openapi_resp)

#### default

Result of user delete request
[v0.0.44\_openapi\_resp](#v0.0.44_openapi_resp)



---

[Up](#__Methods)

```
delete /slurmdb/v0.0.44/wckey/{id}
```

Delete wckey (slurmdbV0044DeleteWckey)

### Path parameters

id (required)

Path Parameter — WCKey ID default: null

### Return type

[v0.0.44\_openapi\_wckey\_removed\_resp](#v0.0.44_openapi_wckey_removed_resp)

### Example data

Content-Type: application/json

```
{
  "deleted_wckeys" : [ "deleted_wckeys", "deleted_wckeys" ],
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces

This API call produces the following media types according to the Accept request header;
the media type will be conveyed by the Content-Type response header.

* `application/json`

### Responses

#### 200

Result of wckey deletion request
[v0.0.44\_openapi\_wckey\_removed\_resp](#v0.0.44_openapi_wckey_removed_resp)

#### default

Result of wckey deletion request
[v0.0.44\_openapi\_wckey\_removed\_resp](#v0.0.44_openapi_wckey_removed_resp)



---

[Up](#__Methods)

```
get /slurmdb/v0.0.44/account/{account_name}
```

Get account info (slurmdbV0044GetAccount)

### Path parameters

account\_name (required)

Path Parameter — Account name default: null

### Query parameters

with\_assocs (optional)

Query Parameter — Include associations default: null

with\_coords (optional)

Query Parameter — Include coordinators default: null

with\_deleted (optional)

Query Parameter — Include deleted default: null

### Return type

[v0.0.44\_openapi\_accounts\_resp](#v0.0.44_openapi_accounts_resp)

### Example data

Content-Type: application/json

```
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "accounts" : [ {
    "associations" : [ {
      "cluster" : "cluster",
      "partition" : "partition",
      "id" : 5,
      "user" : "user",
      "account" : "account"
    }, {
      "cluster" : "cluster",
      "partition" : "partition",
      "id" : 5,
      "user" : "user",
      "account" : "account"
    } ],
    "coordinators" : [ {
      "name" : "name",
      "direct" : true
    }, {
      "name" : "name",
      "direct" : true
    } ],
    "organization" : "organization",
    "name" : "name",
    "flags" : [ "DELETED", "DELETED" ],
    "description" : "description"
  }, {
    "associations" : [ {
      "cluster" : "cluster",
      "partition" : "partition",
      "id" : 5,
      "user" : "user",
      "account" : "account"
    }, {
      "cluster" : "cluster",
      "partition" : "partition",
      "id" : 5,
      "user" : "user",
      "account" : "account"
    } ],
    "coordinators" : [ {
      "name" : "name",
      "direct" : true
    }, {
      "name" : "name",
      "direct" : true
    } ],
    "organization" : "organization",
    "name" : "name",
    "flags" : [ "DELETED", "DELETED" ],
    "description" : "description"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces

This API call produces the following media types according to the Accept request header;
the media type will be conveyed by the Content-Type response header.

* `application/json`

### Responses

#### 200

List of accounts
[v0.0.44\_openapi\_accounts\_resp](#v0.0.44_openapi_accounts_resp)

#### default

List of accounts
[v0.0.44\_openapi\_accounts\_resp](#v0.0.44_openapi_accounts_resp)



---

[Up](#__Methods)

```
get /slurmdb/v0.0.44/accounts/
```

Get account list (slurmdbV0044GetAccounts)

### Query parameters

description (optional)

Query Parameter — CSV description list default: null

DELETED (optional)

Query Parameter — include deleted associations default: null

WithAssociations (optional)

Query Parameter — query includes associations default: null

WithCoordinators (optional)

Query Parameter — query includes coordinators default: null

NoUsersAreCoords (optional)

Query Parameter — remove users as coordinators default: null

UsersAreCoords (optional)

Query Parameter — users are coordinators default: null

### Return type

[v0.0.44\_openapi\_accounts\_resp](#v0.0.44_openapi_accounts_resp)

### Example data

Content-Type: application/json

```
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "accounts" : [ {
    "associations" : [ {
      "cluster" : "cluster",
      "partition" : "partition",
      "id" : 5,
      "user" : "user",
      "account" : "account"
    }, {
      "cluster" : "cluster",
      "partition" : "partition",
      "id" : 5,
      "user" : "user",
      "account" : "account"
    } ],
    "coordinators" : [ {
      "name" : "name",
      "direct" : true
    }, {
      "name" : "name",
      "direct" : true
    } ],
    "organization" : "organization",
    "name" : "name",
    "flags" : [ "DELETED", "DELETED" ],
    "description" : "description"
  }, {
    "associations" : [ {
      "cluster" : "cluster",
      "partition" : "partition",
      "id" : 5,
      "user" : "user",
      "account" : "account"
    }, {
      "cluster" : "cluster",
      "partition" : "partition",
      "id" : 5,
      "user" : "user",
      "account" : "account"
    } ],
    "coordinators" : [ {
      "name" : "name",
      "direct" : true
    }, {
      "name" : "name",
      "direct" : true
    } ],
    "organization" : "organization",
    "name" : "name",
    "flags" : [ "DELETED", "DELETED" ],
    "description" : "description"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces

This API call produces the following media types according to the Accept request header;
the media type will be conveyed by the Content-Type response header.

* `application/json`

### Responses

#### 200

List of accounts
[v0.0.44\_openapi\_accounts\_resp](#v0.0.44_openapi_accounts_resp)

#### default

List of accounts
[v0.0.44\_openapi\_accounts\_resp](#v0.0.44_openapi_accounts_resp)



---

[Up](#__Methods)

```
get /slurmdb/v0.0.44/association/
```

Get association info (slurmdbV0044GetAssociation)

### Query parameters

account (optional)

Query Parameter — CSV accounts list default: null

cluster (optional)

Query Parameter — CSV clusters list default: null

default\_qos (optional)

Query Parameter — CSV QOS list default: null

Include deleted associations (optional)

Query Parameter — default: null

Include usage (optional)

Query Parameter — default: null

Filter to only defaults (optional)

Query Parameter — default: null

Include the raw QOS or delta\_qos (optional)

Query Parameter — default: null

Include sub acct information (optional)

Query Parameter — default: null

Exclude parent id/name (optional)

Query Parameter — default: null

Exclude limits from parents (optional)

Query Parameter — default: null

format (optional)

Query Parameter — Ignored; process JSON manually to control output format default: null

id (optional)

Query Parameter — CSV ID list default: null

parent\_account (optional)

Query Parameter — CSV names of parent account default: null

partition (optional)

Query Parameter — CSV partition name list default: null

qos (optional)

Query Parameter — CSV QOS list default: null

usage\_end (optional)

Query Parameter — Usage end (UNIX timestamp) default: null

usage\_start (optional)

Query Parameter — Usage start (UNIX timestamp) default: null

user (optional)

Query Parameter — CSV user list default: null

### Return type

[v0.0.44\_openapi\_assocs\_resp](#v0.0.44_openapi_assocs_resp)

### Example data

Content-Type: application/json

```
{
  "associations" : [ {
    "lineage" : "lineage",
    "cluster" : "cluster",
    "shares_raw" : 1,
    "max" : {
      "jobs" : {
        "total" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "active" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "accruing" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "per" : {
          "submitted" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "count" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "accruing" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "wall_clock" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          }
        }
      },
      "tres" : {
        "total" : [ {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        }, {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        } ],
        "minutes" : {
          "total" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "per" : {
            "job" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ]
          }
        },
        "per" : {
          "node" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "job" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ]
        },
        "group" : {
          "minutes" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "active" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ]
        }
      },
      "per" : {
        "account" : {
          "wall_clock" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          }
        }
      }
    },
    "flags" : [ "DELETED", "DELETED" ],
    "accounting" : [ {
      "start" : 7,
      "id" : 5,
      "TRES" : {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      },
      "allocated" : {
        "seconds" : 5
      },
      "id_alt" : 2
    }, {
      "start" : 7,
      "id" : 5,
      "TRES" : {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      },
      "allocated" : {
        "seconds" : 5
      },
      "id_alt" : 2
    } ],
    "is_default" : true,
    "priority" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "parent_account" : "parent_account",
    "default" : {
      "qos" : "qos"
    },
    "min" : {
      "priority_threshold" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      }
    },
    "partition" : "partition",
    "qos" : [ "qos", "qos" ],
    "comment" : "comment",
    "id" : 7,
    "user" : "user",
    "account" : "account"
  }, {
    "lineage" : "lineage",
    "cluster" : "cluster",
    "shares_raw" : 1,
    "max" : {
      "jobs" : {
        "total" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "active" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "accruing" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "per" : {
          "submitted" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "count" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "accruing" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "wall_clock" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          }
        }
      },
      "tres" : {
        "total" : [ {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        }, {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        } ],
        "minutes" : {
          "total" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "per" : {
            "job" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ]
          }
        },
        "per" : {
          "node" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "job" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ]
        },
        "group" : {
          "minutes" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "active" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ]
        }
      },
      "per" : {
        "account" : {
          "wall_clock" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          }
        }
      }
    },
    "flags" : [ "DELETED", "DELETED" ],
    "accounting" : [ {
      "start" : 7,
      "id" : 5,
      "TRES" : {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      },
      "allocated" : {
        "seconds" : 5
      },
      "id_alt" : 2
    }, {
      "start" : 7,
      "id" : 5,
      "TRES" : {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      },
      "allocated" : {
        "seconds" : 5
      },
      "id_alt" : 2
    } ],
    "is_default" : true,
    "priority" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "parent_account" : "parent_account",
    "default" : {
      "qos" : "qos"
    },
    "min" : {
      "priority_threshold" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      }
    },
    "partition" : "partition",
    "qos" : [ "qos", "qos" ],
    "comment" : "comment",
    "id" : 7,
    "user" : "user",
    "account" : "account"
  } ],
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces

This API call produces the following media types according to the Accept request header;
the media type will be conveyed by the Content-Type response header.

* `application/json`

### Responses

#### 200

List of associations
[v0.0.44\_openapi\_assocs\_resp](#v0.0.44_openapi_assocs_resp)

#### default

List of associations
[v0.0.44\_openapi\_assocs\_resp](#v0.0.44_openapi_assocs_resp)



---

[Up](#__Methods)

```
get /slurmdb/v0.0.44/associations/
```

Get association list (slurmdbV0044GetAssociations)

### Query parameters

account (optional)

Query Parameter — CSV accounts list default: null

cluster (optional)

Query Parameter — CSV clusters list default: null

default\_qos (optional)

Query Parameter — CSV QOS list default: null

Include deleted associations (optional)

Query Parameter — default: null

Include usage (optional)

Query Parameter — default: null

Filter to only defaults (optional)

Query Parameter — default: null

Include the raw QOS or delta\_qos (optional)

Query Parameter — default: null

Include sub acct information (optional)

Query Parameter — default: null

Exclude parent id/name (optional)

Query Parameter — default: null

Exclude limits from parents (optional)

Query Parameter — default: null

format (optional)

Query Parameter — Ignored; process JSON manually to control output format default: null

id (optional)

Query Parameter — CSV ID list default: null

parent\_account (optional)

Query Parameter — CSV names of parent account default: null

partition (optional)

Query Parameter — CSV partition name list default: null

qos (optional)

Query Parameter — CSV QOS list default: null

usage\_end (optional)

Query Parameter — Usage end (UNIX timestamp) default: null

usage\_start (optional)

Query Parameter — Usage start (UNIX timestamp) default: null

user (optional)

Query Parameter — CSV user list default: null

### Return type

[v0.0.44\_openapi\_assocs\_resp](#v0.0.44_openapi_assocs_resp)

### Example data

Content-Type: application/json

```
{
  "associations" : [ {
    "lineage" : "lineage",
    "cluster" : "cluster",
    "shares_raw" : 1,
    "max" : {
      "jobs" : {
        "total" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "active" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "accruing" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "per" : {
          "submitted" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "count" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "accruing" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "wall_clock" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          }
        }
      },
      "tres" : {
        "total" : [ {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        }, {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        } ],
        "minutes" : {
          "total" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "per" : {
            "job" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ]
          }
        },
        "per" : {
          "node" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "job" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ]
        },
        "group" : {
          "minutes" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "active" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ]
        }
      },
      "per" : {
        "account" : {
          "wall_clock" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          }
        }
      }
    },
    "flags" : [ "DELETED", "DELETED" ],
    "accounting" : [ {
      "start" : 7,
      "id" : 5,
      "TRES" : {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      },
      "allocated" : {
        "seconds" : 5
      },
      "id_alt" : 2
    }, {
      "start" : 7,
      "id" : 5,
      "TRES" : {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      },
      "allocated" : {
        "seconds" : 5
      },
      "id_alt" : 2
    } ],
    "is_default" : true,
    "priority" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "parent_account" : "parent_account",
    "default" : {
      "qos" : "qos"
    },
    "min" : {
      "priority_threshold" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      }
    },
    "partition" : "partition",
    "qos" : [ "qos", "qos" ],
    "comment" : "comment",
    "id" : 7,
    "user" : "user",
    "account" : "account"
  }, {
    "lineage" : "lineage",
    "cluster" : "cluster",
    "shares_raw" : 1,
    "max" : {
      "jobs" : {
        "total" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "active" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "accruing" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "per" : {
          "submitted" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "count" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "accruing" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "wall_clock" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          }
        }
      },
      "tres" : {
        "total" : [ {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        }, {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        } ],
        "minutes" : {
          "total" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "per" : {
            "job" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ]
          }
        },
        "per" : {
          "node" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "job" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ]
        },
        "group" : {
          "minutes" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "active" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ]
        }
      },
      "per" : {
        "account" : {
          "wall_clock" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          }
        }
      }
    },
    "flags" : [ "DELETED", "DELETED" ],
    "accounting" : [ {
      "start" : 7,
      "id" : 5,
      "TRES" : {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      },
      "allocated" : {
        "seconds" : 5
      },
      "id_alt" : 2
    }, {
      "start" : 7,
      "id" : 5,
      "TRES" : {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      },
      "allocated" : {
        "seconds" : 5
      },
      "id_alt" : 2
    } ],
    "is_default" : true,
    "priority" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "parent_account" : "parent_account",
    "default" : {
      "qos" : "qos"
    },
    "min" : {
      "priority_threshold" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      }
    },
    "partition" : "partition",
    "qos" : [ "qos", "qos" ],
    "comment" : "comment",
    "id" : 7,
    "user" : "user",
    "account" : "account"
  } ],
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces

This API call produces the following media types according to the Accept request header;
the media type will be conveyed by the Content-Type response header.

* `application/json`

### Responses

#### 200

List of associations
[v0.0.44\_openapi\_assocs\_resp](#v0.0.44_openapi_assocs_resp)

#### default

List of associations
[v0.0.44\_openapi\_assocs\_resp](#v0.0.44_openapi_assocs_resp)



---

[Up](#__Methods)

```
get /slurmdb/v0.0.44/cluster/{cluster_name}
```

Get cluster info (slurmdbV0044GetCluster)

### Path parameters

cluster\_name (required)

Path Parameter — Cluster name default: null

### Query parameters

classification (optional)

Query Parameter — Type of machine default: null

cluster (optional)

Query Parameter — CSV cluster list default: null

federation (optional)

Query Parameter — CSV federation list default: null

flags (optional)

Query Parameter — Query flags default: null

format (optional)

Query Parameter — Ignored; process JSON manually to control output format default: null

rpc\_version (optional)

Query Parameter — CSV RPC version list default: null

usage\_end (optional)

Query Parameter — Usage end (UNIX timestamp) default: null

usage\_start (optional)

Query Parameter — Usage start (UNIX timestamp) default: null

with\_deleted (optional)

Query Parameter — Include deleted clusters default: null

with\_usage (optional)

Query Parameter — Include usage default: null

### Return type

[v0.0.44\_openapi\_clusters\_resp](#v0.0.44_openapi_clusters_resp)

### Example data

Content-Type: application/json

```
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "clusters" : [ {
    "associations" : {
      "root" : {
        "cluster" : "cluster",
        "partition" : "partition",
        "id" : 5,
        "user" : "user",
        "account" : "account"
      }
    },
    "controller" : {
      "port" : 0,
      "host" : "host"
    },
    "nodes" : "nodes",
    "flags" : [ "DELETED", "DELETED" ],
    "name" : "name",
    "rpc_version" : 6,
    "tres" : [ {
      "name" : "name",
      "count" : 0,
      "id" : 7,
      "type" : "type"
    }, {
      "name" : "name",
      "count" : 0,
      "id" : 7,
      "type" : "type"
    } ],
    "select_plugin" : "select_plugin"
  }, {
    "associations" : {
      "root" : {
        "cluster" : "cluster",
        "partition" : "partition",
        "id" : 5,
        "user" : "user",
        "account" : "account"
      }
    },
    "controller" : {
      "port" : 0,
      "host" : "host"
    },
    "nodes" : "nodes",
    "flags" : [ "DELETED", "DELETED" ],
    "name" : "name",
    "rpc_version" : 6,
    "tres" : [ {
      "name" : "name",
      "count" : 0,
      "id" : 7,
      "type" : "type"
    }, {
      "name" : "name",
      "count" : 0,
      "id" : 7,
      "type" : "type"
    } ],
    "select_plugin" : "select_plugin"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces

This API call produces the following media types according to the Accept request header;
the media type will be conveyed by the Content-Type response header.

* `application/json`

### Responses

#### 200

Cluster information
[v0.0.44\_openapi\_clusters\_resp](#v0.0.44_openapi_clusters_resp)

#### default

Cluster information
[v0.0.44\_openapi\_clusters\_resp](#v0.0.44_openapi_clusters_resp)



---

[Up](#__Methods)

```
get /slurmdb/v0.0.44/clusters/
```

Get cluster list (slurmdbV0044GetClusters)

### Query parameters

update\_time (optional)

Query Parameter — Query reservations updated more recently than this time (UNIX timestamp) default: null

### Return type

[v0.0.44\_openapi\_clusters\_resp](#v0.0.44_openapi_clusters_resp)

### Example data

Content-Type: application/json

```
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "clusters" : [ {
    "associations" : {
      "root" : {
        "cluster" : "cluster",
        "partition" : "partition",
        "id" : 5,
        "user" : "user",
        "account" : "account"
      }
    },
    "controller" : {
      "port" : 0,
      "host" : "host"
    },
    "nodes" : "nodes",
    "flags" : [ "DELETED", "DELETED" ],
    "name" : "name",
    "rpc_version" : 6,
    "tres" : [ {
      "name" : "name",
      "count" : 0,
      "id" : 7,
      "type" : "type"
    }, {
      "name" : "name",
      "count" : 0,
      "id" : 7,
      "type" : "type"
    } ],
    "select_plugin" : "select_plugin"
  }, {
    "associations" : {
      "root" : {
        "cluster" : "cluster",
        "partition" : "partition",
        "id" : 5,
        "user" : "user",
        "account" : "account"
      }
    },
    "controller" : {
      "port" : 0,
      "host" : "host"
    },
    "nodes" : "nodes",
    "flags" : [ "DELETED", "DELETED" ],
    "name" : "name",
    "rpc_version" : 6,
    "tres" : [ {
      "name" : "name",
      "count" : 0,
      "id" : 7,
      "type" : "type"
    }, {
      "name" : "name",
      "count" : 0,
      "id" : 7,
      "type" : "type"
    } ],
    "select_plugin" : "select_plugin"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces

This API call produces the following media types according to the Accept request header;
the media type will be conveyed by the Content-Type response header.

* `application/json`

### Responses

#### 200

List of clusters
[v0.0.44\_openapi\_clusters\_resp](#v0.0.44_openapi_clusters_resp)

#### default

List of clusters
[v0.0.44\_openapi\_clusters\_resp](#v0.0.44_openapi_clusters_resp)



---

[Up](#__Methods)

```
get /slurmdb/v0.0.44/config
```

Dump all configuration information (slurmdbV0044GetConfig)

### Return type

[v0.0.44\_openapi\_slurmdbd\_config\_resp](#v0.0.44_openapi_slurmdbd_config_resp)

### Example data

Content-Type: application/json

```
{
  "associations" : [ {
    "lineage" : "lineage",
    "cluster" : "cluster",
    "shares_raw" : 1,
    "max" : {
      "jobs" : {
        "total" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "active" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "accruing" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "per" : {
          "submitted" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "count" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "accruing" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "wall_clock" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          }
        }
      },
      "tres" : {
        "total" : [ {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        }, {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        } ],
        "minutes" : {
          "total" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "per" : {
            "job" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ]
          }
        },
        "per" : {
          "node" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "job" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ]
        },
        "group" : {
          "minutes" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "active" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ]
        }
      },
      "per" : {
        "account" : {
          "wall_clock" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          }
        }
      }
    },
    "flags" : [ "DELETED", "DELETED" ],
    "accounting" : [ {
      "start" : 7,
      "id" : 5,
      "TRES" : {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      },
      "allocated" : {
        "seconds" : 5
      },
      "id_alt" : 2
    }, {
      "start" : 7,
      "id" : 5,
      "TRES" : {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      },
      "allocated" : {
        "seconds" : 5
      },
      "id_alt" : 2
    } ],
    "is_default" : true,
    "priority" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "parent_account" : "parent_account",
    "default" : {
      "qos" : "qos"
    },
    "min" : {
      "priority_threshold" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      }
    },
    "partition" : "partition",
    "qos" : [ "qos", "qos" ],
    "comment" : "comment",
    "id" : 7,
    "user" : "user",
    "account" : "account"
  }, {
    "lineage" : "lineage",
    "cluster" : "cluster",
    "shares_raw" : 1,
    "max" : {
      "jobs" : {
        "total" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "active" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "accruing" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "per" : {
          "submitted" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "count" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "accruing" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "wall_clock" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          }
        }
      },
      "tres" : {
        "total" : [ {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        }, {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        } ],
        "minutes" : {
          "total" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "per" : {
            "job" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ]
          }
        },
        "per" : {
          "node" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "job" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ]
        },
        "group" : {
          "minutes" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "active" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ]
        }
      },
      "per" : {
        "account" : {
          "wall_clock" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          }
        }
      }
    },
    "flags" : [ "DELETED", "DELETED" ],
    "accounting" : [ {
      "start" : 7,
      "id" : 5,
      "TRES" : {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      },
      "allocated" : {
        "seconds" : 5
      },
      "id_alt" : 2
    }, {
      "start" : 7,
      "id" : 5,
      "TRES" : {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      },
      "allocated" : {
        "seconds" : 5
      },
      "id_alt" : 2
    } ],
    "is_default" : true,
    "priority" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "parent_account" : "parent_account",
    "default" : {
      "qos" : "qos"
    },
    "min" : {
      "priority_threshold" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      }
    },
    "partition" : "partition",
    "qos" : [ "qos", "qos" ],
    "comment" : "comment",
    "id" : 7,
    "user" : "user",
    "account" : "account"
  } ],
  "qos" : [ {
    "flags" : [ "NOT_SET", "NOT_SET" ],
    "name" : "name",
    "usage_threshold" : {
      "number" : 4.145608029883936,
      "set" : true,
      "infinite" : true
    },
    "description" : "description",
    "usage_factor" : {
      "number" : 4.145608029883936,
      "set" : true,
      "infinite" : true
    },
    "id" : 3,
    "priority" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "limits" : {
      "min" : {
        "priority_threshold" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "tres" : {
          "per" : {
            "job" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ]
          }
        }
      },
      "max" : {
        "jobs" : {
          "count" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "per" : {
            "user" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            },
            "account" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            }
          },
          "active_jobs" : {
            "per" : {
              "user" : {
                "number" : 5,
                "set" : true,
                "infinite" : true
              },
              "account" : {
                "number" : 5,
                "set" : true,
                "infinite" : true
              }
            }
          }
        },
        "accruing" : {
          "per" : {
            "user" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            },
            "account" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            }
          }
        },
        "tres" : {
          "total" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "minutes" : {
            "total" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ],
            "per" : {
              "qos" : [ {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              }, {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              } ],
              "job" : [ {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              }, {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              } ],
              "user" : [ {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              }, {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              } ],
              "account" : [ {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              }, {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              } ]
            }
          },
          "per" : {
            "node" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ],
            "job" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ],
            "user" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ],
            "account" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ]
          }
        },
        "wall_clock" : {
          "per" : {
            "qos" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            },
            "job" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            }
          }
        },
        "active_jobs" : {
          "count" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "accruing" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          }
        }
      },
      "factor" : {
        "number" : 4.145608029883936,
        "set" : true,
        "infinite" : true
      },
      "grace_time" : 2
    },
    "preempt" : {
      "mode" : [ "DISABLED", "DISABLED" ],
      "exempt_time" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "list" : [ "list", "list" ]
    }
  }, {
    "flags" : [ "NOT_SET", "NOT_SET" ],
    "name" : "name",
    "usage_threshold" : {
      "number" : 4.145608029883936,
      "set" : true,
      "infinite" : true
    },
    "description" : "description",
    "usage_factor" : {
      "number" : 4.145608029883936,
      "set" : true,
      "infinite" : true
    },
    "id" : 3,
    "priority" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "limits" : {
      "min" : {
        "priority_threshold" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "tres" : {
          "per" : {
            "job" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ]
          }
        }
      },
      "max" : {
        "jobs" : {
          "count" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "per" : {
            "user" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            },
            "account" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            }
          },
          "active_jobs" : {
            "per" : {
              "user" : {
                "number" : 5,
                "set" : true,
                "infinite" : true
              },
              "account" : {
                "number" : 5,
                "set" : true,
                "infinite" : true
              }
            }
          }
        },
        "accruing" : {
          "per" : {
            "user" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            },
            "account" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            }
          }
        },
        "tres" : {
          "total" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "minutes" : {
            "total" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ],
            "per" : {
              "qos" : [ {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              }, {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              } ],
              "job" : [ {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              }, {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              } ],
              "user" : [ {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              }, {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              } ],
              "account" : [ {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              }, {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              } ]
            }
          },
          "per" : {
            "node" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ],
            "job" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ],
            "user" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ],
            "account" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ]
          }
        },
        "wall_clock" : {
          "per" : {
            "qos" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            },
            "job" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            }
          }
        },
        "active_jobs" : {
          "count" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "accruing" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          }
        }
      },
      "factor" : {
        "number" : 4.145608029883936,
        "set" : true,
        "infinite" : true
      },
      "grace_time" : 2
    },
    "preempt" : {
      "mode" : [ "DISABLED", "DISABLED" ],
      "exempt_time" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "list" : [ "list", "list" ]
    }
  } ],
  "wckeys" : [ {
    "cluster" : "cluster",
    "name" : "name",
    "flags" : [ "DELETED", "DELETED" ],
    "accounting" : [ {
      "start" : 7,
      "id" : 5,
      "TRES" : {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      },
      "allocated" : {
        "seconds" : 5
      },
      "id_alt" : 2
    }, {
      "start" : 7,
      "id" : 5,
      "TRES" : {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      },
      "allocated" : {
        "seconds" : 5
      },
      "id_alt" : 2
    } ],
    "id" : 9,
    "user" : "user"
  }, {
    "cluster" : "cluster",
    "name" : "name",
    "flags" : [ "DELETED", "DELETED" ],
    "accounting" : [ {
      "start" : 7,
      "id" : 5,
      "TRES" : {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      },
      "allocated" : {
        "seconds" : 5
      },
      "id_alt" : 2
    }, {
      "start" : 7,
      "id" : 5,
      "TRES" : {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      },
      "allocated" : {
        "seconds" : 5
      },
      "id_alt" : 2
    } ],
    "id" : 9,
    "user" : "user"
  } ],
  "instances" : [ {
    "cluster" : "cluster",
    "instance_id" : "instance_id",
    "extra" : "extra",
    "node_name" : "node_name",
    "time" : {
      "time_start" : 1,
      "time_end" : 1
    },
    "instance_type" : "instance_type"
  }, {
    "cluster" : "cluster",
    "instance_id" : "instance_id",
    "extra" : "extra",
    "node_name" : "node_name",
    "time" : {
      "time_start" : 1,
      "time_end" : 1
    },
    "instance_type" : "instance_type"
  } ],
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "tres" : [ {
    "name" : "name",
    "count" : 0,
    "id" : 7,
    "type" : "type"
  }, {
    "name" : "name",
    "count" : 0,
    "id" : 7,
    "type" : "type"
  } ],
  "accounts" : [ {
    "associations" : [ {
      "cluster" : "cluster",
      "partition" : "partition",
      "id" : 5,
      "user" : "user",
      "account" : "account"
    }, {
      "cluster" : "cluster",
      "partition" : "partition",
      "id" : 5,
      "user" : "user",
      "account" : "account"
    } ],
    "coordinators" : [ {
      "name" : "name",
      "direct" : true
    }, {
      "name" : "name",
      "direct" : true
    } ],
    "organization" : "organization",
    "name" : "name",
    "flags" : [ "DELETED", "DELETED" ],
    "description" : "description"
  }, {
    "associations" : [ {
      "cluster" : "cluster",
      "partition" : "partition",
      "id" : 5,
      "user" : "user",
      "account" : "account"
    }, {
      "cluster" : "cluster",
      "partition" : "partition",
      "id" : 5,
      "user" : "user",
      "account" : "account"
    } ],
    "coordinators" : [ {
      "name" : "name",
      "direct" : true
    }, {
      "name" : "name",
      "direct" : true
    } ],
    "organization" : "organization",
    "name" : "name",
    "flags" : [ "DELETED", "DELETED" ],
    "description" : "description"
  } ],
  "clusters" : [ {
    "associations" : {
      "root" : {
        "cluster" : "cluster",
        "partition" : "partition",
        "id" : 5,
        "user" : "user",
        "account" : "account"
      }
    },
    "controller" : {
      "port" : 0,
      "host" : "host"
    },
    "nodes" : "nodes",
    "flags" : [ "DELETED", "DELETED" ],
    "name" : "name",
    "rpc_version" : 6,
    "tres" : [ {
      "name" : "name",
      "count" : 0,
      "id" : 7,
      "type" : "type"
    }, {
      "name" : "name",
      "count" : 0,
      "id" : 7,
      "type" : "type"
    } ],
    "select_plugin" : "select_plugin"
  }, {
    "associations" : {
      "root" : {
        "cluster" : "cluster",
        "partition" : "partition",
        "id" : 5,
        "user" : "user",
        "account" : "account"
      }
    },
    "controller" : {
      "port" : 0,
      "host" : "host"
    },
    "nodes" : "nodes",
    "flags" : [ "DELETED", "DELETED" ],
    "name" : "name",
    "rpc_version" : 6,
    "tres" : [ {
      "name" : "name",
      "count" : 0,
      "id" : 7,
      "type" : "type"
    }, {
      "name" : "name",
      "count" : 0,
      "id" : 7,
      "type" : "type"
    } ],
    "select_plugin" : "select_plugin"
  } ],
  "users" : [ {
    "associations" : [ {
      "cluster" : "cluster",
      "partition" : "partition",
      "id" : 5,
      "user" : "user",
      "account" : "account"
    }, {
      "cluster" : "cluster",
      "partition" : "partition",
      "id" : 5,
      "user" : "user",
      "account" : "account"
    } ],
    "default" : {
      "qos" : 1,
      "wckey" : "wckey",
      "account" : "account"
    },
    "administrator_level" : [ "Not Set", "Not Set" ],
    "old_name" : "old_name",
    "wckeys" : [ {
      "cluster" : "cluster",
      "name" : "name",
      "flags" : [ "DELETED", "DELETED" ],
      "accounting" : [ {
        "start" : 7,
        "id" : 5,
        "TRES" : {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        },
        "allocated" : {
          "seconds" : 5
        },
        "id_alt" : 2
      }, {
        "start" : 7,
        "id" : 5,
        "TRES" : {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        },
        "allocated" : {
          "seconds" : 5
        },
        "id_alt" : 2
      } ],
      "id" : 9,
      "user" : "user"
    }, {
      "cluster" : "cluster",
      "name" : "name",
      "flags" : [ "DELETED", "DELETED" ],
      "accounting" : [ {
        "start" : 7,
        "id" : 5,
        "TRES" : {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        },
        "allocated" : {
          "seconds" : 5
        },
        "id_alt" : 2
      }, {
        "start" : 7,
        "id" : 5,
        "TRES" : {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        },
        "allocated" : {
          "seconds" : 5
        },
        "id_alt" : 2
      } ],
      "id" : 9,
      "user" : "user"
    } ],
    "coordinators" : [ {
      "name" : "name",
      "direct" : true
    }, {
      "name" : "name",
      "direct" : true
    } ],
    "flags" : [ "NONE", "NONE" ],
    "name" : "name"
  }, {
    "associations" : [ {
      "cluster" : "cluster",
      "partition" : "partition",
      "id" : 5,
      "user" : "user",
      "account" : "account"
    }, {
      "cluster" : "cluster",
      "partition" : "partition",
      "id" : 5,
      "user" : "user",
      "account" : "account"
    } ],
    "default" : {
      "qos" : 1,
      "wckey" : "wckey",
      "account" : "account"
    },
    "administrator_level" : [ "Not Set", "Not Set" ],
    "old_name" : "old_name",
    "wckeys" : [ {
      "cluster" : "cluster",
      "name" : "name",
      "flags" : [ "DELETED", "DELETED" ],
      "accounting" : [ {
        "start" : 7,
        "id" : 5,
        "TRES" : {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        },
        "allocated" : {
          "seconds" : 5
        },
        "id_alt" : 2
      }, {
        "start" : 7,
        "id" : 5,
        "TRES" : {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        },
        "allocated" : {
          "seconds" : 5
        },
        "id_alt" : 2
      } ],
      "id" : 9,
      "user" : "user"
    }, {
      "cluster" : "cluster",
      "name" : "name",
      "flags" : [ "DELETED", "DELETED" ],
      "accounting" : [ {
        "start" : 7,
        "id" : 5,
        "TRES" : {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        },
        "allocated" : {
          "seconds" : 5
        },
        "id_alt" : 2
      }, {
        "start" : 7,
        "id" : 5,
        "TRES" : {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        },
        "allocated" : {
          "seconds" : 5
        },
        "id_alt" : 2
      } ],
      "id" : 9,
      "user" : "user"
    } ],
    "coordinators" : [ {
      "name" : "name",
      "direct" : true
    }, {
      "name" : "name",
      "direct" : true
    } ],
    "flags" : [ "NONE", "NONE" ],
    "name" : "name"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces

This API call produces the following media types according to the Accept request header;
the media type will be conveyed by the Content-Type response header.

* `application/json`

### Responses

#### 200

slurmdbd configuration
[v0.0.44\_openapi\_slurmdbd\_config\_resp](#v0.0.44_openapi_slurmdbd_config_resp)

#### default

slurmdbd configuration
[v0.0.44\_openapi\_slurmdbd\_config\_resp](#v0.0.44_openapi_slurmdbd_config_resp)



---

[Up](#__Methods)

```
get /slurmdb/v0.0.44/diag/
```

Get slurmdb diagnostics (slurmdbV0044GetDiag)

### Return type

[v0.0.44\_openapi\_slurmdbd\_stats\_resp](#v0.0.44_openapi_slurmdbd_stats_resp)

### Example data

Content-Type: application/json

```
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ],
  "statistics" : {
    "time_start" : 0,
    "RPCs" : [ {
      "rpc" : "rpc",
      "count" : 7,
      "time" : {
        "average" : 1,
        "total" : 4
      }
    }, {
      "rpc" : "rpc",
      "count" : 7,
      "time" : {
        "average" : 1,
        "total" : 4
      }
    } ],
    "rollups" : {
      "daily" : {
        "duration" : {
          "last" : 3,
          "max" : 2,
          "time" : 4
        },
        "count" : 7,
        "last_run" : 9
      },
      "monthly" : {
        "duration" : {
          "last" : 1,
          "max" : 1,
          "time" : 6
        },
        "count" : 7,
        "last_run" : 1
      },
      "hourly" : {
        "duration" : {
          "last" : 5,
          "max" : 5,
          "time" : 2
        },
        "count" : 6,
        "last_run" : 1
      }
    },
    "users" : [ {
      "count" : 5,
      "time" : {
        "average" : 1,
        "total" : 4
      },
      "user" : "user"
    }, {
      "count" : 5,
      "time" : {
        "average" : 1,
        "total" : 4
      },
      "user" : "user"
    } ]
  }
}
```

### Produces

This API call produces the following media types according to the Accept request header;
the media type will be conveyed by the Content-Type response header.

* `application/json`

### Responses

#### 200

Dictionary of statistics
[v0.0.44\_openapi\_slurmdbd\_stats\_resp](#v0.0.44_openapi_slurmdbd_stats_resp)

#### default

Dictionary of statistics
[v0.0.44\_openapi\_slurmdbd\_stats\_resp](#v0.0.44_openapi_slurmdbd_stats_resp)



---

[Up](#__Methods)

```
get /slurmdb/v0.0.44/instance/
```

Get instance info (slurmdbV0044GetInstance)

### Query parameters

cluster (optional)

Query Parameter — CSV clusters list default: null

extra (optional)

Query Parameter — CSV extra list default: null

format (optional)

Query Parameter — Ignored; process JSON manually to control output format default: null

instance\_id (optional)

Query Parameter — CSV instance\_id list default: null

instance\_type (optional)

Query Parameter — CSV instance\_type list default: null

node\_list (optional)

Query Parameter — Ranged node string default: null

time\_end (optional)

Query Parameter — Time end (UNIX timestamp) default: null

time\_start (optional)

Query Parameter — Time start (UNIX timestamp) default: null

### Return type

[v0.0.44\_openapi\_instances\_resp](#v0.0.44_openapi_instances_resp)

### Example data

Content-Type: application/json

```
{
  "instances" : [ {
    "cluster" : "cluster",
    "instance_id" : "instance_id",
    "extra" : "extra",
    "node_name" : "node_name",
    "time" : {
      "time_start" : 1,
      "time_end" : 1
    },
    "instance_type" : "instance_type"
  }, {
    "cluster" : "cluster",
    "instance_id" : "instance_id",
    "extra" : "extra",
    "node_name" : "node_name",
    "time" : {
      "time_start" : 1,
      "time_end" : 1
    },
    "instance_type" : "instance_type"
  } ],
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces

This API call produces the following media types according to the Accept request header;
the media type will be conveyed by the Content-Type response header.

* `application/json`

### Responses

#### 200

List of instances
[v0.0.44\_openapi\_instances\_resp](#v0.0.44_openapi_instances_resp)

#### default

List of instances
[v0.0.44\_openapi\_instances\_resp](#v0.0.44_openapi_instances_resp)



---

[Up](#__Methods)

```
get /slurmdb/v0.0.44/instances/
```

Get instance list (slurmdbV0044GetInstances)

### Query parameters

cluster (optional)

Query Parameter — CSV clusters list default: null

extra (optional)

Query Parameter — CSV extra list default: null

format (optional)

Query Parameter — Ignored; process JSON manually to control output format default: null

instance\_id (optional)

Query Parameter — CSV instance\_id list default: null

instance\_type (optional)

Query Parameter — CSV instance\_type list default: null

node\_list (optional)

Query Parameter — Ranged node string default: null

time\_end (optional)

Query Parameter — Time end (UNIX timestamp) default: null

time\_start (optional)

Query Parameter — Time start (UNIX timestamp) default: null

### Return type

[v0.0.44\_openapi\_instances\_resp](#v0.0.44_openapi_instances_resp)

### Example data

Content-Type: application/json

```
{
  "instances" : [ {
    "cluster" : "cluster",
    "instance_id" : "instance_id",
    "extra" : "extra",
    "node_name" : "node_name",
    "time" : {
      "time_start" : 1,
      "time_end" : 1
    },
    "instance_type" : "instance_type"
  }, {
    "cluster" : "cluster",
    "instance_id" : "instance_id",
    "extra" : "extra",
    "node_name" : "node_name",
    "time" : {
      "time_start" : 1,
      "time_end" : 1
    },
    "instance_type" : "instance_type"
  } ],
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces

This API call produces the following media types according to the Accept request header;
the media type will be conveyed by the Content-Type response header.

* `application/json`

### Responses

#### 200

List of instances
[v0.0.44\_openapi\_instances\_resp](#v0.0.44_openapi_instances_resp)

#### default

List of instances
[v0.0.44\_openapi\_instances\_resp](#v0.0.44_openapi_instances_resp)



---

[Up](#__Methods)

```
get /slurmdb/v0.0.44/job/{job_id}
```

Get job info (slurmdbV0044GetJob)

This endpoint may return multiple job entries since job\_id is not a unique key - only the tuple (cluster, job\_id, start\_time) is unique. If the requested job\_id is a component of a heterogeneous job all components are returned.

### Path parameters

job\_id (required)

Path Parameter — Job ID default: null

### Return type

[v0.0.44\_openapi\_slurmdbd\_jobs\_resp](#v0.0.44_openapi_slurmdbd_jobs_resp)

### Example data

Content-Type: application/json

```
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "jobs" : [ {
    "container" : "container",
    "cluster" : "cluster",
    "stdin_expanded" : "stdin_expanded",
    "stdin" : "stdin",
    "stdout" : "stdout",
    "stderr_expanded" : "stderr_expanded",
    "flags" : [ "NONE", "NONE" ],
    "used_gres" : "used_gres",
    "association" : {
      "cluster" : "cluster",
      "partition" : "partition",
      "id" : 5,
      "user" : "user",
      "account" : "account"
    },
    "allocation_nodes" : 0,
    "working_directory" : "working_directory",
    "qosreq" : "qosreq",
    "constraints" : "constraints",
    "required" : {
      "memory_per_node" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "CPUs" : 9,
      "memory_per_cpu" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      }
    },
    "stdout_expanded" : "stdout_expanded",
    "hold" : true,
    "restart_cnt" : 6,
    "partition" : "partition",
    "segment_size" : 9,
    "qos" : "qos",
    "array" : {
      "task" : "task",
      "job_id" : 6,
      "task_id" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "limits" : {
        "max" : {
          "running" : {
            "tasks" : 1
          }
        }
      }
    },
    "het" : {
      "job_id" : 5,
      "job_offset" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      }
    },
    "submit_line" : "submit_line",
    "extra" : "extra",
    "reservation" : {
      "requested" : "requested",
      "name" : "name",
      "id" : 8
    },
    "block" : "block",
    "tres" : {
      "requested" : [ {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      }, {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      } ],
      "allocated" : [ {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      }, {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      } ]
    },
    "state" : {
      "reason" : "reason",
      "current" : [ "PENDING", "PENDING" ]
    },
    "mcs" : {
      "label" : "label"
    },
    "group" : "group",
    "wckey" : {
      "wckey" : "wckey",
      "flags" : [ "ASSIGNED_DEFAULT", "ASSIGNED_DEFAULT" ]
    },
    "priority" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "stderr" : "stderr",
    "steps" : [ {
      "nodes" : {
        "count" : 6,
        "range" : "range",
        "list" : [ "list", "list" ]
      },
      "task" : {
        "distribution" : "distribution"
      },
      "exit_code" : {
        "return_code" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "signal" : {
          "name" : "name",
          "id" : {
            "number" : 2,
            "set" : true,
            "infinite" : true
          }
        },
        "status" : [ "INVALID", "INVALID" ]
      },
      "kill_request_user" : "kill_request_user",
      "CPU" : {
        "governor" : "governor",
        "requested_frequency" : {
          "min" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "max" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          }
        }
      },
      "pid" : "pid",
      "step" : {
        "stdin_expanded" : "stdin_expanded",
        "stdin" : "stdin",
        "stdout" : "stdout",
        "stderr_expanded" : "stderr_expanded",
        "name" : "name",
        "id" : "id",
        "stderr" : "stderr",
        "stdout_expanded" : "stdout_expanded"
      },
      "tres" : {
        "consumed" : {
          "average" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "total" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "min" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "max" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ]
        },
        "requested" : {
          "average" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "total" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "min" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "max" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ]
        },
        "allocated" : [ {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        }, {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        } ]
      },
      "time" : {
        "elapsed" : 6,
        "total" : {
          "seconds" : 2,
          "microseconds" : 6
        },
        "system" : {
          "seconds" : 6,
          "microseconds" : 1
        },
        "start" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        },
        "limit" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "end" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        },
        "user" : {
          "seconds" : 6,
          "microseconds" : 5
        },
        "suspended" : 3
      },
      "state" : [ "PENDING", "PENDING" ],
      "tasks" : {
        "count" : 3
      },
      "statistics" : {
        "CPU" : {
          "actual_frequency" : 3
        },
        "energy" : {
          "consumed" : {
            "number" : 2,
            "set" : true,
            "infinite" : true
          }
        }
      }
    }, {
      "nodes" : {
        "count" : 6,
        "range" : "range",
        "list" : [ "list", "list" ]
      },
      "task" : {
        "distribution" : "distribution"
      },
      "exit_code" : {
        "return_code" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "signal" : {
          "name" : "name",
          "id" : {
            "number" : 2,
            "set" : true,
            "infinite" : true
          }
        },
        "status" : [ "INVALID", "INVALID" ]
      },
      "kill_request_user" : "kill_request_user",
      "CPU" : {
        "governor" : "governor",
        "requested_frequency" : {
          "min" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "max" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          }
        }
      },
      "pid" : "pid",
      "step" : {
        "stdin_expanded" : "stdin_expanded",
        "stdin" : "stdin",
        "stdout" : "stdout",
        "stderr_expanded" : "stderr_expanded",
        "name" : "name",
        "id" : "id",
        "stderr" : "stderr",
        "stdout_expanded" : "stdout_expanded"
      },
      "tres" : {
        "consumed" : {
          "average" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "total" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "min" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "max" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ]
        },
        "requested" : {
          "average" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "total" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "min" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "max" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ]
        },
        "allocated" : [ {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        }, {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        } ]
      },
      "time" : {
        "elapsed" : 6,
        "total" : {
          "seconds" : 2,
          "microseconds" : 6
        },
        "system" : {
          "seconds" : 6,
          "microseconds" : 1
        },
        "start" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        },
        "limit" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "end" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        },
        "user" : {
          "seconds" : 6,
          "microseconds" : 5
        },
        "suspended" : 3
      },
      "state" : [ "PENDING", "PENDING" ],
      "tasks" : {
        "count" : 3
      },
      "statistics" : {
        "CPU" : {
          "actual_frequency" : 3
        },
        "energy" : {
          "consumed" : {
            "number" : 2,
            "set" : true,
            "infinite" : true
          }
        }
      }
    } ],
    "script" : "script",
    "failed_node" : "failed_node",
    "derived_exit_code" : {
      "return_code" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "signal" : {
        "name" : "name",
        "id" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        }
      },
      "status" : [ "INVALID", "INVALID" ]
    },
    "licenses" : "licenses",
    "nodes" : "nodes",
    "job_id" : 9,
    "exit_code" : {
      "return_code" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "signal" : {
        "name" : "name",
        "id" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        }
      },
      "status" : [ "INVALID", "INVALID" ]
    },
    "name" : "name",
    "kill_request_user" : "kill_request_user",
    "comment" : {
      "administrator" : "administrator",
      "system" : "system",
      "job" : "job"
    },
    "time" : {
      "elapsed" : 7,
      "total" : {
        "seconds" : 6,
        "microseconds" : 7
      },
      "system" : {
        "seconds" : 1,
        "microseconds" : 1
      },
      "eligible" : 9,
      "start" : 4,
      "limit" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "end" : 3,
      "submission" : 7,
      "planned" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "user" : {
        "seconds" : 1,
        "microseconds" : 4
      },
      "suspended" : 1
    },
    "user" : "user",
    "account" : "account"
  }, {
    "container" : "container",
    "cluster" : "cluster",
    "stdin_expanded" : "stdin_expanded",
    "stdin" : "stdin",
    "stdout" : "stdout",
    "stderr_expanded" : "stderr_expanded",
    "flags" : [ "NONE", "NONE" ],
    "used_gres" : "used_gres",
    "association" : {
      "cluster" : "cluster",
      "partition" : "partition",
      "id" : 5,
      "user" : "user",
      "account" : "account"
    },
    "allocation_nodes" : 0,
    "working_directory" : "working_directory",
    "qosreq" : "qosreq",
    "constraints" : "constraints",
    "required" : {
      "memory_per_node" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "CPUs" : 9,
      "memory_per_cpu" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      }
    },
    "stdout_expanded" : "stdout_expanded",
    "hold" : true,
    "restart_cnt" : 6,
    "partition" : "partition",
    "segment_size" : 9,
    "qos" : "qos",
    "array" : {
      "task" : "task",
      "job_id" : 6,
      "task_id" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "limits" : {
        "max" : {
          "running" : {
            "tasks" : 1
          }
        }
      }
    },
    "het" : {
      "job_id" : 5,
      "job_offset" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      }
    },
    "submit_line" : "submit_line",
    "extra" : "extra",
    "reservation" : {
      "requested" : "requested",
      "name" : "name",
      "id" : 8
    },
    "block" : "block",
    "tres" : {
      "requested" : [ {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      }, {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      } ],
      "allocated" : [ {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      }, {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      } ]
    },
    "state" : {
      "reason" : "reason",
      "current" : [ "PENDING", "PENDING" ]
    },
    "mcs" : {
      "label" : "label"
    },
    "group" : "group",
    "wckey" : {
      "wckey" : "wckey",
      "flags" : [ "ASSIGNED_DEFAULT", "ASSIGNED_DEFAULT" ]
    },
    "priority" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "stderr" : "stderr",
    "steps" : [ {
      "nodes" : {
        "count" : 6,
        "range" : "range",
        "list" : [ "list", "list" ]
      },
      "task" : {
        "distribution" : "distribution"
      },
      "exit_code" : {
        "return_code" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "signal" : {
          "name" : "name",
          "id" : {
            "number" : 2,
            "set" : true,
            "infinite" : true
          }
        },
        "status" : [ "INVALID", "INVALID" ]
      },
      "kill_request_user" : "kill_request_user",
      "CPU" : {
        "governor" : "governor",
        "requested_frequency" : {
          "min" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "max" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          }
        }
      },
      "pid" : "pid",
      "step" : {
        "stdin_expanded" : "stdin_expanded",
        "stdin" : "stdin",
        "stdout" : "stdout",
        "stderr_expanded" : "stderr_expanded",
        "name" : "name",
        "id" : "id",
        "stderr" : "stderr",
        "stdout_expanded" : "stdout_expanded"
      },
      "tres" : {
        "consumed" : {
          "average" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "total" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "min" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "max" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ]
        },
        "requested" : {
          "average" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "total" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "min" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "max" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ]
        },
        "allocated" : [ {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        }, {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        } ]
      },
      "time" : {
        "elapsed" : 6,
        "total" : {
          "seconds" : 2,
          "microseconds" : 6
        },
        "system" : {
          "seconds" : 6,
          "microseconds" : 1
        },
        "start" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        },
        "limit" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "end" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        },
        "user" : {
          "seconds" : 6,
          "microseconds" : 5
        },
        "suspended" : 3
      },
      "state" : [ "PENDING", "PENDING" ],
      "tasks" : {
        "count" : 3
      },
      "statistics" : {
        "CPU" : {
          "actual_frequency" : 3
        },
        "energy" : {
          "consumed" : {
            "number" : 2,
            "set" : true,
            "infinite" : true
          }
        }
      }
    }, {
      "nodes" : {
        "count" : 6,
        "range" : "range",
        "list" : [ "list", "list" ]
      },
      "task" : {
        "distribution" : "distribution"
      },
      "exit_code" : {
        "return_code" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "signal" : {
          "name" : "name",
          "id" : {
            "number" : 2,
            "set" : true,
            "infinite" : true
          }
        },
        "status" : [ "INVALID", "INVALID" ]
      },
      "kill_request_user" : "kill_request_user",
      "CPU" : {
        "governor" : "governor",
        "requested_frequency" : {
          "min" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "max" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          }
        }
      },
      "pid" : "pid",
      "step" : {
        "stdin_expanded" : "stdin_expanded",
        "stdin" : "stdin",
        "stdout" : "stdout",
        "stderr_expanded" : "stderr_expanded",
        "name" : "name",
        "id" : "id",
        "stderr" : "stderr",
        "stdout_expanded" : "stdout_expanded"
      },
      "tres" : {
        "consumed" : {
          "average" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "total" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "min" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "max" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ]
        },
        "requested" : {
          "average" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "total" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "min" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "max" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ]
        },
        "allocated" : [ {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        }, {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        } ]
      },
      "time" : {
        "elapsed" : 6,
        "total" : {
          "seconds" : 2,
          "microseconds" : 6
        },
        "system" : {
          "seconds" : 6,
          "microseconds" : 1
        },
        "start" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        },
        "limit" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "end" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        },
        "user" : {
          "seconds" : 6,
          "microseconds" : 5
        },
        "suspended" : 3
      },
      "state" : [ "PENDING", "PENDING" ],
      "tasks" : {
        "count" : 3
      },
      "statistics" : {
        "CPU" : {
          "actual_frequency" : 3
        },
        "energy" : {
          "consumed" : {
            "number" : 2,
            "set" : true,
            "infinite" : true
          }
        }
      }
    } ],
    "script" : "script",
    "failed_node" : "failed_node",
    "derived_exit_code" : {
      "return_code" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "signal" : {
        "name" : "name",
        "id" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        }
      },
      "status" : [ "INVALID", "INVALID" ]
    },
    "licenses" : "licenses",
    "nodes" : "nodes",
    "job_id" : 9,
    "exit_code" : {
      "return_code" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "signal" : {
        "name" : "name",
        "id" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        }
      },
      "status" : [ "INVALID", "INVALID" ]
    },
    "name" : "name",
    "kill_request_user" : "kill_request_user",
    "comment" : {
      "administrator" : "administrator",
      "system" : "system",
      "job" : "job"
    },
    "time" : {
      "elapsed" : 7,
      "total" : {
        "seconds" : 6,
        "microseconds" : 7
      },
      "system" : {
        "seconds" : 1,
        "microseconds" : 1
      },
      "eligible" : 9,
      "start" : 4,
      "limit" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "end" : 3,
      "submission" : 7,
      "planned" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "user" : {
        "seconds" : 1,
        "microseconds" : 4
      },
      "suspended" : 1
    },
    "user" : "user",
    "account" : "account"
  } ],
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces

This API call produces the following media types according to the Accept request header;
the media type will be conveyed by the Content-Type response header.

* `application/json`

### Responses

#### 200

Job description
[v0.0.44\_openapi\_slurmdbd\_jobs\_resp](#v0.0.44_openapi_slurmdbd_jobs_resp)

#### default

Job description
[v0.0.44\_openapi\_slurmdbd\_jobs\_resp](#v0.0.44_openapi_slurmdbd_jobs_resp)



---

[Up](#__Methods)

```
get /slurmdb/v0.0.44/jobs/
```

Get job list (slurmdbV0044GetJobs)

### Query parameters

account (optional)

Query Parameter — CSV account list default: null

association (optional)

Query Parameter — CSV association list default: null

cluster (optional)

Query Parameter — CSV cluster list default: null

constraints (optional)

Query Parameter — CSV constraint list default: null

scheduler\_unset (optional)

Query Parameter — Schedule bits not set default: null

scheduled\_on\_submit (optional)

Query Parameter — Job was started on submit default: null

scheduled\_by\_main (optional)

Query Parameter — Job was started from main scheduler default: null

scheduled\_by\_backfill (optional)

Query Parameter — Job was started from backfill default: null

job\_started (optional)

Query Parameter — Job start RPC was received default: null

job\_altered (optional)

Query Parameter — Job record has been altered default: null

exit\_code (optional)

Query Parameter — Job exit code (numeric) default: null

show\_duplicates (optional)

Query Parameter — Include duplicate job entries default: null

skip\_steps (optional)

Query Parameter — Exclude job step details default: null

disable\_truncate\_usage\_time (optional)

Query Parameter — Do not truncate the time to usage\_start and usage\_end default: null

whole\_hetjob (optional)

Query Parameter — Include details on all hetjob components default: null

disable\_whole\_hetjob (optional)

Query Parameter — Only show details on specified hetjob components default: null

disable\_wait\_for\_result (optional)

Query Parameter — Tell dbd not to wait for the result default: null

usage\_time\_as\_submit\_time (optional)

Query Parameter — Use usage\_time as the submit\_time of the job default: null

show\_batch\_script (optional)

Query Parameter — Include job script default: null

show\_job\_environment (optional)

Query Parameter — Include job environment default: null

format (optional)

Query Parameter — Ignored; process JSON manually to control output format default: null

groups (optional)

Query Parameter — CSV group list default: null

job\_name (optional)

Query Parameter — CSV job name list default: null

partition (optional)

Query Parameter — CSV partition name list default: null

qos (optional)

Query Parameter — CSV QOS name list default: null

reason (optional)

Query Parameter — CSV reason list default: null

reservation (optional)

Query Parameter — CSV reservation name list default: null

reservation\_id (optional)

Query Parameter — CSV reservation ID list default: null

state (optional)

Query Parameter — CSV state list default: null

step (optional)

Query Parameter — CSV step id list default: null

end\_time (optional)

Query Parameter — Usage end (UNIX timestamp) default: null

start\_time (optional)

Query Parameter — Usage start (UNIX timestamp) default: null

node (optional)

Query Parameter — Ranged node string where jobs ran default: null

users (optional)

Query Parameter — CSV user name list default: null

wckey (optional)

Query Parameter — CSV WCKey list default: null

### Return type

[v0.0.44\_openapi\_slurmdbd\_jobs\_resp](#v0.0.44_openapi_slurmdbd_jobs_resp)

### Example data

Content-Type: application/json

```
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "jobs" : [ {
    "container" : "container",
    "cluster" : "cluster",
    "stdin_expanded" : "stdin_expanded",
    "stdin" : "stdin",
    "stdout" : "stdout",
    "stderr_expanded" : "stderr_expanded",
    "flags" : [ "NONE", "NONE" ],
    "used_gres" : "used_gres",
    "association" : {
      "cluster" : "cluster",
      "partition" : "partition",
      "id" : 5,
      "user" : "user",
      "account" : "account"
    },
    "allocation_nodes" : 0,
    "working_directory" : "working_directory",
    "qosreq" : "qosreq",
    "constraints" : "constraints",
    "required" : {
      "memory_per_node" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "CPUs" : 9,
      "memory_per_cpu" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      }
    },
    "stdout_expanded" : "stdout_expanded",
    "hold" : true,
    "restart_cnt" : 6,
    "partition" : "partition",
    "segment_size" : 9,
    "qos" : "qos",
    "array" : {
      "task" : "task",
      "job_id" : 6,
      "task_id" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "limits" : {
        "max" : {
          "running" : {
            "tasks" : 1
          }
        }
      }
    },
    "het" : {
      "job_id" : 5,
      "job_offset" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      }
    },
    "submit_line" : "submit_line",
    "extra" : "extra",
    "reservation" : {
      "requested" : "requested",
      "name" : "name",
      "id" : 8
    },
    "block" : "block",
    "tres" : {
      "requested" : [ {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      }, {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      } ],
      "allocated" : [ {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      }, {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      } ]
    },
    "state" : {
      "reason" : "reason",
      "current" : [ "PENDING", "PENDING" ]
    },
    "mcs" : {
      "label" : "label"
    },
    "group" : "group",
    "wckey" : {
      "wckey" : "wckey",
      "flags" : [ "ASSIGNED_DEFAULT", "ASSIGNED_DEFAULT" ]
    },
    "priority" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "stderr" : "stderr",
    "steps" : [ {
      "nodes" : {
        "count" : 6,
        "range" : "range",
        "list" : [ "list", "list" ]
      },
      "task" : {
        "distribution" : "distribution"
      },
      "exit_code" : {
        "return_code" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "signal" : {
          "name" : "name",
          "id" : {
            "number" : 2,
            "set" : true,
            "infinite" : true
          }
        },
        "status" : [ "INVALID", "INVALID" ]
      },
      "kill_request_user" : "kill_request_user",
      "CPU" : {
        "governor" : "governor",
        "requested_frequency" : {
          "min" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "max" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          }
        }
      },
      "pid" : "pid",
      "step" : {
        "stdin_expanded" : "stdin_expanded",
        "stdin" : "stdin",
        "stdout" : "stdout",
        "stderr_expanded" : "stderr_expanded",
        "name" : "name",
        "id" : "id",
        "stderr" : "stderr",
        "stdout_expanded" : "stdout_expanded"
      },
      "tres" : {
        "consumed" : {
          "average" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "total" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "min" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "max" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ]
        },
        "requested" : {
          "average" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "total" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "min" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "max" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ]
        },
        "allocated" : [ {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        }, {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        } ]
      },
      "time" : {
        "elapsed" : 6,
        "total" : {
          "seconds" : 2,
          "microseconds" : 6
        },
        "system" : {
          "seconds" : 6,
          "microseconds" : 1
        },
        "start" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        },
        "limit" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "end" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        },
        "user" : {
          "seconds" : 6,
          "microseconds" : 5
        },
        "suspended" : 3
      },
      "state" : [ "PENDING", "PENDING" ],
      "tasks" : {
        "count" : 3
      },
      "statistics" : {
        "CPU" : {
          "actual_frequency" : 3
        },
        "energy" : {
          "consumed" : {
            "number" : 2,
            "set" : true,
            "infinite" : true
          }
        }
      }
    }, {
      "nodes" : {
        "count" : 6,
        "range" : "range",
        "list" : [ "list", "list" ]
      },
      "task" : {
        "distribution" : "distribution"
      },
      "exit_code" : {
        "return_code" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "signal" : {
          "name" : "name",
          "id" : {
            "number" : 2,
            "set" : true,
            "infinite" : true
          }
        },
        "status" : [ "INVALID", "INVALID" ]
      },
      "kill_request_user" : "kill_request_user",
      "CPU" : {
        "governor" : "governor",
        "requested_frequency" : {
          "min" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "max" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          }
        }
      },
      "pid" : "pid",
      "step" : {
        "stdin_expanded" : "stdin_expanded",
        "stdin" : "stdin",
        "stdout" : "stdout",
        "stderr_expanded" : "stderr_expanded",
        "name" : "name",
        "id" : "id",
        "stderr" : "stderr",
        "stdout_expanded" : "stdout_expanded"
      },
      "tres" : {
        "consumed" : {
          "average" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "total" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "min" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "max" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ]
        },
        "requested" : {
          "average" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "total" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "min" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "max" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ]
        },
        "allocated" : [ {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        }, {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        } ]
      },
      "time" : {
        "elapsed" : 6,
        "total" : {
          "seconds" : 2,
          "microseconds" : 6
        },
        "system" : {
          "seconds" : 6,
          "microseconds" : 1
        },
        "start" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        },
        "limit" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "end" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        },
        "user" : {
          "seconds" : 6,
          "microseconds" : 5
        },
        "suspended" : 3
      },
      "state" : [ "PENDING", "PENDING" ],
      "tasks" : {
        "count" : 3
      },
      "statistics" : {
        "CPU" : {
          "actual_frequency" : 3
        },
        "energy" : {
          "consumed" : {
            "number" : 2,
            "set" : true,
            "infinite" : true
          }
        }
      }
    } ],
    "script" : "script",
    "failed_node" : "failed_node",
    "derived_exit_code" : {
      "return_code" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "signal" : {
        "name" : "name",
        "id" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        }
      },
      "status" : [ "INVALID", "INVALID" ]
    },
    "licenses" : "licenses",
    "nodes" : "nodes",
    "job_id" : 9,
    "exit_code" : {
      "return_code" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "signal" : {
        "name" : "name",
        "id" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        }
      },
      "status" : [ "INVALID", "INVALID" ]
    },
    "name" : "name",
    "kill_request_user" : "kill_request_user",
    "comment" : {
      "administrator" : "administrator",
      "system" : "system",
      "job" : "job"
    },
    "time" : {
      "elapsed" : 7,
      "total" : {
        "seconds" : 6,
        "microseconds" : 7
      },
      "system" : {
        "seconds" : 1,
        "microseconds" : 1
      },
      "eligible" : 9,
      "start" : 4,
      "limit" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "end" : 3,
      "submission" : 7,
      "planned" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "user" : {
        "seconds" : 1,
        "microseconds" : 4
      },
      "suspended" : 1
    },
    "user" : "user",
    "account" : "account"
  }, {
    "container" : "container",
    "cluster" : "cluster",
    "stdin_expanded" : "stdin_expanded",
    "stdin" : "stdin",
    "stdout" : "stdout",
    "stderr_expanded" : "stderr_expanded",
    "flags" : [ "NONE", "NONE" ],
    "used_gres" : "used_gres",
    "association" : {
      "cluster" : "cluster",
      "partition" : "partition",
      "id" : 5,
      "user" : "user",
      "account" : "account"
    },
    "allocation_nodes" : 0,
    "working_directory" : "working_directory",
    "qosreq" : "qosreq",
    "constraints" : "constraints",
    "required" : {
      "memory_per_node" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "CPUs" : 9,
      "memory_per_cpu" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      }
    },
    "stdout_expanded" : "stdout_expanded",
    "hold" : true,
    "restart_cnt" : 6,
    "partition" : "partition",
    "segment_size" : 9,
    "qos" : "qos",
    "array" : {
      "task" : "task",
      "job_id" : 6,
      "task_id" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "limits" : {
        "max" : {
          "running" : {
            "tasks" : 1
          }
        }
      }
    },
    "het" : {
      "job_id" : 5,
      "job_offset" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      }
    },
    "submit_line" : "submit_line",
    "extra" : "extra",
    "reservation" : {
      "requested" : "requested",
      "name" : "name",
      "id" : 8
    },
    "block" : "block",
    "tres" : {
      "requested" : [ {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      }, {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      } ],
      "allocated" : [ {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      }, {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      } ]
    },
    "state" : {
      "reason" : "reason",
      "current" : [ "PENDING", "PENDING" ]
    },
    "mcs" : {
      "label" : "label"
    },
    "group" : "group",
    "wckey" : {
      "wckey" : "wckey",
      "flags" : [ "ASSIGNED_DEFAULT", "ASSIGNED_DEFAULT" ]
    },
    "priority" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "stderr" : "stderr",
    "steps" : [ {
      "nodes" : {
        "count" : 6,
        "range" : "range",
        "list" : [ "list", "list" ]
      },
      "task" : {
        "distribution" : "distribution"
      },
      "exit_code" : {
        "return_code" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "signal" : {
          "name" : "name",
          "id" : {
            "number" : 2,
            "set" : true,
            "infinite" : true
          }
        },
        "status" : [ "INVALID", "INVALID" ]
      },
      "kill_request_user" : "kill_request_user",
      "CPU" : {
        "governor" : "governor",
        "requested_frequency" : {
          "min" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "max" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          }
        }
      },
      "pid" : "pid",
      "step" : {
        "stdin_expanded" : "stdin_expanded",
        "stdin" : "stdin",
        "stdout" : "stdout",
        "stderr_expanded" : "stderr_expanded",
        "name" : "name",
        "id" : "id",
        "stderr" : "stderr",
        "stdout_expanded" : "stdout_expanded"
      },
      "tres" : {
        "consumed" : {
          "average" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "total" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "min" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "max" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ]
        },
        "requested" : {
          "average" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "total" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "min" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "max" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ]
        },
        "allocated" : [ {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        }, {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        } ]
      },
      "time" : {
        "elapsed" : 6,
        "total" : {
          "seconds" : 2,
          "microseconds" : 6
        },
        "system" : {
          "seconds" : 6,
          "microseconds" : 1
        },
        "start" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        },
        "limit" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "end" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        },
        "user" : {
          "seconds" : 6,
          "microseconds" : 5
        },
        "suspended" : 3
      },
      "state" : [ "PENDING", "PENDING" ],
      "tasks" : {
        "count" : 3
      },
      "statistics" : {
        "CPU" : {
          "actual_frequency" : 3
        },
        "energy" : {
          "consumed" : {
            "number" : 2,
            "set" : true,
            "infinite" : true
          }
        }
      }
    }, {
      "nodes" : {
        "count" : 6,
        "range" : "range",
        "list" : [ "list", "list" ]
      },
      "task" : {
        "distribution" : "distribution"
      },
      "exit_code" : {
        "return_code" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "signal" : {
          "name" : "name",
          "id" : {
            "number" : 2,
            "set" : true,
            "infinite" : true
          }
        },
        "status" : [ "INVALID", "INVALID" ]
      },
      "kill_request_user" : "kill_request_user",
      "CPU" : {
        "governor" : "governor",
        "requested_frequency" : {
          "min" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "max" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          }
        }
      },
      "pid" : "pid",
      "step" : {
        "stdin_expanded" : "stdin_expanded",
        "stdin" : "stdin",
        "stdout" : "stdout",
        "stderr_expanded" : "stderr_expanded",
        "name" : "name",
        "id" : "id",
        "stderr" : "stderr",
        "stdout_expanded" : "stdout_expanded"
      },
      "tres" : {
        "consumed" : {
          "average" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "total" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "min" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "max" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ]
        },
        "requested" : {
          "average" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "total" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "min" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "max" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ]
        },
        "allocated" : [ {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        }, {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        } ]
      },
      "time" : {
        "elapsed" : 6,
        "total" : {
          "seconds" : 2,
          "microseconds" : 6
        },
        "system" : {
          "seconds" : 6,
          "microseconds" : 1
        },
        "start" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        },
        "limit" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "end" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        },
        "user" : {
          "seconds" : 6,
          "microseconds" : 5
        },
        "suspended" : 3
      },
      "state" : [ "PENDING", "PENDING" ],
      "tasks" : {
        "count" : 3
      },
      "statistics" : {
        "CPU" : {
          "actual_frequency" : 3
        },
        "energy" : {
          "consumed" : {
            "number" : 2,
            "set" : true,
            "infinite" : true
          }
        }
      }
    } ],
    "script" : "script",
    "failed_node" : "failed_node",
    "derived_exit_code" : {
      "return_code" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "signal" : {
        "name" : "name",
        "id" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        }
      },
      "status" : [ "INVALID", "INVALID" ]
    },
    "licenses" : "licenses",
    "nodes" : "nodes",
    "job_id" : 9,
    "exit_code" : {
      "return_code" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "signal" : {
        "name" : "name",
        "id" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        }
      },
      "status" : [ "INVALID", "INVALID" ]
    },
    "name" : "name",
    "kill_request_user" : "kill_request_user",
    "comment" : {
      "administrator" : "administrator",
      "system" : "system",
      "job" : "job"
    },
    "time" : {
      "elapsed" : 7,
      "total" : {
        "seconds" : 6,
        "microseconds" : 7
      },
      "system" : {
        "seconds" : 1,
        "microseconds" : 1
      },
      "eligible" : 9,
      "start" : 4,
      "limit" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "end" : 3,
      "submission" : 7,
      "planned" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "user" : {
        "seconds" : 1,
        "microseconds" : 4
      },
      "suspended" : 1
    },
    "user" : "user",
    "account" : "account"
  } ],
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces

This API call produces the following media types according to the Accept request header;
the media type will be conveyed by the Content-Type response header.

* `application/json`

### Responses

#### 200

List of jobs
[v0.0.44\_openapi\_slurmdbd\_jobs\_resp](#v0.0.44_openapi_slurmdbd_jobs_resp)

#### default

List of jobs
[v0.0.44\_openapi\_slurmdbd\_jobs\_resp](#v0.0.44_openapi_slurmdbd_jobs_resp)



---

[Up](#__Methods)

```
get /slurmdb/v0.0.44/ping/
```

ping test (slurmdbV0044GetPing)

### Return type

[v0.0.44\_openapi\_slurmdbd\_ping\_resp](#v0.0.44_openapi_slurmdbd_ping_resp)

### Example data

Content-Type: application/json

```
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "pings" : [ {
    "responding" : true,
    "hostname" : "hostname",
    "latency" : 0,
    "primary" : true
  }, {
    "responding" : true,
    "hostname" : "hostname",
    "latency" : 0,
    "primary" : true
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces

This API call produces the following media types according to the Accept request header;
the media type will be conveyed by the Content-Type response header.

* `application/json`

### Responses

#### 200

results of ping test
[v0.0.44\_openapi\_slurmdbd\_ping\_resp](#v0.0.44_openapi_slurmdbd_ping_resp)

#### default

results of ping test
[v0.0.44\_openapi\_slurmdbd\_ping\_resp](#v0.0.44_openapi_slurmdbd_ping_resp)



---

[Up](#__Methods)

```
get /slurmdb/v0.0.44/qos/
```

Get QOS list (slurmdbV0044GetQos)

### Query parameters

description (optional)

Query Parameter — CSV description list default: null

Include deleted QOS (optional)

Query Parameter — default: null

id (optional)

Query Parameter — CSV QOS id list default: null

format (optional)

Query Parameter — Ignored; process JSON manually to control output format default: null

name (optional)

Query Parameter — CSV QOS name list default: null

preempt\_mode (optional)

Query Parameter — PreemptMode used when jobs in this QOS are preempted default: null

### Return type

[v0.0.44\_openapi\_slurmdbd\_qos\_resp](#v0.0.44_openapi_slurmdbd_qos_resp)

### Example data

Content-Type: application/json

```
{
  "qos" : [ {
    "flags" : [ "NOT_SET", "NOT_SET" ],
    "name" : "name",
    "usage_threshold" : {
      "number" : 4.145608029883936,
      "set" : true,
      "infinite" : true
    },
    "description" : "description",
    "usage_factor" : {
      "number" : 4.145608029883936,
      "set" : true,
      "infinite" : true
    },
    "id" : 3,
    "priority" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "limits" : {
      "min" : {
        "priority_threshold" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "tres" : {
          "per" : {
            "job" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ]
          }
        }
      },
      "max" : {
        "jobs" : {
          "count" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "per" : {
            "user" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            },
            "account" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            }
          },
          "active_jobs" : {
            "per" : {
              "user" : {
                "number" : 5,
                "set" : true,
                "infinite" : true
              },
              "account" : {
                "number" : 5,
                "set" : true,
                "infinite" : true
              }
            }
          }
        },
        "accruing" : {
          "per" : {
            "user" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            },
            "account" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            }
          }
        },
        "tres" : {
          "total" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "minutes" : {
            "total" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ],
            "per" : {
              "qos" : [ {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              }, {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              } ],
              "job" : [ {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              }, {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              } ],
              "user" : [ {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              }, {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              } ],
              "account" : [ {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              }, {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              } ]
            }
          },
          "per" : {
            "node" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ],
            "job" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ],
            "user" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ],
            "account" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ]
          }
        },
        "wall_clock" : {
          "per" : {
            "qos" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            },
            "job" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            }
          }
        },
        "active_jobs" : {
          "count" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "accruing" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          }
        }
      },
      "factor" : {
        "number" : 4.145608029883936,
        "set" : true,
        "infinite" : true
      },
      "grace_time" : 2
    },
    "preempt" : {
      "mode" : [ "DISABLED", "DISABLED" ],
      "exempt_time" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "list" : [ "list", "list" ]
    }
  }, {
    "flags" : [ "NOT_SET", "NOT_SET" ],
    "name" : "name",
    "usage_threshold" : {
      "number" : 4.145608029883936,
      "set" : true,
      "infinite" : true
    },
    "description" : "description",
    "usage_factor" : {
      "number" : 4.145608029883936,
      "set" : true,
      "infinite" : true
    },
    "id" : 3,
    "priority" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "limits" : {
      "min" : {
        "priority_threshold" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "tres" : {
          "per" : {
            "job" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ]
          }
        }
      },
      "max" : {
        "jobs" : {
          "count" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "per" : {
            "user" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            },
            "account" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            }
          },
          "active_jobs" : {
            "per" : {
              "user" : {
                "number" : 5,
                "set" : true,
                "infinite" : true
              },
              "account" : {
                "number" : 5,
                "set" : true,
                "infinite" : true
              }
            }
          }
        },
        "accruing" : {
          "per" : {
            "user" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            },
            "account" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            }
          }
        },
        "tres" : {
          "total" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "minutes" : {
            "total" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ],
            "per" : {
              "qos" : [ {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              }, {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              } ],
              "job" : [ {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              }, {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              } ],
              "user" : [ {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              }, {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              } ],
              "account" : [ {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              }, {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              } ]
            }
          },
          "per" : {
            "node" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ],
            "job" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ],
            "user" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ],
            "account" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ]
          }
        },
        "wall_clock" : {
          "per" : {
            "qos" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            },
            "job" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            }
          }
        },
        "active_jobs" : {
          "count" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "accruing" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          }
        }
      },
      "factor" : {
        "number" : 4.145608029883936,
        "set" : true,
        "infinite" : true
      },
      "grace_time" : 2
    },
    "preempt" : {
      "mode" : [ "DISABLED", "DISABLED" ],
      "exempt_time" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "list" : [ "list", "list" ]
    }
  } ],
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces

This API call produces the following media types according to the Accept request header;
the media type will be conveyed by the Content-Type response header.

* `application/json`

### Responses

#### 200

List of QOS
[v0.0.44\_openapi\_slurmdbd\_qos\_resp](#v0.0.44_openapi_slurmdbd_qos_resp)

#### default

List of QOS
[v0.0.44\_openapi\_slurmdbd\_qos\_resp](#v0.0.44_openapi_slurmdbd_qos_resp)



---

[Up](#__Methods)

```
get /slurmdb/v0.0.44/qos/{qos}
```

Get QOS info (slurmdbV0044GetSingleQos)

### Path parameters

qos (required)

Path Parameter — QOS name default: null

### Query parameters

with\_deleted (optional)

Query Parameter — Query includes deleted QOS default: null

### Return type

[v0.0.44\_openapi\_slurmdbd\_qos\_resp](#v0.0.44_openapi_slurmdbd_qos_resp)

### Example data

Content-Type: application/json

```
{
  "qos" : [ {
    "flags" : [ "NOT_SET", "NOT_SET" ],
    "name" : "name",
    "usage_threshold" : {
      "number" : 4.145608029883936,
      "set" : true,
      "infinite" : true
    },
    "description" : "description",
    "usage_factor" : {
      "number" : 4.145608029883936,
      "set" : true,
      "infinite" : true
    },
    "id" : 3,
    "priority" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "limits" : {
      "min" : {
        "priority_threshold" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "tres" : {
          "per" : {
            "job" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ]
          }
        }
      },
      "max" : {
        "jobs" : {
          "count" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "per" : {
            "user" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            },
            "account" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            }
          },
          "active_jobs" : {
            "per" : {
              "user" : {
                "number" : 5,
                "set" : true,
                "infinite" : true
              },
              "account" : {
                "number" : 5,
                "set" : true,
                "infinite" : true
              }
            }
          }
        },
        "accruing" : {
          "per" : {
            "user" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            },
            "account" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            }
          }
        },
        "tres" : {
          "total" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "minutes" : {
            "total" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ],
            "per" : {
              "qos" : [ {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              }, {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              } ],
              "job" : [ {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              }, {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              } ],
              "user" : [ {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              }, {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              } ],
              "account" : [ {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              }, {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              } ]
            }
          },
          "per" : {
            "node" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ],
            "job" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ],
            "user" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ],
            "account" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ]
          }
        },
        "wall_clock" : {
          "per" : {
            "qos" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            },
            "job" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            }
          }
        },
        "active_jobs" : {
          "count" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "accruing" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          }
        }
      },
      "factor" : {
        "number" : 4.145608029883936,
        "set" : true,
        "infinite" : true
      },
      "grace_time" : 2
    },
    "preempt" : {
      "mode" : [ "DISABLED", "DISABLED" ],
      "exempt_time" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "list" : [ "list", "list" ]
    }
  }, {
    "flags" : [ "NOT_SET", "NOT_SET" ],
    "name" : "name",
    "usage_threshold" : {
      "number" : 4.145608029883936,
      "set" : true,
      "infinite" : true
    },
    "description" : "description",
    "usage_factor" : {
      "number" : 4.145608029883936,
      "set" : true,
      "infinite" : true
    },
    "id" : 3,
    "priority" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "limits" : {
      "min" : {
        "priority_threshold" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "tres" : {
          "per" : {
            "job" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ]
          }
        }
      },
      "max" : {
        "jobs" : {
          "count" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "per" : {
            "user" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            },
            "account" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            }
          },
          "active_jobs" : {
            "per" : {
              "user" : {
                "number" : 5,
                "set" : true,
                "infinite" : true
              },
              "account" : {
                "number" : 5,
                "set" : true,
                "infinite" : true
              }
            }
          }
        },
        "accruing" : {
          "per" : {
            "user" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            },
            "account" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            }
          }
        },
        "tres" : {
          "total" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "minutes" : {
            "total" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ],
            "per" : {
              "qos" : [ {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              }, {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              } ],
              "job" : [ {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              }, {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              } ],
              "user" : [ {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              }, {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              } ],
              "account" : [ {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              }, {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              } ]
            }
          },
          "per" : {
            "node" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ],
            "job" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ],
            "user" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ],
            "account" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ]
          }
        },
        "wall_clock" : {
          "per" : {
            "qos" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            },
            "job" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            }
          }
        },
        "active_jobs" : {
          "count" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "accruing" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          }
        }
      },
      "factor" : {
        "number" : 4.145608029883936,
        "set" : true,
        "infinite" : true
      },
      "grace_time" : 2
    },
    "preempt" : {
      "mode" : [ "DISABLED", "DISABLED" ],
      "exempt_time" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "list" : [ "list", "list" ]
    }
  } ],
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces

This API call produces the following media types according to the Accept request header;
the media type will be conveyed by the Content-Type response header.

* `application/json`

### Responses

#### 200

QOS information
[v0.0.44\_openapi\_slurmdbd\_qos\_resp](#v0.0.44_openapi_slurmdbd_qos_resp)

#### default

QOS information
[v0.0.44\_openapi\_slurmdbd\_qos\_resp](#v0.0.44_openapi_slurmdbd_qos_resp)



---

[Up](#__Methods)

```
get /slurmdb/v0.0.44/tres/
```

Get TRES info (slurmdbV0044GetTres)

### Return type

[v0.0.44\_openapi\_tres\_resp](#v0.0.44_openapi_tres_resp)

### Example data

Content-Type: application/json

```
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "TRES" : [ {
    "name" : "name",
    "count" : 0,
    "id" : 7,
    "type" : "type"
  }, {
    "name" : "name",
    "count" : 0,
    "id" : 7,
    "type" : "type"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces

This API call produces the following media types according to the Accept request header;
the media type will be conveyed by the Content-Type response header.

* `application/json`

### Responses

#### 200

List of TRES
[v0.0.44\_openapi\_tres\_resp](#v0.0.44_openapi_tres_resp)

#### default

List of TRES
[v0.0.44\_openapi\_tres\_resp](#v0.0.44_openapi_tres_resp)



---

[Up](#__Methods)

```
get /slurmdb/v0.0.44/user/{name}
```

Get user info (slurmdbV0044GetUser)

### Path parameters

name (required)

Path Parameter — User name default: null

### Query parameters

with\_deleted (optional)

Query Parameter — Include deleted users default: null

with\_assocs (optional)

Query Parameter — Include associations default: null

with\_coords (optional)

Query Parameter — Include coordinators default: null

with\_wckeys (optional)

Query Parameter — Include WCKeys default: null

### Return type

[v0.0.44\_openapi\_users\_resp](#v0.0.44_openapi_users_resp)

### Example data

Content-Type: application/json

```
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "users" : [ {
    "associations" : [ {
      "cluster" : "cluster",
      "partition" : "partition",
      "id" : 5,
      "user" : "user",
      "account" : "account"
    }, {
      "cluster" : "cluster",
      "partition" : "partition",
      "id" : 5,
      "user" : "user",
      "account" : "account"
    } ],
    "default" : {
      "qos" : 1,
      "wckey" : "wckey",
      "account" : "account"
    },
    "administrator_level" : [ "Not Set", "Not Set" ],
    "old_name" : "old_name",
    "wckeys" : [ {
      "cluster" : "cluster",
      "name" : "name",
      "flags" : [ "DELETED", "DELETED" ],
      "accounting" : [ {
        "start" : 7,
        "id" : 5,
        "TRES" : {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        },
        "allocated" : {
          "seconds" : 5
        },
        "id_alt" : 2
      }, {
        "start" : 7,
        "id" : 5,
        "TRES" : {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        },
        "allocated" : {
          "seconds" : 5
        },
        "id_alt" : 2
      } ],
      "id" : 9,
      "user" : "user"
    }, {
      "cluster" : "cluster",
      "name" : "name",
      "flags" : [ "DELETED", "DELETED" ],
      "accounting" : [ {
        "start" : 7,
        "id" : 5,
        "TRES" : {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        },
        "allocated" : {
          "seconds" : 5
        },
        "id_alt" : 2
      }, {
        "start" : 7,
        "id" : 5,
        "TRES" : {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        },
        "allocated" : {
          "seconds" : 5
        },
        "id_alt" : 2
      } ],
      "id" : 9,
      "user" : "user"
    } ],
    "coordinators" : [ {
      "name" : "name",
      "direct" : true
    }, {
      "name" : "name",
      "direct" : true
    } ],
    "flags" : [ "NONE", "NONE" ],
    "name" : "name"
  }, {
    "associations" : [ {
      "cluster" : "cluster",
      "partition" : "partition",
      "id" : 5,
      "user" : "user",
      "account" : "account"
    }, {
      "cluster" : "cluster",
      "partition" : "partition",
      "id" : 5,
      "user" : "user",
      "account" : "account"
    } ],
    "default" : {
      "qos" : 1,
      "wckey" : "wckey",
      "account" : "account"
    },
    "administrator_level" : [ "Not Set", "Not Set" ],
    "old_name" : "old_name",
    "wckeys" : [ {
      "cluster" : "cluster",
      "name" : "name",
      "flags" : [ "DELETED", "DELETED" ],
      "accounting" : [ {
        "start" : 7,
        "id" : 5,
        "TRES" : {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        },
        "allocated" : {
          "seconds" : 5
        },
        "id_alt" : 2
      }, {
        "start" : 7,
        "id" : 5,
        "TRES" : {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        },
        "allocated" : {
          "seconds" : 5
        },
        "id_alt" : 2
      } ],
      "id" : 9,
      "user" : "user"
    }, {
      "cluster" : "cluster",
      "name" : "name",
      "flags" : [ "DELETED", "DELETED" ],
      "accounting" : [ {
        "start" : 7,
        "id" : 5,
        "TRES" : {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        },
        "allocated" : {
          "seconds" : 5
        },
        "id_alt" : 2
      }, {
        "start" : 7,
        "id" : 5,
        "TRES" : {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        },
        "allocated" : {
          "seconds" : 5
        },
        "id_alt" : 2
      } ],
      "id" : 9,
      "user" : "user"
    } ],
    "coordinators" : [ {
      "name" : "name",
      "direct" : true
    }, {
      "name" : "name",
      "direct" : true
    } ],
    "flags" : [ "NONE", "NONE" ],
    "name" : "name"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces

This API call produces the following media types according to the Accept request header;
the media type will be conveyed by the Content-Type response header.

* `application/json`

### Responses

#### 200

List of users
[v0.0.44\_openapi\_users\_resp](#v0.0.44_openapi_users_resp)

#### default

List of users
[v0.0.44\_openapi\_users\_resp](#v0.0.44_openapi_users_resp)



---

[Up](#__Methods)

```
get /slurmdb/v0.0.44/users/
```

Get user list (slurmdbV0044GetUsers)

### Query parameters

admin\_level (optional)

Query Parameter — Administrator level default: null

default\_account (optional)

Query Parameter — CSV default account list default: null

default\_wckey (optional)

Query Parameter — CSV default WCKey list default: null

with\_assocs (optional)

Query Parameter — With associations default: null

with\_coords (optional)

Query Parameter — With coordinators default: null

with\_deleted (optional)

Query Parameter — With deleted default: null

with\_wckeys (optional)

Query Parameter — With WCKeys default: null

without\_defaults (optional)

Query Parameter — Exclude defaults default: null

### Return type

[v0.0.44\_openapi\_users\_resp](#v0.0.44_openapi_users_resp)

### Example data

Content-Type: application/json

```
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "users" : [ {
    "associations" : [ {
      "cluster" : "cluster",
      "partition" : "partition",
      "id" : 5,
      "user" : "user",
      "account" : "account"
    }, {
      "cluster" : "cluster",
      "partition" : "partition",
      "id" : 5,
      "user" : "user",
      "account" : "account"
    } ],
    "default" : {
      "qos" : 1,
      "wckey" : "wckey",
      "account" : "account"
    },
    "administrator_level" : [ "Not Set", "Not Set" ],
    "old_name" : "old_name",
    "wckeys" : [ {
      "cluster" : "cluster",
      "name" : "name",
      "flags" : [ "DELETED", "DELETED" ],
      "accounting" : [ {
        "start" : 7,
        "id" : 5,
        "TRES" : {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        },
        "allocated" : {
          "seconds" : 5
        },
        "id_alt" : 2
      }, {
        "start" : 7,
        "id" : 5,
        "TRES" : {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        },
        "allocated" : {
          "seconds" : 5
        },
        "id_alt" : 2
      } ],
      "id" : 9,
      "user" : "user"
    }, {
      "cluster" : "cluster",
      "name" : "name",
      "flags" : [ "DELETED", "DELETED" ],
      "accounting" : [ {
        "start" : 7,
        "id" : 5,
        "TRES" : {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        },
        "allocated" : {
          "seconds" : 5
        },
        "id_alt" : 2
      }, {
        "start" : 7,
        "id" : 5,
        "TRES" : {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        },
        "allocated" : {
          "seconds" : 5
        },
        "id_alt" : 2
      } ],
      "id" : 9,
      "user" : "user"
    } ],
    "coordinators" : [ {
      "name" : "name",
      "direct" : true
    }, {
      "name" : "name",
      "direct" : true
    } ],
    "flags" : [ "NONE", "NONE" ],
    "name" : "name"
  }, {
    "associations" : [ {
      "cluster" : "cluster",
      "partition" : "partition",
      "id" : 5,
      "user" : "user",
      "account" : "account"
    }, {
      "cluster" : "cluster",
      "partition" : "partition",
      "id" : 5,
      "user" : "user",
      "account" : "account"
    } ],
    "default" : {
      "qos" : 1,
      "wckey" : "wckey",
      "account" : "account"
    },
    "administrator_level" : [ "Not Set", "Not Set" ],
    "old_name" : "old_name",
    "wckeys" : [ {
      "cluster" : "cluster",
      "name" : "name",
      "flags" : [ "DELETED", "DELETED" ],
      "accounting" : [ {
        "start" : 7,
        "id" : 5,
        "TRES" : {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        },
        "allocated" : {
          "seconds" : 5
        },
        "id_alt" : 2
      }, {
        "start" : 7,
        "id" : 5,
        "TRES" : {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        },
        "allocated" : {
          "seconds" : 5
        },
        "id_alt" : 2
      } ],
      "id" : 9,
      "user" : "user"
    }, {
      "cluster" : "cluster",
      "name" : "name",
      "flags" : [ "DELETED", "DELETED" ],
      "accounting" : [ {
        "start" : 7,
        "id" : 5,
        "TRES" : {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        },
        "allocated" : {
          "seconds" : 5
        },
        "id_alt" : 2
      }, {
        "start" : 7,
        "id" : 5,
        "TRES" : {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        },
        "allocated" : {
          "seconds" : 5
        },
        "id_alt" : 2
      } ],
      "id" : 9,
      "user" : "user"
    } ],
    "coordinators" : [ {
      "name" : "name",
      "direct" : true
    }, {
      "name" : "name",
      "direct" : true
    } ],
    "flags" : [ "NONE", "NONE" ],
    "name" : "name"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces

This API call produces the following media types according to the Accept request header;
the media type will be conveyed by the Content-Type response header.

* `application/json`

### Responses

#### 200

List of users
[v0.0.44\_openapi\_users\_resp](#v0.0.44_openapi_users_resp)

#### default

List of users
[v0.0.44\_openapi\_users\_resp](#v0.0.44_openapi_users_resp)



---

[Up](#__Methods)

```
get /slurmdb/v0.0.44/wckey/{id}
```

Get wckey info (slurmdbV0044GetWckey)

### Path parameters

id (required)

Path Parameter — WCKey ID default: null

### Return type

[v0.0.44\_openapi\_wckey\_resp](#v0.0.44_openapi_wckey_resp)

### Example data

Content-Type: application/json

```
{
  "wckeys" : [ {
    "cluster" : "cluster",
    "name" : "name",
    "flags" : [ "DELETED", "DELETED" ],
    "accounting" : [ {
      "start" : 7,
      "id" : 5,
      "TRES" : {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      },
      "allocated" : {
        "seconds" : 5
      },
      "id_alt" : 2
    }, {
      "start" : 7,
      "id" : 5,
      "TRES" : {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      },
      "allocated" : {
        "seconds" : 5
      },
      "id_alt" : 2
    } ],
    "id" : 9,
    "user" : "user"
  }, {
    "cluster" : "cluster",
    "name" : "name",
    "flags" : [ "DELETED", "DELETED" ],
    "accounting" : [ {
      "start" : 7,
      "id" : 5,
      "TRES" : {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      },
      "allocated" : {
        "seconds" : 5
      },
      "id_alt" : 2
    }, {
      "start" : 7,
      "id" : 5,
      "TRES" : {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      },
      "allocated" : {
        "seconds" : 5
      },
      "id_alt" : 2
    } ],
    "id" : 9,
    "user" : "user"
  } ],
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces

This API call produces the following media types according to the Accept request header;
the media type will be conveyed by the Content-Type response header.

* `application/json`

### Responses

#### 200

Description of wckey
[v0.0.44\_openapi\_wckey\_resp](#v0.0.44_openapi_wckey_resp)

#### default

Description of wckey
[v0.0.44\_openapi\_wckey\_resp](#v0.0.44_openapi_wckey_resp)



---

[Up](#__Methods)

```
get /slurmdb/v0.0.44/wckeys/
```

Get wckey list (slurmdbV0044GetWckeys)

### Query parameters

cluster (optional)

Query Parameter — CSV cluster name list default: null

format (optional)

Query Parameter — Ignored; process JSON manually to control output format default: null

id (optional)

Query Parameter — CSV ID list default: null

name (optional)

Query Parameter — CSV name list default: null

only\_defaults (optional)

Query Parameter — Only query defaults default: null

usage\_end (optional)

Query Parameter — Usage end (UNIX timestamp) default: null

usage\_start (optional)

Query Parameter — Usage start (UNIX timestamp) default: null

user (optional)

Query Parameter — CSV user list default: null

with\_usage (optional)

Query Parameter — Include usage default: null

with\_deleted (optional)

Query Parameter — Include deleted WCKeys default: null

### Return type

[v0.0.44\_openapi\_wckey\_resp](#v0.0.44_openapi_wckey_resp)

### Example data

Content-Type: application/json

```
{
  "wckeys" : [ {
    "cluster" : "cluster",
    "name" : "name",
    "flags" : [ "DELETED", "DELETED" ],
    "accounting" : [ {
      "start" : 7,
      "id" : 5,
      "TRES" : {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      },
      "allocated" : {
        "seconds" : 5
      },
      "id_alt" : 2
    }, {
      "start" : 7,
      "id" : 5,
      "TRES" : {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      },
      "allocated" : {
        "seconds" : 5
      },
      "id_alt" : 2
    } ],
    "id" : 9,
    "user" : "user"
  }, {
    "cluster" : "cluster",
    "name" : "name",
    "flags" : [ "DELETED", "DELETED" ],
    "accounting" : [ {
      "start" : 7,
      "id" : 5,
      "TRES" : {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      },
      "allocated" : {
        "seconds" : 5
      },
      "id_alt" : 2
    }, {
      "start" : 7,
      "id" : 5,
      "TRES" : {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      },
      "allocated" : {
        "seconds" : 5
      },
      "id_alt" : 2
    } ],
    "id" : 9,
    "user" : "user"
  } ],
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces

This API call produces the following media types according to the Accept request header;
the media type will be conveyed by the Content-Type response header.

* `application/json`

### Responses

#### 200

List of wckeys
[v0.0.44\_openapi\_wckey\_resp](#v0.0.44_openapi_wckey_resp)

#### default

List of wckeys
[v0.0.44\_openapi\_wckey\_resp](#v0.0.44_openapi_wckey_resp)



---

[Up](#__Methods)

```
post /slurmdb/v0.0.44/accounts/
```

Add/update list of accounts (slurmdbV0044PostAccounts)

### Consumes

This API call consumes the following media types via the Content-Type request header:

* `application/json`

### Request body

v0.0.44\_openapi\_accounts\_resp [v0.0.44\_openapi\_accounts\_resp](#v0.0.44_openapi_accounts_resp) (optional)

Body Parameter —

### Return type

[v0.0.44\_openapi\_resp](#v0.0.44_openapi_resp)

### Example data

Content-Type: application/json

```
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces

This API call produces the following media types according to the Accept request header;
the media type will be conveyed by the Content-Type response header.

* `application/json`

### Responses

#### 200

Status of account update request
[v0.0.44\_openapi\_resp](#v0.0.44_openapi_resp)

#### default

Status of account update request
[v0.0.44\_openapi\_resp](#v0.0.44_openapi_resp)



---

[Up](#__Methods)

```
post /slurmdb/v0.0.44/accounts_association/
```

Add accounts with conditional association (slurmdbV0044PostAccountsAssociation)

### Consumes

This API call consumes the following media types via the Content-Type request header:

* `application/json`

### Request body

v0.0.44\_openapi\_accounts\_add\_cond\_resp [v0.0.44\_openapi\_accounts\_add\_cond\_resp](#v0.0.44_openapi_accounts_add_cond_resp) (optional)

Body Parameter —

### Return type

[v0.0.44\_openapi\_accounts\_add\_cond\_resp\_str](#v0.0.44_openapi_accounts_add_cond_resp_str)

### Example data

Content-Type: application/json

```
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ],
  "added_accounts" : "added_accounts"
}
```

### Produces

This API call produces the following media types according to the Accept request header;
the media type will be conveyed by the Content-Type response header.

* `application/json`

### Responses

#### 200

Status of account addition request
[v0.0.44\_openapi\_accounts\_add\_cond\_resp\_str](#v0.0.44_openapi_accounts_add_cond_resp_str)

#### default

Status of account addition request
[v0.0.44\_openapi\_accounts\_add\_cond\_resp\_str](#v0.0.44_openapi_accounts_add_cond_resp_str)



---

[Up](#__Methods)

```
post /slurmdb/v0.0.44/associations/
```

Set associations info (slurmdbV0044PostAssociations)

### Consumes

This API call consumes the following media types via the Content-Type request header:

* `application/json`

### Request body

v0.0.44\_openapi\_assocs\_resp [v0.0.44\_openapi\_assocs\_resp](#v0.0.44_openapi_assocs_resp) (optional)

Body Parameter —

### Return type

[v0.0.44\_openapi\_resp](#v0.0.44_openapi_resp)

### Example data

Content-Type: application/json

```
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces

This API call produces the following media types according to the Accept request header;
the media type will be conveyed by the Content-Type response header.

* `application/json`

### Responses

#### 200

status of associations update
[v0.0.44\_openapi\_resp](#v0.0.44_openapi_resp)

#### default

status of associations update
[v0.0.44\_openapi\_resp](#v0.0.44_openapi_resp)



---

[Up](#__Methods)

```
post /slurmdb/v0.0.44/clusters/
```

Get cluster list (slurmdbV0044PostClusters)

### Consumes

This API call consumes the following media types via the Content-Type request header:

* `application/json`

### Request body

v0.0.44\_openapi\_clusters\_resp [v0.0.44\_openapi\_clusters\_resp](#v0.0.44_openapi_clusters_resp) (optional)

Body Parameter —

### Query parameters

update\_time (optional)

Query Parameter — Query reservations updated more recently than this time (UNIX timestamp) default: null

### Return type

[v0.0.44\_openapi\_resp](#v0.0.44_openapi_resp)

### Example data

Content-Type: application/json

```
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces

This API call produces the following media types according to the Accept request header;
the media type will be conveyed by the Content-Type response header.

* `application/json`

### Responses

#### 200

Result of modify clusters request
[v0.0.44\_openapi\_resp](#v0.0.44_openapi_resp)

#### default

Result of modify clusters request
[v0.0.44\_openapi\_resp](#v0.0.44_openapi_resp)



---

[Up](#__Methods)

```
post /slurmdb/v0.0.44/config
```

Load all configuration information (slurmdbV0044PostConfig)

### Consumes

This API call consumes the following media types via the Content-Type request header:

* `application/json`

### Request body

v0.0.44\_openapi\_slurmdbd\_config\_resp [v0.0.44\_openapi\_slurmdbd\_config\_resp](#v0.0.44_openapi_slurmdbd_config_resp) (optional)

Body Parameter —

### Return type

[v0.0.44\_openapi\_resp](#v0.0.44_openapi_resp)

### Example data

Content-Type: application/json

```
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces

This API call produces the following media types according to the Accept request header;
the media type will be conveyed by the Content-Type response header.

* `application/json`

### Responses

#### 200

slurmdbd configuration
[v0.0.44\_openapi\_resp](#v0.0.44_openapi_resp)

#### default

slurmdbd configuration
[v0.0.44\_openapi\_resp](#v0.0.44_openapi_resp)



---

[Up](#__Methods)

```
post /slurmdb/v0.0.44/job/{job_id}
```

Update job (slurmdbV0044PostJob)

### Path parameters

job\_id (required)

Path Parameter — Job ID default: null

### Consumes

This API call consumes the following media types via the Content-Type request header:

* `application/json`

### Request body

v0.0.44\_job\_modify [v0.0.44\_job\_modify](#v0.0.44_job_modify) (optional)

Body Parameter —

### Return type

[v0.0.44\_openapi\_job\_modify\_resp](#v0.0.44_openapi_job_modify_resp)

### Example data

Content-Type: application/json

```
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "results" : [ "results", "results" ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces

This API call produces the following media types according to the Accept request header;
the media type will be conveyed by the Content-Type response header.

* `application/json`

### Responses

#### 200

Job update results
[v0.0.44\_openapi\_job\_modify\_resp](#v0.0.44_openapi_job_modify_resp)

#### default

Job update results
[v0.0.44\_openapi\_job\_modify\_resp](#v0.0.44_openapi_job_modify_resp)



---

[Up](#__Methods)

```
post /slurmdb/v0.0.44/jobs/
```

Update jobs (slurmdbV0044PostJobs)

### Consumes

This API call consumes the following media types via the Content-Type request header:

* `application/json`

### Request body

v0.0.44\_openapi\_job\_modify\_req [v0.0.44\_openapi\_job\_modify\_req](#v0.0.44_openapi_job_modify_req) (optional)

Body Parameter —

### Return type

[v0.0.44\_openapi\_job\_modify\_resp](#v0.0.44_openapi_job_modify_resp)

### Example data

Content-Type: application/json

```
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "results" : [ "results", "results" ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces

This API call produces the following media types according to the Accept request header;
the media type will be conveyed by the Content-Type response header.

* `application/json`

### Responses

#### 200

Job update results
[v0.0.44\_openapi\_job\_modify\_resp](#v0.0.44_openapi_job_modify_resp)

#### default

Job update results
[v0.0.44\_openapi\_job\_modify\_resp](#v0.0.44_openapi_job_modify_resp)



---

[Up](#__Methods)

```
post /slurmdb/v0.0.44/qos/
```

Add or update QOSs (slurmdbV0044PostQos)

### Consumes

This API call consumes the following media types via the Content-Type request header:

* `application/json`

### Request body

v0.0.44\_openapi\_slurmdbd\_qos\_resp [v0.0.44\_openapi\_slurmdbd\_qos\_resp](#v0.0.44_openapi_slurmdbd_qos_resp) (optional)

Body Parameter —

### Query parameters

description (optional)

Query Parameter — CSV description list default: null

Include deleted QOS (optional)

Query Parameter — default: null

id (optional)

Query Parameter — CSV QOS id list default: null

format (optional)

Query Parameter — Ignored; process JSON manually to control output format default: null

name (optional)

Query Parameter — CSV QOS name list default: null

preempt\_mode (optional)

Query Parameter — PreemptMode used when jobs in this QOS are preempted default: null

### Return type

[v0.0.44\_openapi\_resp](#v0.0.44_openapi_resp)

### Example data

Content-Type: application/json

```
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces

This API call produces the following media types according to the Accept request header;
the media type will be conveyed by the Content-Type response header.

* `application/json`

### Responses

#### 200

QOS update response
[v0.0.44\_openapi\_resp](#v0.0.44_openapi_resp)

#### default

QOS update response
[v0.0.44\_openapi\_resp](#v0.0.44_openapi_resp)



---

[Up](#__Methods)

```
post /slurmdb/v0.0.44/tres/
```

Add TRES (slurmdbV0044PostTres)

### Consumes

This API call consumes the following media types via the Content-Type request header:

* `application/json`

### Request body

v0.0.44\_openapi\_tres\_resp [v0.0.44\_openapi\_tres\_resp](#v0.0.44_openapi_tres_resp) (optional)

Body Parameter —

### Return type

[v0.0.44\_openapi\_resp](#v0.0.44_openapi_resp)

### Example data

Content-Type: application/json

```
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces

This API call produces the following media types according to the Accept request header;
the media type will be conveyed by the Content-Type response header.

* `application/json`

### Responses

#### 200

TRES update result
[v0.0.44\_openapi\_resp](#v0.0.44_openapi_resp)

#### default

TRES update result
[v0.0.44\_openapi\_resp](#v0.0.44_openapi_resp)



---

[Up](#__Methods)

```
post /slurmdb/v0.0.44/users/
```

Update users (slurmdbV0044PostUsers)

### Consumes

This API call consumes the following media types via the Content-Type request header:

* `application/json`

### Request body

v0.0.44\_openapi\_users\_resp [v0.0.44\_openapi\_users\_resp](#v0.0.44_openapi_users_resp) (optional)

Body Parameter —

### Return type

[v0.0.44\_openapi\_resp](#v0.0.44_openapi_resp)

### Example data

Content-Type: application/json

```
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces

This API call produces the following media types according to the Accept request header;
the media type will be conveyed by the Content-Type response header.

* `application/json`

### Responses

#### 200

Status of user update request
[v0.0.44\_openapi\_resp](#v0.0.44_openapi_resp)

#### default

Status of user update request
[v0.0.44\_openapi\_resp](#v0.0.44_openapi_resp)



---

[Up](#__Methods)

```
post /slurmdb/v0.0.44/users_association/
```

Add users with conditional association (slurmdbV0044PostUsersAssociation)

### Consumes

This API call consumes the following media types via the Content-Type request header:

* `application/json`

### Request body

v0.0.44\_openapi\_users\_add\_cond\_resp [v0.0.44\_openapi\_users\_add\_cond\_resp](#v0.0.44_openapi_users_add_cond_resp) (optional)

Body Parameter —

### Query parameters

update\_time (optional)

Query Parameter — Query partitions updated more recently than this time (UNIX timestamp) default: null

flags (optional)

Query Parameter — Query flags default: null

### Return type

[v0.0.44\_openapi\_users\_add\_cond\_resp\_str](#v0.0.44_openapi_users_add_cond_resp_str)

### Example data

Content-Type: application/json

```
{
  "added_users" : "added_users",
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces

This API call produces the following media types according to the Accept request header;
the media type will be conveyed by the Content-Type response header.

* `application/json`

### Responses

#### 200

Add list of users with conditional association
[v0.0.44\_openapi\_users\_add\_cond\_resp\_str](#v0.0.44_openapi_users_add_cond_resp_str)

#### default

Add list of users with conditional association
[v0.0.44\_openapi\_users\_add\_cond\_resp\_str](#v0.0.44_openapi_users_add_cond_resp_str)



---

[Up](#__Methods)

```
post /slurmdb/v0.0.44/wckeys/
```

Add or update wckeys (slurmdbV0044PostWckeys)

### Consumes

This API call consumes the following media types via the Content-Type request header:

* `application/json`

### Request body

v0.0.44\_openapi\_wckey\_resp [v0.0.44\_openapi\_wckey\_resp](#v0.0.44_openapi_wckey_resp) (optional)

Body Parameter —

### Query parameters

cluster (optional)

Query Parameter — CSV cluster name list default: null

format (optional)

Query Parameter — Ignored; process JSON manually to control output format default: null

id (optional)

Query Parameter — CSV ID list default: null

name (optional)

Query Parameter — CSV name list default: null

only\_defaults (optional)

Query Parameter — Only query defaults default: null

usage\_end (optional)

Query Parameter — Usage end (UNIX timestamp) default: null

usage\_start (optional)

Query Parameter — Usage start (UNIX timestamp) default: null

user (optional)

Query Parameter — CSV user list default: null

with\_usage (optional)

Query Parameter — Include usage default: null

with\_deleted (optional)

Query Parameter — Include deleted WCKeys default: null

### Return type

[v0.0.44\_openapi\_resp](#v0.0.44_openapi_resp)

### Example data

Content-Type: application/json

```
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces

This API call produces the following media types according to the Accept request header;
the media type will be conveyed by the Content-Type response header.

* `application/json`

### Responses

#### 200

Result of wckey addition or update request
[v0.0.44\_openapi\_resp](#v0.0.44_openapi_resp)

#### default

Result of wckey addition or update request
[v0.0.44\_openapi\_resp](#v0.0.44_openapi_resp)



---

## Models

[ Jump to [Methods](#__Methods) ]

### Table of Contents

1. [`v0.0.44_account` -](#v0.0.44_account)
2. [`v0.0.44_account_short` -](#v0.0.44_account_short)
3. [`v0.0.44_accounting` -](#v0.0.44_accounting)
4. [`v0.0.44_accounts_add_cond` -](#v0.0.44_accounts_add_cond)
5. [`v0.0.44_acct_gather_energy` -](#v0.0.44_acct_gather_energy)
6. [`v0.0.44_assoc` -](#v0.0.44_assoc)
7. [`v0.0.44_assoc_rec_set` -](#v0.0.44_assoc_rec_set)
8. [`v0.0.44_assoc_shares_obj_wrap` -](#v0.0.44_assoc_shares_obj_wrap)
9. [`v0.0.44_assoc_short` -](#v0.0.44_assoc_short)
10. [`v0.0.44_bf_exit_fields` -](#v0.0.44_bf_exit_fields)
11. [`v0.0.44_cluster_rec` -](#v0.0.44_cluster_rec)
12. [`v0.0.44_controller_ping` -](#v0.0.44_controller_ping)
13. [`v0.0.44_coord` -](#v0.0.44_coord)
14. [`v0.0.44_cron_entry` -](#v0.0.44_cron_entry)
15. [`v0.0.44_float64_no_val_struct` -](#v0.0.44_float64_no_val_struct)
16. [`v0.0.44_instance` -](#v0.0.44_instance)
17. [`v0.0.44_job` -](#v0.0.44_job)
18. [`v0.0.44_job_alloc_req` -](#v0.0.44_job_alloc_req)
19. [`v0.0.44_job_array_response_msg_entry` -](#v0.0.44_job_array_response_msg_entry)
20. [`v0.0.44_job_desc_msg` -](#v0.0.44_job_desc_msg)
21. [`v0.0.44_job_info` -](#v0.0.44_job_info)
22. [`v0.0.44_job_modify` -](#v0.0.44_job_modify)
23. [`v0.0.44_job_res` -](#v0.0.44_job_res)
24. [`v0.0.44_job_res_core` -](#v0.0.44_job_res_core)
25. [`v0.0.44_job_res_node` -](#v0.0.44_job_res_node)
26. [`v0.0.44_job_res_socket` -](#v0.0.44_job_res_socket)
27. [`v0.0.44_job_submit_req` -](#v0.0.44_job_submit_req)
28. [`v0.0.44_kill_jobs_msg` -](#v0.0.44_kill_jobs_msg)
29. [`v0.0.44_kill_jobs_resp_job` -](#v0.0.44_kill_jobs_resp_job)
30. [`v0.0.44_license` -](#v0.0.44_license)
31. [`v0.0.44_node` -](#v0.0.44_node)
32. [`v0.0.44_node_gres_layout` -](#v0.0.44_node_gres_layout)
33. [`v0.0.44_node_resource_layout` -](#v0.0.44_node_resource_layout)
34. [`v0.0.44_openapi_accounts_add_cond_resp` -](#v0.0.44_openapi_accounts_add_cond_resp)
35. [`v0.0.44_openapi_accounts_add_cond_resp_str` -](#v0.0.44_openapi_accounts_add_cond_resp_str)
36. [`v0.0.44_openapi_accounts_removed_resp` -](#v0.0.44_openapi_accounts_removed_resp)
37. [`v0.0.44_openapi_accounts_resp` -](#v0.0.44_openapi_accounts_resp)
38. [`v0.0.44_openapi_assocs_removed_resp` -](#v0.0.44_openapi_assocs_removed_resp)
39. [`v0.0.44_openapi_assocs_resp` -](#v0.0.44_openapi_assocs_resp)
40. [`v0.0.44_openapi_clusters_removed_resp` -](#v0.0.44_openapi_clusters_removed_resp)
41. [`v0.0.44_openapi_clusters_resp` -](#v0.0.44_openapi_clusters_resp)
42. [`v0.0.44_openapi_create_node_req` -](#v0.0.44_openapi_create_node_req)
43. [`v0.0.44_openapi_diag_resp` -](#v0.0.44_openapi_diag_resp)
44. [`v0.0.44_openapi_error` -](#v0.0.44_openapi_error)
45. [`v0.0.44_openapi_instances_resp` -](#v0.0.44_openapi_instances_resp)
46. [`v0.0.44_openapi_job_alloc_resp` -](#v0.0.44_openapi_job_alloc_resp)
47. [`v0.0.44_openapi_job_info_resp` -](#v0.0.44_openapi_job_info_resp)
48. [`v0.0.44_openapi_job_modify_req` -](#v0.0.44_openapi_job_modify_req)
49. [`v0.0.44_openapi_job_modify_resp` -](#v0.0.44_openapi_job_modify_resp)
50. [`v0.0.44_openapi_job_post_response` -](#v0.0.44_openapi_job_post_response)
51. [`v0.0.44_openapi_job_submit_response` -](#v0.0.44_openapi_job_submit_response)
52. [`v0.0.44_openapi_kill_job_resp` -](#v0.0.44_openapi_kill_job_resp)
53. [`v0.0.44_openapi_kill_jobs_resp` -](#v0.0.44_openapi_kill_jobs_resp)
54. [`v0.0.44_openapi_licenses_resp` -](#v0.0.44_openapi_licenses_resp)
55. [`v0.0.44_openapi_meta` -](#v0.0.44_openapi_meta)
56. [`v0.0.44_openapi_nodes_resp` -](#v0.0.44_openapi_nodes_resp)
57. [`v0.0.44_openapi_partition_resp` -](#v0.0.44_openapi_partition_resp)
58. [`v0.0.44_openapi_ping_array_resp` -](#v0.0.44_openapi_ping_array_resp)
59. [`v0.0.44_openapi_reservation_mod_resp` -](#v0.0.44_openapi_reservation_mod_resp)
60. [`v0.0.44_openapi_reservation_resp` -](#v0.0.44_openapi_reservation_resp)
61. [`v0.0.44_openapi_resource_layout_resp` -](#v0.0.44_openapi_resource_layout_resp)
62. [`v0.0.44_openapi_resp` -](#v0.0.44_openapi_resp)
63. [`v0.0.44_openapi_shares_resp` -](#v0.0.44_openapi_shares_resp)
64. [`v0.0.44_openapi_slurmdbd_config_resp` -](#v0.0.44_openapi_slurmdbd_config_resp)
65. [`v0.0.44_openapi_slurmdbd_jobs_resp` -](#v0.0.44_openapi_slurmdbd_jobs_resp)
66. [`v0.0.44_openapi_slurmdbd_ping_resp` -](#v0.0.44_openapi_slurmdbd_ping_resp)
67. [`v0.0.44_openapi_slurmdbd_qos_removed_resp` -](#v0.0.44_openapi_slurmdbd_qos_removed_resp)
68. [`v0.0.44_openapi_slurmdbd_qos_resp` -](#v0.0.44_openapi_slurmdbd_qos_resp)
69. [`v0.0.44_openapi_slurmdbd_stats_resp` -](#v0.0.44_openapi_slurmdbd_stats_resp)
70. [`v0.0.44_openapi_tres_resp` -](#v0.0.44_openapi_tres_resp)
71. [`v0.0.44_openapi_users_add_cond_resp` -](#v0.0.44_openapi_users_add_cond_resp)
72. [`v0.0.44_openapi_users_add_cond_resp_str` -](#v0.0.44_openapi_users_add_cond_resp_str)
73. [`v0.0.44_openapi_users_resp` -](#v0.0.44_openapi_users_resp)
74. [`v0.0.44_openapi_warning` -](#v0.0.44_openapi_warning)
75. [`v0.0.44_openapi_wckey_removed_resp` -](#v0.0.44_openapi_wckey_removed_resp)
76. [`v0.0.44_openapi_wckey_resp` -](#v0.0.44_openapi_wckey_resp)
77. [`v0.0.44_part_prio` -](#v0.0.44_part_prio)
78. [`v0.0.44_partition_info` -](#v0.0.44_partition_info)
79. [`v0.0.44_process_exit_code_verbose` -](#v0.0.44_process_exit_code_verbose)
80. [`v0.0.44_qos` -](#v0.0.44_qos)
81. [`v0.0.44_reservation_core_spec` -](#v0.0.44_reservation_core_spec)
82. [`v0.0.44_reservation_desc_msg` -](#v0.0.44_reservation_desc_msg)
83. [`v0.0.44_reservation_info` -](#v0.0.44_reservation_info)
84. [`v0.0.44_reservation_mod_req` -](#v0.0.44_reservation_mod_req)
85. [`v0.0.44_rollup_stats` -](#v0.0.44_rollup_stats)
86. [`v0.0.44_schedule_exit_fields` -](#v0.0.44_schedule_exit_fields)
87. [`v0.0.44_shares_float128_tres` -](#v0.0.44_shares_float128_tres)
88. [`v0.0.44_shares_resp_msg` -](#v0.0.44_shares_resp_msg)
89. [`v0.0.44_shares_uint64_tres` -](#v0.0.44_shares_uint64_tres)
90. [`v0.0.44_slurm_step_id` -](#v0.0.44_slurm_step_id)
91. [`v0.0.44_slurmdbd_ping` -](#v0.0.44_slurmdbd_ping)
92. [`v0.0.44_stats_msg` -](#v0.0.44_stats_msg)
93. [`v0.0.44_stats_msg_rpc_dump` -](#v0.0.44_stats_msg_rpc_dump)
94. [`v0.0.44_stats_msg_rpc_queue` -](#v0.0.44_stats_msg_rpc_queue)
95. [`v0.0.44_stats_msg_rpc_type` -](#v0.0.44_stats_msg_rpc_type)
96. [`v0.0.44_stats_msg_rpc_user` -](#v0.0.44_stats_msg_rpc_user)
97. [`v0.0.44_stats_rec` -](#v0.0.44_stats_rec)
98. [`v0.0.44_stats_rpc` -](#v0.0.44_stats_rpc)
99. [`v0.0.44_stats_user` -](#v0.0.44_stats_user)
100. [`v0.0.44_step` -](#v0.0.44_step)
101. [`v0.0.44_tres` -](#v0.0.44_tres)
102. [`v0.0.44_uint16_no_val_struct` -](#v0.0.44_uint16_no_val_struct)
103. [`v0.0.44_uint32_no_val_struct` -](#v0.0.44_uint32_no_val_struct)
104. [`v0.0.44_uint64_no_val_struct` -](#v0.0.44_uint64_no_val_struct)
105. [`v0.0.44_update_node_msg` -](#v0.0.44_update_node_msg)
106. [`v0.0.44_user` -](#v0.0.44_user)
107. [`v0.0.44_user_short` -](#v0.0.44_user_short)
108. [`v0.0.44_users_add_cond` -](#v0.0.44_users_add_cond)
109. [`v0.0.44_wckey` -](#v0.0.44_wckey)
110. [`v0.0.44_wckey_tag_struct` -](#v0.0.44_wckey_tag_struct)
111. [`v0_0_44_accounting_allocated` -](#v0_0_44_accounting_allocated)
112. [`v0_0_44_assoc_default` -](#v0_0_44_assoc_default)
113. [`v0_0_44_assoc_max` -](#v0_0_44_assoc_max)
114. [`v0_0_44_assoc_max_jobs` -](#v0_0_44_assoc_max_jobs)
115. [`v0_0_44_assoc_max_jobs_per` -](#v0_0_44_assoc_max_jobs_per)
116. [`v0_0_44_assoc_max_per` -](#v0_0_44_assoc_max_per)
117. [`v0_0_44_assoc_max_per_account` -](#v0_0_44_assoc_max_per_account)
118. [`v0_0_44_assoc_max_tres` -](#v0_0_44_assoc_max_tres)
119. [`v0_0_44_assoc_max_tres_group` -](#v0_0_44_assoc_max_tres_group)
120. [`v0_0_44_assoc_max_tres_minutes` -](#v0_0_44_assoc_max_tres_minutes)
121. [`v0_0_44_assoc_max_tres_per` -](#v0_0_44_assoc_max_tres_per)
122. [`v0_0_44_assoc_min` -](#v0_0_44_assoc_min)
123. [`v0_0_44_assoc_shares_obj_wrap_fairshare` -](#v0_0_44_assoc_shares_obj_wrap_fairshare)
124. [`v0_0_44_assoc_shares_obj_wrap_tres` -](#v0_0_44_assoc_shares_obj_wrap_tres)
125. [`v0_0_44_cluster_rec_associations` -](#v0_0_44_cluster_rec_associations)
126. [`v0_0_44_cluster_rec_controller` -](#v0_0_44_cluster_rec_controller)
127. [`v0_0_44_cron_entry_line` -](#v0_0_44_cron_entry_line)
128. [`v0_0_44_instance_time` -](#v0_0_44_instance_time)
129. [`v0_0_44_job_array` -](#v0_0_44_job_array)
130. [`v0_0_44_job_array_limits` -](#v0_0_44_job_array_limits)
131. [`v0_0_44_job_array_limits_max` -](#v0_0_44_job_array_limits_max)
132. [`v0_0_44_job_array_limits_max_running` -](#v0_0_44_job_array_limits_max_running)
133. [`v0_0_44_job_comment` -](#v0_0_44_job_comment)
134. [`v0_0_44_job_desc_msg_rlimits` -](#v0_0_44_job_desc_msg_rlimits)
135. [`v0_0_44_job_het` -](#v0_0_44_job_het)
136. [`v0_0_44_job_info_power` -](#v0_0_44_job_info_power)
137. [`v0_0_44_job_mcs` -](#v0_0_44_job_mcs)
138. [`v0_0_44_job_modify_tres` -](#v0_0_44_job_modify_tres)
139. [`v0_0_44_job_required` -](#v0_0_44_job_required)
140. [`v0_0_44_job_res_node_cpus` -](#v0_0_44_job_res_node_cpus)
141. [`v0_0_44_job_res_node_memory` -](#v0_0_44_job_res_node_memory)
142. [`v0_0_44_job_res_nodes` -](#v0_0_44_job_res_nodes)
143. [`v0_0_44_job_reservation` -](#v0_0_44_job_reservation)
144. [`v0_0_44_job_state` -](#v0_0_44_job_state)
145. [`v0_0_44_job_time` -](#v0_0_44_job_time)
146. [`v0_0_44_job_time_system` -](#v0_0_44_job_time_system)
147. [`v0_0_44_job_time_total` -](#v0_0_44_job_time_total)
148. [`v0_0_44_job_time_user` -](#v0_0_44_job_time_user)
149. [`v0_0_44_job_tres` -](#v0_0_44_job_tres)
150. [`v0_0_44_kill_jobs_resp_job_error` -](#v0_0_44_kill_jobs_resp_job_error)
151. [`v0_0_44_kill_jobs_resp_job_federation` -](#v0_0_44_kill_jobs_resp_job_federation)
152. [`v0_0_44_openapi_meta_client` -](#v0_0_44_openapi_meta_client)
153. [`v0_0_44_openapi_meta_plugin` -](#v0_0_44_openapi_meta_plugin)
154. [`v0_0_44_openapi_meta_slurm` -](#v0_0_44_openapi_meta_slurm)
155. [`v0_0_44_openapi_meta_slurm_version` -](#v0_0_44_openapi_meta_slurm_version)
156. [`v0_0_44_partition_info_accounts` -](#v0_0_44_partition_info_accounts)
157. [`v0_0_44_partition_info_cpus` -](#v0_0_44_partition_info_cpus)
158. [`v0_0_44_partition_info_defaults` -](#v0_0_44_partition_info_defaults)
159. [`v0_0_44_partition_info_groups` -](#v0_0_44_partition_info_groups)
160. [`v0_0_44_partition_info_maximums` -](#v0_0_44_partition_info_maximums)
161. [`v0_0_44_partition_info_maximums_oversubscribe` -](#v0_0_44_partition_info_maximums_oversubscribe)
162. [`v0_0_44_partition_info_minimums` -](#v0_0_44_partition_info_minimums)
163. [`v0_0_44_partition_info_nodes` -](#v0_0_44_partition_info_nodes)
164. [`v0_0_44_partition_info_partition` -](#v0_0_44_partition_info_partition)
165. [`v0_0_44_partition_info_priority` -](#v0_0_44_partition_info_priority)
166. [`v0_0_44_partition_info_qos` -](#v0_0_44_partition_info_qos)
167. [`v0_0_44_partition_info_timeouts` -](#v0_0_44_partition_info_timeouts)
168. [`v0_0_44_partition_info_tres` -](#v0_0_44_partition_info_tres)
169. [`v0_0_44_process_exit_code_verbose_signal` -](#v0_0_44_process_exit_code_verbose_signal)
170. [`v0_0_44_qos_limits` -](#v0_0_44_qos_limits)
171. [`v0_0_44_qos_limits_max` -](#v0_0_44_qos_limits_max)
172. [`v0_0_44_qos_limits_max_active_jobs` -](#v0_0_44_qos_limits_max_active_jobs)
173. [`v0_0_44_qos_limits_max_jobs` -](#v0_0_44_qos_limits_max_jobs)
174. [`v0_0_44_qos_limits_max_jobs_active_jobs` -](#v0_0_44_qos_limits_max_jobs_active_jobs)
175. [`v0_0_44_qos_limits_max_jobs_active_jobs_per` -](#v0_0_44_qos_limits_max_jobs_active_jobs_per)
176. [`v0_0_44_qos_limits_max_tres` -](#v0_0_44_qos_limits_max_tres)
177. [`v0_0_44_qos_limits_max_tres_minutes` -](#v0_0_44_qos_limits_max_tres_minutes)
178. [`v0_0_44_qos_limits_max_tres_minutes_per` -](#v0_0_44_qos_limits_max_tres_minutes_per)
179. [`v0_0_44_qos_limits_max_tres_per` -](#v0_0_44_qos_limits_max_tres_per)
180. [`v0_0_44_qos_limits_max_wall_clock` -](#v0_0_44_qos_limits_max_wall_clock)
181. [`v0_0_44_qos_limits_max_wall_clock_per` -](#v0_0_44_qos_limits_max_wall_clock_per)
182. [`v0_0_44_qos_limits_min` -](#v0_0_44_qos_limits_min)
183. [`v0_0_44_qos_limits_min_tres` -](#v0_0_44_qos_limits_min_tres)
184. [`v0_0_44_qos_limits_min_tres_per` -](#v0_0_44_qos_limits_min_tres_per)
185. [`v0_0_44_qos_preempt` -](#v0_0_44_qos_preempt)
186. [`v0_0_44_reservation_info_purge_completed` -](#v0_0_44_reservation_info_purge_completed)
187. [`v0_0_44_rollup_stats_daily` -](#v0_0_44_rollup_stats_daily)
188. [`v0_0_44_rollup_stats_daily_duration` -](#v0_0_44_rollup_stats_daily_duration)
189. [`v0_0_44_rollup_stats_hourly` -](#v0_0_44_rollup_stats_hourly)
190. [`v0_0_44_rollup_stats_hourly_duration` -](#v0_0_44_rollup_stats_hourly_duration)
191. [`v0_0_44_rollup_stats_monthly` -](#v0_0_44_rollup_stats_monthly)
192. [`v0_0_44_rollup_stats_monthly_duration` -](#v0_0_44_rollup_stats_monthly_duration)
193. [`v0_0_44_stats_rpc_time` -](#v0_0_44_stats_rpc_time)
194. [`v0_0_44_step_CPU` -](#v0_0_44_step_CPU)
195. [`v0_0_44_step_CPU_requested_frequency` -](#v0_0_44_step_CPU_requested_frequency)
196. [`v0_0_44_step_nodes` -](#v0_0_44_step_nodes)
197. [`v0_0_44_step_statistics` -](#v0_0_44_step_statistics)
198. [`v0_0_44_step_statistics_CPU` -](#v0_0_44_step_statistics_CPU)
199. [`v0_0_44_step_statistics_energy` -](#v0_0_44_step_statistics_energy)
200. [`v0_0_44_step_step` -](#v0_0_44_step_step)
201. [`v0_0_44_step_task` -](#v0_0_44_step_task)
202. [`v0_0_44_step_tasks` -](#v0_0_44_step_tasks)
203. [`v0_0_44_step_time` -](#v0_0_44_step_time)
204. [`v0_0_44_step_time_system` -](#v0_0_44_step_time_system)
205. [`v0_0_44_step_time_total` -](#v0_0_44_step_time_total)
206. [`v0_0_44_step_time_user` -](#v0_0_44_step_time_user)
207. [`v0_0_44_step_tres` -](#v0_0_44_step_tres)
208. [`v0_0_44_step_tres_consumed` -](#v0_0_44_step_tres_consumed)
209. [`v0_0_44_step_tres_requested` -](#v0_0_44_step_tres_requested)
210. [`v0_0_44_user_default` -](#v0_0_44_user_default)

### `v0.0.44_account` - [Up](#__Models)

associations (optional)

[array[v0.0.44\_assoc\_short]](#v0.0.44_assoc_short)

coordinators (optional)

[array[v0.0.44\_coord]](#v0.0.44_coord)

description

[String](#string) Arbitrary string describing the account

name

[String](#string) Account name

organization

[String](#string) Organization to which the account belongs

flags (optional)

[array[String]](#string) Flags associated with this account

Enum:

### `v0.0.44_account_short` - [Up](#__Models)

description (optional)

[String](#string) Arbitrary string describing the account

organization (optional)

[String](#string) Organization to which the account belongs

### `v0.0.44_accounting` - [Up](#__Models)

allocated (optional)

[v0\_0\_44\_accounting\_allocated](#v0_0_44_accounting_allocated)

id (optional)

[Integer](#integer) Association ID or Workload characterization key ID format: int32

id\_alt (optional)

[Integer](#integer) Alternate ID (not currently used) format: int32

start (optional)

[Long](#long) When the record was started (UNIX timestamp) (UNIX timestamp or time string recognized by Slurm (e.g., '[MM/DD[/YY]-]HH:MM[:SS]')) format: int64

TRES (optional)

[v0.0.44\_tres](#v0.0.44_tres)

### `v0.0.44_accounts_add_cond` - [Up](#__Models)

accounts

[array[String]](#string)

association (optional)

[v0.0.44\_assoc\_rec\_set](#v0.0.44_assoc_rec_set)

clusters (optional)

[array[String]](#string)

### `v0.0.44_acct_gather_energy` - [Up](#__Models)

average\_watts (optional)

[Integer](#integer) Average power consumption, in watts format: int32

base\_consumed\_energy (optional)

[Long](#long) The energy consumed between when the node was powered on and the last time it was registered by slurmd, in joules format: int64

consumed\_energy (optional)

[Long](#long) The energy consumed between the last time the node was registered by the slurmd daemon and the last node energy accounting sample, in joules format: int64

current\_watts (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

previous\_consumed\_energy (optional)

[Long](#long) Previous value of consumed\_energy format: int64

last\_collected (optional)

[Long](#long) Time when energy data was last retrieved (UNIX timestamp) (UNIX timestamp or time string recognized by Slurm (e.g., '[MM/DD[/YY]-]HH:MM[:SS]')) format: int64

### `v0.0.44_assoc` - [Up](#__Models)

accounting (optional)

[array[v0.0.44\_accounting]](#v0.0.44_accounting)

account (optional)

[String](#string) Account name

cluster (optional)

[String](#string) Cluster name

comment (optional)

[String](#string) Arbitrary comment

default (optional)

[v0\_0\_44\_assoc\_default](#v0_0_44_assoc_default)

flags (optional)

[array[String]](#string) Flags on the association

Enum:

max (optional)

[v0\_0\_44\_assoc\_max](#v0_0_44_assoc_max)

id (optional)

[Integer](#integer) Unique ID (Association ID) format: int32

is\_default (optional)

[Boolean](#boolean) Is default association for user

lineage (optional)

[String](#string) Complete path up the hierarchy to the root association

min (optional)

[v0\_0\_44\_assoc\_min](#v0_0_44_assoc_min)

parent\_account (optional)

[String](#string) Name of parent account

partition (optional)

[String](#string) Partition name

priority (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

qos (optional)

[array[String]](#string) List of QOS names

shares\_raw (optional)

[Integer](#integer) Allocated shares used for fairshare calculation format: int32

user

[String](#string) User name

### `v0.0.44_assoc_rec_set` - [Up](#__Models)

comment (optional)

[String](#string) Arbitrary comment

defaultqos (optional)

[String](#string) Default QOS

grpjobs (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

grpjobsaccrue (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

grpsubmitjobs (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

grptres (optional)

[array[v0.0.44\_tres]](#v0.0.44_tres)

grptresmins (optional)

[array[v0.0.44\_tres]](#v0.0.44_tres)

grptresrunmins (optional)

[array[v0.0.44\_tres]](#v0.0.44_tres)

grpwall (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

maxjobs (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

maxjobsaccrue (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

maxsubmitjobs (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

maxtresminsperjob (optional)

[array[v0.0.44\_tres]](#v0.0.44_tres)

maxtresrunmins (optional)

[array[v0.0.44\_tres]](#v0.0.44_tres)

maxtresperjob (optional)

[array[v0.0.44\_tres]](#v0.0.44_tres)

maxtrespernode (optional)

[array[v0.0.44\_tres]](#v0.0.44_tres)

maxwalldurationperjob (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

minpriothresh (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

parent (optional)

[String](#string) Name of parent account

priority (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

qoslevel (optional)

[array[String]](#string) List of QOS names

fairshare (optional)

[Integer](#integer) Allocated shares used for fairshare calculation format: int32

### `v0.0.44_assoc_shares_obj_wrap` - [Up](#__Models)

id (optional)

[Integer](#integer) Association ID format: int32

cluster (optional)

[String](#string) Cluster name

name (optional)

[String](#string) Share name

parent (optional)

[String](#string) Parent name

partition (optional)

[String](#string) Partition name

shares\_normalized (optional)

[v0.0.44\_float64\_no\_val\_struct](#v0.0.44_float64_no_val_struct)

shares (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

tres (optional)

[v0\_0\_44\_assoc\_shares\_obj\_wrap\_tres](#v0_0_44_assoc_shares_obj_wrap_tres)

effective\_usage (optional)

[v0.0.44\_float64\_no\_val\_struct](#v0.0.44_float64_no_val_struct)

usage\_normalized (optional)

[v0.0.44\_float64\_no\_val\_struct](#v0.0.44_float64_no_val_struct)

usage (optional)

[Long](#long) Measure of tresbillableunits usage format: int64

fairshare (optional)

[v0\_0\_44\_assoc\_shares\_obj\_wrap\_fairshare](#v0_0_44_assoc_shares_obj_wrap_fairshare)

type (optional)

[array[String]](#string) User or account association

Enum:

### `v0.0.44_assoc_short` - [Up](#__Models)

account (optional)

[String](#string) Account name

cluster (optional)

[String](#string) Cluster name

partition (optional)

[String](#string) Partition name

user

[String](#string) User name

id (optional)

[Integer](#integer) Numeric association ID format: int32

### `v0.0.44_bf_exit_fields` - [Up](#__Models)

end\_job\_queue (optional)

[Integer](#integer) Reached end of queue format: int32

bf\_max\_job\_start (optional)

[Integer](#integer) Reached number of jobs allowed to start format: int32

bf\_max\_job\_test (optional)

[Integer](#integer) Reached number of jobs allowed to be tested format: int32

bf\_max\_time (optional)

[Integer](#integer) Reached maximum allowed scheduler time format: int32

bf\_node\_space\_size (optional)

[Integer](#integer) Reached table size limit format: int32

state\_changed (optional)

[Integer](#integer) System state changed format: int32

### `v0.0.44_cluster_rec` - [Up](#__Models)

controller (optional)

[v0\_0\_44\_cluster\_rec\_controller](#v0_0_44_cluster_rec_controller)

flags (optional)

[array[String]](#string) Flags

Enum:

name (optional)

[String](#string) ClusterName

nodes (optional)

[String](#string) Node names

select\_plugin (optional)

[String](#string)

associations (optional)

[v0\_0\_44\_cluster\_rec\_associations](#v0_0_44_cluster_rec_associations)

rpc\_version (optional)

[Integer](#integer) RPC version used in the cluster format: int32

tres (optional)

[array[v0.0.44\_tres]](#v0.0.44_tres)

### `v0.0.44_controller_ping` - [Up](#__Models)

hostname (optional)

[String](#string) Target for ping

pinged (optional)

[String](#string) Ping result

responding

[Boolean](#boolean) If ping RPC responded with pong from controller

latency (optional)

[Long](#long) Number of microseconds it took to successfully ping or timeout format: int64

mode (optional)

[String](#string) The operating mode of the responding slurmctld

primary

[Boolean](#boolean) Is responding slurmctld the primary controller (Is responding slurmctld the primary controller)

### `v0.0.44_coord` - [Up](#__Models)

name

[String](#string) User name

direct (optional)

[Boolean](#boolean) Indicates whether the coordinator was directly assigned to this account

### `v0.0.44_cron_entry` - [Up](#__Models)

flags (optional)

[array[String]](#string) Flags

Enum:

minute (optional)

[String](#string) Ranged string specifying eligible minute values (e.g. 0-10,50)

hour (optional)

[String](#string) Ranged string specifying eligible hour values (e.g. 0-5,23)

day\_of\_month (optional)

[String](#string) Ranged string specifying eligible day of month values (e.g. 0-10,29)

month (optional)

[String](#string) Ranged string specifying eligible month values (e.g. 0-5,12)

day\_of\_week (optional)

[String](#string) Ranged string specifying eligible day of week values (e.g.0-3,7)

specification (optional)

[String](#string) Complete time specification (\* means valid for all allowed values) - minute hour day\_of\_month month day\_of\_week

command (optional)

[String](#string) Command to run

line (optional)

[v0\_0\_44\_cron\_entry\_line](#v0_0_44_cron_entry_line)

### `v0.0.44_float64_no_val_struct` - [Up](#__Models)

set (optional)

[Boolean](#boolean) True if number has been set; False if number is unset

infinite (optional)

[Boolean](#boolean) True if number has been set to infinite; "set" and "number" will be ignored

number (optional)

[Double](#double) If "set" is True the number will be set with value; otherwise ignore number contents format: double

### `v0.0.44_instance` - [Up](#__Models)

cluster (optional)

[String](#string) Cluster name

extra (optional)

[String](#string) Arbitrary string used for node filtering if extra constraints are enabled

instance\_id (optional)

[String](#string) Cloud instance ID

instance\_type (optional)

[String](#string) Cloud instance type

node\_name (optional)

[String](#string) NodeName

time (optional)

[v0\_0\_44\_instance\_time](#v0_0_44_instance_time)

### `v0.0.44_job` - [Up](#__Models)

account (optional)

[String](#string) Account the job ran under

comment (optional)

[v0\_0\_44\_job\_comment](#v0_0_44_job_comment)

allocation\_nodes (optional)

[Integer](#integer) List of nodes allocated to the job format: int32

array (optional)

[v0\_0\_44\_job\_array](#v0_0_44_job_array)

association (optional)

[v0.0.44\_assoc\_short](#v0.0.44_assoc_short)

block (optional)

[String](#string) The name of the block to be used (used with Blue Gene systems)

cluster (optional)

[String](#string) Cluster name

constraints (optional)

[String](#string) Feature(s) the job requested as a constraint

container (optional)

[String](#string) Absolute path to OCI container bundle

derived\_exit\_code (optional)

[v0.0.44\_process\_exit\_code\_verbose](#v0.0.44_process_exit_code_verbose)

time (optional)

[v0\_0\_44\_job\_time](#v0_0_44_job_time)

exit\_code (optional)

[v0.0.44\_process\_exit\_code\_verbose](#v0.0.44_process_exit_code_verbose)

extra (optional)

[String](#string) Arbitrary string used for node filtering if extra constraints are enabled

failed\_node (optional)

[String](#string) Name of node that caused job failure

flags (optional)

[array[String]](#string) Flags associated with this job

Enum:

group (optional)

[String](#string) Group ID of the user that owns the job

het (optional)

[v0\_0\_44\_job\_het](#v0_0_44_job_het)

job\_id (optional)

[Integer](#integer) Job ID format: int32

name (optional)

[String](#string) Job name

licenses (optional)

[String](#string) License(s) required by the job

mcs (optional)

[v0\_0\_44\_job\_mcs](#v0_0_44_job_mcs)

nodes (optional)

[String](#string) Node(s) allocated to the job

partition (optional)

[String](#string) Partition assigned to the job

hold (optional)

[Boolean](#boolean) Hold (true) or release (false) job (Job held)

priority (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

qos (optional)

[String](#string) Quality of Service assigned to the job

qosreq (optional)

[String](#string) Requested QOS

required (optional)

[v0\_0\_44\_job\_required](#v0_0_44_job_required)

kill\_request\_user (optional)

[String](#string) User ID that requested termination of the job

restart\_cnt (optional)

[Integer](#integer) How many times this job has been requeued/restarted format: int32

reservation (optional)

[v0\_0\_44\_job\_reservation](#v0_0_44_job_reservation)

script (optional)

[String](#string) Job batch script contents; only the first component in a HetJob is populated or honored

segment\_size (optional)

[Integer](#integer) Requested segment size format: int32

stdin\_expanded (optional)

[String](#string) Job stdin with expanded fields

stdout\_expanded (optional)

[String](#string) Job stdout with expanded fields

stderr\_expanded (optional)

[String](#string) Job stderr with expanded fields

stdout (optional)

[String](#string) Path to stdout file

stderr (optional)

[String](#string) Path to stderr file

stdin (optional)

[String](#string) Path to stdin file

state (optional)

[v0\_0\_44\_job\_state](#v0_0_44_job_state)

steps (optional)

[array[v0.0.44\_step]](#v0.0.44_step)

submit\_line (optional)

[String](#string) Command used to submit the job

tres (optional)

[v0\_0\_44\_job\_tres](#v0_0_44_job_tres)

used\_gres (optional)

[String](#string) Generic resources used by job

user (optional)

[String](#string) User that owns the job

wckey (optional)

[v0.0.44\_wckey\_tag\_struct](#v0.0.44_wckey_tag_struct)

working\_directory (optional)

[String](#string) Path to current working directory

### `v0.0.44_job_alloc_req` - [Up](#__Models)

hetjob (optional)

[array[v0.0.44\_job\_desc\_msg]](#v0.0.44_job_desc_msg)

job (optional)

[v0.0.44\_job\_desc\_msg](#v0.0.44_job_desc_msg)

### `v0.0.44_job_array_response_msg_entry` - [Up](#__Models)

job\_id (optional)

[Integer](#integer) Job ID for updated job format: int32

step\_id (optional)

[String](#string) Step ID for updated job

error (optional)

[String](#string) Verbose update status or error

error\_code (optional)

[Integer](#integer) Verbose update status or error format: int32

why (optional)

[String](#string) Update response message

### `v0.0.44_job_desc_msg` - [Up](#__Models)

account (optional)

[String](#string) Account associated with the job

account\_gather\_frequency (optional)

[String](#string) Job accounting and profiling sampling intervals in seconds

admin\_comment (optional)

[String](#string) Arbitrary comment made by administrator

allocation\_node\_list (optional)

[String](#string) Local node making the resource allocation

allocation\_node\_port (optional)

[Integer](#integer) Port to send allocation confirmation to format: int32

argv (optional)

[array[String]](#string)

array (optional)

[String](#string) Job array index value specification

batch\_features (optional)

[String](#string) Features required for batch script's node

begin\_time (optional)

[v0.0.44\_uint64\_no\_val\_struct](#v0.0.44_uint64_no_val_struct)

flags (optional)

[array[String]](#string) Job flags

Enum:

burst\_buffer (optional)

[String](#string) Burst buffer specifications

clusters (optional)

[String](#string) Clusters that a federated job can run on

cluster\_constraint (optional)

[String](#string) Required features that a federated cluster must have to have a sibling job submitted to it

comment (optional)

[String](#string) Arbitrary comment made by user

contiguous (optional)

[Boolean](#boolean) True if job requires contiguous nodes

container (optional)

[String](#string) Absolute path to OCI container bundle

container\_id (optional)

[String](#string) OCI container ID

core\_specification (optional)

[Integer](#integer) Specialized core count format: int32

thread\_specification (optional)

[Integer](#integer) Specialized thread count format: int32

cpu\_binding (optional)

[String](#string) Method for binding tasks to allocated CPUs

cpu\_binding\_flags (optional)

[array[String]](#string) Flags for CPU binding

Enum:

cpu\_frequency (optional)

[String](#string) Requested CPU frequency range [-p2][:p3]

cpus\_per\_tres (optional)

[String](#string) Semicolon delimited list of TRES=# values values indicating how many CPUs should be allocated for each specified TRES (currently only used for gres/gpu)

crontab (optional)

[v0.0.44\_cron\_entry](#v0.0.44_cron_entry)

deadline (optional)

[Long](#long) Latest time that the job may start (UNIX timestamp) (UNIX timestamp or time string recognized by Slurm (e.g., '[MM/DD[/YY]-]HH:MM[:SS]')) format: int64

delay\_boot (optional)

[Integer](#integer) Number of seconds after job eligible start that nodes will be rebooted to satisfy feature specification format: int32

dependency (optional)

[String](#string) Other jobs that must meet certain criteria before this job can start

end\_time (optional)

[Long](#long) Expected end time (UNIX timestamp) (UNIX timestamp or time string recognized by Slurm (e.g., '[MM/DD[/YY]-]HH:MM[:SS]')) format: int64

environment (optional)

[array[String]](#string)

rlimits (optional)

[v0\_0\_44\_job\_desc\_msg\_rlimits](#v0_0_44_job_desc_msg_rlimits)

excluded\_nodes (optional)

[array[String]](#string)

extra (optional)

[String](#string) Arbitrary string used for node filtering if extra constraints are enabled

constraints (optional)

[String](#string) Comma-separated list of features that are required

group\_id (optional)

[String](#string) Group ID of the user that owns the job

hetjob\_group (optional)

[Integer](#integer) Unique sequence number applied to this component of the heterogeneous job format: int32

immediate (optional)

[Boolean](#boolean) If true, exit if resources are not available within the time period specified

job\_id (optional)

[Integer](#integer) Job ID format: int32

kill\_on\_node\_fail (optional)

[Boolean](#boolean) If true, kill job on node failure

licenses (optional)

[String](#string) License(s) required by the job

mail\_type (optional)

[array[String]](#string) Mail event type(s)

Enum:

mail\_user (optional)

[String](#string) User to receive email notifications

mcs\_label (optional)

[String](#string) Multi-Category Security label on the job

memory\_binding (optional)

[String](#string) Binding map for map/mask\_cpu

memory\_binding\_type (optional)

[array[String]](#string) Method for binding tasks to memory

Enum:

memory\_per\_tres (optional)

[String](#string) Semicolon delimited list of TRES=# values indicating how much memory in megabytes should be allocated for each specified TRES (currently only used for gres/gpu)

name (optional)

[String](#string) Job name

network (optional)

[String](#string) Network specs for job step

nice (optional)

[Integer](#integer) Requested job priority change format: int32

tasks (optional)

[Integer](#integer) Number of tasks format: int32

oom\_kill\_step (optional)

[Integer](#integer) Kill whole step in case of OOM in one of the tasks format: int32

open\_mode (optional)

[array[String]](#string) Open mode used for stdout and stderr files

Enum:

reserve\_ports (optional)

[Integer](#integer) Port to send various notification msg to format: int32

overcommit (optional)

[Boolean](#boolean) Overcommit resources

partition (optional)

[String](#string) Partition assigned to the job

distribution\_plane\_size (optional)

[v0.0.44\_uint16\_no\_val\_struct](#v0.0.44_uint16_no_val_struct)

power\_flags (optional)

[array[oas\_any\_type\_not\_mapped]](#AnyType)

prefer (optional)

[String](#string) Comma-separated list of features that are preferred but not required

hold (optional)

[Boolean](#boolean) Hold (true) or release (false) job (Job held)

priority (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

profile (optional)

[array[String]](#string) Profile used by the acct\_gather\_profile plugin

Enum:

qos (optional)

[String](#string) Quality of Service assigned to the job

reboot (optional)

[Boolean](#boolean) Node reboot requested before start

required\_nodes (optional)

[array[String]](#string)

requeue (optional)

[Boolean](#boolean) Determines whether the job may be requeued

reservation (optional)

[String](#string) Name of reservation to use

script (optional)

[String](#string) Job batch script contents; only the first component in a HetJob is populated or honored

shared (optional)

[array[String]](#string) How the job can share resources with other jobs, if at all

Enum:

site\_factor (optional)

[Integer](#integer) Site-specific priority factor format: int32

spank\_environment (optional)

[array[String]](#string)

step\_id (optional)

[v0.0.44\_slurm\_step\_id](#v0.0.44_slurm_step_id)

distribution (optional)

[String](#string) Layout

time\_limit (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

time\_minimum (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

tres\_bind (optional)

[String](#string) Task to TRES binding directives

tres\_freq (optional)

[String](#string) TRES frequency directives

tres\_per\_job (optional)

[String](#string) Comma-separated list of TRES=# values to be allocated for every job

tres\_per\_node (optional)

[String](#string) Comma-separated list of TRES=# values to be allocated for every node

tres\_per\_socket (optional)

[String](#string) Comma-separated list of TRES=# values to be allocated for every socket

tres\_per\_task (optional)

[String](#string) Comma-separated list of TRES=# values to be allocated for every task

user\_id (optional)

[String](#string) User ID that owns the job

wait\_all\_nodes (optional)

[Boolean](#boolean) If true, wait to start until after all nodes have booted

kill\_warning\_flags (optional)

[array[String]](#string) Flags related to job signals

Enum:

kill\_warning\_signal (optional)

[String](#string) Signal to send when approaching end time (e.g. "10" or "USR1")

kill\_warning\_delay (optional)

[v0.0.44\_uint16\_no\_val\_struct](#v0.0.44_uint16_no_val_struct)

current\_working\_directory (optional)

[String](#string) Working directory to use for the job

cpus\_per\_task (optional)

[Integer](#integer) Number of CPUs required by each task format: int32

minimum\_cpus (optional)

[Integer](#integer) Minimum number of CPUs required format: int32

maximum\_cpus (optional)

[Integer](#integer) Maximum number of CPUs required format: int32

nodes (optional)

[String](#string) Node count range specification (e.g. 1-15:4)

minimum\_nodes (optional)

[Integer](#integer) Minimum node count format: int32

maximum\_nodes (optional)

[Integer](#integer) Maximum node count format: int32

minimum\_boards\_per\_node (optional)

[Integer](#integer) Boards per node required format: int32

minimum\_sockets\_per\_board (optional)

[Integer](#integer) Sockets per board required format: int32

sockets\_per\_node (optional)

[Integer](#integer) Sockets per node required format: int32

threads\_per\_core (optional)

[Integer](#integer) Threads per core required format: int32

tasks\_per\_node (optional)

[Integer](#integer) Number of tasks to invoke on each node format: int32

tasks\_per\_socket (optional)

[Integer](#integer) Number of tasks to invoke on each socket format: int32

tasks\_per\_core (optional)

[Integer](#integer) Number of tasks to invoke on each core format: int32

tasks\_per\_board (optional)

[Integer](#integer) Number of tasks to invoke on each board format: int32

ntasks\_per\_tres (optional)

[Integer](#integer) Number of tasks that can access each GPU format: int32

minimum\_cpus\_per\_node (optional)

[Integer](#integer) Minimum number of CPUs per node format: int32

memory\_per\_cpu (optional)

[v0.0.44\_uint64\_no\_val\_struct](#v0.0.44_uint64_no_val_struct)

memory\_per\_node (optional)

[v0.0.44\_uint64\_no\_val\_struct](#v0.0.44_uint64_no_val_struct)

temporary\_disk\_per\_node (optional)

[Integer](#integer) Minimum tmp disk space required per node format: int32

selinux\_context (optional)

[String](#string) SELinux context

required\_switches (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

segment\_size (optional)

[v0.0.44\_uint16\_no\_val\_struct](#v0.0.44_uint16_no_val_struct)

standard\_error (optional)

[String](#string) Path to stderr file

standard\_input (optional)

[String](#string) Path to stdin file

standard\_output (optional)

[String](#string) Path to stdout file

wait\_for\_switch (optional)

[Integer](#integer) Maximum time to wait for switches in seconds format: int32

wckey (optional)

[String](#string) Workload characterization key

x11 (optional)

[array[String]](#string) X11 forwarding options

Enum:

x11\_magic\_cookie (optional)

[String](#string) Magic cookie for X11 forwarding

x11\_target\_host (optional)

[String](#string) Hostname or UNIX socket if x11\_target\_port=0

x11\_target\_port (optional)

[Integer](#integer) TCP port format: int32

### `v0.0.44_job_info` - [Up](#__Models)

account (optional)

[String](#string) Account associated with the job

accrue\_time (optional)

[v0.0.44\_uint64\_no\_val\_struct](#v0.0.44_uint64_no_val_struct)

admin\_comment (optional)

[String](#string) Arbitrary comment made by administrator

allocating\_node (optional)

[String](#string) Local node making the resource allocation

array\_job\_id (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

array\_task\_id (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

array\_max\_tasks (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

array\_task\_string (optional)

[String](#string) String expression of task IDs in this record

association\_id (optional)

[Integer](#integer) Unique identifier for the association format: int32

batch\_features (optional)

[String](#string) Features required for batch script's node

batch\_flag (optional)

[Boolean](#boolean) True if batch job

batch\_host (optional)

[String](#string) Name of host running batch script

flags (optional)

[array[String]](#string) Job flags

Enum:

burst\_buffer (optional)

[String](#string) Burst buffer specifications

burst\_buffer\_state (optional)

[String](#string) Burst buffer state details

cluster (optional)

[String](#string) Cluster name

cluster\_features (optional)

[String](#string) List of required cluster features

command (optional)

[String](#string) Executed command

comment (optional)

[String](#string) Arbitrary comment

container (optional)

[String](#string) Absolute path to OCI container bundle

container\_id (optional)

[String](#string) OCI container ID

contiguous (optional)

[Boolean](#boolean) True if job requires contiguous nodes

core\_spec (optional)

[Integer](#integer) Specialized core count format: int32

thread\_spec (optional)

[Integer](#integer) Specialized thread count format: int32

cores\_per\_socket (optional)

[v0.0.44\_uint16\_no\_val\_struct](#v0.0.44_uint16_no_val_struct)

billable\_tres (optional)

[v0.0.44\_float64\_no\_val\_struct](#v0.0.44_float64_no_val_struct)

cpus\_per\_task (optional)

[v0.0.44\_uint16\_no\_val\_struct](#v0.0.44_uint16_no_val_struct)

cpu\_frequency\_minimum (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

cpu\_frequency\_maximum (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

cpu\_frequency\_governor (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

cpus\_per\_tres (optional)

[String](#string) Semicolon delimited list of TRES=# values indicating how many CPUs should be allocated for each specified TRES (currently only used for gres/gpu)

cron (optional)

[String](#string) Time specification for scrontab job

deadline (optional)

[v0.0.44\_uint64\_no\_val\_struct](#v0.0.44_uint64_no_val_struct)

delay\_boot (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

dependency (optional)

[String](#string) Other jobs that must meet certain criteria before this job can start

derived\_exit\_code (optional)

[v0.0.44\_process\_exit\_code\_verbose](#v0.0.44_process_exit_code_verbose)

eligible\_time (optional)

[v0.0.44\_uint64\_no\_val\_struct](#v0.0.44_uint64_no_val_struct)

end\_time (optional)

[v0.0.44\_uint64\_no\_val\_struct](#v0.0.44_uint64_no_val_struct)

excluded\_nodes (optional)

[String](#string) Comma-separated list of nodes that may not be used

exit\_code (optional)

[v0.0.44\_process\_exit\_code\_verbose](#v0.0.44_process_exit_code_verbose)

extra (optional)

[String](#string) Arbitrary string used for node filtering if extra constraints are enabled

failed\_node (optional)

[String](#string) Name of node that caused job failure

features (optional)

[String](#string) Comma-separated list of features that are required

federation\_origin (optional)

[String](#string) Origin cluster's name (when using federation)

federation\_siblings\_active (optional)

[String](#string) Active sibling job names

federation\_siblings\_viable (optional)

[String](#string) Viable sibling job names

gres\_detail (optional)

[array[String]](#string)

group\_id (optional)

[Integer](#integer) Group ID of the user that owns the job format: int32

group\_name (optional)

[String](#string) Group name of the user that owns the job

het\_job\_id (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

het\_job\_id\_set (optional)

[String](#string) Job ID range for all heterogeneous job components

het\_job\_offset (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

job\_id (optional)

[Integer](#integer) Job ID format: int32

job\_resources (optional)

[v0.0.44\_job\_res](#v0.0.44_job_res)

job\_size\_str (optional)

[array[String]](#string)

job\_state (optional)

[array[String]](#string) Current state

Enum:

last\_sched\_evaluation (optional)

[v0.0.44\_uint64\_no\_val\_struct](#v0.0.44_uint64_no_val_struct)

licenses (optional)

[String](#string) License(s) required by the job

licenses\_allocated (optional)

[String](#string) License(s) allocated to the job

mail\_type (optional)

[array[String]](#string) Mail event type(s)

Enum:

mail\_user (optional)

[String](#string) User to receive email notifications

max\_cpus (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

max\_nodes (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

mcs\_label (optional)

[String](#string) Multi-Category Security label on the job

memory\_per\_tres (optional)

[String](#string) Semicolon delimited list of TRES=# values indicating how much memory in megabytes should be allocated for each specified TRES (currently only used for gres/gpu)

name (optional)

[String](#string) Job name

network (optional)

[String](#string) Network specs for the job

nodes (optional)

[String](#string) Node(s) allocated to the job

nice (optional)

[Integer](#integer) Requested job priority change format: int32

tasks\_per\_core (optional)

[v0.0.44\_uint16\_no\_val\_struct](#v0.0.44_uint16_no_val_struct)

tasks\_per\_tres (optional)

[v0.0.44\_uint16\_no\_val\_struct](#v0.0.44_uint16_no_val_struct)

tasks\_per\_node (optional)

[v0.0.44\_uint16\_no\_val\_struct](#v0.0.44_uint16_no_val_struct)

tasks\_per\_socket (optional)

[v0.0.44\_uint16\_no\_val\_struct](#v0.0.44_uint16_no_val_struct)

tasks\_per\_board (optional)

[v0.0.44\_uint16\_no\_val\_struct](#v0.0.44_uint16_no_val_struct)

cpus (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

node\_count (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

tasks (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

partition (optional)

[String](#string) Partition assigned to the job

prefer (optional)

[String](#string) Feature(s) the job requested but that are not required

memory\_per\_cpu (optional)

[v0.0.44\_uint64\_no\_val\_struct](#v0.0.44_uint64_no_val_struct)

memory\_per\_node (optional)

[v0.0.44\_uint64\_no\_val\_struct](#v0.0.44_uint64_no_val_struct)

minimum\_cpus\_per\_node (optional)

[v0.0.44\_uint16\_no\_val\_struct](#v0.0.44_uint16_no_val_struct)

minimum\_tmp\_disk\_per\_node (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

power (optional)

[v0\_0\_44\_job\_info\_power](#v0_0_44_job_info_power)

preempt\_time (optional)

[v0.0.44\_uint64\_no\_val\_struct](#v0.0.44_uint64_no_val_struct)

preemptable\_time (optional)

[v0.0.44\_uint64\_no\_val\_struct](#v0.0.44_uint64_no_val_struct)

pre\_sus\_time (optional)

[v0.0.44\_uint64\_no\_val\_struct](#v0.0.44_uint64_no_val_struct)

hold (optional)

[Boolean](#boolean) Hold (true) or release (false) job (Job held)

priority (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

priority\_by\_partition (optional)

[array[v0.0.44\_part\_prio]](#v0.0.44_part_prio)

profile (optional)

[array[String]](#string) Profile used by the acct\_gather\_profile plugin

Enum:

qos (optional)

[String](#string) Quality of Service assigned to the job, if pending the QOS requested

reboot (optional)

[Boolean](#boolean) Node reboot requested before start

required\_nodes (optional)

[String](#string) Comma-separated list of required nodes

required\_switches (optional)

[Integer](#integer) Maximum number of switches format: int32

requeue (optional)

[Boolean](#boolean) Determines whether the job may be requeued

resize\_time (optional)

[v0.0.44\_uint64\_no\_val\_struct](#v0.0.44_uint64_no_val_struct)

restart\_cnt (optional)

[Integer](#integer) Number of job restarts format: int32

resv\_name (optional)

[String](#string) Name of reservation to use

scheduled\_nodes (optional)

[String](#string) List of nodes scheduled to be used for the job

segment\_size (optional)

[Integer](#integer) Requested segment size format: int32

selinux\_context (optional)

[String](#string) SELinux context

shared (optional)

[array[String]](#string) How the job can share resources with other jobs, if at all

Enum:

step\_id (optional)

[v0.0.44\_slurm\_step\_id](#v0.0.44_slurm_step_id)

sockets\_per\_board (optional)

[Integer](#integer) Number of sockets per board required format: int32

sockets\_per\_node (optional)

[v0.0.44\_uint16\_no\_val\_struct](#v0.0.44_uint16_no_val_struct)

start\_time (optional)

[v0.0.44\_uint64\_no\_val\_struct](#v0.0.44_uint64_no_val_struct)

state\_description (optional)

[String](#string) Optional details for state\_reason

state\_reason (optional)

[String](#string) Reason for current Pending or Failed state

standard\_input (optional)

[String](#string) Path to stdin file

standard\_output (optional)

[String](#string) Path to stdout file

standard\_error (optional)

[String](#string) Path to stderr file

stdin\_expanded (optional)

[String](#string) Job stdin with expanded fields

stdout\_expanded (optional)

[String](#string) Job stdout with expanded fields

stderr\_expanded (optional)

[String](#string) Job stderr with expanded fields

submit\_time (optional)

[v0.0.44\_uint64\_no\_val\_struct](#v0.0.44_uint64_no_val_struct)

submit\_line (optional)

[String](#string) Job submit line (e.g. 'sbatch -N3 job.sh job\_arg'

suspend\_time (optional)

[v0.0.44\_uint64\_no\_val\_struct](#v0.0.44_uint64_no_val_struct)

system\_comment (optional)

[String](#string) Arbitrary comment from slurmctld

time\_limit (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

time\_minimum (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

threads\_per\_core (optional)

[v0.0.44\_uint16\_no\_val\_struct](#v0.0.44_uint16_no_val_struct)

tres\_bind (optional)

[String](#string) Task to TRES binding directives

tres\_freq (optional)

[String](#string) TRES frequency directives

tres\_per\_job (optional)

[String](#string) Comma-separated list of TRES=# values to be allocated per job

tres\_per\_node (optional)

[String](#string) Comma-separated list of TRES=# values to be allocated per node

tres\_per\_socket (optional)

[String](#string) Comma-separated list of TRES=# values to be allocated per socket

tres\_per\_task (optional)

[String](#string) Comma-separated list of TRES=# values to be allocated per task

tres\_req\_str (optional)

[String](#string) TRES requested by the job

tres\_alloc\_str (optional)

[String](#string) TRES used by the job

user\_id (optional)

[Integer](#integer) User ID that owns the job format: int32

user\_name (optional)

[String](#string) User name that owns the job

maximum\_switch\_wait\_time (optional)

[Integer](#integer) Maximum time to wait for switches in seconds format: int32

wckey (optional)

[String](#string) Workload characterization key

current\_working\_directory (optional)

[String](#string) Working directory to use for the job

### `v0.0.44_job_modify` - [Up](#__Models)

comment (optional)

[v0\_0\_44\_job\_comment](#v0_0_44_job_comment)

derived\_exit\_code (optional)

[v0.0.44\_process\_exit\_code\_verbose](#v0.0.44_process_exit_code_verbose)

extra (optional)

[String](#string) Arbitrary string used for node filtering if extra constraints are enabled

tres (optional)

[v0\_0\_44\_job\_modify\_tres](#v0_0_44_job_modify_tres)

wckey (optional)

[String](#string) Workload characterization key

### `v0.0.44_job_res` - [Up](#__Models)

select\_type

[array[String]](#string) Scheduler consumable resource selection type

Enum:

nodes (optional)

[v0\_0\_44\_job\_res\_nodes](#v0_0_44_job_res_nodes)

cpus

[Integer](#integer) Number of allocated CPUs format: int32

threads\_per\_core

[v0.0.44\_uint16\_no\_val\_struct](#v0.0.44_uint16_no_val_struct)

### `v0.0.44_job_res_core` - [Up](#__Models)

index

[Integer](#integer) Core index format: int32

status

[array[String]](#string) Core status

Enum:

### `v0.0.44_job_res_node` - [Up](#__Models)

index

[Integer](#integer) Node index format: int32

name

[String](#string) Node name

cpus (optional)

[v0\_0\_44\_job\_res\_node\_cpus](#v0_0_44_job_res_node_cpus)

memory (optional)

[v0\_0\_44\_job\_res\_node\_memory](#v0_0_44_job_res_node_memory)

sockets

[array[v0.0.44\_job\_res\_socket]](#v0.0.44_job_res_socket)

### `v0.0.44_job_res_socket` - [Up](#__Models)

index

[Integer](#integer) Core index format: int32

cores

[array[v0.0.44\_job\_res\_core]](#v0.0.44_job_res_core)

### `v0.0.44_job_submit_req` - [Up](#__Models)

script (optional)

[String](#string) Job batch script contents; Same as the script field in jobs[0] or job.

jobs (optional)

[array[v0.0.44\_job\_desc\_msg]](#v0.0.44_job_desc_msg)

job (optional)

[v0.0.44\_job\_desc\_msg](#v0.0.44_job_desc_msg)

### `v0.0.44_kill_jobs_msg` - [Up](#__Models)

account (optional)

[String](#string) Filter jobs to a specific account

flags (optional)

[array[String]](#string) Filter jobs according to flags

Enum:

job\_name (optional)

[String](#string) Filter jobs to a specific name

jobs (optional)

[array[String]](#string)

partition (optional)

[String](#string) Filter jobs to a specific partition

qos (optional)

[String](#string) Filter jobs to a specific QOS

reservation (optional)

[String](#string) Filter jobs to a specific reservation

signal (optional)

[String](#string) Signal to send to jobs

job\_state (optional)

[array[String]](#string) Filter jobs to a specific state

Enum:

user\_id (optional)

[String](#string) Filter jobs to a specific numeric user id

user\_name (optional)

[String](#string) Filter jobs to a specific user name

wckey (optional)

[String](#string) Filter jobs to a specific wckey

nodes (optional)

[array[String]](#string)

### `v0.0.44_kill_jobs_resp_job` - [Up](#__Models)

error (optional)

[v0\_0\_44\_kill\_jobs\_resp\_job\_error](#v0_0_44_kill_jobs_resp_job_error)

step\_id

[String](#string) Job or Step ID that signaling failed

job\_id

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

federation (optional)

[v0\_0\_44\_kill\_jobs\_resp\_job\_federation](#v0_0_44_kill_jobs_resp_job_federation)

### `v0.0.44_license` - [Up](#__Models)

LicenseName (optional)

[String](#string) Name of the license

Total (optional)

[Integer](#integer) Total number of licenses present format: int32

Used (optional)

[Integer](#integer) Number of licenses in use format: int32

Free (optional)

[Integer](#integer) Number of licenses currently available format: int32

Remote (optional)

[Boolean](#boolean) Indicates whether licenses are served by the database

Reserved (optional)

[Integer](#integer) Number of licenses reserved format: int32

LastConsumed (optional)

[Integer](#integer) Last known number of licenses that were consumed in the license manager (Remote Only) format: int32

LastDeficit (optional)

[Integer](#integer) Number of "missing licenses" from the cluster's perspective format: int32

LastUpdate (optional)

[Long](#long) When the license information was last updated (UNIX Timestamp) (UNIX timestamp or time string recognized by Slurm (e.g., '[MM/DD[/YY]-]HH:MM[:SS]')) format: int64

Nodes (optional)

[String](#string) HRes nodes

### `v0.0.44_node` - [Up](#__Models)

architecture (optional)

[String](#string) Computer architecture

burstbuffer\_network\_address (optional)

[String](#string) Alternate network path to be used for sbcast network traffic

boards (optional)

[Integer](#integer) Number of Baseboards in nodes with a baseboard controller format: int32

boot\_time (optional)

[v0.0.44\_uint64\_no\_val\_struct](#v0.0.44_uint64_no_val_struct)

tls\_cert\_last\_renewal (optional)

[v0.0.44\_uint64\_no\_val\_struct](#v0.0.44_uint64_no_val_struct)

cert\_flags (optional)

[array[String]](#string) Certmgr status flags

Enum:

cluster\_name (optional)

[String](#string) Cluster name (only set in federated environments)

cores (optional)

[Integer](#integer) Number of cores in a single physical processor socket format: int32

specialized\_cores (optional)

[Integer](#integer) Number of cores reserved for system use format: int32

cpu\_binding (optional)

[Integer](#integer) Default method for binding tasks to allocated CPUs format: int32

cpu\_load (optional)

[Integer](#integer) CPU load as reported by the OS format: int32

free\_mem (optional)

[v0.0.44\_uint64\_no\_val\_struct](#v0.0.44_uint64_no_val_struct)

cpus (optional)

[Integer](#integer) Total CPUs, including cores and threads format: int32

effective\_cpus (optional)

[Integer](#integer) Number of effective CPUs (excluding specialized CPUs) format: int32

specialized\_cpus (optional)

[String](#string) Abstract CPU IDs on this node reserved for exclusive use by slurmd and slurmstepd

energy (optional)

[v0.0.44\_acct\_gather\_energy](#v0.0.44_acct_gather_energy)

external\_sensors (optional)

[Object](#)

extra (optional)

[String](#string) Arbitrary string used for node filtering if extra constraints are enabled

power (optional)

[Object](#)

features (optional)

[array[String]](#string)

active\_features (optional)

[array[String]](#string)

gpu\_spec (optional)

[String](#string) CPU cores reserved for jobs that also use a GPU

gres (optional)

[String](#string) Generic resources

gres\_drained (optional)

[String](#string) Drained generic resources

gres\_used (optional)

[String](#string) Generic resources currently in use

instance\_id (optional)

[String](#string) Cloud instance ID

instance\_type (optional)

[String](#string) Cloud instance type

last\_busy (optional)

[v0.0.44\_uint64\_no\_val\_struct](#v0.0.44_uint64_no_val_struct)

mcs\_label (optional)

[String](#string) Multi-Category Security label

specialized\_memory (optional)

[Long](#long) Combined memory limit, in MB, for Slurm compute node daemons format: int64

name (optional)

[String](#string) NodeName

next\_state\_after\_reboot (optional)

[array[String]](#string) The state the node will be assigned after rebooting

Enum:

address (optional)

[String](#string) NodeAddr, used to establish a communication path

hostname (optional)

[String](#string) NodeHostname

state (optional)

[array[String]](#string) Node state(s) applicable to this node

Enum:

operating\_system (optional)

[String](#string) Operating system reported by the node

owner (optional)

[String](#string) User allowed to run jobs on this node (unset if no restriction)

partitions (optional)

[array[String]](#string)

port (optional)

[Integer](#integer) TCP port number of the slurmd format: int32

real\_memory (optional)

[Long](#long) Total memory in MB on the node format: int64

res\_cores\_per\_gpu (optional)

[Integer](#integer) Number of CPU cores per GPU restricted to GPU jobs format: int32

comment (optional)

[String](#string) Arbitrary comment

reason (optional)

[String](#string) Describes why the node is in a "DOWN", "DRAINED", "DRAINING", "FAILING" or "FAIL" state

reason\_changed\_at (optional)

[v0.0.44\_uint64\_no\_val\_struct](#v0.0.44_uint64_no_val_struct)

reason\_set\_by\_user (optional)

[String](#string) User who set the reason

resume\_after (optional)

[v0.0.44\_uint64\_no\_val\_struct](#v0.0.44_uint64_no_val_struct)

reservation (optional)

[String](#string) Name of reservation containing this node

alloc\_memory (optional)

[Long](#long) Total memory in MB currently allocated for jobs format: int64

alloc\_cpus (optional)

[Integer](#integer) Total number of CPUs currently allocated for jobs format: int32

alloc\_idle\_cpus (optional)

[Integer](#integer) Total number of idle CPUs format: int32

tres\_used (optional)

[String](#string) Trackable resources currently allocated for jobs

tres\_weighted (optional)

[Double](#double) Ignored. Was weighted number of billable trackable resources allocated format: double

slurmd\_start\_time (optional)

[v0.0.44\_uint64\_no\_val\_struct](#v0.0.44_uint64_no_val_struct)

sockets (optional)

[Integer](#integer) Number of physical processor sockets/chips on the node format: int32

threads (optional)

[Integer](#integer) Number of logical threads in a single physical core format: int32

temporary\_disk (optional)

[Integer](#integer) Total size in MB of temporary disk storage in TmpFS format: int32

weight (optional)

[Integer](#integer) Weight of the node for scheduling purposes format: int32

topology (optional)

[String](#string) Topology

tres (optional)

[String](#string) Configured trackable resources

version (optional)

[String](#string) Slurmd version

### `v0.0.44_node_gres_layout` - [Up](#__Models)

name

[String](#string) GRES name

type (optional)

[String](#string) GRES type (optional)

count (optional)

[Long](#long) Count format: int64

index (optional)

[String](#string) Index

### `v0.0.44_node_resource_layout` - [Up](#__Models)

node

[String](#string) Node name

sockets\_per\_node (optional)

[Integer](#integer) Sockets per node format: int32

cores\_per\_socket (optional)

[Integer](#integer) Cores per socket format: int32

mem\_alloc (optional)

[Long](#long) Allocated memory format: int64

core\_bitmap (optional)

[String](#string) Abstract core bitmap

channel (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

gres (optional)

[array[v0.0.44\_node\_gres\_layout]](#v0.0.44_node_gres_layout)

### `v0.0.44_openapi_accounts_add_cond_resp` - [Up](#__Models)

association\_condition

[v0.0.44\_accounts\_add\_cond](#v0.0.44_accounts_add_cond)

account (optional)

[v0.0.44\_account\_short](#v0.0.44_account_short)

meta (optional)

[v0.0.44\_openapi\_meta](#v0.0.44_openapi_meta)

errors (optional)

[array[v0.0.44\_openapi\_error]](#v0.0.44_openapi_error)

warnings (optional)

[array[v0.0.44\_openapi\_warning]](#v0.0.44_openapi_warning)

### `v0.0.44_openapi_accounts_add_cond_resp_str` - [Up](#__Models)

added\_accounts

[String](#string) added\_accounts

meta (optional)

[v0.0.44\_openapi\_meta](#v0.0.44_openapi_meta)

errors (optional)

[array[v0.0.44\_openapi\_error]](#v0.0.44_openapi_error)

warnings (optional)

[array[v0.0.44\_openapi\_warning]](#v0.0.44_openapi_warning)

### `v0.0.44_openapi_accounts_removed_resp` - [Up](#__Models)

removed\_accounts

[array[String]](#string)

meta (optional)

[v0.0.44\_openapi\_meta](#v0.0.44_openapi_meta)

errors (optional)

[array[v0.0.44\_openapi\_error]](#v0.0.44_openapi_error)

warnings (optional)

[array[v0.0.44\_openapi\_warning]](#v0.0.44_openapi_warning)

### `v0.0.44_openapi_accounts_resp` - [Up](#__Models)

accounts

[array[v0.0.44\_account]](#v0.0.44_account)

meta (optional)

[v0.0.44\_openapi\_meta](#v0.0.44_openapi_meta)

errors (optional)

[array[v0.0.44\_openapi\_error]](#v0.0.44_openapi_error)

warnings (optional)

[array[v0.0.44\_openapi\_warning]](#v0.0.44_openapi_warning)

### `v0.0.44_openapi_assocs_removed_resp` - [Up](#__Models)

removed\_associations

[array[String]](#string)

meta (optional)

[v0.0.44\_openapi\_meta](#v0.0.44_openapi_meta)

errors (optional)

[array[v0.0.44\_openapi\_error]](#v0.0.44_openapi_error)

warnings (optional)

[array[v0.0.44\_openapi\_warning]](#v0.0.44_openapi_warning)

### `v0.0.44_openapi_assocs_resp` - [Up](#__Models)

associations

[array[v0.0.44\_assoc]](#v0.0.44_assoc)

meta (optional)

[v0.0.44\_openapi\_meta](#v0.0.44_openapi_meta)

errors (optional)

[array[v0.0.44\_openapi\_error]](#v0.0.44_openapi_error)

warnings (optional)

[array[v0.0.44\_openapi\_warning]](#v0.0.44_openapi_warning)

### `v0.0.44_openapi_clusters_removed_resp` - [Up](#__Models)

deleted\_clusters

[array[String]](#string)

meta (optional)

[v0.0.44\_openapi\_meta](#v0.0.44_openapi_meta)

errors (optional)

[array[v0.0.44\_openapi\_error]](#v0.0.44_openapi_error)

warnings (optional)

[array[v0.0.44\_openapi\_warning]](#v0.0.44_openapi_warning)

### `v0.0.44_openapi_clusters_resp` - [Up](#__Models)

clusters

[array[v0.0.44\_cluster\_rec]](#v0.0.44_cluster_rec)

meta (optional)

[v0.0.44\_openapi\_meta](#v0.0.44_openapi_meta)

errors (optional)

[array[v0.0.44\_openapi\_error]](#v0.0.44_openapi_error)

warnings (optional)

[array[v0.0.44\_openapi\_warning]](#v0.0.44_openapi_warning)

### `v0.0.44_openapi_create_node_req` - [Up](#__Models)

node\_conf

[String](#string) Node configuration line

meta (optional)

[v0.0.44\_openapi\_meta](#v0.0.44_openapi_meta)

errors (optional)

[array[v0.0.44\_openapi\_error]](#v0.0.44_openapi_error)

warnings (optional)

[array[v0.0.44\_openapi\_warning]](#v0.0.44_openapi_warning)

### `v0.0.44_openapi_diag_resp` - [Up](#__Models)

statistics

[v0.0.44\_stats\_msg](#v0.0.44_stats_msg)

meta (optional)

[v0.0.44\_openapi\_meta](#v0.0.44_openapi_meta)

errors (optional)

[array[v0.0.44\_openapi\_error]](#v0.0.44_openapi_error)

warnings (optional)

[array[v0.0.44\_openapi\_warning]](#v0.0.44_openapi_warning)

### `v0.0.44_openapi_error` - [Up](#__Models)

description (optional)

[String](#string) Long form error description

error\_number (optional)

[Integer](#integer) Slurm numeric error identifier format: int32

error (optional)

[String](#string) Short form error description

source (optional)

[String](#string) Source of error or where error was first detected

### `v0.0.44_openapi_instances_resp` - [Up](#__Models)

instances

[array[v0.0.44\_instance]](#v0.0.44_instance)

meta (optional)

[v0.0.44\_openapi\_meta](#v0.0.44_openapi_meta)

errors (optional)

[array[v0.0.44\_openapi\_error]](#v0.0.44_openapi_error)

warnings (optional)

[array[v0.0.44\_openapi\_warning]](#v0.0.44_openapi_warning)

### `v0.0.44_openapi_job_alloc_resp` - [Up](#__Models)

job\_id (optional)

[Integer](#integer) Submitted Job ID format: int32

job\_submit\_user\_msg (optional)

[String](#string) Job submission user message

meta (optional)

[v0.0.44\_openapi\_meta](#v0.0.44_openapi_meta)

errors (optional)

[array[v0.0.44\_openapi\_error]](#v0.0.44_openapi_error)

warnings (optional)

[array[v0.0.44\_openapi\_warning]](#v0.0.44_openapi_warning)

### `v0.0.44_openapi_job_info_resp` - [Up](#__Models)

jobs

[array[v0.0.44\_job\_info]](#v0.0.44_job_info)

last\_backfill

[v0.0.44\_uint64\_no\_val\_struct](#v0.0.44_uint64_no_val_struct)

last\_update

[v0.0.44\_uint64\_no\_val\_struct](#v0.0.44_uint64_no_val_struct)

meta (optional)

[v0.0.44\_openapi\_meta](#v0.0.44_openapi_meta)

errors (optional)

[array[v0.0.44\_openapi\_error]](#v0.0.44_openapi_error)

warnings (optional)

[array[v0.0.44\_openapi\_warning]](#v0.0.44_openapi_warning)

### `v0.0.44_openapi_job_modify_req` - [Up](#__Models)

job\_id\_list (optional)

[array[String]](#string)

job\_rec (optional)

[v0.0.44\_job\_modify](#v0.0.44_job_modify)

meta (optional)

[v0.0.44\_openapi\_meta](#v0.0.44_openapi_meta)

errors (optional)

[array[v0.0.44\_openapi\_error]](#v0.0.44_openapi_error)

warnings (optional)

[array[v0.0.44\_openapi\_warning]](#v0.0.44_openapi_warning)

### `v0.0.44_openapi_job_modify_resp` - [Up](#__Models)

results

[array[String]](#string)

meta (optional)

[v0.0.44\_openapi\_meta](#v0.0.44_openapi_meta)

errors (optional)

[array[v0.0.44\_openapi\_error]](#v0.0.44_openapi_error)

warnings (optional)

[array[v0.0.44\_openapi\_warning]](#v0.0.44_openapi_warning)

### `v0.0.44_openapi_job_post_response` - [Up](#__Models)

results (optional)

[array[v0.0.44\_job\_array\_response\_msg\_entry]](#v0.0.44_job_array_response_msg_entry)

meta (optional)

[v0.0.44\_openapi\_meta](#v0.0.44_openapi_meta)

errors (optional)

[array[v0.0.44\_openapi\_error]](#v0.0.44_openapi_error)

warnings (optional)

[array[v0.0.44\_openapi\_warning]](#v0.0.44_openapi_warning)

### `v0.0.44_openapi_job_submit_response` - [Up](#__Models)

job\_id (optional)

[Integer](#integer) submitted Job ID format: int32

step\_id (optional)

[String](#string) submitted Step ID

job\_submit\_user\_msg (optional)

[String](#string) Job submission user message

meta (optional)

[v0.0.44\_openapi\_meta](#v0.0.44_openapi_meta)

errors (optional)

[array[v0.0.44\_openapi\_error]](#v0.0.44_openapi_error)

warnings (optional)

[array[v0.0.44\_openapi\_warning]](#v0.0.44_openapi_warning)

### `v0.0.44_openapi_kill_job_resp` - [Up](#__Models)

status

[array[v0.0.44\_kill\_jobs\_resp\_job]](#v0.0.44_kill_jobs_resp_job) List of jobs signal responses

meta (optional)

[v0.0.44\_openapi\_meta](#v0.0.44_openapi_meta)

errors (optional)

[array[v0.0.44\_openapi\_error]](#v0.0.44_openapi_error)

warnings (optional)

[array[v0.0.44\_openapi\_warning]](#v0.0.44_openapi_warning)

### `v0.0.44_openapi_kill_jobs_resp` - [Up](#__Models)

status

[array[v0.0.44\_kill\_jobs\_resp\_job]](#v0.0.44_kill_jobs_resp_job) List of jobs signal responses

meta (optional)

[v0.0.44\_openapi\_meta](#v0.0.44_openapi_meta)

errors (optional)

[array[v0.0.44\_openapi\_error]](#v0.0.44_openapi_error)

warnings (optional)

[array[v0.0.44\_openapi\_warning]](#v0.0.44_openapi_warning)

### `v0.0.44_openapi_licenses_resp` - [Up](#__Models)

licenses

[array[v0.0.44\_license]](#v0.0.44_license)

last\_update

[v0.0.44\_uint64\_no\_val\_struct](#v0.0.44_uint64_no_val_struct)

meta (optional)

[v0.0.44\_openapi\_meta](#v0.0.44_openapi_meta)

errors (optional)

[array[v0.0.44\_openapi\_error]](#v0.0.44_openapi_error)

warnings (optional)

[array[v0.0.44\_openapi\_warning]](#v0.0.44_openapi_warning)

### `v0.0.44_openapi_meta` - [Up](#__Models)

plugin (optional)

[v0\_0\_44\_openapi\_meta\_plugin](#v0_0_44_openapi_meta_plugin)

client (optional)

[v0\_0\_44\_openapi\_meta\_client](#v0_0_44_openapi_meta_client)

command (optional)

[array[String]](#string)

slurm (optional)

[v0\_0\_44\_openapi\_meta\_slurm](#v0_0_44_openapi_meta_slurm)

### `v0.0.44_openapi_nodes_resp` - [Up](#__Models)

nodes

[array[v0.0.44\_node]](#v0.0.44_node)

last\_update

[v0.0.44\_uint64\_no\_val\_struct](#v0.0.44_uint64_no_val_struct)

meta (optional)

[v0.0.44\_openapi\_meta](#v0.0.44_openapi_meta)

errors (optional)

[array[v0.0.44\_openapi\_error]](#v0.0.44_openapi_error)

warnings (optional)

[array[v0.0.44\_openapi\_warning]](#v0.0.44_openapi_warning)

### `v0.0.44_openapi_partition_resp` - [Up](#__Models)

partitions

[array[v0.0.44\_partition\_info]](#v0.0.44_partition_info)

last\_update

[v0.0.44\_uint64\_no\_val\_struct](#v0.0.44_uint64_no_val_struct)

meta (optional)

[v0.0.44\_openapi\_meta](#v0.0.44_openapi_meta)

errors (optional)

[array[v0.0.44\_openapi\_error]](#v0.0.44_openapi_error)

warnings (optional)

[array[v0.0.44\_openapi\_warning]](#v0.0.44_openapi_warning)

### `v0.0.44_openapi_ping_array_resp` - [Up](#__Models)

pings

[array[v0.0.44\_controller\_ping]](#v0.0.44_controller_ping)

meta (optional)

[v0.0.44\_openapi\_meta](#v0.0.44_openapi_meta)

errors (optional)

[array[v0.0.44\_openapi\_error]](#v0.0.44_openapi_error)

warnings (optional)

[array[v0.0.44\_openapi\_warning]](#v0.0.44_openapi_warning)

### `v0.0.44_openapi_reservation_mod_resp` - [Up](#__Models)

reservations

[array[v0.0.44\_reservation\_desc\_msg]](#v0.0.44_reservation_desc_msg)

meta (optional)

[v0.0.44\_openapi\_meta](#v0.0.44_openapi_meta)

errors (optional)

[array[v0.0.44\_openapi\_error]](#v0.0.44_openapi_error)

warnings (optional)

[array[v0.0.44\_openapi\_warning]](#v0.0.44_openapi_warning)

### `v0.0.44_openapi_reservation_resp` - [Up](#__Models)

reservations

[array[v0.0.44\_reservation\_info]](#v0.0.44_reservation_info)

last\_update

[v0.0.44\_uint64\_no\_val\_struct](#v0.0.44_uint64_no_val_struct)

meta (optional)

[v0.0.44\_openapi\_meta](#v0.0.44_openapi_meta)

errors (optional)

[array[v0.0.44\_openapi\_error]](#v0.0.44_openapi_error)

warnings (optional)

[array[v0.0.44\_openapi\_warning]](#v0.0.44_openapi_warning)

### `v0.0.44_openapi_resource_layout_resp` - [Up](#__Models)

nodes

[array[v0.0.44\_node\_resource\_layout]](#v0.0.44_node_resource_layout)

meta (optional)

[v0.0.44\_openapi\_meta](#v0.0.44_openapi_meta)

errors (optional)

[array[v0.0.44\_openapi\_error]](#v0.0.44_openapi_error)

warnings (optional)

[array[v0.0.44\_openapi\_warning]](#v0.0.44_openapi_warning)

### `v0.0.44_openapi_resp` - [Up](#__Models)

meta (optional)

[v0.0.44\_openapi\_meta](#v0.0.44_openapi_meta)

errors (optional)

[array[v0.0.44\_openapi\_error]](#v0.0.44_openapi_error)

warnings (optional)

[array[v0.0.44\_openapi\_warning]](#v0.0.44_openapi_warning)

### `v0.0.44_openapi_shares_resp` - [Up](#__Models)

shares

[v0.0.44\_shares\_resp\_msg](#v0.0.44_shares_resp_msg)

meta (optional)

[v0.0.44\_openapi\_meta](#v0.0.44_openapi_meta)

errors (optional)

[array[v0.0.44\_openapi\_error]](#v0.0.44_openapi_error)

warnings (optional)

[array[v0.0.44\_openapi\_warning]](#v0.0.44_openapi_warning)

### `v0.0.44_openapi_slurmdbd_config_resp` - [Up](#__Models)

clusters (optional)

[array[v0.0.44\_cluster\_rec]](#v0.0.44_cluster_rec)

tres (optional)

[array[v0.0.44\_tres]](#v0.0.44_tres)

accounts (optional)

[array[v0.0.44\_account]](#v0.0.44_account)

users (optional)

[array[v0.0.44\_user]](#v0.0.44_user)

qos (optional)

[array[v0.0.44\_qos]](#v0.0.44_qos)

wckeys (optional)

[array[v0.0.44\_wckey]](#v0.0.44_wckey)

associations (optional)

[array[v0.0.44\_assoc]](#v0.0.44_assoc)

instances (optional)

[array[v0.0.44\_instance]](#v0.0.44_instance)

meta (optional)

[v0.0.44\_openapi\_meta](#v0.0.44_openapi_meta)

errors (optional)

[array[v0.0.44\_openapi\_error]](#v0.0.44_openapi_error)

warnings (optional)

[array[v0.0.44\_openapi\_warning]](#v0.0.44_openapi_warning)

### `v0.0.44_openapi_slurmdbd_jobs_resp` - [Up](#__Models)

jobs

[array[v0.0.44\_job]](#v0.0.44_job)

meta (optional)

[v0.0.44\_openapi\_meta](#v0.0.44_openapi_meta)

errors (optional)

[array[v0.0.44\_openapi\_error]](#v0.0.44_openapi_error)

warnings (optional)

[array[v0.0.44\_openapi\_warning]](#v0.0.44_openapi_warning)

### `v0.0.44_openapi_slurmdbd_ping_resp` - [Up](#__Models)

pings

[array[v0.0.44\_slurmdbd\_ping]](#v0.0.44_slurmdbd_ping)

meta (optional)

[v0.0.44\_openapi\_meta](#v0.0.44_openapi_meta)

errors (optional)

[array[v0.0.44\_openapi\_error]](#v0.0.44_openapi_error)

warnings (optional)

[array[v0.0.44\_openapi\_warning]](#v0.0.44_openapi_warning)

### `v0.0.44_openapi_slurmdbd_qos_removed_resp` - [Up](#__Models)

removed\_qos

[array[String]](#string)

meta (optional)

[v0.0.44\_openapi\_meta](#v0.0.44_openapi_meta)

errors (optional)

[array[v0.0.44\_openapi\_error]](#v0.0.44_openapi_error)

warnings (optional)

[array[v0.0.44\_openapi\_warning]](#v0.0.44_openapi_warning)

### `v0.0.44_openapi_slurmdbd_qos_resp` - [Up](#__Models)

qos

[array[v0.0.44\_qos]](#v0.0.44_qos)

meta (optional)

[v0.0.44\_openapi\_meta](#v0.0.44_openapi_meta)

errors (optional)

[array[v0.0.44\_openapi\_error]](#v0.0.44_openapi_error)

warnings (optional)

[array[v0.0.44\_openapi\_warning]](#v0.0.44_openapi_warning)

### `v0.0.44_openapi_slurmdbd_stats_resp` - [Up](#__Models)

statistics

[v0.0.44\_stats\_rec](#v0.0.44_stats_rec)

meta (optional)

[v0.0.44\_openapi\_meta](#v0.0.44_openapi_meta)

errors (optional)

[array[v0.0.44\_openapi\_error]](#v0.0.44_openapi_error)

warnings (optional)

[array[v0.0.44\_openapi\_warning]](#v0.0.44_openapi_warning)

### `v0.0.44_openapi_tres_resp` - [Up](#__Models)

TRES

[array[v0.0.44\_tres]](#v0.0.44_tres)

meta (optional)

[v0.0.44\_openapi\_meta](#v0.0.44_openapi_meta)

errors (optional)

[array[v0.0.44\_openapi\_error]](#v0.0.44_openapi_error)

warnings (optional)

[array[v0.0.44\_openapi\_warning]](#v0.0.44_openapi_warning)

### `v0.0.44_openapi_users_add_cond_resp` - [Up](#__Models)

association\_condition

[v0.0.44\_users\_add\_cond](#v0.0.44_users_add_cond)

user

[v0.0.44\_user\_short](#v0.0.44_user_short)

meta (optional)

[v0.0.44\_openapi\_meta](#v0.0.44_openapi_meta)

errors (optional)

[array[v0.0.44\_openapi\_error]](#v0.0.44_openapi_error)

warnings (optional)

[array[v0.0.44\_openapi\_warning]](#v0.0.44_openapi_warning)

### `v0.0.44_openapi_users_add_cond_resp_str` - [Up](#__Models)

added\_users

[String](#string) added\_users

meta (optional)

[v0.0.44\_openapi\_meta](#v0.0.44_openapi_meta)

errors (optional)

[array[v0.0.44\_openapi\_error]](#v0.0.44_openapi_error)

warnings (optional)

[array[v0.0.44\_openapi\_warning]](#v0.0.44_openapi_warning)

### `v0.0.44_openapi_users_resp` - [Up](#__Models)

users

[array[v0.0.44\_user]](#v0.0.44_user)

meta (optional)

[v0.0.44\_openapi\_meta](#v0.0.44_openapi_meta)

errors (optional)

[array[v0.0.44\_openapi\_error]](#v0.0.44_openapi_error)

warnings (optional)

[array[v0.0.44\_openapi\_warning]](#v0.0.44_openapi_warning)

### `v0.0.44_openapi_warning` - [Up](#__Models)

description (optional)

[String](#string) Long form warning description

source (optional)

[String](#string) Source of warning or where warning was first detected

### `v0.0.44_openapi_wckey_removed_resp` - [Up](#__Models)

deleted\_wckeys

[array[String]](#string)

meta (optional)

[v0.0.44\_openapi\_meta](#v0.0.44_openapi_meta)

errors (optional)

[array[v0.0.44\_openapi\_error]](#v0.0.44_openapi_error)

warnings (optional)

[array[v0.0.44\_openapi\_warning]](#v0.0.44_openapi_warning)

### `v0.0.44_openapi_wckey_resp` - [Up](#__Models)

wckeys

[array[v0.0.44\_wckey]](#v0.0.44_wckey)

meta (optional)

[v0.0.44\_openapi\_meta](#v0.0.44_openapi_meta)

errors (optional)

[array[v0.0.44\_openapi\_error]](#v0.0.44_openapi_error)

warnings (optional)

[array[v0.0.44\_openapi\_warning]](#v0.0.44_openapi_warning)

### `v0.0.44_part_prio` - [Up](#__Models)

partition (optional)

[String](#string) Partition name

priority (optional)

[Integer](#integer) Prospective job priority if it runs in this partition format: int32

### `v0.0.44_partition_info` - [Up](#__Models)

nodes (optional)

[v0\_0\_44\_partition\_info\_nodes](#v0_0_44_partition_info_nodes)

accounts (optional)

[v0\_0\_44\_partition\_info\_accounts](#v0_0_44_partition_info_accounts)

groups (optional)

[v0\_0\_44\_partition\_info\_groups](#v0_0_44_partition_info_groups)

qos (optional)

[v0\_0\_44\_partition\_info\_qos](#v0_0_44_partition_info_qos)

alternate (optional)

[String](#string) Alternate - Partition name of alternate partition to be used if the state of this partition is DRAIN or INACTIVE

tres (optional)

[v0\_0\_44\_partition\_info\_tres](#v0_0_44_partition_info_tres)

cluster (optional)

[String](#string) Cluster name

select\_type (optional)

[array[String]](#string) Scheduler consumable resource selection type

Enum:

cpus (optional)

[v0\_0\_44\_partition\_info\_cpus](#v0_0_44_partition_info_cpus)

defaults (optional)

[v0\_0\_44\_partition\_info\_defaults](#v0_0_44_partition_info_defaults)

grace\_time (optional)

[Integer](#integer) GraceTime - Grace time in seconds to be extended to a job which has been selected for preemption format: int32

maximums (optional)

[v0\_0\_44\_partition\_info\_maximums](#v0_0_44_partition_info_maximums)

minimums (optional)

[v0\_0\_44\_partition\_info\_minimums](#v0_0_44_partition_info_minimums)

name (optional)

[String](#string) PartitionName - Name by which the partition may be referenced

node\_sets (optional)

[String](#string) NodeSets - Comma-separated list of nodesets which are associated with this partition

priority (optional)

[v0\_0\_44\_partition\_info\_priority](#v0_0_44_partition_info_priority)

timeouts (optional)

[v0\_0\_44\_partition\_info\_timeouts](#v0_0_44_partition_info_timeouts)

topology (optional)

[String](#string) Topology - Name of the topology, defined in topology.yaml, used by jobs in this partition

partition (optional)

[v0\_0\_44\_partition\_info\_partition](#v0_0_44_partition_info_partition)

suspend\_time (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

### `v0.0.44_process_exit_code_verbose` - [Up](#__Models)

status (optional)

[array[String]](#string) Status given by return code

Enum:

return\_code (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

signal (optional)

[v0\_0\_44\_process\_exit\_code\_verbose\_signal](#v0_0_44_process_exit_code_verbose_signal)

### `v0.0.44_qos` - [Up](#__Models)

description (optional)

[String](#string) Arbitrary description

flags (optional)

[array[String]](#string) Flags, to avoid modifying current values specify NOT\_SET

Enum:

id (optional)

[Integer](#integer) Unique ID format: int32

limits (optional)

[v0\_0\_44\_qos\_limits](#v0_0_44_qos_limits)

name (optional)

[String](#string) Name

preempt (optional)

[v0\_0\_44\_qos\_preempt](#v0_0_44_qos_preempt)

priority (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

usage\_factor (optional)

[v0.0.44\_float64\_no\_val\_struct](#v0.0.44_float64_no_val_struct)

usage\_threshold (optional)

[v0.0.44\_float64\_no\_val\_struct](#v0.0.44_float64_no_val_struct)

### `v0.0.44_reservation_core_spec` - [Up](#__Models)

node (optional)

[String](#string) Name of reserved node

core (optional)

[String](#string) IDs of reserved cores

### `v0.0.44_reservation_desc_msg` - [Up](#__Models)

accounts (optional)

[array[String]](#string)

burst\_buffer (optional)

[String](#string) BurstBuffer

comment (optional)

[String](#string) Arbitrary string

core\_count (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

duration (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

end\_time (optional)

[v0.0.44\_uint64\_no\_val\_struct](#v0.0.44_uint64_no_val_struct)

features (optional)

[String](#string) Requested node features. Multiple values may be "&" separated if all features are required (AND operation) or separated by "|" if any of the specified features are required (OR operation). Parenthesis are also supported for features to be ANDed together with counts of nodes having the specified features.

flags (optional)

[array[String]](#string) Flags associated with this reservation. Note, to remove flags use "NO\_" prefixed flag excluding NO\_HOLD\_JOBS\_AFTER\_END

Enum:

groups (optional)

[array[String]](#string)

licenses (optional)

[array[String]](#string)

max\_start\_delay (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

name (optional)

[String](#string) ReservationName

node\_count (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

node\_list (optional)

[array[String]](#string)

partition (optional)

[String](#string) Partition used to reserve nodes from. This will attempt to allocate all nodes in the specified partition unless you request fewer resources than are available with core\_cnt, node\_cnt or tres.

purge\_completed (optional)

[v0\_0\_44\_reservation\_info\_purge\_completed](#v0_0_44_reservation_info_purge_completed)

start\_time (optional)

[v0.0.44\_uint64\_no\_val\_struct](#v0.0.44_uint64_no_val_struct)

tres (optional)

[array[v0.0.44\_tres]](#v0.0.44_tres)

users (optional)

[array[String]](#string)

### `v0.0.44_reservation_info` - [Up](#__Models)

accounts (optional)

[String](#string) Comma-separated list of permitted accounts

burst\_buffer (optional)

[String](#string) BurstBuffer - Burst buffer resources reserved

core\_count (optional)

[Integer](#integer) CoreCnt - Number of cores reserved format: int32

core\_specializations (optional)

[array[v0.0.44\_reservation\_core\_spec]](#v0.0.44_reservation_core_spec)

end\_time (optional)

[v0.0.44\_uint64\_no\_val\_struct](#v0.0.44_uint64_no_val_struct)

features (optional)

[String](#string) Features - Expression describing the reservation's required node features

flags (optional)

[array[String]](#string) Flags associated with this reservation

Enum:

groups (optional)

[String](#string) Groups - Comma-separated list of permitted groups

licenses (optional)

[String](#string) Licenses - Comma-separated list of licenses reserved

max\_start\_delay (optional)

[Integer](#integer) MaxStartDelay - Maximum time an eligible job not requesting this reservation can delay a job requesting it in seconds format: int32

name (optional)

[String](#string) ReservationName - Name of the reservation

node\_count (optional)

[Integer](#integer) NodeCnt - Number of nodes reserved format: int32

node\_list (optional)

[String](#string) Nodes - Comma-separated list of node names and/or node ranges reserved

partition (optional)

[String](#string) PartitionName - Partition used to reserve nodes from

purge\_completed (optional)

[v0\_0\_44\_reservation\_info\_purge\_completed](#v0_0_44_reservation_info_purge_completed)

start\_time (optional)

[v0.0.44\_uint64\_no\_val\_struct](#v0.0.44_uint64_no_val_struct)

watts (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

tres (optional)

[String](#string) Comma-separated list of required TRES

users (optional)

[String](#string) Comma-separated list of permitted users

### `v0.0.44_reservation_mod_req` - [Up](#__Models)

reservations (optional)

[array[v0.0.44\_reservation\_desc\_msg]](#v0.0.44_reservation_desc_msg)

### `v0.0.44_rollup_stats` - [Up](#__Models)

hourly (optional)

[v0\_0\_44\_rollup\_stats\_hourly](#v0_0_44_rollup_stats_hourly)

daily (optional)

[v0\_0\_44\_rollup\_stats\_daily](#v0_0_44_rollup_stats_daily)

monthly (optional)

[v0\_0\_44\_rollup\_stats\_monthly](#v0_0_44_rollup_stats_monthly)

### `v0.0.44_schedule_exit_fields` - [Up](#__Models)

end\_job\_queue (optional)

[Integer](#integer) Reached end of queue format: int32

default\_queue\_depth (optional)

[Integer](#integer) Reached number of jobs allowed to be tested format: int32

max\_job\_start (optional)

[Integer](#integer) Reached number of jobs allowed to start format: int32

max\_rpc\_cnt (optional)

[Integer](#integer) Reached RPC limit format: int32

max\_sched\_time (optional)

[Integer](#integer) Reached maximum allowed scheduler time format: int32

licenses (optional)

[Integer](#integer) Blocked on licenses format: int32

### `v0.0.44_shares_float128_tres` - [Up](#__Models)

name (optional)

[String](#string) TRES name

value (optional)

[BigDecimal](#number) TRES value

### `v0.0.44_shares_resp_msg` - [Up](#__Models)

shares (optional)

[array[v0.0.44\_assoc\_shares\_obj\_wrap]](#v0.0.44_assoc_shares_obj_wrap)

total\_shares (optional)

[Long](#long) Total number of shares format: int64

### `v0.0.44_shares_uint64_tres` - [Up](#__Models)

name (optional)

[String](#string) TRES name

value (optional)

[v0.0.44\_uint64\_no\_val\_struct](#v0.0.44_uint64_no_val_struct)

### `v0.0.44_slurm_step_id` - [Up](#__Models)

sluid (optional)

[String](#string) SLUID (Slurm Lexicographically-sortable Unique ID)

job\_id (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

step\_het\_component (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

step\_id (optional)

[String](#string) Job step ID

### `v0.0.44_slurmdbd_ping` - [Up](#__Models)

hostname

[String](#string) Target for ping

responding

[Boolean](#boolean) If ping RPC responded with pong from slurmdbd

latency

[Long](#long) Number of microseconds it took to successfully ping or timeout format: int64

primary

[Boolean](#boolean) Is responding slurmdbd the primary controller (Is responding slurmctld the primary controller)

### `v0.0.44_stats_msg` - [Up](#__Models)

parts\_packed (optional)

[Integer](#integer) Zero if only RPC statistic included format: int32

req\_time (optional)

[v0.0.44\_uint64\_no\_val\_struct](#v0.0.44_uint64_no_val_struct)

req\_time\_start (optional)

[v0.0.44\_uint64\_no\_val\_struct](#v0.0.44_uint64_no_val_struct)

server\_thread\_count (optional)

[Integer](#integer) Number of current active slurmctld threads format: int32

agent\_queue\_size (optional)

[Integer](#integer) Number of enqueued outgoing RPC requests in an internal retry list format: int32

agent\_count (optional)

[Integer](#integer) Number of agent threads format: int32

agent\_thread\_count (optional)

[Integer](#integer) Total number of active threads created by all agent threads format: int32

dbd\_agent\_queue\_size (optional)

[Integer](#integer) Number of messages for SlurmDBD that are queued format: int32

gettimeofday\_latency (optional)

[Integer](#integer) Latency of 1000 calls to the gettimeofday() syscall in microseconds, as measured at controller startup format: int32

schedule\_cycle\_max (optional)

[Integer](#integer) Max time of any scheduling cycle in microseconds since last reset format: int32

schedule\_cycle\_last (optional)

[Integer](#integer) Time in microseconds for last scheduling cycle format: int32

schedule\_cycle\_sum (optional)

[Long](#long) Total run time in microseconds for all scheduling cycles since last reset format: int64

schedule\_cycle\_total (optional)

[Integer](#integer) Number of scheduling cycles since last reset format: int32

schedule\_cycle\_mean (optional)

[Long](#long) Mean time in microseconds for all scheduling cycles since last reset format: int64

schedule\_cycle\_mean\_depth (optional)

[Long](#long) Mean of the number of jobs processed in a scheduling cycle format: int64

schedule\_cycle\_per\_minute (optional)

[Long](#long) Number of scheduling executions per minute format: int64

schedule\_cycle\_depth (optional)

[Integer](#integer) Total number of jobs processed in scheduling cycles format: int32

schedule\_exit (optional)

[v0.0.44\_schedule\_exit\_fields](#v0.0.44_schedule_exit_fields)

schedule\_queue\_length (optional)

[Integer](#integer) Number of jobs pending in queue format: int32

jobs\_submitted (optional)

[Integer](#integer) Number of jobs submitted since last reset format: int32

jobs\_started (optional)

[Integer](#integer) Number of jobs started since last reset format: int32

jobs\_completed (optional)

[Integer](#integer) Number of jobs completed since last reset format: int32

jobs\_canceled (optional)

[Integer](#integer) Number of jobs canceled since the last reset format: int32

jobs\_failed (optional)

[Integer](#integer) Number of jobs failed due to slurmd or other internal issues since last reset format: int32

jobs\_pending (optional)

[Integer](#integer) Number of jobs pending at the time of listed in job\_state\_ts format: int32

jobs\_running (optional)

[Integer](#integer) Number of jobs running at the time of listed in job\_state\_ts format: int32

job\_states\_ts (optional)

[v0.0.44\_uint64\_no\_val\_struct](#v0.0.44_uint64_no_val_struct)

bf\_backfilled\_jobs (optional)

[Integer](#integer) Number of jobs started through backfilling since last slurm start format: int32

bf\_last\_backfilled\_jobs (optional)

[Integer](#integer) Number of jobs started through backfilling since last reset format: int32

bf\_backfilled\_het\_jobs (optional)

[Integer](#integer) Number of heterogeneous job components started through backfilling since last Slurm start format: int32

bf\_cycle\_counter (optional)

[Integer](#integer) Number of backfill scheduling cycles since last reset format: int32

bf\_cycle\_mean (optional)

[Long](#long) Mean time in microseconds of backfilling scheduling cycles since last reset format: int64

bf\_depth\_mean (optional)

[Long](#long) Mean number of eligible to run jobs processed during all backfilling scheduling cycles since last reset format: int64

bf\_depth\_mean\_try (optional)

[Long](#long) The subset of Depth Mean that the backfill scheduler attempted to schedule format: int64

bf\_cycle\_sum (optional)

[Long](#long) Total time in microseconds of backfilling scheduling cycles since last reset format: int64

bf\_cycle\_last (optional)

[Integer](#integer) Execution time in microseconds of last backfill scheduling cycle format: int32

bf\_cycle\_max (optional)

[Integer](#integer) Execution time in microseconds of longest backfill scheduling cycle format: int32

bf\_exit (optional)

[v0.0.44\_bf\_exit\_fields](#v0.0.44_bf_exit_fields)

bf\_last\_depth (optional)

[Integer](#integer) Number of processed jobs during last backfilling scheduling cycle format: int32

bf\_last\_depth\_try (optional)

[Integer](#integer) Number of processed jobs during last backfilling scheduling cycle that had a chance to start using available resources format: int32

bf\_depth\_sum (optional)

[Integer](#integer) Total number of jobs processed during all backfilling scheduling cycles since last reset format: int32

bf\_depth\_try\_sum (optional)

[Integer](#integer) Subset of bf\_depth\_sum that the backfill scheduler attempted to schedule format: int32

bf\_queue\_len (optional)

[Integer](#integer) Number of jobs pending to be processed by backfilling algorithm format: int32

bf\_queue\_len\_mean (optional)

[Long](#long) Mean number of jobs pending to be processed by backfilling algorithm format: int64

bf\_queue\_len\_sum (optional)

[Integer](#integer) Total number of jobs pending to be processed by backfilling algorithm since last reset format: int32

bf\_table\_size (optional)

[Integer](#integer) Number of different time slots tested by the backfill scheduler in its last iteration format: int32

bf\_table\_size\_sum (optional)

[Integer](#integer) Total number of different time slots tested by the backfill scheduler format: int32

bf\_table\_size\_mean (optional)

[Long](#long) Mean number of different time slots tested by the backfill scheduler format: int64

bf\_when\_last\_cycle (optional)

[v0.0.44\_uint64\_no\_val\_struct](#v0.0.44_uint64_no_val_struct)

bf\_active (optional)

[Boolean](#boolean) Backfill scheduler currently running

rpcs\_by\_message\_type (optional)

[array[v0.0.44\_stats\_msg\_rpc\_type]](#v0.0.44_stats_msg_rpc_type) RPCs by type

rpcs\_by\_user (optional)

[array[v0.0.44\_stats\_msg\_rpc\_user]](#v0.0.44_stats_msg_rpc_user) RPCs by user

pending\_rpcs (optional)

[array[v0.0.44\_stats\_msg\_rpc\_queue]](#v0.0.44_stats_msg_rpc_queue) Pending RPCs

pending\_rpcs\_by\_hostlist (optional)

[array[v0.0.44\_stats\_msg\_rpc\_dump]](#v0.0.44_stats_msg_rpc_dump) Pending RPCs by hostlist

### `v0.0.44_stats_msg_rpc_dump` - [Up](#__Models)

type\_id

[Integer](#integer) Message type as integer format: int32

message\_type

[String](#string) Message type as string (Slurm RPC message type)

count

[array[String]](#string)

### `v0.0.44_stats_msg_rpc_queue` - [Up](#__Models)

type\_id

[Integer](#integer) Message type as integer format: int32

message\_type

[String](#string) Message type as string (Slurm RPC message type)

count

[Integer](#integer) Number of pending RPCs queued format: int32

### `v0.0.44_stats_msg_rpc_type` - [Up](#__Models)

type\_id

[Integer](#integer) Message type as integer format: int32

message\_type

[String](#string) Message type as string (Slurm RPC message type)

count

[Integer](#integer) Number of RPCs received format: int32

queued

[Integer](#integer) Number of RPCs queued format: int32

dropped

[Long](#long) Number of RPCs dropped format: int64

cycle\_last

[Integer](#integer) Number of RPCs processed within the last RPC queue cycle format: int32

cycle\_max

[Integer](#integer) Maximum number of RPCs processed within a RPC queue cycle since start format: int32

total\_time

[Long](#long) Total time spent processing RPC in seconds format: int64

average\_time

[v0.0.44\_uint64\_no\_val\_struct](#v0.0.44_uint64_no_val_struct)

### `v0.0.44_stats_msg_rpc_user` - [Up](#__Models)

user\_id

[Integer](#integer) User ID (numeric) format: int32

user

[String](#string) User name

count

[Integer](#integer) Number of RPCs received format: int32

total\_time

[Long](#long) Total time spent processing RPC in seconds format: int64

average\_time

[v0.0.44\_uint64\_no\_val\_struct](#v0.0.44_uint64_no_val_struct)

### `v0.0.44_stats_rec` - [Up](#__Models)

time\_start (optional)

[Long](#long) When data collection started (UNIX timestamp) (UNIX timestamp or time string recognized by Slurm (e.g., '[MM/DD[/YY]-]HH:MM[:SS]')) format: int64

rollups (optional)

[v0.0.44\_rollup\_stats](#v0.0.44_rollup_stats)

RPCs (optional)

[array[v0.0.44\_stats\_rpc]](#v0.0.44_stats_rpc)

users (optional)

[array[v0.0.44\_stats\_user]](#v0.0.44_stats_user)

### `v0.0.44_stats_rpc` - [Up](#__Models)

rpc (optional)

[String](#string) RPC type

count (optional)

[Integer](#integer) Number of RPCs processed format: int32

time (optional)

[v0\_0\_44\_stats\_rpc\_time](#v0_0_44_stats_rpc_time)

### `v0.0.44_stats_user` - [Up](#__Models)

user (optional)

[String](#string) User ID

count (optional)

[Integer](#integer) Number of RPCs processed format: int32

time (optional)

[v0\_0\_44\_stats\_rpc\_time](#v0_0_44_stats_rpc_time)

### `v0.0.44_step` - [Up](#__Models)

time (optional)

[v0\_0\_44\_step\_time](#v0_0_44_step_time)

exit\_code (optional)

[v0.0.44\_process\_exit\_code\_verbose](#v0.0.44_process_exit_code_verbose)

nodes (optional)

[v0\_0\_44\_step\_nodes](#v0_0_44_step_nodes)

tasks (optional)

[v0\_0\_44\_step\_tasks](#v0_0_44_step_tasks)

pid (optional)

[String](#string) Deprecated; Process ID

CPU (optional)

[v0\_0\_44\_step\_CPU](#v0_0_44_step_CPU)

kill\_request\_user (optional)

[String](#string) User ID that requested termination of the step

state (optional)

[array[String]](#string) Current state

Enum:

statistics (optional)

[v0\_0\_44\_step\_statistics](#v0_0_44_step_statistics)

step (optional)

[v0\_0\_44\_step\_step](#v0_0_44_step_step)

task (optional)

[v0\_0\_44\_step\_task](#v0_0_44_step_task)

tres (optional)

[v0\_0\_44\_step\_tres](#v0_0_44_step_tres)

### `v0.0.44_tres` - [Up](#__Models)

type

[String](#string) TRES type (CPU, MEM, etc)

name (optional)

[String](#string) TRES name (if applicable)

id (optional)

[Integer](#integer) ID used in the database format: int32

count (optional)

[Long](#long) TRES count (0 if listed generically) format: int64

### `v0.0.44_uint16_no_val_struct` - [Up](#__Models)

set (optional)

[Boolean](#boolean) True if number has been set; False if number is unset

infinite (optional)

[Boolean](#boolean) True if number has been set to infinite; "set" and "number" will be ignored

number (optional)

[Integer](#integer) If "set" is True the number will be set with value; otherwise ignore number contents format: int32

### `v0.0.44_uint32_no_val_struct` - [Up](#__Models)

set (optional)

[Boolean](#boolean) True if number has been set; False if number is unset

infinite (optional)

[Boolean](#boolean) True if number has been set to infinite; "set" and "number" will be ignored

number (optional)

[Integer](#integer) If "set" is True the number will be set with value; otherwise ignore number contents format: int32

### `v0.0.44_uint64_no_val_struct` - [Up](#__Models)

set (optional)

[Boolean](#boolean) True if number has been set; False if number is unset

infinite (optional)

[Boolean](#boolean) True if number has been set to infinite; "set" and "number" will be ignored

number (optional)

[Long](#long) If "set" is True the number will be set with value; otherwise ignore number contents format: int64

### `v0.0.44_update_node_msg` - [Up](#__Models)

comment (optional)

[String](#string) Arbitrary comment

cpu\_bind (optional)

[Integer](#integer) Default method for binding tasks to allocated CPUs format: int32

extra (optional)

[String](#string) Arbitrary string used for node filtering if extra constraints are enabled

features (optional)

[array[String]](#string)

features\_act (optional)

[array[String]](#string)

gres (optional)

[String](#string) Generic resources

address (optional)

[array[String]](#string)

hostname (optional)

[array[String]](#string)

name (optional)

[array[String]](#string)

state (optional)

[array[String]](#string) New state to assign to the node

Enum:

reason (optional)

[String](#string) Reason for node being DOWN or DRAINING

reason\_uid (optional)

[String](#string) User ID to associate with the reason (needed if user root is sending message)

resume\_after (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

topology\_str (optional)

[String](#string) Topology

weight (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

### `v0.0.44_user` - [Up](#__Models)

administrator\_level (optional)

[array[String]](#string) AdminLevel granted to the user

Enum:

associations (optional)

[array[v0.0.44\_assoc\_short]](#v0.0.44_assoc_short)

coordinators (optional)

[array[v0.0.44\_coord]](#v0.0.44_coord)

default (optional)

[v0\_0\_44\_user\_default](#v0_0_44_user_default)

flags (optional)

[array[String]](#string) Flags associated with this user

Enum:

name

[String](#string) User name

old\_name (optional)

[String](#string) Previous user name

wckeys (optional)

[array[v0.0.44\_wckey]](#v0.0.44_wckey)

### `v0.0.44_user_short` - [Up](#__Models)

adminlevel (optional)

[array[String]](#string) AdminLevel granted to the user

Enum:

defaultqos (optional)

[Integer](#integer) Default QOS format: int32

defaultaccount (optional)

[String](#string) Default account

defaultwckey (optional)

[String](#string) Default WCKey

### `v0.0.44_users_add_cond` - [Up](#__Models)

accounts (optional)

[array[String]](#string)

association (optional)

[v0.0.44\_assoc\_rec\_set](#v0.0.44_assoc_rec_set)

clusters (optional)

[array[String]](#string)

partitions (optional)

[array[String]](#string)

users

[array[String]](#string)

wckeys (optional)

[array[String]](#string)

### `v0.0.44_wckey` - [Up](#__Models)

accounting (optional)

[array[v0.0.44\_accounting]](#v0.0.44_accounting)

cluster

[String](#string) Cluster name

id (optional)

[Integer](#integer) Unique ID for this user-cluster-wckey combination format: int32

name

[String](#string) WCKey name

user

[String](#string) User name

flags (optional)

[array[String]](#string) Flags associated with this WCKey

Enum:

### `v0.0.44_wckey_tag_struct` - [Up](#__Models)

wckey

[String](#string) WCKey name

flags

[array[String]](#string) Active flags

Enum:

### `v0_0_44_accounting_allocated` - [Up](#__Models)

seconds (optional)

[Long](#long) Number of seconds allocated format: int64

### `v0_0_44_assoc_default` - [Up](#__Models)

qos (optional)

[String](#string) Default QOS

### `v0_0_44_assoc_max` - [Up](#__Models)

jobs (optional)

[v0\_0\_44\_assoc\_max\_jobs](#v0_0_44_assoc_max_jobs)

tres (optional)

[v0\_0\_44\_assoc\_max\_tres](#v0_0_44_assoc_max_tres)

per (optional)

[v0\_0\_44\_assoc\_max\_per](#v0_0_44_assoc_max_per)

### `v0_0_44_assoc_max_jobs` - [Up](#__Models)

per (optional)

[v0\_0\_44\_assoc\_max\_jobs\_per](#v0_0_44_assoc_max_jobs_per)

active (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

accruing (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

total (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

### `v0_0_44_assoc_max_jobs_per` - [Up](#__Models)

count (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

accruing (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

submitted (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

wall\_clock (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

### `v0_0_44_assoc_max_per` - [Up](#__Models)

account (optional)

[v0\_0\_44\_assoc\_max\_per\_account](#v0_0_44_assoc_max_per_account)

### `v0_0_44_assoc_max_per_account` - [Up](#__Models)

wall\_clock (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

### `v0_0_44_assoc_max_tres` - [Up](#__Models)

total (optional)

[array[v0.0.44\_tres]](#v0.0.44_tres)

group (optional)

[v0\_0\_44\_assoc\_max\_tres\_group](#v0_0_44_assoc_max_tres_group)

minutes (optional)

[v0\_0\_44\_assoc\_max\_tres\_minutes](#v0_0_44_assoc_max_tres_minutes)

per (optional)

[v0\_0\_44\_assoc\_max\_tres\_per](#v0_0_44_assoc_max_tres_per)

### `v0_0_44_assoc_max_tres_group` - [Up](#__Models)

minutes (optional)

[array[v0.0.44\_tres]](#v0.0.44_tres)

active (optional)

[array[v0.0.44\_tres]](#v0.0.44_tres)

### `v0_0_44_assoc_max_tres_minutes` - [Up](#__Models)

total (optional)

[array[v0.0.44\_tres]](#v0.0.44_tres)

per (optional)

[v0\_0\_44\_qos\_limits\_min\_tres\_per](#v0_0_44_qos_limits_min_tres_per)

### `v0_0_44_assoc_max_tres_per` - [Up](#__Models)

job (optional)

[array[v0.0.44\_tres]](#v0.0.44_tres)

node (optional)

[array[v0.0.44\_tres]](#v0.0.44_tres)

### `v0_0_44_assoc_min` - [Up](#__Models)

priority\_threshold (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

### `v0_0_44_assoc_shares_obj_wrap_fairshare` - [Up](#__Models)

factor (optional)

[v0.0.44\_float64\_no\_val\_struct](#v0.0.44_float64_no_val_struct)

level (optional)

[v0.0.44\_float64\_no\_val\_struct](#v0.0.44_float64_no_val_struct)

### `v0_0_44_assoc_shares_obj_wrap_tres` - [Up](#__Models)

run\_seconds (optional)

[array[v0.0.44\_shares\_uint64\_tres]](#v0.0.44_shares_uint64_tres)

group\_minutes (optional)

[array[v0.0.44\_shares\_uint64\_tres]](#v0.0.44_shares_uint64_tres)

usage (optional)

[array[v0.0.44\_shares\_float128\_tres]](#v0.0.44_shares_float128_tres)

### `v0_0_44_cluster_rec_associations` - [Up](#__Models)

root (optional)

[v0.0.44\_assoc\_short](#v0.0.44_assoc_short)

### `v0_0_44_cluster_rec_controller` - [Up](#__Models)

host (optional)

[String](#string) ControlHost

port (optional)

[Integer](#integer) ControlPort format: int32

### `v0_0_44_cron_entry_line` - [Up](#__Models)

start (optional)

[Integer](#integer) Start of this entry in file format: int32

end (optional)

[Integer](#integer) End of this entry in file format: int32

### `v0_0_44_instance_time` - [Up](#__Models)

time\_end (optional)

[Long](#long) When the instance will end (UNIX timestamp) (UNIX timestamp or time string recognized by Slurm (e.g., '[MM/DD[/YY]-]HH:MM[:SS]')) format: int64

time\_start (optional)

[Long](#long) When the instance will start (UNIX timestamp) (UNIX timestamp or time string recognized by Slurm (e.g., '[MM/DD[/YY]-]HH:MM[:SS]')) format: int64

### `v0_0_44_job_array` - [Up](#__Models)

job\_id (optional)

[Integer](#integer) Job ID of job array, or 0 if N/A format: int32

limits (optional)

[v0\_0\_44\_job\_array\_limits](#v0_0_44_job_array_limits)

task\_id (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

task (optional)

[String](#string) String expression of task IDs in this record

### `v0_0_44_job_array_limits` - [Up](#__Models)

max (optional)

[v0\_0\_44\_job\_array\_limits\_max](#v0_0_44_job_array_limits_max)

### `v0_0_44_job_array_limits_max` - [Up](#__Models)

running (optional)

[v0\_0\_44\_job\_array\_limits\_max\_running](#v0_0_44_job_array_limits_max_running)

### `v0_0_44_job_array_limits_max_running` - [Up](#__Models)

tasks (optional)

[Integer](#integer) Maximum number of simultaneously running tasks, 0 if no limit format: int32

### `v0_0_44_job_comment` - [Up](#__Models)

administrator (optional)

[String](#string) Arbitrary comment made by administrator

job (optional)

[String](#string) Arbitrary comment made by user

system (optional)

[String](#string) Arbitrary comment from slurmctld

### `v0_0_44_job_desc_msg_rlimits` - [Up](#__Models)

cpu (optional)

[v0.0.44\_uint64\_no\_val\_struct](#v0.0.44_uint64_no_val_struct)

fsize (optional)

[v0.0.44\_uint64\_no\_val\_struct](#v0.0.44_uint64_no_val_struct)

data (optional)

[v0.0.44\_uint64\_no\_val\_struct](#v0.0.44_uint64_no_val_struct)

stack (optional)

[v0.0.44\_uint64\_no\_val\_struct](#v0.0.44_uint64_no_val_struct)

core (optional)

[v0.0.44\_uint64\_no\_val\_struct](#v0.0.44_uint64_no_val_struct)

rss (optional)

[v0.0.44\_uint64\_no\_val\_struct](#v0.0.44_uint64_no_val_struct)

nproc (optional)

[v0.0.44\_uint64\_no\_val\_struct](#v0.0.44_uint64_no_val_struct)

nofile (optional)

[v0.0.44\_uint64\_no\_val\_struct](#v0.0.44_uint64_no_val_struct)

memlock (optional)

[v0.0.44\_uint64\_no\_val\_struct](#v0.0.44_uint64_no_val_struct)

as (optional)

[v0.0.44\_uint64\_no\_val\_struct](#v0.0.44_uint64_no_val_struct)

### `v0_0_44_job_het` - [Up](#__Models)

job\_id (optional)

[Integer](#integer) Heterogeneous job ID, if applicable format: int32

job\_offset (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

### `v0_0_44_job_info_power` - [Up](#__Models)

flags (optional)

[array[oas\_any\_type\_not\_mapped]](#AnyType)

### `v0_0_44_job_mcs` - [Up](#__Models)

label (optional)

[String](#string) Multi-Category Security label on the job

### `v0_0_44_job_modify_tres` - [Up](#__Models)

allocated (optional)

[array[v0.0.44\_tres]](#v0.0.44_tres)

### `v0_0_44_job_required` - [Up](#__Models)

CPUs (optional)

[Integer](#integer) Minimum number of CPUs required format: int32

memory\_per\_cpu (optional)

[v0.0.44\_uint64\_no\_val\_struct](#v0.0.44_uint64_no_val_struct)

memory\_per\_node (optional)

[v0.0.44\_uint64\_no\_val\_struct](#v0.0.44_uint64_no_val_struct)

### `v0_0_44_job_res_node_cpus` - [Up](#__Models)

count (optional)

[Integer](#integer) Total number of CPUs assigned to job format: int32

used (optional)

[Integer](#integer) Total number of CPUs used by job format: int32

### `v0_0_44_job_res_node_memory` - [Up](#__Models)

used (optional)

[Long](#long) Total memory (MiB) used by job format: int64

allocated (optional)

[Long](#long) Total memory (MiB) allocated to job format: int64

### `v0_0_44_job_res_nodes` - [Up](#__Models)

count (optional)

[Integer](#integer) Number of allocated nodes format: int32

select\_type (optional)

[array[String]](#string) Node scheduling selection method

Enum:

list (optional)

[String](#string) Node(s) allocated to the job

whole (optional)

[Boolean](#boolean) Whether whole nodes were allocated

allocation (optional)

[array[v0.0.44\_job\_res\_node]](#v0.0.44_job_res_node) Job resources for a node

### `v0_0_44_job_reservation` - [Up](#__Models)

id (optional)

[Integer](#integer) Unique identifier of requested reservation format: int32

name (optional)

[String](#string) Name of reservation to use

requested (optional)

[String](#string) Comma-separated list of requested reservation names

### `v0_0_44_job_state` - [Up](#__Models)

current (optional)

[array[String]](#string) Current state

Enum:

reason (optional)

[String](#string) Reason for previous Pending or Failed state

### `v0_0_44_job_time` - [Up](#__Models)

elapsed (optional)

[Integer](#integer) Elapsed time in seconds format: int32

eligible (optional)

[Long](#long) Time when the job became eligible to run (UNIX timestamp) (UNIX timestamp or time string recognized by Slurm (e.g., '[MM/DD[/YY]-]HH:MM[:SS]')) format: int64

end (optional)

[Long](#long) End time (UNIX timestamp) (UNIX timestamp or time string recognized by Slurm (e.g., '[MM/DD[/YY]-]HH:MM[:SS]')) format: int64

planned (optional)

[v0.0.44\_uint64\_no\_val\_struct](#v0.0.44_uint64_no_val_struct)

start (optional)

[Long](#long) Time execution began (UNIX timestamp) (UNIX timestamp or time string recognized by Slurm (e.g., '[MM/DD[/YY]-]HH:MM[:SS]')) format: int64

submission (optional)

[Long](#long) Time when the job was submitted (UNIX timestamp) (UNIX timestamp or time string recognized by Slurm (e.g., '[MM/DD[/YY]-]HH:MM[:SS]')) format: int64

suspended (optional)

[Integer](#integer) Total time in suspended state in seconds format: int32

system (optional)

[v0\_0\_44\_job\_time\_system](#v0_0_44_job_time_system)

limit (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

total (optional)

[v0\_0\_44\_job\_time\_total](#v0_0_44_job_time_total)

user (optional)

[v0\_0\_44\_job\_time\_user](#v0_0_44_job_time_user)

### `v0_0_44_job_time_system` - [Up](#__Models)

seconds (optional)

[Long](#long) System CPU time used by the job in seconds format: int64

microseconds (optional)

[Long](#long) System CPU time used by the job in microseconds format: int64

### `v0_0_44_job_time_total` - [Up](#__Models)

seconds (optional)

[Long](#long) Sum of System and User CPU time used by the job in seconds format: int64

microseconds (optional)

[Long](#long) Sum of System and User CPU time used by the job in microseconds format: int64

### `v0_0_44_job_time_user` - [Up](#__Models)

seconds (optional)

[Long](#long) User CPU time used by the job in seconds format: int64

microseconds (optional)

[Long](#long) User CPU time used by the job in microseconds format: int64

### `v0_0_44_job_tres` - [Up](#__Models)

allocated (optional)

[array[v0.0.44\_tres]](#v0.0.44_tres)

requested (optional)

[array[v0.0.44\_tres]](#v0.0.44_tres)

### `v0_0_44_kill_jobs_resp_job_error` - [Up](#__Models)

string (optional)

[String](#string) String error encountered signaling job

code (optional)

[Integer](#integer) Numeric error encountered signaling job format: int32

message (optional)

[String](#string) Error message why signaling job failed

### `v0_0_44_kill_jobs_resp_job_federation` - [Up](#__Models)

sibling (optional)

[String](#string) Name of federation sibling (may be empty for non-federation)

### `v0_0_44_openapi_meta_client` - [Up](#__Models)

source (optional)

[String](#string) Client source description

user (optional)

[String](#string) Client user (if known)

group (optional)

[String](#string) Client group (if known)

### `v0_0_44_openapi_meta_plugin` - [Up](#__Models)

type (optional)

[String](#string) Slurm plugin type (if applicable)

name (optional)

[String](#string) Slurm plugin name (if applicable)

data\_parser (optional)

[String](#string) Slurm data\_parser plugin

accounting\_storage (optional)

[String](#string) Slurm accounting plugin

### `v0_0_44_openapi_meta_slurm` - [Up](#__Models)

version (optional)

[v0\_0\_44\_openapi\_meta\_slurm\_version](#v0_0_44_openapi_meta_slurm_version)

release (optional)

[String](#string) Slurm release string

cluster (optional)

[String](#string) Slurm cluster name

### `v0_0_44_openapi_meta_slurm_version` - [Up](#__Models)

major (optional)

[String](#string) Slurm release major version

micro (optional)

[String](#string) Slurm release micro version

minor (optional)

[String](#string) Slurm release minor version

### `v0_0_44_partition_info_accounts` - [Up](#__Models)

allowed (optional)

[String](#string) AllowAccounts - Comma-separated list of accounts which may execute jobs in the partition

deny (optional)

[String](#string) DenyAccounts - Comma-separated list of accounts which may not execute jobs in the partition

### `v0_0_44_partition_info_cpus` - [Up](#__Models)

task\_binding (optional)

[Integer](#integer) CpuBind - Default method controlling how tasks are bound to allocated resources format: int32

total (optional)

[Integer](#integer) TotalCPUs - Number of CPUs available in this partition format: int32

### `v0_0_44_partition_info_defaults` - [Up](#__Models)

memory\_per\_cpu (optional)

[Long](#long) Raw value for DefMemPerCPU or DefMemPerNode format: int64

partition\_memory\_per\_cpu (optional)

[v0.0.44\_uint64\_no\_val\_struct](#v0.0.44_uint64_no_val_struct)

partition\_memory\_per\_node (optional)

[v0.0.44\_uint64\_no\_val\_struct](#v0.0.44_uint64_no_val_struct)

time (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

job (optional)

[String](#string) JobDefaults - Comma-separated list of job default values (this field is only used to set new defaults)

### `v0_0_44_partition_info_groups` - [Up](#__Models)

allowed (optional)

[String](#string) AllowGroups - Comma-separated list of group names which may execute jobs in this partition

### `v0_0_44_partition_info_maximums` - [Up](#__Models)

cpus\_per\_node (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

cpus\_per\_socket (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

memory\_per\_cpu (optional)

[Long](#long) Raw value for MaxMemPerCPU or MaxMemPerNode format: int64

partition\_memory\_per\_cpu (optional)

[v0.0.44\_uint64\_no\_val\_struct](#v0.0.44_uint64_no_val_struct)

partition\_memory\_per\_node (optional)

[v0.0.44\_uint64\_no\_val\_struct](#v0.0.44_uint64_no_val_struct)

nodes (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

shares (optional)

[Integer](#integer) OverSubscribe - Controls the ability of the partition to execute more than one job at a time on each resource format: int32

oversubscribe (optional)

[v0\_0\_44\_partition\_info\_maximums\_oversubscribe](#v0_0_44_partition_info_maximums_oversubscribe)

time (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

over\_time\_limit (optional)

[v0.0.44\_uint16\_no\_val\_struct](#v0.0.44_uint16_no_val_struct)

### `v0_0_44_partition_info_maximums_oversubscribe` - [Up](#__Models)

jobs (optional)

[Integer](#integer) Maximum number of jobs allowed to oversubscribe resources format: int32

flags (optional)

[array[String]](#string) Flags applicable to the OverSubscribe setting

Enum:

### `v0_0_44_partition_info_minimums` - [Up](#__Models)

nodes (optional)

[Integer](#integer) MinNodes - Minimum count of nodes which may be allocated to any single job format: int32

### `v0_0_44_partition_info_nodes` - [Up](#__Models)

allowed\_allocation (optional)

[String](#string) AllocNodes - Comma-separated list of nodes from which users can submit jobs in the partition

configured (optional)

[String](#string) Nodes - Comma-separated list of nodes which are associated with this partition

total (optional)

[Integer](#integer) TotalNodes - Number of nodes available in this partition format: int32

### `v0_0_44_partition_info_partition` - [Up](#__Models)

state (optional)

[array[String]](#string) Current state(s)

Enum:

### `v0_0_44_partition_info_priority` - [Up](#__Models)

job\_factor (optional)

[Integer](#integer) PriorityJobFactor - Partition factor used by priority/multifactor plugin in calculating job priority format: int32

tier (optional)

[Integer](#integer) PriorityTier - Controls the order in which the scheduler evaluates jobs from different partitions format: int32

### `v0_0_44_partition_info_qos` - [Up](#__Models)

allowed (optional)

[String](#string) AllowQOS - Comma-separated list of Qos which may execute jobs in the partition

deny (optional)

[String](#string) DenyQOS - Comma-separated list of Qos which may not execute jobs in the partition

assigned (optional)

[String](#string) QOS - QOS name containing limits that will apply to all jobs in this partition

### `v0_0_44_partition_info_timeouts` - [Up](#__Models)

resume (optional)

[v0.0.44\_uint16\_no\_val\_struct](#v0.0.44_uint16_no_val_struct)

suspend (optional)

[v0.0.44\_uint16\_no\_val\_struct](#v0.0.44_uint16_no_val_struct)

### `v0_0_44_partition_info_tres` - [Up](#__Models)

billing\_weights (optional)

[String](#string) TRESBillingWeights - Billing weights of each tracked TRES type that will be used in calculating the usage of a job

configured (optional)

[String](#string) TRES - Number of each applicable TRES type available in this partition

### `v0_0_44_process_exit_code_verbose_signal` - [Up](#__Models)

id (optional)

[v0.0.44\_uint16\_no\_val\_struct](#v0.0.44_uint16_no_val_struct)

name (optional)

[String](#string) Signal sent to process (name)

### `v0_0_44_qos_limits` - [Up](#__Models)

grace\_time (optional)

[Integer](#integer) GraceTime - Preemption grace time in seconds to be extended to a job which has been selected for preemption format: int32

max (optional)

[v0\_0\_44\_qos\_limits\_max](#v0_0_44_qos_limits_max)

factor (optional)

[v0.0.44\_float64\_no\_val\_struct](#v0.0.44_float64_no_val_struct)

min (optional)

[v0\_0\_44\_qos\_limits\_min](#v0_0_44_qos_limits_min)

### `v0_0_44_qos_limits_max` - [Up](#__Models)

active\_jobs (optional)

[v0\_0\_44\_qos\_limits\_max\_active\_jobs](#v0_0_44_qos_limits_max_active_jobs)

jobs (optional)

[v0\_0\_44\_qos\_limits\_max\_jobs](#v0_0_44_qos_limits_max_jobs)

tres (optional)

[v0\_0\_44\_qos\_limits\_max\_tres](#v0_0_44_qos_limits_max_tres)

wall\_clock (optional)

[v0\_0\_44\_qos\_limits\_max\_wall\_clock](#v0_0_44_qos_limits_max_wall_clock)

accruing (optional)

[v0\_0\_44\_qos\_limits\_max\_jobs\_active\_jobs](#v0_0_44_qos_limits_max_jobs_active_jobs)

### `v0_0_44_qos_limits_max_active_jobs` - [Up](#__Models)

accruing (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

count (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

### `v0_0_44_qos_limits_max_jobs` - [Up](#__Models)

count (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

active\_jobs (optional)

[v0\_0\_44\_qos\_limits\_max\_jobs\_active\_jobs](#v0_0_44_qos_limits_max_jobs_active_jobs)

per (optional)

[v0\_0\_44\_qos\_limits\_max\_jobs\_active\_jobs\_per](#v0_0_44_qos_limits_max_jobs_active_jobs_per)

### `v0_0_44_qos_limits_max_jobs_active_jobs` - [Up](#__Models)

per (optional)

[v0\_0\_44\_qos\_limits\_max\_jobs\_active\_jobs\_per](#v0_0_44_qos_limits_max_jobs_active_jobs_per)

### `v0_0_44_qos_limits_max_jobs_active_jobs_per` - [Up](#__Models)

account (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

user (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

### `v0_0_44_qos_limits_max_tres` - [Up](#__Models)

total (optional)

[array[v0.0.44\_tres]](#v0.0.44_tres)

minutes (optional)

[v0\_0\_44\_qos\_limits\_max\_tres\_minutes](#v0_0_44_qos_limits_max_tres_minutes)

per (optional)

[v0\_0\_44\_qos\_limits\_max\_tres\_per](#v0_0_44_qos_limits_max_tres_per)

### `v0_0_44_qos_limits_max_tres_minutes` - [Up](#__Models)

total (optional)

[array[v0.0.44\_tres]](#v0.0.44_tres)

per (optional)

[v0\_0\_44\_qos\_limits\_max\_tres\_minutes\_per](#v0_0_44_qos_limits_max_tres_minutes_per)

### `v0_0_44_qos_limits_max_tres_minutes_per` - [Up](#__Models)

qos (optional)

[array[v0.0.44\_tres]](#v0.0.44_tres)

job (optional)

[array[v0.0.44\_tres]](#v0.0.44_tres)

account (optional)

[array[v0.0.44\_tres]](#v0.0.44_tres)

user (optional)

[array[v0.0.44\_tres]](#v0.0.44_tres)

### `v0_0_44_qos_limits_max_tres_per` - [Up](#__Models)

account (optional)

[array[v0.0.44\_tres]](#v0.0.44_tres)

job (optional)

[array[v0.0.44\_tres]](#v0.0.44_tres)

node (optional)

[array[v0.0.44\_tres]](#v0.0.44_tres)

user (optional)

[array[v0.0.44\_tres]](#v0.0.44_tres)

### `v0_0_44_qos_limits_max_wall_clock` - [Up](#__Models)

per (optional)

[v0\_0\_44\_qos\_limits\_max\_wall\_clock\_per](#v0_0_44_qos_limits_max_wall_clock_per)

### `v0_0_44_qos_limits_max_wall_clock_per` - [Up](#__Models)

qos (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

job (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

### `v0_0_44_qos_limits_min` - [Up](#__Models)

priority\_threshold (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

tres (optional)

[v0\_0\_44\_qos\_limits\_min\_tres](#v0_0_44_qos_limits_min_tres)

### `v0_0_44_qos_limits_min_tres` - [Up](#__Models)

per (optional)

[v0\_0\_44\_qos\_limits\_min\_tres\_per](#v0_0_44_qos_limits_min_tres_per)

### `v0_0_44_qos_limits_min_tres_per` - [Up](#__Models)

job (optional)

[array[v0.0.44\_tres]](#v0.0.44_tres)

### `v0_0_44_qos_preempt` - [Up](#__Models)

list (optional)

[array[String]](#string)

mode (optional)

[array[String]](#string) PreemptMode - Mechanism used to preempt jobs or enable gang scheduling

Enum:

exempt\_time (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

### `v0_0_44_reservation_info_purge_completed` - [Up](#__Models)

time (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

### `v0_0_44_rollup_stats_daily` - [Up](#__Models)

count (optional)

[Integer](#integer) Number of daily rollups since last\_run format: int32

last\_run (optional)

[Long](#long) Last time daily rollup ran (UNIX timestamp) (UNIX timestamp or time string recognized by Slurm (e.g., '[MM/DD[/YY]-]HH:MM[:SS]')) format: int64

duration (optional)

[v0\_0\_44\_rollup\_stats\_daily\_duration](#v0_0_44_rollup_stats_daily_duration)

### `v0_0_44_rollup_stats_daily_duration` - [Up](#__Models)

last (optional)

[Long](#long) Total time spent doing daily daily rollup (seconds) format: int64

max (optional)

[Long](#long) Longest daily rollup time (seconds) format: int64

time (optional)

[Long](#long) Total time spent doing daily rollups (seconds) format: int64

### `v0_0_44_rollup_stats_hourly` - [Up](#__Models)

count (optional)

[Integer](#integer) Number of hourly rollups since last\_run format: int32

last\_run (optional)

[Long](#long) Last time hourly rollup ran (UNIX timestamp) (UNIX timestamp or time string recognized by Slurm (e.g., '[MM/DD[/YY]-]HH:MM[:SS]')) format: int64

duration (optional)

[v0\_0\_44\_rollup\_stats\_hourly\_duration](#v0_0_44_rollup_stats_hourly_duration)

### `v0_0_44_rollup_stats_hourly_duration` - [Up](#__Models)

last (optional)

[Long](#long) Total time spent doing last daily rollup (seconds) format: int64

max (optional)

[Long](#long) Longest hourly rollup time (seconds) format: int64

time (optional)

[Long](#long) Total time spent doing hourly rollups (seconds) format: int64

### `v0_0_44_rollup_stats_monthly` - [Up](#__Models)

count (optional)

[Integer](#integer) Number of monthly rollups since last\_run format: int32

last\_run (optional)

[Long](#long) Last time monthly rollup ran (UNIX timestamp) (UNIX timestamp or time string recognized by Slurm (e.g., '[MM/DD[/YY]-]HH:MM[:SS]')) format: int64

duration (optional)

[v0\_0\_44\_rollup\_stats\_monthly\_duration](#v0_0_44_rollup_stats_monthly_duration)

### `v0_0_44_rollup_stats_monthly_duration` - [Up](#__Models)

last (optional)

[Long](#long) Total time spent doing monthly daily rollup (seconds) format: int64

max (optional)

[Long](#long) Longest monthly rollup time (seconds) format: int64

time (optional)

[Long](#long) Total time spent doing monthly rollups (seconds) format: int64

### `v0_0_44_stats_rpc_time` - [Up](#__Models)

average (optional)

[Long](#long) Average RPC processing time in microseconds format: int64

total (optional)

[Long](#long) Total RPC processing time in microseconds format: int64

### `v0_0_44_step_CPU` - [Up](#__Models)

requested\_frequency (optional)

[v0\_0\_44\_step\_CPU\_requested\_frequency](#v0_0_44_step_CPU_requested_frequency)

governor (optional)

[String](#string) Requested CPU frequency governor in kHz

### `v0_0_44_step_CPU_requested_frequency` - [Up](#__Models)

min (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

max (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

### `v0_0_44_step_nodes` - [Up](#__Models)

count (optional)

[Integer](#integer) Number of nodes in the job step format: int32

range (optional)

[String](#string) Node(s) allocated to the job step

list (optional)

[array[String]](#string)

### `v0_0_44_step_statistics` - [Up](#__Models)

CPU (optional)

[v0\_0\_44\_step\_statistics\_CPU](#v0_0_44_step_statistics_CPU)

energy (optional)

[v0\_0\_44\_step\_statistics\_energy](#v0_0_44_step_statistics_energy)

### `v0_0_44_step_statistics_CPU` - [Up](#__Models)

actual\_frequency (optional)

[Long](#long) Average weighted CPU frequency of all tasks in kHz format: int64

### `v0_0_44_step_statistics_energy` - [Up](#__Models)

consumed (optional)

[v0.0.44\_uint64\_no\_val\_struct](#v0.0.44_uint64_no_val_struct)

### `v0_0_44_step_step` - [Up](#__Models)

id (optional)

[String](#string) Step ID (Slurm job step ID)

name (optional)

[String](#string) Step name

stderr (optional)

[String](#string) Path to stderr file

stdin (optional)

[String](#string) Path to stdin file

stdout (optional)

[String](#string) Path to stdout file

stderr\_expanded (optional)

[String](#string) Step stderr with expanded fields

stdin\_expanded (optional)

[String](#string) Step stdin with expanded fields

stdout\_expanded (optional)

[String](#string) Step stdout with expanded fields

### `v0_0_44_step_task` - [Up](#__Models)

distribution (optional)

[String](#string) The layout of the step was when it was running

### `v0_0_44_step_tasks` - [Up](#__Models)

count (optional)

[Integer](#integer) Total number of tasks format: int32

### `v0_0_44_step_time` - [Up](#__Models)

elapsed (optional)

[Integer](#integer) Elapsed time in seconds format: int32

end (optional)

[v0.0.44\_uint64\_no\_val\_struct](#v0.0.44_uint64_no_val_struct)

start (optional)

[v0.0.44\_uint64\_no\_val\_struct](#v0.0.44_uint64_no_val_struct)

suspended (optional)

[Integer](#integer) Total time in suspended state in seconds format: int32

system (optional)

[v0\_0\_44\_step\_time\_system](#v0_0_44_step_time_system)

limit (optional)

[v0.0.44\_uint32\_no\_val\_struct](#v0.0.44_uint32_no_val_struct)

total (optional)

[v0\_0\_44\_step\_time\_total](#v0_0_44_step_time_total)

user (optional)

[v0\_0\_44\_step\_time\_user](#v0_0_44_step_time_user)

### `v0_0_44_step_time_system` - [Up](#__Models)

seconds (optional)

[Long](#long) System CPU time used by the step in seconds format: int64

microseconds (optional)

[Integer](#integer) System CPU time used by the step in microseconds format: int32

### `v0_0_44_step_time_total` - [Up](#__Models)

seconds (optional)

[Long](#long) Total CPU time used by the step in seconds format: int64

microseconds (optional)

[Integer](#integer) Total CPU time used by the step in microseconds format: int32

### `v0_0_44_step_time_user` - [Up](#__Models)

seconds (optional)

[Long](#long) User CPU time used by the step in seconds format: int64

microseconds (optional)

[Integer](#integer) User CPU time used by the step in microseconds format: int32

### `v0_0_44_step_tres` - [Up](#__Models)

requested (optional)

[v0\_0\_44\_step\_tres\_requested](#v0_0_44_step_tres_requested)

consumed (optional)

[v0\_0\_44\_step\_tres\_consumed](#v0_0_44_step_tres_consumed)

allocated (optional)

[array[v0.0.44\_tres]](#v0.0.44_tres)

### `v0_0_44_step_tres_consumed` - [Up](#__Models)

max (optional)

[array[v0.0.44\_tres]](#v0.0.44_tres)

min (optional)

[array[v0.0.44\_tres]](#v0.0.44_tres)

average (optional)

[array[v0.0.44\_tres]](#v0.0.44_tres)

total (optional)

[array[v0.0.44\_tres]](#v0.0.44_tres)

### `v0_0_44_step_tres_requested` - [Up](#__Models)

max (optional)

[array[v0.0.44\_tres]](#v0.0.44_tres)

min (optional)

[array[v0.0.44\_tres]](#v0.0.44_tres)

average (optional)

[array[v0.0.44\_tres]](#v0.0.44_tres)

total (optional)

[array[v0.0.44\_tres]](#v0.0.44_tres)

### `v0_0_44_user_default` - [Up](#__Models)

qos (optional)

[Integer](#integer) Default QOS format: int32

account (optional)

[String](#string) Default account

wckey (optional)

[String](#string) Default WCKey