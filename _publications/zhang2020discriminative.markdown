---
layout: publication
title: Discriminative Nearest Neighbor Few-shot Intent Detection By Transferring Natural
  Language Inference
authors: Jian-Guo Zhang, Kazuma Hashimoto, Wenhao Liu, Chien-Sheng Wu, Yao Wan, Philip
  S. Yu, Richard Socher, Caiming Xiong
conference: Proceedings of the 2020 Conference on Empirical Methods in Natural Language
  Processing (EMNLP)
year: 2020
bibkey: zhang2020discriminative
citations: 65
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2010.13009'}]
tags: ["EMNLP", "Few Shot & Zero Shot", "Scalability"]
short_authors: Zhang et al.
---
Intent detection is one of the core components of goal-oriented dialog
systems, and detecting out-of-scope (OOS) intents is also a practically
important skill. Few-shot learning is attracting much attention to mitigate
data scarcity, but OOS detection becomes even more challenging. In this paper,
we present a simple yet effective approach, discriminative nearest neighbor
classification with deep self-attention. Unlike softmax classifiers, we
leverage BERT-style pairwise encoding to train a binary classifier that
estimates the best matched training example for a user input. We propose to
boost the discriminative ability by transferring a natural language inference
(NLI) model. Our extensive experiments on a large-scale multi-domain intent
detection task show that our method achieves more stable and accurate in-domain
and OOS detection accuracy than RoBERTa-based classifiers and embedding-based
nearest neighbor approaches. More notably, the NLI transfer enables our 10-shot
model to perform competitively with 50-shot or even full-shot classifiers,
while we can keep the inference time constant by leveraging a faster embedding
retrieval model.