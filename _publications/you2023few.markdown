---
layout: publication
title: Few-shot Object Counting With Similarity-aware Feature Enhancement
authors: Zhiyuan You, Kai Yang, Wenhan Luo, Xin Lu, Lei Cui, Xinyi Le
conference: 2023 IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)
year: 2023
bibkey: you2023few
citations: 49
additional_links: [{name: Code, url: 'https://github.com/zhiyuanyou/SAFECount'}, {
    name: Paper, url: 'https://arxiv.org/abs/2201.08959'}]
tags: ["Few Shot & Zero Shot"]
short_authors: You et al.
---
This work studies the problem of few-shot object counting, which counts the
number of exemplar objects (i.e., described by one or several support images)
occurring in the query image. The major challenge lies in that the target
objects can be densely packed in the query image, making it hard to recognize
every single one. To tackle the obstacle, we propose a novel learning block,
equipped with a similarity comparison module and a feature enhancement module.
Concretely, given a support image and a query image, we first derive a score
map by comparing their projected features at every spatial position. The score
maps regarding all support images are collected together and normalized across
both the exemplar dimension and the spatial dimensions, producing a reliable
similarity map. We then enhance the query feature with the support features by
employing the developed point-wise similarities as the weighting coefficients.
Such a design encourages the model to inspect the query image by focusing more
on the regions akin to the support images, leading to much clearer boundaries
between different objects. Extensive experiments on various benchmarks and
training setups suggest that we surpass the state-of-the-art methods by a
sufficiently large margin. For instance, on a recent large-scale FSC-147
dataset, we surpass the state-of-the-art method by improving the mean absolute
error from 22.08 to 14.32 (35%\\(\uparrow\\)). Code has been released in
https://github.com/zhiyuanyou/SAFECount.