---
layout: publication
title: Compact Token Representations With Contextual Quantization For Efficient Document
  Re-ranking
authors: Yang Yingrui, Qiao Yifan, Yang Tao
conference: 'Proceedings of the 60th Annual Meeting of the Association for Computational
  Linguistics (Volume 1: Long Papers)'
year: 2022
bibkey: yang2022compact
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2203.15328'}]
tags: ["Efficiency", "Quantization", "Hybrid-Ann-Methods", "Evaluation", "Re-Ranking"]
short_authors: Yang Yingrui, Qiao Yifan, Yang Tao
---
Transformer based re-ranking models can achieve high search relevance through
context-aware soft matching of query tokens with document tokens. To alleviate
runtime complexity of such inference, previous work has adopted a late
interaction architecture with pre-computed contextual token representations at
the cost of a large online storage. This paper proposes contextual quantization
of token embeddings by decoupling document-specific and document-independent
ranking contributions during codebook-based compression. This allows effective
online decompression and embedding composition for better search relevance.
This paper presents an evaluation of the above compact token representation
model in terms of relevance and space efficiency.