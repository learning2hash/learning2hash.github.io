---
layout: publication
title: 'PETR: Position Embedding Transformation For Multi-view 3D Object Detection'
authors: Yingfei Liu, Tiancai Wang, Xiangyu Zhang, Jian Sun
conference: Lecture Notes in Computer Science
year: 2022
bibkey: liu2022petr
citations: 293
additional_links: [{name: Code, url: 'https://github.com/megvii-research/PETR'}, {
    name: Paper, url: 'https://arxiv.org/abs/2203.05625'}]
tags: []
short_authors: Liu et al.
---
In this paper, we develop position embedding transformation (PETR) for
multi-view 3D object detection. PETR encodes the position information of 3D
coordinates into image features, producing the 3D position-aware features.
Object query can perceive the 3D position-aware features and perform end-to-end
object detection. PETR achieves state-of-the-art performance (50.4% NDS and
44.1% mAP) on standard nuScenes dataset and ranks 1st place on the benchmark.
It can serve as a simple yet strong baseline for future research. Code is
available at https://github.com/megvii-research/PETR.