---
layout: publication
title: Hard-aware Deeply Cascaded Embedding
authors: Yuhui Yuan, Kuiyuan Yang, Chao Zhang
conference: Arxiv
year: 2016
bibkey: yuan2016hard
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1611.05720'}]
tags: [Distance Metric Learning, Datasets]
short_authors: Yuhui Yuan, Kuiyuan Yang, Chao Zhang
---
Riding on the waves of deep neural networks, deep metric learning has also
achieved promising results in various tasks using triplet network or Siamese
network. Though the basic goal of making images from the same category closer
than the ones from different categories is intuitive, it is hard to directly
optimize due to the quadratic or cubic sample size. To solve the problem, hard
example mining which only focuses on a subset of samples that are considered
hard is widely used. However, hard is defined relative to a model, where
complex models treat most samples as easy ones and vice versa for simple
models, and both are not good for training. Samples are also with different
hard levels, it is hard to define a model with the just right complexity and
choose hard examples adequately. This motivates us to ensemble a set of models
with different complexities in cascaded manner and mine hard examples
adaptively, a sample is judged by a series of models with increasing
complexities and only updates models that consider the sample as a hard case.
We evaluate our method on CARS196, CUB-200-2011, Stanford Online Products,
VehicleID and DeepFashion datasets. Our method outperforms state-of-the-art
methods by a large margin.