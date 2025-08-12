---
layout: publication
title: 'Openvis: Open-vocabulary Video Instance Segmentation'
authors: Pinxue Guo, Tony Huang, Peiyang He, Xuefeng Liu, Tianjun Xiao, Zhaoyu Chen,
  Wenqiang Zhang
conference: Arxiv
year: 2023
bibkey: guo2023openvis
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2305.16835'}]
tags: ["Tools & Libraries"]
short_authors: Guo et al.
---
Open-vocabulary Video Instance Segmentation (OpenVIS) can simultaneously
detect, segment, and track arbitrary object categories in a video, without
being constrained to categories seen during training. In this work, we propose
InstFormer, a carefully designed framework for the OpenVIS task that achieves
powerful open-vocabulary capabilities through lightweight fine-tuning with
limited-category data. InstFormer begins with the open-world mask proposal
network, encouraged to propose all potential instance class-agnostic masks by
the contrastive instance margin loss. Next, we introduce InstCLIP, adapted from
pre-trained CLIP with Instance Guidance Attention, which encodes
open-vocabulary instance tokens efficiently. These instance tokens not only
enable open-vocabulary classification but also offer strong universal tracking
capabilities. Furthermore, to prevent the tracking module from being
constrained by the training data with limited categories, we propose the
universal rollout association, which transforms the tracking problem into
predicting the next frame's instance tracking token. The experimental results
demonstrate the proposed InstFormer achieve state-of-the-art capabilities on a
comprehensive OpenVIS evaluation benchmark, while also achieves competitive
performance in fully supervised VIS task.