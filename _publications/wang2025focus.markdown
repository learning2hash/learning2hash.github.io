---
layout: publication
title: 'Focus On Local: Finding Reliable Discriminative Regions For Visual Place Recognition'
authors: Changwei Wang, Shunpeng Chen, Yukun Song, Rongtao Xu, Zherui Zhang, Jiguang
  Zhang, Haoran Yang, Yu Zhang, Kexue Fu, Shide Du, Zhiwei Xu, Longxiang Gao, Li Guo,
  Shibiao Xu
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2025
bibkey: wang2025focus
citations: 1
additional_links: [{name: Code, url: 'https://github.com/chenshunpeng/FoL'}, {name: Paper,
    url: 'https://arxiv.org/abs/2504.09881'}]
tags: [Evaluation, Supervised, Image Retrieval, Re-ranking, Efficiency, Datasets,
  Hybrid ANN Methods, AAAI]
short_authors: Wang et al.
---
Visual Place Recognition (VPR) is aimed at predicting the location of a query
image by referencing a database of geotagged images. For VPR task, often fewer
discriminative local regions in an image produce important effects while
mundane background regions do not contribute or even cause perceptual aliasing
because of easy overlap. However, existing methods lack precisely modeling and
full exploitation of these discriminative regions. In this paper, we propose
the Focus on Local (FoL) approach to stimulate the performance of image
retrieval and re-ranking in VPR simultaneously by mining and exploiting
reliable discriminative local regions in images and introducing
pseudo-correlation supervision. First, we design two losses,
Extraction-Aggregation Spatial Alignment Loss (SAL) and Foreground-Background
Contrast Enhancement Loss (CEL), to explicitly model reliable discriminative
local regions and use them to guide the generation of global representations
and efficient re-ranking. Second, we introduce a weakly-supervised local
feature training strategy based on pseudo-correspondences obtained from
aggregating global features to alleviate the lack of local correspondences
ground truth for the VPR task. Third, we suggest an efficient re-ranking
pipeline that is efficiently and precisely based on discriminative region
guidance. Finally, experimental results show that our FoL achieves the
state-of-the-art on multiple VPR benchmarks in both image retrieval and
re-ranking stages and also significantly outperforms existing two-stage VPR
methods in terms of computational efficiency. Code and models are available at
https://github.com/chenshunpeng/FoL