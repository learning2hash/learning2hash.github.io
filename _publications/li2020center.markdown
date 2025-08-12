---
layout: publication
title: Center-wise Local Image Mixture For Contrastive Representation Learning
authors: Hao Li, Xiaopeng Zhang, Hongkai Xiong
conference: Arxiv
year: 2020
bibkey: li2020center
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2011.02697'}]
tags: ["Self-Supervised"]
short_authors: Hao Li, Xiaopeng Zhang, Hongkai Xiong
---
Contrastive learning based on instance discrimination trains model to
discriminate different transformations of the anchor sample from other samples,
which does not consider the semantic similarity among samples. This paper
proposes a new kind of contrastive learning method, named CLIM, which uses
positives from other samples in the dataset. This is achieved by searching
local similar samples of the anchor, and selecting samples that are closer to
the corresponding cluster center, which we denote as center-wise local image
selection. The selected samples are instantiated via an data mixture strategy,
which performs as a smoothing regularization. As a result, CLIM encourages both
local similarity and global aggregation in a robust way, which we find is
beneficial for feature representation. Besides, we introduce
*multi-resolution* augmentation, which enables the representation to be
scale invariant. We reach 75.5% top-1 accuracy with linear evaluation over
ResNet-50, and 59.3% top-1 accuracy when fine-tuned with only 1% labels.