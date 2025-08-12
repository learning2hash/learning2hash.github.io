---
layout: publication
title: 'Looking For The Devil In The Details: Learning Trilinear Attention Sampling
  Network For Fine-grained Image Recognition'
authors: Heliang Zheng, Jianlong Fu, Zheng-Jun Zha, Jiebo Luo
conference: 2019 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2019
bibkey: zheng2019looking
citations: 436
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1903.06150'}]
tags: ["CVPR"]
short_authors: Zheng et al.
---
Learning subtle yet discriminative features (e.g., beak and eyes for a bird)
plays a significant role in fine-grained image recognition. Existing
attention-based approaches localize and amplify significant parts to learn
fine-grained details, which often suffer from a limited number of parts and
heavy computational cost. In this paper, we propose to learn such fine-grained
features from hundreds of part proposals by Trilinear Attention Sampling
Network (TASN) in an efficient teacher-student manner. Specifically, TASN
consists of 1) a trilinear attention module, which generates attention maps by
modeling the inter-channel relationships, 2) an attention-based sampler which
highlights attended parts with high resolution, and 3) a feature distiller,
which distills part features into a global one by weight sharing and feature
preserving strategies. Extensive experiments verify that TASN yields the best
performance under the same settings with the most competitive approaches, in
iNaturalist-2017, CUB-Bird, and Stanford-Cars datasets.