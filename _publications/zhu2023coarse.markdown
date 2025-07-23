---
layout: publication
title: 'Coarse-to-fine: Learning Compact Discriminative Representation For Single-stage
  Image Retrieval'
authors: Zhu Yunquan, Gao Xinkai, Ke Bo, Qiao Ruizhi, Sun Xing
conference: 2023 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2023
bibkey: zhu2023coarse
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2308.04008'}]
tags: ["Compact Codes", "Distance Metric Learning", "Efficiency", "ICCV", "Image Retrieval", "Re-Ranking"]
short_authors: Zhu et al.
---
Image retrieval targets to find images from a database that are visually
similar to the query image. Two-stage methods following retrieve-and-rerank
paradigm have achieved excellent performance, but their separate local and
global modules are inefficient to real-world applications. To better trade-off
retrieval efficiency and accuracy, some approaches fuse global and local
feature into a joint representation to perform single-stage image retrieval.
However, they are still challenging due to various situations to tackle,
\\(e.g.\\), background, occlusion and viewpoint. In this work, we design a
Coarse-to-Fine framework to learn Compact Discriminative representation (CFCD)
for end-to-end single-stage image retrieval-requiring only image-level labels.
Specifically, we first design a novel adaptive softmax-based loss which
dynamically tunes its scale and margin within each mini-batch and increases
them progressively to strengthen supervision during training and intra-class
compactness. Furthermore, we propose a mechanism which attentively selects
prominent local descriptors and infuse fine-grained semantic relations into the
global representation by a hard negative sampling strategy to optimize
inter-class distinctiveness at a global scale. Extensive experimental results
have demonstrated the effectiveness of our method, which achieves
state-of-the-art single-stage image retrieval performance on benchmarks such as
Revisited Oxford and Revisited Paris. Code is available at
https://github.com/bassyess/CFCD.