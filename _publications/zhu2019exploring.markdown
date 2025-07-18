---
layout: publication
title: 'Exploring Auxiliary Context: Discrete Semantic Transfer Hashing For Scalable
  Image Retrieval'
authors: Zhu et al.
conference: IEEE Transactions on Neural Networks and Learning Systems
year: 2019
bibkey: zhu2019exploring
citations: 154
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1904.11207'}]
tags: [Image Retrieval, DATASETS, Hashing Methods, Efficiency And Optimization, Tools
    & Libraries, Evaluation]
---
Unsupervised hashing can desirably support scalable content-based image
retrieval (SCBIR) for its appealing advantages of semantic label independence,
memory and search efficiency. However, the learned hash codes are embedded with
limited discriminative semantics due to the intrinsic limitation of image
representation. To address the problem, in this paper, we propose a novel
hashing approach, dubbed as *Discrete Semantic Transfer Hashing* (DSTH).
The key idea is to *directly* augment the semantics of discrete image hash
codes by exploring auxiliary contextual modalities. To this end, a unified
hashing framework is formulated to simultaneously preserve visual similarities
of images and perform semantic transfer from contextual modalities. Further, to
guarantee direct semantic transfer and avoid information loss, we explicitly
impose the discrete constraint, bit--uncorrelation constraint and bit-balance
constraint on hash codes. A novel and effective discrete optimization method
based on augmented Lagrangian multiplier is developed to iteratively solve the
optimization problem. The whole learning process has linear computation
complexity and desirable scalability. Experiments on three benchmark datasets
demonstrate the superiority of DSTH compared with several state-of-the-art
approaches.