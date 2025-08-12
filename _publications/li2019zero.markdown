---
layout: publication
title: Zero-shot Sketch-based Image Retrieval With Structure-aware Asymmetric Disentanglement
authors: Jiangtong Li, Zhixin Ling, Li Niu, Liqing Zhang
conference: Computer Vision and Image Understanding
year: 2022
bibkey: li2019zero
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1911.13251'}]
tags: ["Image Retrieval"]
short_authors: Li et al.
---
The goal of Sketch-Based Image Retrieval (SBIR) is using free-hand sketches
to retrieve images of the same category from a natural image gallery. However,
SBIR requires all test categories to be seen during training, which cannot be
guaranteed in real-world applications. So we investigate more challenging
Zero-Shot SBIR (ZS-SBIR), in which test categories do not appear in the
training stage. After realizing that sketches mainly contain structure
information while images contain additional appearance information, we attempt
to achieve structure-aware retrieval via asymmetric disentanglement.For this
purpose, we propose our STRucture-aware Asymmetric Disentanglement (STRAD)
method, in which image features are disentangled into structure features and
appearance features while sketch features are only projected to structure
space. Through disentangling structure and appearance space, bi-directional
domain translation is performed between the sketch domain and the image domain.
Extensive experiments demonstrate that our STRAD method remarkably outperforms
state-of-the-art methods on three large-scale benchmark datasets.