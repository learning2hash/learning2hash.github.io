---
layout: publication
title: Making Text Embedders Few-shot Learners
authors: Chaofan Li, Minghao Qin, Shitao Xiao, Jianlyu Chen, Kun Luo, Yingxia Shao,
  Defu Lian, Zheng Liu
conference: Arxiv
year: 2024
bibkey: li2024making
citations: 2
additional_links: [{name: Code, url: 'https://github.com/FlagOpen/FlagEmbedding'},
  {name: Paper, url: 'https://arxiv.org/abs/2409.15700'}]
tags: ["Evaluation", "Few Shot & Zero Shot", "Tools & Libraries"]
short_authors: Li et al.
---
Large language models (LLMs) with decoder-only architectures demonstrate
remarkable in-context learning (ICL) capabilities. This feature enables them to
effectively handle both familiar and novel tasks by utilizing examples provided
within their input context. Recognizing the potential of this capability, we
propose leveraging the ICL feature in LLMs to enhance the process of text
embedding generation. To this end, we introduce a novel model bge-en-icl, which
employs few-shot examples to produce high-quality text embeddings. Our approach
integrates task-related examples directly into the query side, resulting in
significant improvements across various tasks. Additionally, we have
investigated how to effectively utilize LLMs as embedding models, including
various attention mechanisms, pooling methods, etc. Our findings suggest that
retaining the original framework often yields the best results, underscoring
that simplicity is best. Experimental results on the MTEB and AIR-Bench
benchmarks demonstrate that our approach sets new state-of-the-art (SOTA)
performance. Our model, code and dataset are freely available at
https://github.com/FlagOpen/FlagEmbedding .