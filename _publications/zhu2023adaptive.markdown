---
layout: publication
title: Adaptive Confidence Multi-view Hashing For Multimedia Retrieval
authors: Jian Zhu, Yu Cui, Zhangmin Huang, Xingyu Li, Lei Liu, Lingfang Zeng, Li-Rong
  Dai
conference: ICASSP 2024 - 2024 IEEE International Conference on Acoustics, Speech
  and Signal Processing (ICASSP)
year: 2024
bibkey: zhu2023adaptive
citations: 2
additional_links: [{name: Code, url: 'https://github.com/HackerHyper/ACMVH.'}, {name: Paper,
    url: 'https://arxiv.org/abs/2312.07327'}]
tags: ["Datasets", "Hashing Methods", "ICASSP"]
short_authors: Zhu et al.
---
The multi-view hash method converts heterogeneous data from multiple views
into binary hash codes, which is one of the critical technologies in multimedia
retrieval. However, the current methods mainly explore the complementarity
among multiple views while lacking confidence learning and fusion. Moreover, in
practical application scenarios, the single-view data contain redundant noise.
To conduct the confidence learning and eliminate unnecessary noise, we propose
a novel Adaptive Confidence Multi-View Hashing (ACMVH) method. First, a
confidence network is developed to extract useful information from various
single-view features and remove noise information. Furthermore, an adaptive
confidence multi-view network is employed to measure the confidence of each
view and then fuse multi-view features through a weighted summation. Lastly, a
dilation network is designed to further enhance the feature representation of
the fused features. To the best of our knowledge, we pioneer the application of
confidence learning into the field of multimedia retrieval. Extensive
experiments on two public datasets show that the proposed ACMVH performs better
than state-of-the-art methods (maximum increase of 3.24%). The source code is
available at https://github.com/HackerHyper/ACMVH.