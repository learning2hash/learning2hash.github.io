---
layout: publication
title: Vocabulary-informed Zero-shot And Open-set Learning
authors: Yanwei Fu, Xiaomei Wang, Hanze Dong, Yu-Gang Jiang, Meng Wang, Xiangyang
  Xue, Leonid Sigal
conference: IEEE Transactions on Pattern Analysis and Machine Intelligence
year: 2019
bibkey: fu2019vocabulary
citations: 23
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2301.00998'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Fu et al.
---
Despite significant progress in object categorization, in recent years, a
number of important challenges remain; mainly, the ability to learn from
limited labeled data and to recognize object classes within large, potentially
open, set of labels. Zero-shot learning is one way of addressing these
challenges, but it has only been shown to work with limited sized class
vocabularies and typically requires separation between supervised and
unsupervised classes, allowing former to inform the latter but not vice versa.
We propose the notion of vocabulary-informed learning to alleviate the above
mentioned challenges and address problems of supervised, zero-shot, generalized
zero-shot and open set recognition using a unified framework. Specifically, we
propose a weighted maximum margin framework for semantic manifold-based
recognition that incorporates distance constraints from (both supervised and
unsupervised) vocabulary atoms. Distance constraints ensure that labeled
samples are projected closer to their correct prototypes, in the embedding
space, than to others. We illustrate that resulting model shows improvements in
supervised, zero-shot, generalized zero-shot, and large open set recognition,
with up to 310K class vocabulary on Animal with Attributes and ImageNet
datasets.