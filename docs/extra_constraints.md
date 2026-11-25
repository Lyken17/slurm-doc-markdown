# Slurm Workload Manager - Extra Constraints

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

# Extra Constraints

## Contents

* [Overview](#Overview)
* [Configuration](#Configuration)
* [Node Extra Data](#Node_Extra_Data)
* [Job Submission](#Job_Submission)
  + [Syntax](#Syntax)
  + [Warnings](#Warnings)
  + [Valid and Invalid Requests](#Valid)
* [Scheduling](#Scheduling)
* [Examples](#Examples)

## Overview

Extra data may be added to a node, and jobs may request extra constraints
to filter nodes based on their extra data. This is disabled by
default, but may be enabled in slurm.conf. **Warning**: Slurm's backfill
scheduler cannot accurately plan nodes for jobs whose request extra constraints
are not immediately satisfied. This means that the more often extra data for
nodes is changed, the less accurate the backfill scheduler will be.

## Configuration

* In slurm.conf, configure
  `SchedulerParameters=extra_constraints`
* Load a serializer plugin that provides JSON, which is set by
  [SerializerPlugins](slurm.conf.md#OPT_SerializerPlugins).
  slurmctld fails to start without one.
  The default loads all serializer plugins, which includes one that provides
  JSON. If SerializerPlugins is set, it must include **json** or
  **xjson**.

## Node Extra Data

A node's extra data is a json formatted string. It may be initialized on
slurmd startup with the --extra flag for slurmd. For example:

```
slurmd --extra '{ "a": 1.23, "b": true, "c": 0, "foo": "bar", "zed": 23 }'
```

Or, it may be updated with scontrol. For example:

```
scontrol update nodename=node123 extra='{ "a": 1.23, "b": true, "c": 0, "foo": "bar", "zed": 23 }'
```

This defines the features that may be requested by the --extra option in
salloc, sbatch, and srun. Values may be any string, number, or boolean value.
Other JSON values (null, objects, and arrays) are accepted, but no request can
match them.

With **SchedulerParameters=extra\_constraints** enabled, extra data is parsed
by the serializer plugin that provides JSON, which is set by
[SerializerPlugins](slurm.conf.md#OPT_SerializerPlugins).
`scontrol update node` rejects extra data that the plugin cannot
parse with the error "Invalid extra constraints specification".
Extra data from `slurmd --extra` that the plugin cannot parse is
still stored and shown by `scontrol show node`, but no request can
match that node.
The same is true of stored extra data, which slurmctld parses again when it
starts, such as extra data set while **extra\_constraints** was not enabled
and so was not checked.
In each case, slurmctld logs "Failed to decode extra".
An empty value clears the extra data.

The extra data from `slurmd --extra` is applied when slurmd starts
and the node has not registered with slurmctld before, such as a new node or
after slurmctld is started with `-c`, or has booted since it last
responded, including when it is powered up by power saving.
It is not applied when only slurmd is restarted, so a value set with
`scontrol update node` is kept until the node boots again with
slurmd started with `--extra`.

## Job Submission

### Syntax

The salloc, sbatch, or srun --extra field is an arbitrary string enclosed in
single or double quotes if using spaces or some special characters.

If **SchedulerParameters=extra\_constraints** is enabled, this string is used
for node filtering based on the *Extra* field in each node.

The most basic request is structured like this:

```
<key><comparison_operator><value>
```

Key and value are arbitrary, non-empty strings that cannot contain any
characters that are part of operators and cannot contain parentheses. Thus,
the following characters are not allowed in a key or value:

```
,&|<>=!()
```

The following comparison operators are allowed:

* `= (equal to)`
* `!= (not equal to)`
* `> (greater than)`
* `>= (greater than or equal to)`
* `< (less than)`
* `<= (less than or equal to)`

The requested value is compared as the type of the node's value for the key:

* Numbers: two numbers are equal if their difference is less than 0.00001.
  Numerical suffixes (such as kb or mb) are not supported. A request whose value
  is not a number, such as `zed=23kb`, is not fulfilled by a node with
  a number for that key, whatever the comparison operator.
* Booleans: the requested value is false if it is a number equal to 0, or
  one of `false`, `f`, `no`, `n`,
  `off`, or `null`, or starts with `~` (not case
  sensitive). Any other value is true. A boolean is compared to a boolean with
  false less than true, so `b<=0.05` is fulfilled by a node with
  `"b": true` (0.05 is true) but `b<0.05` is not.
* Strings: compared byte by byte and are case sensitive, so
  `foo<baz` is fulfilled by a node with `"foo": "bar"`.
  A number in quotes, such as `"zed": "23"`, is a string.

A request for a key the node does not have is not fulfilled.

Requests can be joined together with boolean operators.

```
<request><boolean_operator><request>
```

The following boolean operators are allowed:

```
&   (AND)
,   (AND)
|   (OR)
```

Any number of parentheses may be used to group requests together.
AND and OR cannot be mixed at any given level of parentheses, but
`&` and `,` may be. Boolean operators at different
levels of parentheses may be different.
For example, this is not allowed:

```
a=1&b=2|c=foobar
```

But this is allowed:

```
(a=1&b=2)|c=foobar
```

### Warnings

Whitespace characters are not treated specially. Any whitespace characters will
be considered part of a key or value. This means that the following is invalid:

```
--extra " (a=b)"
```

The space at the beginning is parsed as a key of a request. Then the opening
parenthesis character is recognized as an invalid character for either a key
or a comparison operator. This request would result in the job being rejected.
However, this is valid:

```
--extra "( a=b)"
```

This has a single request. The key is " a", the comparison operator is "=", and
the value is "b".

This same warning applies to single and double quotes. These are not considered
special characters, and thus are part of a string. Thus, bar and "bar" are not
equal.

### Valid and Invalid Requests

Here are some examples of **valid** requests:

```
a=1.23
a=   b
a!=1.24
a!=1.23|foo!=blah
b=200
b=true
foo<baz
(c<=0.0001&a=1.25)|zed=23.0
((c<=0.0001&a=1.25)|zed=23.0)&(a<1|b=false|c>=0.00000001)
((c<=0.0001&a=1.25)|zed=23.0)&(a<1|b=true|c>=0.1)
```

Here are some examples of **invalid** requests:

Invalid comparison operator:

```
a,<=6
```

Trailing operator:

```
a<=6<=
```

Multiple boolean operators in a row:

```
a=5&&&b=5
a=5|||b=5
```

Multiple comparison operators in a row:

```
a====5
b<=<=5
```

Parentheses without anything inside:

```
a=5&()
```

Different boolean operators at a single level of parentheses:

```
a=5&b=5|c=5
(a=1)&(b=2)|(c=3)
```

No boolean operator between individual requests:

```
a=1(b=2)
(a=1)(b=2)
(((a=1)b=2))
```

## Scheduling

A request that is not valid is rejected when the job is submitted with the
error "Invalid extra constraints specification".
`scontrol update job` rejects a request that is not valid with the
same error.

A valid request that no node fulfills is not rejected. The job stays pending
with the reason "Constraints" until enough nodes fulfill the request, for
example after their extra data is updated with scontrol. This is the same for
salloc, sbatch, and srun; salloc and srun wait until the job starts unless
`--immediate` is used, in which case the job fails.

## Examples

Given a node with the following extra data:

```
Extra={ "a": 1.23, "b": true, "c": 0, "foo": "bar", "zed": 23 }
```

The following --extra requests are fulfilled by this node:

```
a=1.23
a!=1.24
a!=1.23|foo!=blah
b=200
b=true
foo<baz
(c<=0.0001&a=1.25)|zed=23.0
((c<=0.0001&a=1.25)|zed=23.0)&(a<1|b=false|c>=0.00000001)
((c<=0.0001&a=1.25)|zed=23.0)&(a<1|b=true|c>=0.1)
```

The following --extra requests are not fulfilled by this node:

```
a!=1.23
b=0
b=false
foo>baz
((c<=0.0001&a=1.25)|zed=23.0)&(a<1|b=false|c>=0.00001)
```

Reminder: in order for two numbers to be considered equal, their difference
must be less than 0.00001. This is why 0.00001 is not considered equal to 0 and
thus the request `c>=0.00001` is not fulfilled,
but 0.00000001 is considered equal to 0 and thus the request
`c>=0.00000001` is fulfilled. Because of floating point precision,
numbers whose difference is close to 0.00001 may or may not be considered equal.

A practical example might be to have a script that looks at the load average
of each node and updates the extra attribute for each node with the current
value. This would allow users to restrict their jobs to nodes whose load
average is below a certain threshold.

In this simple example, the three nodes in a cluster are being monitored and
the extra attribute is being populated with their load average.

```
$ scontrol show nodes node[01-03] | grep -E 'NodeName|Extra'
NodeName=node01 Arch=x86_64 CoresPerSocket=6
   Extra={ "load": 0.99 }
NodeName=node02 Arch=x86_64 CoresPerSocket=6
   Extra={ "load": 0.75 }
NodeName=node03 Arch=x86_64 CoresPerSocket=6
   Extra={ "load": 0.45 }
```

A job can request to run on a machine with less than half of the CPU time
being utilized.

```
$ sbatch -n12 --extra "load<0.5" --wrap='srun sleep 10'
Submitted batch job 11206

$ squeue
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
             11206     debug     wrap      ben  R       0:03      1 node03
```

A job can also request to run on a node between a range of acceptable load values.

```
$ sbatch -n12 --extra "(load<0.9&load>0.5)" --wrap='srun sleep 10'
Submitted batch job 11207

$ squeue
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
             11207     debug     wrap      ben  R       0:01      1 node02
```