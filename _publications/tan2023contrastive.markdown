---
layout: publication
title: Contrastive Learning Is Spectral Clustering On Similarity Graph
authors: Zhiquan Tan, Yifan Zhang, Jingqin Yang, Yang Yuan
conference: Arxiv
year: 2023
bibkey: tan2023contrastive
citations: 1
additional_links: [{name: Code, url: 'https://github.com/yifanzhang-pro/Kernel-InfoNCE'},
  {name: Paper, url: 'https://arxiv.org/abs/2303.15103'}]
tags: ["Self-Supervised"]
short_authors: Tan et al.
---
Contrastive learning is a powerful self-supervised learning method, but we
have a limited theoretical understanding of how it works and why it works. In
this paper, we prove that contrastive learning with the standard InfoNCE loss
is equivalent to spectral clustering on the similarity graph. Using this
equivalence as the building block, we extend our analysis to the CLIP model and
rigorously characterize how similar multi-modal objects are embedded together.
Motivated by our theoretical insights, we introduce the Kernel-InfoNCE loss,
incorporating mixtures of kernel functions that outperform the standard
Gaussian kernel on several vision datasets. The code is available at
https://github.com/yifanzhang-pro/Kernel-InfoNCE.