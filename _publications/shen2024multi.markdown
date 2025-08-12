---
layout: publication
title: Multi-grained Contrast For Data-efficient Unsupervised Representation Learning
authors: Chengchao Shen, Jianzhong Chen, Jianxin Wang
conference: Arxiv
year: 2024
bibkey: shen2024multi
citations: 1
additional_links: [{name: Code, url: 'https://github.com/visresearch/mgc'}, {name: Paper,
    url: 'https://arxiv.org/abs/2407.02014'}]
tags: ["Unsupervised"]
short_authors: Chengchao Shen, Jianzhong Chen, Jianxin Wang
---
The existing contrastive learning methods mainly focus on single-grained
representation learning, e.g., part-level, object-level or scene-level ones,
thus inevitably neglecting the transferability of representations on other
granularity levels. In this paper, we aim to learn multi-grained
representations, which can effectively describe the image on various
granularity levels, thus improving generalization on extensive downstream
tasks. To this end, we propose a novel Multi-Grained Contrast method (MGC) for
unsupervised representation learning. Specifically, we construct delicate
multi-grained correspondences between positive views and then conduct
multi-grained contrast by the correspondences to learn more general
unsupervised representations.
  Without pretrained on large-scale dataset, our method significantly
outperforms the existing state-of-the-art methods on extensive downstream
tasks, including object detection, instance segmentation, scene parsing,
semantic segmentation and keypoint detection. Moreover, experimental results
support the data-efficient property and excellent representation
transferability of our method. The source code and trained weights are
available at https://github.com/visresearch/mgc.