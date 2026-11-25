# Slurm Workload Manager - Workload Characterization Key (WCKey) Management

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

# Workload Characterization Key (WCKey) Management

A WCKey (Workload Characterization Key) is a label recorded against a
job for accounting purposes. It is an orthogonal way to do accounting
against possibly unrelated accounts: a job is charged to exactly one
account in the account hierarchy, but its WCKey cuts across that
hierarchy. This can be useful where users from different accounts are
all working on the same project.

For example, a "climate\_model" project may draw on users in both the
"physics" and the "cs" account. Accounting by account tells you what
each department consumed; accounting by WCKey tells you what the
project consumed, no matter which account paid for it.

WCKeys are tracked per user and per cluster. Once
[WCKey tracking is enabled](#enable), every job gets a
WCKey, whether or not the user asked for one. New WCKeys appear as
jobs naming them start; see [Enforcing WCKeys](#enforce) to
restrict jobs to a controlled set of valid WCKeys instead.

## Contents

* [Enabling WCKeys](#enable)
* [sbatch/salloc/srun](#submit)
* [sacct](#sacct)
* [sreport](#sreport)
* [sacctmgr](#sacctmgr)
* [Enforcing WCKeys](#enforce)

## Enabling WCKeys

WCKey tracking requires Slurm accounting, so
[AccountingStorageType](slurm.conf.md#OPT_AccountingStorageType)
must be set to **accounting\_storage/slurmdbd** before any of this
applies.

To track the value of a job's WCKey, set the **TrackWCKey** option
to **yes** in both slurm.conf and slurmdbd.conf. The slurm.conf
setting records the WCKey on each job, while the slurmdbd.conf setting
generates the rolled-up WCKey usage tables that
[sreport](#sreport) consumes. Neither setting takes effect
until its daemon rereads its configuration.

**NOTE**: If **TrackWCKey** is set in your slurmdbd.conf file
but not in your slurm.conf file, jobs that do not request a WCKey will
be attributed to the user's default WCKey. See the
[slurmdbd.conf](slurmdbd.conf.md#OPT_TrackWCKey) man page
for details.

## sbatch/salloc/srun

Each submitting tool has the `--wckey=` option that can set
the WCKey for a job. [SBATCH|SALLOC|SLURM]\_WCKEY can also be set in the
environment to set the WCKey.

If no WCKey is given, the job is recorded under the user's default
WCKey for the cluster, which is set with [sacctmgr](#sacctmgr).
In that case the recorded WCKey is prefixed with a '\*' to signify that the
user did not ask for it. This is useful for a manager to determine if a
user is specifying their WCKey or not. The '\*' prefix is reserved, so a
WCKey beginning with '\*' cannot be requested with `--wckey`.

If the user has no default WCKey either, the job is recorded under a
WCKey of '\*' alone, unless [enforcement](#enforce) is
enabled, in which case the job is rejected at submission.

## sacct

Sacct can be used to view the WCKey by adding "wckey" to the
--format option. You can also single out jobs by using the
--wckeys= option which would only send information about jobs that
ran with specific WCKeys.

```
sacct --format=jobid,user,account,wckey
sacct --wckeys='secret_project,*secret_project'
```

The `--wckeys` option matches the recorded WCKey exactly, so
jobs that inherited the WCKey as a default and were recorded as
`*secret_project` only appear if you ask for that form too.

## sreport

The sreport command provides four reports covering WCKeys:

* `cluster UserUtilizationByWCKey` — users by WCKey in order
  of utilization, without grouping a user's WCKeys together.
* `cluster WCKeyUtilizationByUser` — utilization sorted by
  WCKey name.
* `job SizesByAccountAndWCKey` — time spent per account,
  broken down by job size, with each account paired with its WCKeys so the
  identifier is account:wckey.
* `job SizesByWCKey` — time spent per WCKey, broken down by
  job size.

Further information can be found on
the [sreport man page](sreport.md).

## sacctmgr

Sacctmgr is used to manage WCKeys. You can add and remove WCKeys
from users or list them. It is also used to set a user's default
WCKey and to create the WCKeys that
[enforcement](#enforce) requires.

You add a user to a WCKey much like you do an account, only the
WCKey doesn't need to be created before hand. i.e.

```
sacctmgr add user da wckey=secret_project
```

You can remove them from a WCKey in the same fashion.

```
sacctmgr del user da wckey=secret_project
```

To alter the user's default WCKey you can run a line like

```
sacctmgr mod user da cluster=snowflake set defaultwckey=secret_project
```

Which will change the default WCKey for user "da" on cluster
"snowflake" to be "secret\_project". If you want this for all clusters
just remove the cluster= option.

## Enforcing WCKeys

By default a WCKey is created the first time a job that names it
starts. That is convenient, but it means a typo silently becomes a new
WCKey, and a project's usage ends up split across several rows of your
[sreport](#sreport) output.

Add **wckeys** to **AccountingStorageEnforce** in slurm.conf to
enforce WCKeys per job. This means only jobs naming a WCKey that was
previously added for that user through [sacctmgr](#sacctmgr)
will be allowed to run. WCKeys are held per user, so adding one for a
single user does not let anyone else submit against it. A job naming a
WCKey the submitting user does not have is rejected when it is submitted,
as is a job that names no WCKey at all if that user has no default WCKey.

```
# slurm.conf
AccountingStorageEnforce=associations,wckeys
```

**NOTE**: Setting **AccountingStorageEnforce=wckeys** also
implies **associations**, so every user must have a valid
association before their jobs will be scheduled. It sets
**TrackWCKey** in slurm.conf automatically, but it has no effect on
slurmdbd. You must still set **TrackWCKey** in your slurmdbd.conf
file, or no rolled-up WCKey usage will be recorded.