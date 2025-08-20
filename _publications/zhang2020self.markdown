---
layout: publication
title: Self-supervised Visual Representation Learning From Hierarchical Grouping
authors: Xiao Zhang, Michael Maire
conference: Arxiv
year: 2020
bibkey: zhang2020self
citations: 31
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2012.03044'}]
tags: [Tools & Libraries, Datasets, Supervised, Self-Supervised]
short_authors: Xiao Zhang, Michael Maire
---
We create a framework for bootstrapping visual representation learning from a
primitive visual grouping capability. We operationalize grouping via a contour
detector that partitions an image into regions, followed by merging of those
regions into a tree hierarchy. A small supervised dataset suffices for training
this grouping primitive. Across a large unlabeled dataset, we apply this
learned primitive to automatically predict hierarchical region structure. These
predictions serve as guidance for self-supervised contrastive feature learning:
we task a deep network with producing per-pixel embeddings whose pairwise
distances respect the region hierarchy. Experiments demonstrate that our
approach can serve as state-of-the-art generic pre-training, benefiting
downstream tasks. We additionally explore applications to semantic region
search and video-based object instance tracking.