---
layout: publication
title: Image Co-segmentation Via Multi-scale Local Shape Transfer
authors: Wei Teng, Yu Zhang, Xiaowu Chen, Jia Li, Zhiqiang He
conference: Arxiv
year: 2018
bibkey: teng2018image
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1805.05610'}]
tags: []
short_authors: Teng et al.
---
Image co-segmentation is a challenging task in computer vision that aims to
segment all pixels of the objects from a predefined semantic category. In
real-world cases, however, common foreground objects often vary greatly in
appearance, making their global shapes highly inconsistent across images and
difficult to be segmented. To address this problem, this paper proposes a novel
co-segmentation approach that transfers patch-level local object shapes which
appear more consistent across different images. In our framework, a multi-scale
patch neighbourhood system is first generated using proposal flow on arbitrary
image-pair, which is further refined by Locally Linear Embedding. Based on the
patch relationships, we propose an efficient algorithm to jointly segment the
objects in each image while transferring their local shapes across different
images. Extensive experiments demonstrate that the proposed method can robustly
and effectively segment common objects from an image set. On iCoseg, MSRC and
Coseg-Rep dataset, the proposed approach performs comparable or better than the
state-of-thearts, while on a more challenging benchmark Fashionista dataset,
our method achieves significant improvements.