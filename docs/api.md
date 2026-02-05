# Slurm Workload Manager - Slurm APIs

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

# Slurm APIs

### Overview

All of the Slurm commands utilize a collection of Application Programming
Interfaces (APIs) exposed through the "slurm.h" and "slurmdb.h" headers.
Slurm's APIs are fixed within each major release. They do change —
significantly — between each major release.

Developers are encouraged to target Slurm's [REST API](rest_api.md) which provides for broader cross-version compatibility.