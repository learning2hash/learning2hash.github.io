---
layout: publication
title: 'GIFT: Learning Transformation-invariant Dense Visual Descriptors Via Group
  Cnns'
authors: Yuan Liu, Zehong Shen, Zhixuan Lin, Sida Peng, Hujun Bao, Xiaowei Zhou
conference: Arxiv
year: 2019
bibkey: liu2019gift
citations: 47
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1911.05932'}]
tags: []
short_authors: Liu et al.
---
Finding local correspondences between images with different viewpoints
requires local descriptors that are robust against geometric transformations.
An approach for transformation invariance is to integrate out the
transformations by pooling the features extracted from transformed versions of
an image. However, the feature pooling may sacrifice the distinctiveness of the
resulting descriptors. In this paper, we introduce a novel visual descriptor
named Group Invariant Feature Transform (GIFT), which is both discriminative
and robust to geometric transformations. The key idea is that the features
extracted from the transformed versions of an image can be viewed as a function
defined on the group of the transformations. Instead of feature pooling, we use
group convolutions to exploit underlying structures of the extracted features
on the group, resulting in descriptors that are both discriminative and
provably invariant to the group of transformations. Extensive experiments show
that GIFT outperforms state-of-the-art methods on several benchmark datasets
and practically improves the performance of relative pose estimation.