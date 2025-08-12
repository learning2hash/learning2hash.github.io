---
layout: publication
title: Hierarchical Attention Network For Few-shot Object Detection Via Meta-contrastive
  Learning
authors: Dongwoo Park, Jong-Min Lee
conference: Arxiv
year: 2022
bibkey: park2022hierarchical
citations: 7
additional_links: [{name: Code, url: 'https://github.com/infinity7428/hANMCL'}, {
    name: Paper, url: 'https://arxiv.org/abs/2208.07039'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Dongwoo Park, Jong-Min Lee
---
Few-shot object detection (FSOD) aims to classify and detect few images of
novel categories. Existing meta-learning methods insufficiently exploit
features between support and query images owing to structural limitations. We
propose a hierarchical attention network with sequentially large receptive
fields to fully exploit the query and support images. In addition,
meta-learning does not distinguish the categories well because it determines
whether the support and query images match. In other words, metric-based
learning for classification is ineffective because it does not work directly.
Thus, we propose a contrastive learning method called meta-contrastive
learning, which directly helps achieve the purpose of the meta-learning
strategy. Finally, we establish a new state-of-the-art network, by realizing
significant margins. Our method brings 2.3, 1.0, 1.3, 3.4 and 2.4% AP
improvements for 1-30 shots object detection on COCO dataset. Our code is
available at: https://github.com/infinity7428/hANMCL