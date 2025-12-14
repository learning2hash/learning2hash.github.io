---
layout: publication
title: Towards Unsupervised Sketch-based Image Retrieval
authors: Conghui Hu, Yongxin Yang, Yunpeng Li, Timothy M. Hospedales, Yi-Zhe Song
conference: Arxiv
year: 2021
bibkey: hu2021towards
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2105.08237'}]
tags: [Evaluation, Supervised, Image Retrieval, Few-shot & Zero-shot, Datasets, Scalability,
  Unsupervised, Tools & Libraries]
short_authors: Hu et al.
---
The practical value of existing supervised sketch-based image retrieval
(SBIR) algorithms is largely limited by the requirement for intensive data
collection and labeling. In this paper, we present the first attempt at
unsupervised SBIR to remove the labeling cost (both category annotations and
sketch-photo pairings) that is conventionally needed for training. Existing
single-domain unsupervised representation learning methods perform poorly in
this application, due to the unique cross-domain (sketch and photo) nature of
the problem. We therefore introduce a novel framework that simultaneously
performs sketch-photo domain alignment and semantic-aware representation
learning. Technically this is underpinned by introducing joint distribution
optimal transport (JDOT) to align data from different domains, which we extend
with trainable cluster prototypes and feature memory banks to further improve
scalability and efficacy. Extensive experiments show that our framework
achieves excellent performance in the new unsupervised setting, and performs
comparably or better than state-of-the-art in the zero-shot setting.