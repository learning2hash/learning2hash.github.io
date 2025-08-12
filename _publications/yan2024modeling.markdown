---
layout: publication
title: Modeling Multi-modal Cross-interaction For Multi-label Few-shot Image Classification
  Based On Local Feature Selection
authors: Kun Yan, Zied Bouraoui, Fangyun Wei, Chang Xu, Ping Wang, Shoaib Jameel,
  Steven Schockaert
conference: ACM Transactions on Multimedia Computing, Communications, and Applications
year: 2025
bibkey: yan2024modeling
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.13732'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Yan et al.
---
The aim of multi-label few-shot image classification (ML-FSIC) is to assign
semantic labels to images, in settings where only a small number of training
examples are available for each label. A key feature of the multi-label setting
is that an image often has several labels, which typically refer to objects
appearing in different regions of the image. When estimating label prototypes,
in a metric-based setting, it is thus important to determine which regions are
relevant for which labels, but the limited amount of training data and the
noisy nature of local features make this highly challenging. As a solution, we
propose a strategy in which label prototypes are gradually refined. First, we
initialize the prototypes using word embeddings, which allows us to leverage
prior knowledge about the meaning of the labels. Second, taking advantage of
these initial prototypes, we then use a Loss Change Measurement (LCM) strategy
to select the local features from the training images (i.e. the support set)
that are most likely to be representative of a given label. Third, we construct
the final prototype of the label by aggregating these representative local
features using a multi-modal cross-interaction mechanism, which again relies on
the initial word embedding-based prototypes. Experiments on COCO, PASCAL VOC,
NUS-WIDE, and iMaterialist show that our model substantially improves the
current state-of-the-art.