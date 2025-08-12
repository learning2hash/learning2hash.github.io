---
layout: publication
title: 'Towards Cross-granularity Few-shot Learning: Coarse-to-fine Pseudo-labeling
  With Visual-semantic Meta-embedding'
authors: Jinhai Yang, Hua Yang, Lin Chen
conference: Proceedings of the 29th ACM International Conference on Multimedia
year: 2021
bibkey: yang2020towards
citations: 13
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2007.05675'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Jinhai Yang, Hua Yang, Lin Chen
---
Few-shot learning aims at rapidly adapting to novel categories with only a
handful of samples at test time, which has been predominantly tackled with the
idea of meta-learning. However, meta-learning approaches essentially learn
across a variety of few-shot tasks and thus still require large-scale training
data with fine-grained supervision to derive a generalized model, thereby
involving prohibitive annotation cost. In this paper, we advance the few-shot
classification paradigm towards a more challenging scenario, i.e.,
cross-granularity few-shot classification, where the model observes only coarse
labels during training while is expected to perform fine-grained classification
during testing. This task largely relieves the annotation cost since
fine-grained labeling usually requires strong domain-specific expertise. To
bridge the cross-granularity gap, we approximate the fine-grained data
distribution by greedy clustering of each coarse-class into pseudo-fine-classes
according to the similarity of image embeddings. We then propose a
meta-embedder that jointly optimizes the visual- and semantic-discrimination,
in both instance-wise and coarse class-wise, to obtain a good feature space for
this coarse-to-fine pseudo-labeling process. Extensive experiments and ablation
studies are conducted to demonstrate the effectiveness and robustness of our
approach on three representative datasets.