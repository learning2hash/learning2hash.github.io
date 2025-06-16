---
layout: publication
title: Cascading Hierarchical Networks With Multi-task Balanced Loss For Fine-grained
  Hashing
authors: Xianxian Zeng, Yanjun Zheng
conference: Arxiv
year: 2023
citations: 2
bibkey: zeng2023cascading
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2303.11274'}, {name: Code,
    url: 'https://github.com/kaiba007/FG-CNET'}]
tags: [Hashing Methods, Deep Hashing, Evaluation Metrics]
---
With the explosive growth in the number of fine-grained images in the
Internet era, it has become a challenging problem to perform fast and efficient
retrieval from large-scale fine-grained images. Among the many retrieval
methods, hashing methods are widely used due to their high efficiency and small
storage space occupation. Fine-grained hashing is more challenging than
traditional hashing problems due to the difficulties such as low inter-class
variances and high intra-class variances caused by the characteristics of
fine-grained images. To improve the retrieval accuracy of fine-grained hashing,
we propose a cascaded network to learn compact and highly semantic hash codes,
and introduce an attention-guided data augmentation method. We refer to this
network as a cascaded hierarchical data augmentation network. We also propose a
novel approach to coordinately balance the loss of multi-task learning. We do
extensive experiments on some common fine-grained visual classification
datasets. The experimental results demonstrate that our proposed method
outperforms several state-of-art hashing methods and can effectively improve
the accuracy of fine-grained retrieval. The source code is publicly available:
https://github.com/kaiba007/FG-CNET.