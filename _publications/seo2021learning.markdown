---
layout: publication
title: Learning To Discover Reflection Symmetry Via Polar Matching Convolution
authors: Ahyun Seo, Woohyeon Shim, Minsu Cho
conference: 2021 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2021
bibkey: seo2021learning
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2108.12952'}]
tags: ["ICCV"]
short_authors: Ahyun Seo, Woohyeon Shim, Minsu Cho
---
The task of reflection symmetry detection remains challenging due to
significant variations and ambiguities of symmetry patterns in the wild.
Furthermore, since the local regions are required to match in reflection for
detecting a symmetry pattern, it is hard for standard convolutional networks,
which are not equivariant to rotation and reflection, to learn the task. To
address the issue, we introduce a new convolutional technique, dubbed the polar
matching convolution, which leverages a polar feature pooling, a
self-similarity encoding, and a systematic kernel design for axes of different
angles. The proposed high-dimensional kernel convolution network effectively
learns to discover symmetry patterns from real-world images, overcoming the
limitations of standard convolution. In addition, we present a new dataset and
introduce a self-supervised learning strategy by augmenting the dataset with
synthesizing images. Experiments demonstrate that our method outperforms
state-of-the-art methods in terms of accuracy and robustness.