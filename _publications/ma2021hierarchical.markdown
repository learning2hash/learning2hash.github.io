---
layout: publication
title: "Hierarchical Similarity Learning for Language-based Product Image Retrieval"
authors: Ma Zhe, Liu Fenghao, Dong Jianfeng, Qu Xiaoye, He Yuan, Ji Shouling
conference: Arxiv
year: 2021
bibkey: ma2021hierarchical
additional_links:
- {name: "Paper", url: "https://arxiv.org/abs/2102.09375"}
  - {name: "Code", url: "https://github.com/liufh1/hsl."}
tags: ['ARXIV', 'Cross Modal', 'Image Retrieval', 'TIP']
---
This paper aims for the language-based product image retrieval task. The majority of previous works have made significant progress by designing network structure, similarity measurement, and loss function. However, they typically perform vision-text matching at certain granularity regardless of the intrinsic multiple granularities of images. In this paper, we focus on the cross-modal similarity measurement, and propose a novel Hierarchical Similarity Learning (HSL) network. HSL first learns multi-level representations of input data by stacked encoders, and object-granularity similarity and image-granularity similarity are computed at each level. All the similarities are combined as the final hierarchical cross-modal similarity. Experiments on a large-scale product retrieval dataset demonstrate the effectiveness of our proposed method. Code and data are available at https://github.com/liufh1/hsl.