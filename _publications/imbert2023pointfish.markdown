---
layout: publication
title: Pointfish -- Learning Point Cloud Representations For RNA Localization Patterns
authors: Arthur Imbert, Florian Mueller, Thomas Walter
conference: Lecture Notes in Computer Science
year: 2023
bibkey: imbert2023pointfish
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2302.10923'}]
tags: []
short_authors: Arthur Imbert, Florian Mueller, Thomas Walter
---
Subcellular RNA localization is a critical mechanism for the spatial control
of gene expression. Its mechanism and precise functional role is not yet very
well understood. Single Molecule Fluorescence in Situ Hybridization (smFISH)
images allow for the detection of individual RNA molecules with subcellular
accuracy. In return, smFISH requires robust methods to quantify and classify
RNA spatial distribution. Here, we present PointFISH, a novel computational
approach for the recognition of RNA localization patterns. PointFISH is an
attention-based network for computing continuous vector representations of RNA
point clouds. Trained on simulations only, it can directly process extracted
coordinates from experimental smFISH images. The resulting embedding allows
scalable and flexible spatial transcriptomics analysis and matches performance
of hand-crafted pipelines.