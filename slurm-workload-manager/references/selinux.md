# Slurm Workload Manager - SELinux

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

# SELinux

Starting with version 21.08, Slurm includes support for setting an SELinux
context for jobs as a technology preview. The implementation may change in
future releases, and support for it is not enabled by default.

## Architecture

When enabled, the Slurm job submission commands — salloc, sbatch, and
srun — will automatically set a field with the current operating context.
This field can be overwritten by the --context
command line option.

It is important to note that this value can be directly manipulated by the
end-user, and it is up to site-specific scripts to validate and control access
to these contexts. At this time MUNGE, which Slurm users to security identify
users and hosts on the cluster, does not provide an SELinux context field, and
as such there is no secure mechanism to send the current context to the Slurm
controller. Thus the context, as provided at job submission time, **must**
be validated by a job\_submit plugin running within the slurmctld.

Without such a script, no context is set or managed for a user's job.

## Installation

### Source:

SELinux support is disabled by default and must be enabled at configure time.
It requires the libselinux1 library and development headers to build.

```
configure --enable-selinux
```

## Setup

Once a version of Slurm that supports SELinux is installed, you will need to
enable and create a job\_submit plugin that will perform verification of the
SELinux context, before passing it along to the slurmctld. At this time, there
is not a reliable and secure way to get/verify contexts internally so you MUST
create this script and perform verification in the job\_submit plugin.

Example:

```
function slurm_job_submit(job_desc, part_list, submit_uid)
  if job_desc.req_context then
    local element = 0
    for str in string.gmatch(job_desc.req_context, "([^:]+)") do
      if element == 0 and str ~= "unconfined_u" then
        slurm.log_user("Error: invalid SELinux context")
        return slurm.ERROR
      elseif element == 1 and str ~= "unconfined_r" then
        slurm.log_user("Error: %s is not a valid SELinux role")
        return slurm.ERROR
      end
      element = element + 1
    end
    job_desc.selinux_context = job_desc.req_context
  else
    -- Force a specific context if one wasn't requested
    job_desc.selinux_context = unconfined_u:unconfined_r:slurm_t:s0
  end
  return slurm.SUCCESS
end
```

Note that **job\_desc.selinux\_context** is set based on the contents of
**job\_desc.req\_context** if they are considered valid.
**job\_desc.selinux\_context** is what set the context that will be used.

## Initial Testing

id is very useful for showing what context a user is currently in. As a test
to make sure that we are switching contexts, you can run a quick test with srun.

```
mcmult@master:~$ srun id
uid=1000(mcmult) gid=1000(mcmult) groups=1000(mcmult),27(sudo) context=unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023
mcmult@master:~$ srun --context=unconfined_u:unconfined_r:unconfined_t:s0 id
uid=1000(mcmult) gid=1000(mcmult) groups=1000(mcmult),27(sudo) context=unconfined_u:unconfined_r:unconfined_t:s0
```

## Accounting

There is currently no support for tracking the SELinux context in Slurm's
accounting. This may change as support evolves in future releases.
If you need to keep track of the SELinux Context, it is possible to store it in
the admin comment field as part of your job\_submit plugin as is show in the
example below.

Example:

```
function slurm_job_submit(job_desc, part_list, submit_uid)
  if job_desc.req_context then
    local element = 0
    for str in string.gmatch(job_desc.req_context, "([^:]+)") do
      if element == 0 and str ~= "unconfined_u" then
        slurm.log_user("Error: invalid SELinux context")
        return slurm.ERROR
      elseif element == 1 and str ~= "unconfined_r" then
        slurm.log_user("Error: %s is not a valid SELinux role")
        return slurm.ERROR
      end
      element = element + 1
    end
    job_desc.selinux_context = job_desc.req_context
  else
    -- Force a specific context if one wasn't requested
    job_desc.selinux_context = unconfined_u:unconfined_r:slurm_t:s0
  end
  job_desc.admin_comment = "SELinuxContext=" .. job_desc.selinux_context
  return slurm.SUCCESS
end
```

Note the addition of setting "job\_desc.admin\_comment" before returning. This
will set the admin comment to show what context we will try to set for the job.

## Notes

If you wish to use pam\_slurm\_adopt with SELinux, see the
[pam\_slurm\_adopt](pam_slurm_adopt.md) documentation for hints on how
to get this working. Note that that when using this feature and
pam\_slurm\_adopt at the same time that the ssh session may not land in the same
context as the job.