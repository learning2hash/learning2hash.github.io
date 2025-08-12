---
layout: publication
title: Inferring Prototypes For Multi-label Few-shot Image Classification With Word
  Vector Guided Attention
authors: Kun Yan, Chenbin Zhang, Jun Hou, Ping Wang, Zied Bouraoui, Shoaib Jameel,
  Steven Schockaert
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2022
bibkey: yan2021inferring
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2112.01037'}]
tags: ["AAAI", "Few Shot & Zero Shot"]
short_authors: Yan et al.
---
Multi-label few-shot image classification (ML-FSIC) is the task of assigning
descriptive labels to previously unseen images, based on a small number of
training examples. A key feature of the multi-label setting is that images
often have multiple labels, which typically refer to different regions of the
image. When estimating prototypes, in a metric-based setting, it is thus
important to determine which regions are relevant for which labels, but the
limited amount of training data makes this highly challenging. As a solution,
in this paper we propose to use word embeddings as a form of prior knowledge
about the meaning of the labels. In particular, visual prototypes are obtained
by aggregating the local feature maps of the support images, using an attention
mechanism that relies on the label embeddings. As an important advantage, our
model can infer prototypes for unseen labels without the need for fine-tuning
any model parameters, which demonstrates its strong generalization abilities.
Experiments on COCO and PASCAL VOC furthermore show that our model
substantially improves the current state-of-the-art.