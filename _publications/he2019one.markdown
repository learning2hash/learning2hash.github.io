---
layout: publication
title: 'One Network For Multi-domains: Domain Adaptive Hashing With Intersectant Generative
  Adversarial Network'
authors: Tao He, Yuan-fang Li, Lianli Gao, Dongxiang Zhang, Jingkuan Song
conference: Proceedings of the Twenty-Eighth International Joint Conference on Artificial
  Intelligence
year: 2019
bibkey: he2019one
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1907.00612'}]
tags: ["Datasets", "Evaluation", "Hashing Methods", "Image Retrieval", "Robustness"]
short_authors: He et al.
---
With the recent explosive increase of digital data, image recognition and
retrieval become a critical practical application. Hashing is an effective
solution to this problem, due to its low storage requirement and high query
speed. However, most of past works focus on hashing in a single (source)
domain. Thus, the learned hash function may not adapt well in a new (target)
domain that has a large distributional difference with the source domain. In
this paper, we explore an end-to-end domain adaptive learning framework that
simultaneously and precisely generates discriminative hash codes and classifies
target domain images. Our method encodes two domains images into a semantic
common space, followed by two independent generative adversarial networks
arming at crosswise reconstructing two domains' images, reducing domain
disparity and improving alignment in the shared space. We evaluate our
framework on \{four\} public benchmark datasets, all of which show that our
method is superior to the other state-of-the-art methods on the tasks of object
recognition and image retrieval.