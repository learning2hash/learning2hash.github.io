---
layout: publication
title: 'Smarter, Better, Faster, Longer: A Modern Bidirectional Encoder For Fast,
  Memory Efficient, And Long Context Finetuning And Inference'
authors: "Benjamin Warner, Antoine Chaffin, Benjamin Clavi\xE9, Orion Weller, Oskar\
  \ Hallstr\xF6m, Said Taghadouini, Alexis Gallagher, Raja Biswas, Faisal Ladhak,\
  \ Tom Aarsen, Nathan Cooper, Griffin Adams, Jeremy Howard, Iacopo Poli"
conference: 'Proceedings of the 63rd Annual Meeting of the Association for Computational
  Linguistics (Volume 1: Long Papers)'
year: 2024
bibkey: warner2024smarter
citations: 48
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.13663'}]
tags: ["Evaluation"]
short_authors: Warner et al.
---
Encoder-only transformer models such as BERT offer a great performance-size
tradeoff for retrieval and classification tasks with respect to larger
decoder-only models. Despite being the workhorse of numerous production
pipelines, there have been limited Pareto improvements to BERT since its
release. In this paper, we introduce ModernBERT, bringing modern model
optimizations to encoder-only models and representing a major Pareto
improvement over older encoders. Trained on 2 trillion tokens with a native
8192 sequence length, ModernBERT models exhibit state-of-the-art results on a
large pool of evaluations encompassing diverse classification tasks and both
single and multi-vector retrieval on different domains (including code). In
addition to strong downstream performance, ModernBERT is also the most speed
and memory efficient encoder and is designed for inference on common GPUs.