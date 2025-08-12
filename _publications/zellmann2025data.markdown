---
layout: publication
title: Data Parallel Visualization And Rendering On The RAMSES Supercomputer With
  ANARI
authors: Stefan Zellmann
conference: Problems of Modeling and Design Automatization
year: 2025
bibkey: zellmann2025data
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2501.01628'}]
tags: []
short_authors: Stefan Zellmann
---
3D visualization and rendering in HPC are very heterogenous applications,
though fundamentally the tasks involved are well-defined and do not differ much
from application to application. The Khronos Group's ANARI standard seeks to
consolidate 3D rendering across sci-vis applications. This paper makes an
effort to convey challenges of 3D rendering and visualization with ANARI in the
context of HPC, where the data does not fit within a single node or GPU but
must be distributed. It also provides a gentle introduction to parallel
rendering concepts and challenges to practitioners from the field of HPC in
general. Finally, we present a case study showcasing data parallel rendering on
the new supercomputer RAMSES at the University of Cologne.