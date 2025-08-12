---
layout: publication
title: Deep Multi-spectral Registration Using Invariant Descriptor Learning
authors: Nati Ofir, Shai Silberstein, Hila Levi, Dani Rozenbaum, Yosi Keller, Sharon
  Duvdevani Bar
conference: 2018 25th IEEE International Conference on Image Processing (ICIP)
year: 2018
bibkey: ofir2018deep
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1801.05171'}]
tags: ["Image Retrieval"]
short_authors: Ofir et al.
---
In this paper, we introduce a novel deep-learning method to align
cross-spectral images. Our approach relies on a learned descriptor which is
invariant to different spectra. Multi-modal images of the same scene capture
different signals and therefore their registration is challenging and it is not
solved by classic approaches. To that end, we developed a feature-based
approach that solves the visible (VIS) to Near-Infra-Red (NIR) registration
problem. Our algorithm detects corners by Harris and matches them by a
patch-metric learned on top of CIFAR-10 network descriptor. As our experiments
demonstrate we achieve a high-quality alignment of cross-spectral images with a
sub-pixel accuracy. Comparing to other existing methods, our approach is more
accurate in the task of VIS to NIR registration.