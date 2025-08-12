---
layout: publication
title: Hybrid Multi-stage Decoding For Few-shot NER With Entity-aware Contrastive
  Learning
authors: Peipei Liu, Gaosheng Wang, Ying Tong, Jian Liang, Zhenquan Ding, Hongsong
  Zhu
conference: Arxiv
year: 2024
bibkey: liu2024hybrid
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2404.06970'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Liu et al.
---
Few-shot named entity recognition can identify new types of named entities
based on a few labeled examples. Previous methods employing token-level or
span-level metric learning suffer from the computational burden and a large
number of negative sample spans. In this paper, we propose the Hybrid
Multi-stage Decoding for Few-shot NER with Entity-aware Contrastive Learning
(MsFNER), which splits the general NER into two stages: entity-span detection
and entity classification. There are 3 processes for introducing MsFNER:
training, finetuning, and inference. In the training process, we train and get
the best entity-span detection model and the entity classification model
separately on the source domain using meta-learning, where we create a
contrastive learning module to enhance entity representations for entity
classification. During finetuning, we finetune the both models on the support
dataset of target domain. In the inference process, for the unlabeled data, we
first detect the entity-spans, then the entity-spans are jointly determined by
the entity classification model and the KNN. We conduct experiments on the open
FewNERD dataset and the results demonstrate the advance of MsFNER.