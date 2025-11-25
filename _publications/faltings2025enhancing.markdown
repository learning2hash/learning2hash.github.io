---
layout: publication
title: Enhancing Retrieval Systems With Inference-time Logical Reasoning
authors: Felix Faltings, Wei Wei, Yujia Bao
conference: 'Proceedings of the 63rd Annual Meeting of the Association for Computational
  Linguistics (Volume 2: Short Papers)'
year: 2025
bibkey: faltings2025enhancing
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2503.17860'}]
tags: ["Efficiency", "Evaluation"]
short_authors: Felix Faltings, Wei Wei, Yujia Bao
---
Traditional retrieval methods rely on transforming user queries into vector
representations and retrieving documents based on cosine similarity within an
embedding space. While efficient and scalable, this approach often fails to
handle complex queries involving logical constructs such as negations,
conjunctions, and disjunctions. In this paper, we propose a novel
inference-time logical reasoning framework that explicitly incorporates logical
reasoning into the retrieval process. Our method extracts logical reasoning
structures from natural language queries and then composes the individual
cosine similarity scores to formulate the final document scores. This approach
enables the retrieval process to handle complex logical reasoning without
compromising computational efficiency. Our results on both synthetic and
real-world benchmarks demonstrate that the proposed method consistently
outperforms traditional retrieval methods across different models and datasets,
significantly improving retrieval performance for complex queries.