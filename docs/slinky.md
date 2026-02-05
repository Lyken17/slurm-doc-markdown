# Slurm Workload Manager - Slinky 

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

# Slinky — Slurm and Kubernetes

## Contents

* [Overview](#overview)
* [Links](#links)
* [Presentations](#presentations)

## Overview

[Slinky™](https://www.schedmd.com/slinky/why-slinky/) is
SchedMD's set of projects to enable interoperability between Slurm and [Kubernetes](https://kubernetes.io/).

## Links

Slinky documentation can be found [here](https://slinky.schedmd.com/).

Slinky repositories are publicly available on
[GitHub](https://github.com/SlinkyProject) and
[GitLab](https://gitlab.com/SchedMD/slinky):

* [slurm-operator](https://github.com/SlinkyProject/slurm-operator):
  Run Slurm on Kubernetes. Manage and scale Slurm clusters on Kubernetes as
  pods.
* [slurm-bridge](https://github.com/SlinkyProject/slurm-bridge):
  Run Slurm as a Kubernetes scheduler. Schedule both Slurm and Kubernetes
  workloads with Slurm.
* [slurm-client](https://github.com/SlinkyProject/slurm-client):
  Golang library for Slurm REST communication. Shared by Slinky repositories.
* [containers](https://github.com/SlinkyProject/containers):
  Dockerfiles for building Slurm container images.

Public container images and helm chart artifacts can be found
[here](https://github.com/orgs/SlinkyProject/packages).

## Presentations

Note that older presentations may contain outdated information.

### Presentations from 2025

* [Slurm Bridge: Slurm Scheduling Superpowers in Kubernetes](https://slurm.schedmd.com/MISC25/Slurm_Bridge_KubeCon_25.pdf),
  Alan Mutschelknaus and Tim Wickberg, SchedMD (KubeCon NA, November 2025)
* [Slurm Bridge](https://slurm.schedmd.com/MISC25/Slurm_Bridge_CNCF-Batch-20250729.pdf), Alan Mutschelknaus, Skyler Malinowski, and Marlow Warnicke,
  SchedMD (CNCF Batch Working Group, July 2025)
* [Slinky: The
  Missing Link Between Slurm and Kubernetes](https://slurm.schedmd.com/MISC25/Slinky-CUG2025.pdf), Skyler Malinowski, Alan
  Mutschelknaus, Marlow Warnicke, and Tim Wickberg, SchedMD (CUG25, May 2025)
* [Slinky: Slurm in Kubernetes, Performant AI and HPC Workload Management](https://slurm.schedmd.com/MISC25/Slinky-KubeConEurope2025.pdf),
  Tim Wickberg, SchedMD (KubeCon Europe, April 2025)

### Presentations from 2024

* [Slinky: The
  Missing Link Between Slurm and Kubernetes](https://slurm.schedmd.com/SC24/Slinky-CANOPIE.pdf), Skyler Malinowski and
  Tim Wickberg, SchedMD (SC24, November 2024)
* [Slinky
  — Slurm Operator](https://slurm.schedmd.com/SLUG24/Slinky-Slurm-Operator.pdf), Skyler Malinowski, Alan Mutschelknaus, and
  Marlow Warnicke, SchedMD (SLUG24, September 2024)
* [Slinky
  — Slurm Bridge](https://slurm.schedmd.com/SLUG24/Slinky-Slurm-Bridge.pdf), Skyler Malinowski, Alan Mutschelknaus, and
  Marlow Warnicke, SchedMD (SLUG24, September 2024)