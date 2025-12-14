---
layout: publication
title: End-to-end Efficient Representation Learning Via Cascading Combinatorial Optimization
authors: Yeonwoo Jeong, Yoonsung Kim, Hyun Oh Song
conference: 2019 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2019
bibkey: jeong2019end
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1902.10990'}]
tags: [Evaluation, Efficiency, Datasets, Quantization, CVPR, Hashing Methods]
short_authors: Yeonwoo Jeong, Yoonsung Kim, Hyun Oh Song
---
We develop hierarchically quantized efficient embedding representations for
similarity-based search and show that this representation provides not only the
state of the art performance on the search accuracy but also provides several
orders of speed up during inference. The idea is to hierarchically quantize the
representation so that the quantization granularity is greatly increased while
maintaining the accuracy and keeping the computational complexity low. We also
show that the problem of finding the optimal sparse compound hash code
respecting the hierarchical structure can be optimized in polynomial time via
minimum cost flow in an equivalent flow network. This allows us to train the
method end-to-end in a mini-batch stochastic gradient descent setting. Our
experiments on Cifar100 and ImageNet datasets show the state of the art search
accuracy while providing several orders of magnitude search speedup
respectively over exhaustive linear search over the dataset.