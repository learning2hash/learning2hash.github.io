---
layout: publication
title: 'Multires-netvlad: Augmenting Place Recognition Training With Low-resolution
  Imagery'
authors: Khaliq Ahmad, Milford Michael, Garg Sourav
conference: IEEE Robotics and Automation Letters
year: 2022
bibkey: khaliq2022multires
citations: 37
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2202.09146'}]
tags: ["Datasets", "Evaluation", "Image Retrieval", "Similarity Search"]
short_authors: Khaliq Ahmad, Milford Michael, Garg Sourav
---
Visual Place Recognition (VPR) is a crucial component of 6-DoF localization,
visual SLAM and structure-from-motion pipelines, tasked to generate an initial
list of place match hypotheses by matching global place descriptors. However,
commonly-used CNN-based methods either process multiple image resolutions after
training or use a single resolution and limit multi-scale feature extraction to
the last convolutional layer during training. In this paper, we augment NetVLAD
representation learning with low-resolution image pyramid encoding which leads
to richer place representations. The resultant multi-resolution feature pyramid
can be conveniently aggregated through VLAD into a single compact
representation, avoiding the need for concatenation or summation of multiple
patches in recent multi-scale approaches. Furthermore, we show that the
underlying learnt feature tensor can be combined with existing multi-scale
approaches to improve their baseline performance. Evaluation on 15
viewpoint-varying and viewpoint-consistent benchmarking datasets confirm that
the proposed MultiRes-NetVLAD leads to state-of-the-art Recall@N performance
for global descriptor based retrieval, compared against 11 existing techniques.
Source code is publicly available at
https://github.com/Ahmedest61/MultiRes-NetVLAD.