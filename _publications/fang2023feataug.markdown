---
layout: publication
title: 'Feataug-detr: Enriching One-to-many Matching For Detrs With Feature Augmentation'
authors: Rongyao Fang, Peng Gao, Aojun Zhou, Yingjie Cai, Si Liu, Jifeng Dai, Hongsheng
  Li
conference: IEEE Transactions on Pattern Analysis and Machine Intelligence
year: 2024
bibkey: fang2023feataug
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2303.01503'}]
tags: []
short_authors: Fang et al.
---
One-to-one matching is a crucial design in DETR-like object detection
frameworks. It enables the DETR to perform end-to-end detection. However, it
also faces challenges of lacking positive sample supervision and slow
convergence speed. Several recent works proposed the one-to-many matching
mechanism to accelerate training and boost detection performance. We revisit
these methods and model them in a unified format of augmenting the object
queries. In this paper, we propose two methods that realize one-to-many
matching from a different perspective of augmenting images or image features.
The first method is One-to-many Matching via Data Augmentation (denoted as
DataAug-DETR). It spatially transforms the images and includes multiple
augmented versions of each image in the same training batch. Such a simple
augmentation strategy already achieves one-to-many matching and surprisingly
improves DETR's performance. The second method is One-to-many matching via
Feature Augmentation (denoted as FeatAug-DETR). Unlike DataAug-DETR, it
augments the image features instead of the original images and includes
multiple augmented features in the same batch to realize one-to-many matching.
FeatAug-DETR significantly accelerates DETR training and boosts detection
performance while keeping the inference speed unchanged. We conduct extensive
experiments to evaluate the effectiveness of the proposed approach on DETR
variants, including DAB-DETR, Deformable-DETR, and H-Deformable-DETR. Without
extra training data, FeatAug-DETR shortens the training convergence periods of
Deformable-DETR to 24 epochs and achieves 58.3 AP on COCO val2017 set with
Swin-L as the backbone.