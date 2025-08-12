---
layout: publication
title: Glocal Energy-based Learning For Few-shot Open-set Recognition
authors: Haoyu Wang, Guansong Pang, Peng Wang, Lei Zhang, Wei Wei, Yanning Zhang
conference: 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2023
bibkey: wang2023glocal
citations: 18
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2304.11855'}]
tags: ["CVPR", "Few Shot & Zero Shot"]
short_authors: Wang et al.
---
Few-shot open-set recognition (FSOR) is a challenging task of great practical
value. It aims to categorize a sample to one of the pre-defined, closed-set
classes illustrated by few examples while being able to reject the sample from
unknown classes. In this work, we approach the FSOR task by proposing a novel
energy-based hybrid model. The model is composed of two branches, where a
classification branch learns a metric to classify a sample to one of closed-set
classes and the energy branch explicitly estimates the open-set probability. To
achieve holistic detection of open-set samples, our model leverages both
class-wise and pixel-wise features to learn a glocal energy-based score, in
which a global energy score is learned using the class-wise features, while a
local energy score is learned using the pixel-wise features. The model is
enforced to assign large energy scores to samples that are deviated from the
few-shot examples in either the class-wise features or the pixel-wise features,
and to assign small energy scores otherwise. Experiments on three standard FSOR
datasets show the superior performance of our model.