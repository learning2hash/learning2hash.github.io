---
layout: publication
title: 'Angle Tree: Nearest Neighbor Search In High Dimensions With Low Intrinsic
  Dimensionality'
authors: Ilia Zvedeniouk, Sanjay Chawla
conference: Arxiv
year: 2010
bibkey: zvedeniouk2010angle
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1003.5474'}]
tags: [Tree-based ANN]
short_authors: Ilia Zvedeniouk, Sanjay Chawla
---
We propose an extension of tree-based space-partitioning indexing structures
for data with low intrinsic dimensionality embedded in a high dimensional
space. We call this extension an Angle Tree. Our extension can be applied to
both classical kd-trees as well as the more recent rp-trees. The key idea of
our approach is to store the angle (the "dihedral angle") between the data
region (which is a low dimensional manifold) and the random hyperplane that
splits the region (the "splitter"). We show that the dihedral angle can be used
to obtain a tight lower bound on the distance between the query point and any
point on the opposite side of the splitter. This in turn can be used to
efficiently prune the search space. We introduce a novel randomized strategy to
efficiently calculate the dihedral angle with a high degree of accuracy.
Experiments and analysis on real and synthetic data sets shows that the Angle
Tree is the most efficient known indexing structure for nearest neighbor
queries in terms of preprocessing and space usage while achieving high accuracy
and fast search time.