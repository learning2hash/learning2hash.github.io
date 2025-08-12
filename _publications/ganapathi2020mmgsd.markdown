---
layout: publication
title: 'MMGSD: Multi-modal Gaussian Shape Descriptors For Correspondence Matching
  In 1D And 2D Deformable Objects'
authors: Aditya Ganapathi, Priya Sundaresan, Brijen Thananjeyan, Ashwin Balakrishna,
  Daniel Seita, Ryan Hoque, Joseph E. Gonzalez, Ken Goldberg
conference: Arxiv
year: 2020
bibkey: ganapathi2020mmgsd
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2010.04339'}]
tags: ["Distance Metric Learning"]
short_authors: Ganapathi et al.
---
We explore learning pixelwise correspondences between images of deformable
objects in different configurations. Traditional correspondence matching
approaches such as SIFT, SURF, and ORB can fail to provide sufficient
contextual information for fine-grained manipulation. We propose Multi-Modal
Gaussian Shape Descriptor (MMGSD), a new visual representation of deformable
objects which extends ideas from dense object descriptors to predict all
symmetric correspondences between different object configurations. MMGSD is
learned in a self-supervised manner from synthetic data and produces
correspondence heatmaps with measurable uncertainty. In simulation, experiments
suggest that MMGSD can achieve an RMSE of 32.4 and 31.3 for square cloth and
braided synthetic nylon rope respectively. The results demonstrate an average
of 47.7% improvement over a provided baseline based on contrastive learning,
symmetric pixel-wise contrastive loss (SPCL), as opposed to MMGSD which
enforces distributional continuity.