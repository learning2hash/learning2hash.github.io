---
layout: publication
title: 'OASIS: Order-augmented Strategy For Improved Code Search'
authors: Zuchen Gao, Zizheng Zhan, Xianming Li, Erxin Yu, Haotian Zhang, Bin Chen,
  Yuqun Zhang, Jing Li
conference: 'Proceedings of the 63rd Annual Meeting of the Association for Computational
  Linguistics (Volume 1: Long Papers)'
year: 2025
bibkey: gao2025oasis
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2503.08161'}]
tags: ["Evaluation"]
short_authors: Gao et al.
---
Code embeddings capture the semantic representations of code and are crucial
for various code-related large language model (LLM) applications, such as code
search. Previous training primarily relies on optimizing the InfoNCE loss by
comparing positive natural language (NL)-code pairs with in-batch negatives.
However, due to the sparse nature of code contexts, training solely by
comparing the major differences between positive and negative pairs may fail to
capture deeper semantic nuances. To address this issue, we propose a novel
order-augmented strategy for improved code search (OASIS). It leverages
order-based similarity labels to train models to capture subtle differences in
similarity among negative pairs. Extensive benchmark evaluations demonstrate
that our OASIS model significantly outperforms previous state-of-the-art models
focusing solely on major positive-negative differences. It underscores the
value of exploiting subtle differences among negative pairs with order labels
for effective code embedding training.