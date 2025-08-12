---
layout: publication
title: Fully And Weakly Supervised Referring Expression Segmentation With End-to-end
  Learning
authors: Hui Li, Mingjie Sun, Jimin Xiao, Eng Gee Lim, Yao Zhao
conference: IEEE Transactions on Circuits and Systems for Video Technology
year: 2023
bibkey: li2022fully
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2212.10278'}]
tags: ["Supervised"]
short_authors: Li et al.
---
Referring Expression Segmentation (RES), which is aimed at localizing and
segmenting the target according to the given language expression, has drawn
increasing attention. Existing methods jointly consider the localization and
segmentation steps, which rely on the fused visual and linguistic features for
both steps. We argue that the conflict between the purpose of identifying an
object and generating a mask limits the RES performance. To solve this problem,
we propose a parallel position-kernel-segmentation pipeline to better isolate
and then interact the localization and segmentation steps. In our pipeline,
linguistic information will not directly contaminate the visual feature for
segmentation. Specifically, the localization step localizes the target object
in the image based on the referring expression, and then the visual kernel
obtained from the localization step guides the segmentation step. This pipeline
also enables us to train RES in a weakly-supervised way, where the pixel-level
segmentation labels are replaced by click annotations on center and corner
points. The position head is fully-supervised and trained with the click
annotations as supervision, and the segmentation head is trained with
weakly-supervised segmentation losses. To validate our framework on a
weakly-supervised setting, we annotated three RES benchmark datasets (RefCOCO,
RefCOCO+ and RefCOCOg) with click annotations.Our method is simple but
surprisingly effective, outperforming all previous state-of-the-art RES methods
on fully- and weakly-supervised settings by a large margin. The benchmark code
and datasets will be released.