---
layout: publication
title: 'Beyond The Deep Metric Learning: Enhance The Cross-modal Matching With Adversarial
  Discriminative Domain Regularization'
authors: Li Ren, Kai Li, Liqiang Wang, Kien Hua
conference: Arxiv
year: 2020
bibkey: ren2020beyond
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2010.12126'}]
tags: [Evaluation, Efficiency, Distance Metric Learning, Robustness, Tools & Libraries]
short_authors: Ren et al.
---
Matching information across image and text modalities is a fundamental
challenge for many applications that involve both vision and natural language
processing. The objective is to find efficient similarity metrics to compare
the similarity between visual and textual information. Existing approaches
mainly match the local visual objects and the sentence words in a shared space
with attention mechanisms. The matching performance is still limited because
the similarity computation is based on simple comparisons of the matching
features, ignoring the characteristics of their distribution in the data. In
this paper, we address this limitation with an efficient learning objective
that considers the discriminative feature distributions between the visual
objects and sentence words. Specifically, we propose a novel Adversarial
Discriminative Domain Regularization (ADDR) learning framework, beyond the
paradigm metric learning objective, to construct a set of discriminative data
domains within each image-text pairs. Our approach can generally improve the
learning efficiency and the performance of existing metrics learning frameworks
by regulating the distribution of the hidden space between the matching pairs.
The experimental results show that this new approach significantly improves the
overall performance of several popular cross-modal matching techniques (SCAN,
VSRN, BFAN) on the MS-COCO and Flickr30K benchmarks.