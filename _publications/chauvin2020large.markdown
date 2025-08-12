---
layout: publication
title: Large Scale Indexing Of Generic Medical Image Data Using Unbiased Shallow Keypoints
  And Deep CNN Features
authors: L. Chauvin, M. Ben Lazreg, J. B. Carluer, W. Wells, M. Toews
conference: Arxiv
year: 2020
bibkey: chauvin2020large
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2010.04283'}]
tags: ["Scalability", "Tools & Libraries"]
short_authors: Chauvin et al.
---
We propose a unified appearance model accounting for traditional shallow
(i.e. 3D SIFT keypoints) and deep (i.e. CNN output layers) image feature
representations, encoding respectively specific, localized neuroanatomical
patterns and rich global information into a single indexing and classification
framework. A novel Bayesian model combines shallow and deep features based on
an assumption of conditional independence and validated by experiments indexing
specific family members and general group categories in 3D MRI neuroimage data
of 1010 subjects from the Human Connectome Project, including twins and
non-twin siblings. A novel domain adaptation strategy is presented,
transforming deep CNN vectors elements into binary class-informative
descriptors. A GPU-based implementation of all processing is provided.
State-of-the-art performance is achieved in large-scale neuroimage indexing,
both in terms of computational complexity, accuracy in identifying family
members and sex classification.