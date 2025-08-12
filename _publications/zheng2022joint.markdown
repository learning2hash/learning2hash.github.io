---
layout: publication
title: Joint Debiased Representation And Image Clustering Learning With Self-supervision
authors: Shunjie-Fabian Zheng, Jaeeun Nam, Emilio Dorigatti, Bernd Bischl, Shekoofeh
  Azizi, Mina Rezaei
conference: Arxiv
year: 2022
bibkey: zheng2022joint
citations: 0
additional_links: [{name: Code, url: 'https://anonymous.4open.science/r/SSL-debiased-clustering'},
  {name: Paper, url: 'https://arxiv.org/abs/2209.06941'}]
tags: ["Self-Supervised"]
short_authors: Zheng et al.
---
Contrastive learning is among the most successful methods for visual
representation learning, and its performance can be further improved by jointly
performing clustering on the learned representations. However, existing methods
for joint clustering and contrastive learning do not perform well on
long-tailed data distributions, as majority classes overwhelm and distort the
loss of minority classes, thus preventing meaningful representations to be
learned. Motivated by this, we develop a novel joint clustering and contrastive
learning framework by adapting the debiased contrastive loss to avoid
under-clustering minority classes of imbalanced datasets. We show that our
proposed modified debiased contrastive loss and divergence clustering loss
improves the performance across multiple datasets and learning tasks. The
source code is available at
https://anonymous.4open.science/r/SSL-debiased-clustering