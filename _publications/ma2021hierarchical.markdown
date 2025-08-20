---
layout: publication
title: Hierarchical Similarity Learning For Language-based Product Image Retrieval
authors: Zhe Ma, Fenghao Liu, Jianfeng Dong, Xiaoye Qu, Yuan He, Shouling Ji
conference: ICASSP 2021 - 2021 IEEE International Conference on Acoustics, Speech
  and Signal Processing (ICASSP)
year: 2021
bibkey: ma2021hierarchical
citations: 3
additional_links: [{name: Code, url: 'https://github.com/liufh1/hsl.'}, {name: Paper,
    url: 'https://arxiv.org/abs/2102.09375'}]
tags: [Scalability, ICASSP, Image Retrieval, Datasets]
short_authors: Ma et al.
---
This paper aims for the language-based product image retrieval task. The
majority of previous works have made significant progress by designing network
structure, similarity measurement, and loss function. However, they typically
perform vision-text matching at certain granularity regardless of the intrinsic
multiple granularities of images. In this paper, we focus on the cross-modal
similarity measurement, and propose a novel Hierarchical Similarity Learning
(HSL) network. HSL first learns multi-level representations of input data by
stacked encoders, and object-granularity similarity and image-granularity
similarity are computed at each level. All the similarities are combined as the
final hierarchical cross-modal similarity. Experiments on a large-scale product
retrieval dataset demonstrate the effectiveness of our proposed method. Code
and data are available at https://github.com/liufh1/hsl.