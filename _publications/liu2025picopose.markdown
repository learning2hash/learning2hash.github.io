---
layout: publication
title: 'Picopose: Progressive Pixel-to-pixel Correspondence Learning For Novel Object
  Pose Estimation'
authors: Lihua Liu, Jiehong Lin, Zhenxin Liu, Kui Jia
conference: Arxiv
year: 2025
bibkey: liu2025picopose
citations: 0
additional_links: [{name: Code, url: 'https://github.com/foollh/PicoPose'}, {name: Paper,
    url: 'https://arxiv.org/abs/2504.02617'}]
tags: []
short_authors: Liu et al.
---
Novel object pose estimation from RGB images presents a significant challenge
for zero-shot generalization, as it involves estimating the relative 6D
transformation between an RGB observation and a CAD model of an object that was
not seen during training. In this paper, we introduce PicoPose, a novel
framework designed to tackle this task using a three-stage pixel-to-pixel
correspondence learning process. Firstly, PicoPose matches features from the
RGB observation with those from rendered object templates, identifying the
best-matched template and establishing coarse correspondences. Secondly,
PicoPose smooths the correspondences by globally regressing a 2D affine
transformation, including in-plane rotation, scale, and 2D translation, from
the coarse correspondence map. Thirdly, PicoPose applies the affine
transformation to the feature map of the best-matched template and learns
correspondence offsets within local regions to achieve fine-grained
correspondences. By progressively refining the correspondences, PicoPose
significantly improves the accuracy of object poses computed via PnP/RANSAC.
PicoPose achieves state-of-the-art performance on the seven core datasets of
the BOP benchmark, demonstrating exceptional generalization to novel objects
represented by CAD models or object reference images. Code and models are
available at https://github.com/foollh/PicoPose.