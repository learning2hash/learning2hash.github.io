---
layout: publication
title: A Unified Label-aware Contrastive Learning Framework For Few-shot Named Entity
  Recognition
authors: Haojie Zhang, Yimeng Zhuang
conference: Arxiv
year: 2024
bibkey: zhang2024unified
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2404.17178'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Haojie Zhang, Yimeng Zhuang
---
Few-shot Named Entity Recognition (NER) aims to extract named entities using
only a limited number of labeled examples. Existing contrastive learning
methods often suffer from insufficient distinguishability in context vector
representation because they either solely rely on label semantics or completely
disregard them. To tackle this issue, we propose a unified label-aware
token-level contrastive learning framework. Our approach enriches the context
by utilizing label semantics as suffix prompts. Additionally, it simultaneously
optimizes context-context and context-label contrastive learning objectives to
enhance generalized discriminative contextual representations.Extensive
experiments on various traditional test domains (OntoNotes, CoNLL'03, WNUT'17,
GUM, I2B2) and the large-scale few-shot NER dataset (FEWNERD) demonstrate the
effectiveness of our approach. It outperforms prior state-of-the-art models by
a significant margin, achieving an average absolute gain of 7% in micro F1
scores across most scenarios. Further analysis reveals that our model benefits
from its powerful transfer capability and improved contextual representations.