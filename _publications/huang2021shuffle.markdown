---
layout: publication
title: 'Shuffle Transformer: Rethinking Spatial Shuffle For Vision Transformer'
authors: Zilong Huang, Youcheng Ben, Guozhong Luo, Pei Cheng, Gang Yu, Bin Fu
conference: Arxiv
year: 2021
bibkey: huang2021shuffle
citations: 118
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2106.03650'}]
tags: []
short_authors: Huang et al.
---
Very recently, Window-based Transformers, which computed self-attention
within non-overlapping local windows, demonstrated promising results on image
classification, semantic segmentation, and object detection. However, less
study has been devoted to the cross-window connection which is the key element
to improve the representation ability. In this work, we revisit the spatial
shuffle as an efficient way to build connections among windows. As a result, we
propose a new vision transformer, named Shuffle Transformer, which is highly
efficient and easy to implement by modifying two lines of code. Furthermore,
the depth-wise convolution is introduced to complement the spatial shuffle for
enhancing neighbor-window connections. The proposed architectures achieve
excellent performance on a wide range of visual tasks including image-level
classification, object detection, and semantic segmentation. Code will be
released for reproduction.