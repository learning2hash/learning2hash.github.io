---
layout: publication
title: Purely Geometric Scene Association And Retrieval - A Case For Macro Scale 3D
  Geometry
authors: Rahul Sawhney, Fuxin Li, Henrik I. Christensen, Charles L. Isbell
conference: Arxiv
year: 2018
bibkey: sawhney2018purely
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1808.01343'}]
tags: []
short_authors: Sawhney et al.
---
We address the problems of measuring geometric similarity between 3D scenes,
represented through point clouds or range data frames, and associating them.
Our approach leverages macro-scale 3D structural geometry - the relative
configuration of arbitrary surfaces and relationships among structures that are
potentially far apart. We express such discriminative information in a
viewpoint-invariant feature space. These are subsequently encoded in a
frame-level signature that can be utilized to measure geometric similarity.
Such a characterization is robust to noise, incomplete and partially
overlapping data besides viewpoint changes. We show how it can be employed to
select a diverse set of data frames which have structurally similar content,
and how to validate whether views with similar geometric content are from the
same scene. The problem is formulated as one of general purpose retrieval from
an unannotated, spatio-temporally unordered database. Empirical analysis
indicates that the presented approach thoroughly outperforms baselines on depth
/ range data. Its depth-only performance is competitive with state-of-the-art
approaches with RGB or RGB-D inputs, including ones based on deep learning.
Experiments show retrieval performance to hold up well with much sparser
databases, which is indicative of the approach's robustness. The approach
generalized well - it did not require dataset specific training, and scaled up
in our experiments. Finally, we also demonstrate how geometrically diverse
selection of views can result in richer 3D reconstructions.