---
layout: publication
title: Parallelizing Spectral Algorithms For Kernel Learning
authors: "Gilles Blanchard, Nicole M\xFCcke"
conference: Arxiv
year: 2016
bibkey: blanchard2016parallelizing
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1610.07487'}]
tags: []
short_authors: "Gilles Blanchard, Nicole M\xFCcke"
---
We consider a distributed learning approach in supervised learning for a
large class of spectral regularization methods in an RKHS framework. The data
set of size n is partitioned into \(m=O(n^\alpha)\) disjoint subsets. On each
subset, some spectral regularization method (belonging to a large class,
including in particular Kernel Ridge Regression, \(L^2\)-boosting and spectral
cut-off) is applied. The regression function \(f\) is then estimated via simple
averaging, leading to a substantial reduction in computation time. We show that
minimax optimal rates of convergence are preserved if m grows sufficiently
slowly (corresponding to an upper bound for \(\alpha\)) as \(n \to \infty\),
depending on the smoothness assumptions on \(f\) and the intrinsic
dimensionality. In spirit, our approach is classical.