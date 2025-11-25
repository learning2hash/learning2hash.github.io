---
layout: publication
title: Adversarial Learning Of Hard Positives For Place Recognition
authors: Wenxuan Fang, Kai Zhang, Yoli Shavit, Wensen Feng
conference: 2022 International Joint Conference on Neural Networks (IJCNN)
year: 2022
bibkey: fang2022adversarial
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2205.03871'}]
tags: ["Image Retrieval", "Robustness"]
short_authors: Fang et al.
---
Image retrieval methods for place recognition learn global image descriptors
that are used for fetching geo-tagged images at inference time. Recent works
have suggested employing weak and self-supervision for mining hard positives
and hard negatives in order to improve localization accuracy and robustness to
visibility changes (e.g. in illumination or view point). However, generating
hard positives, which is essential for obtaining robustness, is still limited
to hard-coded or global augmentations. In this work we propose an adversarial
method to guide the creation of hard positives for training image retrieval
networks. Our method learns local and global augmentation policies which will
increase the training loss, while the image retrieval network is forced to
learn more powerful features for discriminating increasingly difficult
examples. This approach allows the image retrieval network to generalize beyond
the hard examples presented in the data and learn features that are robust to a
wide range of variations. Our method achieves state-of-the-art recalls on the
Pitts250 and Tokyo 24/7 benchmarks and outperforms recent image retrieval
methods on the rOxford and rParis datasets by a noticeable margin.