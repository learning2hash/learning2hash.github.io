---
layout: publication
title: Boosting Few-shot Semantic Segmentation With Transformers
authors: Guolei Sun, Yun Liu, Jingyun Liang, Luc van Gool
conference: Arxiv
year: 2021
bibkey: sun2021boosting
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2108.02266'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Sun et al.
---
Due to the fact that fully supervised semantic segmentation methods require
sufficient fully-labeled data to work well and can not generalize to unseen
classes, few-shot segmentation has attracted lots of research attention.
Previous arts extract features from support and query images, which are
processed jointly before making predictions on query images. The whole process
is based on convolutional neural networks (CNN), leading to the problem that
only local information is used. In this paper, we propose a TRansformer-based
Few-shot Semantic segmentation method (TRFS). Specifically, our model consists
of two modules: Global Enhancement Module (GEM) and Local Enhancement Module
(LEM). GEM adopts transformer blocks to exploit global information, while LEM
utilizes conventional convolutions to exploit local information, across query
and support features. Both GEM and LEM are complementary, helping to learn
better feature representations for segmenting query images. Extensive
experiments on PASCAL-5i and COCO datasets show that our approach achieves new
state-of-the-art performance, demonstrating its effectiveness.