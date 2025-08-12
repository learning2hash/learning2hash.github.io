---
layout: publication
title: Spectral Descriptors For Deformable Shapes
authors: Alexander M. Bronstein
conference: Arxiv
year: 2011
bibkey: bronstein2011spectral
citations: 20
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1110.5015'}]
tags: []
short_authors: Alexander M. Bronstein
---
Informative and discriminative feature descriptors play a fundamental role in
deformable shape analysis. For example, they have been successfully employed in
correspondence, registration, and retrieval tasks. In the recent years,
significant attention has been devoted to descriptors obtained from the
spectral decomposition of the Laplace-Beltrami operator associated with the
shape. Notable examples in this family are the heat kernel signature (HKS) and
the wave kernel signature (WKS). Laplacian-based descriptors achieve
state-of-the-art performance in numerous shape analysis tasks; they are
computationally efficient, isometry-invariant by construction, and can
gracefully cope with a variety of transformations. In this paper, we formulate
a generic family of parametric spectral descriptors. We argue that in order to
be optimal for a specific task, the descriptor should take into account the
statistics of the corpus of shapes to which it is applied (the "signal") and
those of the class of transformations to which it is made insensitive (the
"noise"). While such statistics are hard to model axiomatically, they can be
learned from examples. Following the spirit of the Wiener filter in signal
processing, we show a learning scheme for the construction of optimal spectral
descriptors and relate it to Mahalanobis metric learning. The superiority of
the proposed approach is demonstrated on the SHREC'10 benchmark.