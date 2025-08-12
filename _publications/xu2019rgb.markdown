---
layout: publication
title: RGB-D Individual Segmentation
authors: Wenqiang Xu, Yanjun Fu, Yuchen Luo, Chang Liu, Cewu Lu
conference: Arxiv
year: 2019
bibkey: xu2019rgb
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1910.07641'}]
tags: ["Datasets"]
short_authors: Xu et al.
---
Fine-grained recognition task deals with sub-category classification problem,
which is important for real-world applications. In this work, we are
particularly interested in the segmentation task on the *finest-grained*
level, which is specifically named "individual segmentation". In other words,
the individual-level category has no sub-category under it. Segmentation
problem in the individual level reveals some new properties, limited training
data for single individual object, unknown background, and difficulty for the
use of depth. To address these new problems, we propose a "Context Less-Aware"
(CoLA) pipeline, which produces RGB-D object-predominated images that have less
background context, and enables a scale-aware training and testing with 3D
information. Extensive experiments show that the proposed CoLA strategy largely
outperforms baseline methods on YCB-Video dataset and our proposed
Supermarket-10K dataset. Code, trained model and new dataset will be published
with this paper.