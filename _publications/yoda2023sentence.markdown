---
layout: publication
title: Sentence Representations Via Gaussian Embedding
authors: Shohei Yoda, Hayato Tsukagoshi, Ryohei Sasano, Koichi Takeda
conference: Arxiv
year: 2023
bibkey: yoda2023sentence
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2305.12990'}]
tags: ["Evaluation", "Self-Supervised", "Tools & Libraries"]
short_authors: Yoda et al.
---
Recent progress in sentence embedding, which represents the meaning of a
sentence as a point in a vector space, has achieved high performance on tasks
such as a semantic textual similarity (STS) task. However, sentence
representations as a point in a vector space can express only a part of the
diverse information that sentences have, such as asymmetrical relationships
between sentences. This paper proposes GaussCSE, a Gaussian distribution-based
contrastive learning framework for sentence embedding that can handle
asymmetric relationships between sentences, along with a similarity measure for
identifying inclusion relations. Our experiments show that GaussCSE achieves
the same performance as previous methods in natural language inference tasks,
and is able to estimate the direction of entailment relations, which is
difficult with point representations.