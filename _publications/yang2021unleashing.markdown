---
layout: publication
title: Unleashing The Potential Of Unsupervised Pre-training With Intra-identity Regularization
  For Person Re-identification
authors: Zizheng Yang, Xin Jin, Kecheng Zheng, Feng Zhao
conference: Arxiv
year: 2021
bibkey: yang2021unleashing
citations: 3
additional_links: [{name: Code, url: 'https://github.com/Frost-Yang-99/UP-ReID'},
  {name: Paper, url: 'https://arxiv.org/abs/2112.00317'}]
tags: ["Datasets", "Robustness", "Self-Supervised", "Unsupervised"]
short_authors: Yang et al.
---
Existing person re-identification (ReID) methods typically directly load the
pre-trained ImageNet weights for initialization. However, as a fine-grained
classification task, ReID is more challenging and exists a large domain gap
between ImageNet classification. Inspired by the great success of
self-supervised representation learning with contrastive objectives, in this
paper, we design an Unsupervised Pre-training framework for ReID based on the
contrastive learning (CL) pipeline, dubbed UP-ReID. During the pre-training, we
attempt to address two critical issues for learning fine-grained ReID features:
(1) the augmentations in CL pipeline may distort the discriminative clues in
person images. (2) the fine-grained local features of person images are not
fully-explored. Therefore, we introduce an intra-identity
(I\(^2\)-)regularization in the UP-ReID, which is instantiated as two constraints
coming from global image aspect and local patch aspect: a global consistency is
enforced between augmented and original person images to increase robustness to
augmentation, while an intrinsic contrastive constraint among local patches of
each image is employed to fully explore the local discriminative clues.
Extensive experiments on multiple popular Re-ID datasets, including PersonX,
Market1501, CUHK03, and MSMT17, demonstrate that our UP-ReID pre-trained model
can significantly benefit the downstream ReID fine-tuning and achieve
state-of-the-art performance. Codes and models will be released to
https://github.com/Frost-Yang-99/UP-ReID.