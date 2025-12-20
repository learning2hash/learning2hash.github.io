---
layout: publication
title: Compressing Sentence Representation For Semantic Retrieval Via Homomorphic
  Projective Distillation
authors: Xuandong Zhao, Zhiguo Yu, Ming Wu, Lei Li
conference: 'Findings of the Association for Computational Linguistics: ACL 2022'
year: 2022
bibkey: zhao2022compressing
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2203.07687'}]
tags: ["Evaluation", "Memory Efficiency"]
short_authors: Zhao et al.
---
How to learn highly compact yet effective sentence representation?
Pre-trained language models have been effective in many NLP tasks. However,
these models are often huge and produce large sentence embeddings. Moreover,
there is a big performance gap between large and small models. In this paper,
we propose Homomorphic Projective Distillation (HPD) to learn compressed
sentence embeddings. Our method augments a small Transformer encoder model with
learnable projection layers to produce compact representations while mimicking
a large pre-trained language model to retain the sentence representation
quality. We evaluate our method with different model sizes on both semantic
textual similarity (STS) and semantic retrieval (SR) tasks. Experiments show
that our method achieves 2.7-4.5 points performance gain on STS tasks compared
with previous best representations of the same size. In SR tasks, our method
improves retrieval speed (8.2\(\times\)) and memory usage (8.0\(\times\)) compared
with state-of-the-art large models.