---
layout: publication
title: 'Sfm On-the-fly: Get Better 3D From What You Capture'
authors: Zongqian Zhan, Yifei Yu, Rui Xia, Wentian Gan, Hong Xie, Giulio Perda, Luca
  Morelli, Fabio Remondino, Xin Wang
conference: Arxiv
year: 2024
bibkey: zhan2024sfm
citations: 0
additional_links: [{name: Code, url: 'http://yifeiyu225.github.io/on-the-flySfMv2.github.io/'},
  {name: Paper, url: 'https://arxiv.org/abs/2407.03939'}]
tags: ["Efficiency", "Graph Based ANN"]
short_authors: Zhan et al.
---
In the last twenty years, Structure from Motion (SfM) has been a constant
research hotspot in the fields of photogrammetry, computer vision, robotics
etc., whereas real-time performance is just a recent topic of growing interest.
This work builds upon the original on-the-fly SfM (Zhan et al., 2024) and
presents an updated version with three new advancements to get better 3D from
what you capture: (i) real-time image matching is further boosted by employing
the Hierarchical Navigable Small World (HNSW) graphs, thus more true positive
overlapping image candidates are faster identified; (ii) a self-adaptive
weighting strategy is proposed for robust hierarchical local bundle adjustment
to improve the SfM results; (iii) multiple agents are included for supporting
collaborative SfM and seamlessly merge multiple 3D reconstructions into a
complete 3D scene when commonly registered images appear. Various comprehensive
experiments demonstrate that the proposed SfM method (named on-the-fly SfMv2)
can generate more complete and robust 3D reconstructions in a high
time-efficient way. Code is available at
http://yifeiyu225.github.io/on-the-flySfMv2.github.io/.