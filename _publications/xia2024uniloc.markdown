---
layout: publication
title: 'Uniloc: Towards Universal Place Recognition Using Any Single Modality'
authors: "Yan Xia, Zhendong Li, Yun-Jin Li, Letian Shi, Hu Cao, Jo\xE3o F. Henriques,\
  \ Daniel Cremers"
conference: Arxiv
year: 2024
bibkey: xia2024uniloc
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.12079'}]
tags: []
short_authors: Xia et al.
---
To date, most place recognition methods focus on single-modality retrieval.
While they perform well in specific environments, cross-modal methods offer
greater flexibility by allowing seamless switching between map and query
sources. It also promises to reduce computation requirements by having a
unified model, and achieving greater sample efficiency by sharing parameters.
In this work, we develop a universal solution to place recognition, UniLoc,
that works with any single query modality (natural language, image, or point
cloud). UniLoc leverages recent advances in large-scale contrastive learning,
and learns by matching hierarchically at two levels: instance-level matching
and scene-level matching. Specifically, we propose a novel Self-Attention based
Pooling (SAP) module to evaluate the importance of instance descriptors when
aggregated into a place-level descriptor. Experiments on the KITTI-360 dataset
demonstrate the benefits of cross-modality for place recognition, achieving
superior performance in cross-modal settings and competitive results also for
uni-modal scenarios. Our project page is publicly available at
https://yan-xia.github.io/projects/UniLoc/.