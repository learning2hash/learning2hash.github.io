---
layout: publication
title: 'Learning To Compare Relation: Semantic Alignment For Few-shot Learning'
authors: Congqi Cao, Yanning Zhang
conference: IEEE Transactions on Image Processing
year: 2022
bibkey: cao2020learning
citations: 30
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2003.00210'}]
tags: ["Distance Metric Learning"]
short_authors: Congqi Cao, Yanning Zhang
---
Few-shot learning is a fundamental and challenging problem since it requires
recognizing novel categories from only a few examples. The objects for
recognition have multiple variants and can locate anywhere in images. Directly
comparing query images with example images can not handle content misalignment.
The representation and metric for comparison are critical but challenging to
learn due to the scarcity and wide variation of the samples in few-shot
learning. In this paper, we present a novel semantic alignment model to compare
relations, which is robust to content misalignment. We propose to add two key
ingredients to existing few-shot learning frameworks for better feature and
metric learning ability. First, we introduce a semantic alignment loss to align
the relation statistics of the features from samples that belong to the same
category. And second, local and global mutual information maximization is
introduced, allowing for representations that contain locally-consistent and
intra-class shared information across structural locations in an image.
Thirdly, we introduce a principled approach to weigh multiple loss functions by
considering the homoscedastic uncertainty of each stream. We conduct extensive
experiments on several few-shot learning datasets. Experimental results show
that the proposed method is capable of comparing relations with semantic
alignment strategies, and achieves state-of-the-art performance.