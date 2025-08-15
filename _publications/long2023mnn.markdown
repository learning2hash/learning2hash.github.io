---
layout: publication
title: 'MNN: Mixed Nearest-neighbors For Self-supervised Learning'
authors: Xianzhong Long, Chen Peng, Yun Li
conference: Pattern Recognition
year: 2024
bibkey: long2023mnn
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2311.00562'}]
tags: ["Datasets", "Efficiency", "Evaluation", "Self-Supervised"]
short_authors: Xianzhong Long, Chen Peng, Yun Li
---
In contrastive self-supervised learning, positive samples are typically drawn
from the same image but in different augmented views, resulting in a relatively
limited source of positive samples. An effective way to alleviate this problem
is to incorporate the relationship between samples, which involves including
the top-K nearest neighbors of positive samples. However, the problem of false
neighbors (i.e., neighbors that do not belong to the same category as the
positive sample) is an objective but often overlooked challenge due to the
query of neighbor samples without supervision information. In this paper, we
present a simple self-supervised learning framework called Mixed
Nearest-Neighbors for Self-Supervised Learning (MNN). MNN optimizes the
influence of neighbor samples on the semantics of positive samples through an
intuitive weighting approach and image mixture operations. The results
demonstrate that MNN exhibits exceptional generalization performance and
training efficiency on four benchmark datasets.