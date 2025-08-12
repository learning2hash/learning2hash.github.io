---
layout: publication
title: Visual Attribute Transfer Through Deep Image Analogy
authors: Jing Liao, Yuan Yao, Lu Yuan, Gang Hua, Sing Bing Kang
conference: ACM Transactions on Graphics
year: 2017
bibkey: liao2017visual
citations: 490
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1705.01088'}]
tags: ["CVPR", "Image Retrieval"]
short_authors: Liao et al.
---
We propose a new technique for visual attribute transfer across images that
may have very different appearance but have perceptually similar semantic
structure. By visual attribute transfer, we mean transfer of visual information
(such as color, tone, texture, and style) from one image to another. For
example, one image could be that of a painting or a sketch while the other is a
photo of a real scene, and both depict the same type of scene.
  Our technique finds semantically-meaningful dense correspondences between two
input images. To accomplish this, it adapts the notion of "image analogy" with
features extracted from a Deep Convolutional Neutral Network for matching; we
call our technique Deep Image Analogy. A coarse-to-fine strategy is used to
compute the nearest-neighbor field for generating the results. We validate the
effectiveness of our proposed method in a variety of cases, including
style/texture transfer, color/style swap, sketch/painting to photo, and time
lapse.