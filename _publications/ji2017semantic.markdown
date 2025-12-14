---
layout: publication
title: Semantic Softmax Loss For Zero-shot Learning
authors: Zhong Ji, Yunxin Sun, Yulong Yu, Jichang Guo, Yanwei Pang
conference: Arxiv
year: 2017
bibkey: ji2017semantic
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1705.07692'}]
tags: [Evaluation, Tools & Libraries, Few-shot & Zero-shot, Datasets]
short_authors: Ji et al.
---
A typical pipeline for Zero-Shot Learning (ZSL) is to integrate the visual
features and the class semantic descriptors into a multimodal framework with a
linear or bilinear model. However, the visual features and the class semantic
descriptors locate in different structural spaces, a linear or bilinear model
can not capture the semantic interactions between different modalities well. In
this letter, we propose a nonlinear approach to impose ZSL as a multi-class
classification problem via a Semantic Softmax Loss by embedding the class
semantic descriptors into the softmax layer of multi-class classification
network. To narrow the structural differences between the visual features and
semantic descriptors, we further use an L2 normalization constraint to the
differences between the visual features and visual prototypes reconstructed
with the semantic descriptors. The results on three benchmark datasets, i.e.,
AwA, CUB and SUN demonstrate the proposed approach can boost the performances
steadily and achieve the state-of-the-art performance for both zero-shot
classification and zero-shot retrieval.