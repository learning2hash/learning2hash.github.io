---
layout: publication
title: A Generic Method For Fine-grained Category Discovery In Natural Language Texts
authors: Chang Tian, Matthew B. Blaschko, Wenpeng Yin, Mingzhe Xing, Yinliang Yue,
  Marie-Francine Moens
conference: Proceedings of the 2024 Conference on Empirical Methods in Natural Language
  Processing
year: 2024
bibkey: tian2024generic
citations: 1
additional_links: [{name: Code, url: 'https://github.com/changtianluckyforever/F-grained-STAR'},
  {name: Paper, url: 'https://arxiv.org/abs/2406.13103'}]
tags: ["EMNLP"]
short_authors: Tian et al.
---
Fine-grained category discovery using only coarse-grained supervision is a
cost-effective yet challenging task. Previous training methods focus on
aligning query samples with positive samples and distancing them from
negatives. They often neglect intra-category and inter-category semantic
similarities of fine-grained categories when navigating sample distributions in
the embedding space. Furthermore, some evaluation techniques that rely on
pre-collected test samples are inadequate for real-time applications. To
address these shortcomings, we introduce a method that successfully detects
fine-grained clusters of semantically similar texts guided by a novel objective
function. The method uses semantic similarities in a logarithmic space to guide
sample distributions in the Euclidean space and to form distinct clusters that
represent fine-grained categories. We also propose a centroid inference
mechanism to support real-time applications. The efficacy of the method is both
theoretically justified and empirically confirmed on three benchmark tasks. The
proposed objective function is integrated in multiple contrastive learning
based neural models. Its results surpass existing state-of-the-art approaches
in terms of Accuracy, Adjusted Rand Index and Normalized Mutual Information of
the detected fine-grained categories. Code and data will be available at Code
and data are publicly available at
https://github.com/changtianluckyforever/F-grained-STAR.