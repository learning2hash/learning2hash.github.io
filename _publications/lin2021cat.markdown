---
layout: publication
title: 'CAT: Cross-attention Transformer For One-shot Object Detection'
authors: Weidong Lin, Yuyan Deng, Yang Gao, Ning Wang, Jinghao Zhou, Lingqiao Liu,
  Lei Zhang, Peng Wang
conference: Arxiv
year: 2021
bibkey: lin2021cat
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2104.14984'}]
tags: ["Efficiency"]
short_authors: Lin et al.
---
Given a query patch from a novel class, one-shot object detection aims to
detect all instances of that class in a target image through the semantic
similarity comparison. However, due to the extremely limited guidance in the
novel class as well as the unseen appearance difference between query and
target instances, it is difficult to appropriately exploit their semantic
similarity and generalize well. To mitigate this problem, we present a
universal Cross-Attention Transformer (CAT) module for accurate and efficient
semantic similarity comparison in one-shot object detection. The proposed CAT
utilizes transformer mechanism to comprehensively capture bi-directional
correspondence between any paired pixels from the query and the target image,
which empowers us to sufficiently exploit their semantic characteristics for
accurate similarity comparison. In addition, the proposed CAT enables feature
dimensionality compression for inference speedup without performance loss.
Extensive experiments on COCO, VOC, and FSOD under one-shot settings
demonstrate the effectiveness and efficiency of our method, e.g., it surpasses
CoAE, a major baseline in this task by 1.0% in AP on COCO and runs nearly 2.5
times faster. Code will be available in the future.