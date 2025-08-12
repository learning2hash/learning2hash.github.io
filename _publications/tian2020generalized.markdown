---
layout: publication
title: Generalized Few-shot Semantic Segmentation
authors: Zhuotao Tian, Xin Lai, Li Jiang, Shu Liu, Michelle Shu, Hengshuang Zhao,
  Jiaya Jia
conference: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2022
bibkey: tian2020generalized
citations: 73
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2010.05210'}]
tags: ["CVPR", "Few Shot & Zero Shot"]
short_authors: Tian et al.
---
Training semantic segmentation models requires a large amount of finely
annotated data, making it hard to quickly adapt to novel classes not satisfying
this condition. Few-Shot Segmentation (FS-Seg) tackles this problem with many
constraints. In this paper, we introduce a new benchmark, called Generalized
Few-Shot Semantic Segmentation (GFS-Seg), to analyze the generalization ability
of simultaneously segmenting the novel categories with very few examples and
the base categories with sufficient examples. It is the first study showing
that previous representative state-of-the-art FS-Seg methods fall short in
GFS-Seg and the performance discrepancy mainly comes from the constrained
setting of FS-Seg. To make GFS-Seg tractable, we set up a GFS-Seg baseline that
achieves decent performance without structural change on the original model.
Then, since context is essential for semantic segmentation, we propose the
Context-Aware Prototype Learning (CAPL) that significantly improves performance
by 1) leveraging the co-occurrence prior knowledge from support samples, and 2)
dynamically enriching contextual information to the classifier, conditioned on
the content of each query image. Both two contributions are experimentally
shown to have substantial practical merit. Extensive experiments on Pascal-VOC
and COCO manifest the effectiveness of CAPL, and CAPL generalizes well to
FS-Seg by achieving competitive performance. Code is available at
https://github.com/dvlab-research/GFS-Seg.