---
layout: publication
title: User-guided Deep Anime Line Art Colorization With Conditional Adversarial Networks
authors: Yuanzheng Ci, Xinzhu Ma, Zhihui Wang, Haojie Li, Zhongxuan Luo
conference: Proceedings of the 26th ACM international conference on Multimedia
year: 2018
bibkey: ci2018user
citations: 131
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1808.03240'}]
tags: []
short_authors: Ci et al.
---
Scribble colors based line art colorization is a challenging computer vision
problem since neither greyscale values nor semantic information is presented in
line arts, and the lack of authentic illustration-line art training pairs also
increases difficulty of model generalization. Recently, several Generative
Adversarial Nets (GANs) based methods have achieved great success. They can
generate colorized illustrations conditioned on given line art and color hints.
However, these methods fail to capture the authentic illustration distributions
and are hence perceptually unsatisfying in the sense that they often lack
accurate shading. To address these challenges, we propose a novel deep
conditional adversarial architecture for scribble based anime line art
colorization. Specifically, we integrate the conditional framework with WGAN-GP
criteria as well as the perceptual loss to enable us to robustly train a deep
network that makes the synthesized images more natural and real. We also
introduce a local features network that is independent of synthetic data. With
GANs conditioned on features from such network, we notably increase the
generalization capability over "in the wild" line arts. Furthermore, we collect
two datasets that provide high-quality colorful illustrations and authentic
line arts for training and benchmarking. With the proposed model trained on our
illustration dataset, we demonstrate that images synthesized by the presented
approach are considerably more realistic and precise than alternative
approaches.