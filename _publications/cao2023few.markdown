---
layout: publication
title: Few-shot Rotation-invariant Aerial Image Semantic Segmentation
authors: Qinglong Cao, Yuntian Chen, Chao Ma, Xiaokang Yang
conference: IEEE Transactions on Geoscience and Remote Sensing
year: 2023
bibkey: cao2023few
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2306.11734'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Cao et al.
---
Few-shot aerial image segmentation is a challenging task that involves
precisely parsing objects in query aerial images with limited annotated
support. Conventional matching methods without consideration of varying object
orientations can fail to activate same-category objects with different
orientations. Moreover, conventional algorithms can lead to false recognition
of lower-scored rotated semantic objects. In response to these challenges, the
authors propose a novel few-shot rotation-invariant aerial semantic
segmentation network (FRINet). FRINet matches each query feature
rotation-adaptively with orientation-varying yet category-consistent support
information. The segmentation predictions from different orientations are
supervised by the same label, and the backbones are pre-trained in the base
category to boost segmentation performance. Experimental results demonstrate
that FRINet achieves state-of-the-art performance in few-shot aerial semantic
segmentation benchmark.