---
layout: publication
title: Cross-level Multi-instance Distillation For Self-supervised Fine-grained Visual
  Categorization
authors: Qi Bi, Wei Ji, Jingjun Yi, Haolan Zhan, Gui-song Xia
conference: IEEE Transactions on Image Processing
year: 2025
bibkey: bi2024cross
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2401.08860'}]
tags: ["Self-Supervised"]
short_authors: Bi et al.
---
High-quality annotation of fine-grained visual categories demands great expert knowledge, which is taxing and time consuming. Alternatively, learning fine-grained visual representation from enormous unlabeled images (e.g., species, brands) by self-supervised learning becomes a feasible solution. However, recent researches find that existing self-supervised learning methods are less qualified to represent fine-grained categories. The bottleneck lies in that the pre-text representation is built from every patch-wise embedding, while fine-grained categories are only determined by several key patches of an image. In this paper, we propose a Cross-level Multi-instance Distillation (CMD) framework to tackle the challenge. Our key idea is to consider the importance of each image patch in determining the fine-grained pre-text representation by multiple instance learning. To comprehensively learn the relation between informative patches and fine-grained semantics, the multi-instance knowledge distillation is implemented on both the region/image crop pairs from the teacher and student net, and the region-image crops inside the teacher / student net, which we term as intra-level multi-instance distillation and inter-level multi-instance distillation. Extensive experiments on CUB-200-2011, Stanford Cars and FGVC Aircraft show that the proposed method outperforms the contemporary method by upto 10.14% and existing state-of-the-art self-supervised learning approaches by upto 19.78% on both top-1 accuracy and Rank-1 retrieval metric.