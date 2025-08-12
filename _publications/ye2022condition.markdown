---
layout: publication
title: Condition-invariant And Compact Visual Place Description By Convolutional Autoencoder
authors: Hanjing Ye, Weinan Chen, Jingwen Yu, Li He, Yisheng Guan, Hong Zhang
conference: Robotica
year: 2023
bibkey: ye2022condition
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2204.07350'}]
tags: []
short_authors: Ye et al.
---
Visual place recognition (VPR) in condition-varying environments is still an
open problem. Popular solutions are CNN-based image descriptors, which have
been shown to outperform traditional image descriptors based on hand-crafted
visual features. However, there are two drawbacks of current CNN-based
descriptors: a) their high dimension and b) lack of generalization, leading to
low efficiency and poor performance in applications. In this paper, we propose
to use a convolutional autoencoder (CAE) to tackle this problem. We employ a
high-level layer of a pre-trained CNN to generate features, and train a CAE to
map the features to a low-dimensional space to improve the condition invariance
property of the descriptor and reduce its dimension at the same time. We verify
our method in three challenging datasets involving significant illumination
changes, and our method is shown to be superior to the state-of-the-art. For
the benefit of the community, we make public the source code.