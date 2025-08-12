---
layout: publication
title: 'Tinydet: Accurate Small Object Detection In Lightweight Generic Detectors'
authors: Shaoyu Chen, Tianheng Cheng, Jiemin Fang, Qian Zhang, Yuan Li, Wenyu Liu,
  Xinggang Wang
conference: Arxiv
year: 2023
bibkey: chen2023tinydet
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2304.03428'}]
tags: ["Evaluation"]
short_authors: Chen et al.
---
Small object detection requires the detection head to scan a large number of
positions on image feature maps, which is extremely hard for computation- and
energy-efficient lightweight generic detectors. To accurately detect small
objects with limited computation, we propose a two-stage lightweight detection
framework with extremely low computation complexity, termed as TinyDet. It
enables high-resolution feature maps for dense anchoring to better cover small
objects, proposes a sparsely-connected convolution for computation reduction,
enhances the early stage features in the backbone, and addresses the feature
misalignment problem for accurate small object detection. On the COCO
benchmark, our TinyDet-M achieves 30.3 AP and 13.5 AP^s with only 991 MFLOPs,
which is the first detector that has an AP over 30 with less than 1 GFLOPs;
besides, TinyDet-S and TinyDet-L achieve promising performance under different
computation limitation.