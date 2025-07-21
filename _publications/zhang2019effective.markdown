---
layout: publication
title: Effective Image Retrieval via Multilinear Multi-index Fusion
authors: Zhang et al.
conference: IEEE Transactions on Multimedia
year: 2019
bibkey: zhang2019effective
citations: 24
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1709.09304'}]
tags: ["Vector Indexing", "Image Retrieval"]
---
Multi-index fusion has demonstrated impressive performances in retrieval task
by integrating different visual representations in a unified framework.
However, previous works mainly consider propagating similarities via neighbor
structure, ignoring the high order information among different visual
representations. In this paper, we propose a new multi-index fusion scheme for
image retrieval. By formulating this procedure as a multilinear based
optimization problem, the complementary information hidden in different indexes
can be explored more thoroughly. Specially, we first build our multiple indexes
from various visual representations. Then a so-called index-specific functional
matrix, which aims to propagate similarities, is introduced for updating the
original index. The functional matrices are then optimized in a unified tensor
space to achieve a refinement, such that the relevant images can be pushed more
closer. The optimization problem can be efficiently solved by the augmented
Lagrangian method with theoretical convergence guarantee. Unlike the
traditional multi-index fusion scheme, our approach embeds the multi-index
subspace structure into the new indexes with sparse constraint, thus it has
little additional memory consumption in online query stage. Experimental
evaluation on three benchmark datasets reveals that the proposed approach
achieves the state-of-the-art performance, i.e., N-score 3.94 on UKBench, mAP
94.1% on Holiday and 62.39% on Market-1501.