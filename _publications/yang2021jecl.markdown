---
layout: publication
title: 'JECL: Joint Embedding And Cluster Learning For Image-text Pairs'
authors: Sean T. Yang, Kuan-hao Huang, Bill Howe
conference: 2020 25th International Conference on Pattern Recognition (ICPR)
year: 2021
bibkey: yang2021jecl
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1901.01860'}]
tags: []
short_authors: Sean T. Yang, Kuan-hao Huang, Bill Howe
---
We propose JECL, a method for clustering image-caption pairs by training
parallel encoders with regularized clustering and alignment objectives,
simultaneously learning both representations and cluster assignments. These
image-caption pairs arise frequently in high-value applications where
structured training data is expensive to produce, but free-text descriptions
are common. JECL trains by minimizing the Kullback-Leibler divergence between
the distribution of the images and text to that of a combined joint target
distribution and optimizing the Jensen-Shannon divergence between the soft
cluster assignments of the images and text. Regularizers are also applied to
JECL to prevent trivial solutions. Experiments show that JECL outperforms both
single-view and multi-view methods on large benchmark image-caption datasets,
and is remarkably robust to missing captions and varying data sizes.