---
layout: publication
title: 'SQN: Weakly-supervised Semantic Segmentation Of Large-scale 3D Point Clouds'
authors: Qingyong Hu, Bo Yang, Guangchi Fang, Yulan Guo, Ales Leonardis, Niki Trigoni,
  Andrew Markham
conference: Lecture Notes in Computer Science
year: 2022
bibkey: hu2021sqn
citations: 76
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2104.04891'}]
tags: ["Datasets", "Evaluation", "Scalability"]
short_authors: Hu et al.
---
Labelling point clouds fully is highly time-consuming and costly. As larger
point cloud datasets with billions of points become more common, we ask whether
the full annotation is even necessary, demonstrating that existing baselines
designed under a fully annotated assumption only degrade slightly even when
faced with 1% random point annotations. However, beyond this point, e.g., at
0.1% annotations, segmentation accuracy is unacceptably low. We observe that,
as point clouds are samples of the 3D world, the distribution of points in a
local neighborhood is relatively homogeneous, exhibiting strong semantic
similarity. Motivated by this, we propose a new weak supervision method to
implicitly augment highly sparse supervision signals. Extensive experiments
demonstrate the proposed Semantic Query Network (SQN) achieves promising
performance on seven large-scale open datasets under weak supervision schemes,
while requiring only 0.1% randomly annotated points for training, greatly
reducing annotation cost and effort. The code is available at
https://github.com/QingyongHu/SQN.