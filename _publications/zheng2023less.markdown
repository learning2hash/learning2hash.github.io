---
layout: publication
title: 'Less Is More: Focus Attention For Efficient DETR'
authors: Dehua Zheng, Wenhui Dong, Hailin Hu, Xinghao Chen, Yunhe Wang
conference: 2023 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2023
bibkey: zheng2023less
citations: 45
additional_links: [{name: Code, url: 'https://github.com/huawei-noah/noah-research/tree/master/Focus-DETR'},
  {name: Code, url: 'https://gitee.com/mindspore/models/tree/master/research/cv/Focus-DETR'},
  {name: Paper, url: 'https://arxiv.org/abs/2307.12612'}]
tags: ["Efficiency", "ICCV"]
short_authors: Zheng et al.
---
DETR-like models have significantly boosted the performance of detectors and
even outperformed classical convolutional models. However, all tokens are
treated equally without discrimination brings a redundant computational burden
in the traditional encoder structure. The recent sparsification strategies
exploit a subset of informative tokens to reduce attention complexity
maintaining performance through the sparse encoder. But these methods tend to
rely on unreliable model statistics. Moreover, simply reducing the token
population hinders the detection performance to a large extent, limiting the
application of these sparse models. We propose Focus-DETR, which focuses
attention on more informative tokens for a better trade-off between computation
efficiency and model accuracy. Specifically, we reconstruct the encoder with
dual attention, which includes a token scoring mechanism that considers both
localization and category semantic information of the objects from multi-scale
feature maps. We efficiently abandon the background queries and enhance the
semantic interaction of the fine-grained object queries based on the scores.
Compared with the state-of-the-art sparse DETR-like detectors under the same
setting, our Focus-DETR gets comparable complexity while achieving 50.4AP
(+2.2) on COCO. The code is available at
https://github.com/huawei-noah/noah-research/tree/master/Focus-DETR and
https://gitee.com/mindspore/models/tree/master/research/cv/Focus-DETR.