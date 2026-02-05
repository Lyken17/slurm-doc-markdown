# Slurm Workload Manager - Adding Files or Plugins to Slurm

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

# Adding Files or Plugins to Slurm

## Adding a File to Slurm

This is the procedure to follow in order to add a new C file to the Slurm
code base. We recommend using a git branch for this purpose.

1. Add your new file to the git repository.
2. Modify the "Makefile.am" file in the file's parent directory.
3. Execute "autoreconf" in Slurm's top level directory.
   If you have older versions of the autoconf, automake, libtool or aclocal then
   you may need to manually modify the Makefile.in file in the file's parent
   directory. If you have different versions of the files than were originally
   used by the Slurm team, this may rebuild all of the Makefile.in files in Slurm.

## Adding a Plugin to Slurm

This is the procedure to follow in order to add a new plugin to the Slurm
code base. We recommend using a git branch for this purpose. In this example,
we show which files would need to be modified in order to add a plugin named
"topology/4d\_torus".

1. Create a new directory for this plugin
   (e.g. "src/plugins/topology/4d\_torus").
2. Add this new directory to its parent directory's "Makefile.am" file
   (e.g. "src/plugins/topology/Makefile.am").
3. Put your new file(s) in the appropriate directory
   (e.g. "src/plugins/topology/4d\_torus/topology\_4d\_torus.c").
4. Create a "Makefile.am" file in the new directory identifying the new file(s)
   (e.g. "src/plugins/topology/4d\_torus/Makefile.am"). Use an existing "Makefile.am"
   file as a model.
5. Identify the new Makefile to be built at Slurm configure time in the file
   "configure.ac". Please maintain the alphabetic ordering of entries.
6. Execute "autoreconf" in Slurm's top level directory.
   If you have older versions of the autoconf, automake, libtool or aclocal then
   you may need to manually create or modify the Makefile.in files.
   If you have different versions of the files than were originally used by the
   Slurm team, this may rebuild all of the Makefile.in files in Slurm.
7. Modify the "slurm.spec" file to include the new plugin file in an
   appropriate RPM.
8. Add the new files, including "Makefile.am" and "Makefile.in", to the git
   repository.