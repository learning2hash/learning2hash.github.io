---
layout: publication
title: Coarse-to-fine Visual Localization Using Semantic Compact Map
authors: Ziwei Liao, Jieqi Shi, Xianyu Qi, Xiaoyu Zhang, Wei Wang, Yijia He, Ran Wei,
  Xiao Liu
conference: 2020 3rd International Conference on Control and Robots (ICCR)
year: 2020
bibkey: liao2019coarse
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1910.04936'}]
tags: []
short_authors: Liao et al.
---
Robust visual localization for urban vehicles remains challenging and
unsolved. The limitation of computation efficiency and memory size has made it
harder for large-scale applications. Since semantic information serves as a
stable and compact representation of the environment, we propose a
coarse-to-fine localization system based on a semantic compact map. Pole-like
objects are stored in the compact map, then are extracted from semantically
segmented images as observations. Localization is performed by a particle
filter, followed by a pose alignment module decoupling translation and rotation
to achieve better accuracy. We evaluate our system both on synthetic and
realistic datasets and compare it with two baselines, a state-of-art semantic
feature-based system, and a traditional SIFT feature-based system. Experiments
demonstrate that even with a significantly small map, such as a 10 KB map for a
3.7 km long trajectory, our system provides a comparable accuracy with the
baselines.