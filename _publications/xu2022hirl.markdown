---
layout: publication
title: 'HIRL: A General Framework For Hierarchical Image Representation Learning'
authors: Minghao Xu, Yuanfan Guo, Xuanyu Zhu, Jiawen Li, Zhenbang Sun, Jian Tang,
  Yi Xu, Bingbing Ni
conference: Arxiv
year: 2022
bibkey: xu2022hirl
citations: 2
additional_links: [{name: Code, url: 'https://github.com/hirl-team/HIRL'}, {name: Paper,
    url: 'https://arxiv.org/abs/2205.13159'}]
tags: []
short_authors: Xu et al.
---
Learning self-supervised image representations has been broadly studied to
boost various visual understanding tasks. Existing methods typically learn a
single level of image semantics like pairwise semantic similarity or image
clustering patterns. However, these methods can hardly capture multiple levels
of semantic information that naturally exists in an image dataset, e.g., the
semantic hierarchy of "Persian cat to cat to mammal" encoded in an image
database for species. It is thus unknown whether an arbitrary image
self-supervised learning (SSL) approach can benefit from learning such
hierarchical semantics. To answer this question, we propose a general framework
for Hierarchical Image Representation Learning (HIRL). This framework aims to
learn multiple semantic representations for each image, and these
representations are structured to encode image semantics from fine-grained to
coarse-grained. Based on a probabilistic factorization, HIRL learns the most
fine-grained semantics by an off-the-shelf image SSL approach and learns
multiple coarse-grained semantics by a novel semantic path discrimination
scheme. We adopt six representative image SSL methods as baselines and study
how they perform under HIRL. By rigorous fair comparison, performance gain is
observed on all the six methods for diverse downstream tasks, which, for the
first time, verifies the general effectiveness of learning hierarchical image
semantics. All source code and model weights are available at
https://github.com/hirl-team/HIRL