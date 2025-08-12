---
layout: publication
title: Boosting Few-shot Classification With View-learnable Contrastive Learning
authors: Xu Luo, Yuxuan Chen, Liangjian Wen, Lili Pan, Zenglin Xu
conference: 2021 IEEE International Conference on Multimedia and Expo (ICME)
year: 2021
bibkey: luo2021boosting
citations: 24
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2107.09242'}]
tags: ["Distance Metric Learning", "Few Shot & Zero Shot", "Self-Supervised"]
short_authors: Luo et al.
---
The goal of few-shot classification is to classify new categories with few
labeled examples within each class. Nowadays, the excellent performance in
handling few-shot classification problems is shown by metric-based
meta-learning methods. However, it is very hard for previous methods to
discriminate the fine-grained sub-categories in the embedding space without
fine-grained labels. This may lead to unsatisfactory generalization to
fine-grained subcategories, and thus affects model interpretation. To tackle
this problem, we introduce the contrastive loss into few-shot classification
for learning latent fine-grained structure in the embedding space. Furthermore,
to overcome the drawbacks of random image transformation used in current
contrastive learning in producing noisy and inaccurate image pairs (i.e.,
views), we develop a learning-to-learn algorithm to automatically generate
different views of the same image. Extensive experiments on standard few-shot
learning benchmarks demonstrate the superiority of our method.