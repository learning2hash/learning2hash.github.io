---
layout: publication
title: 'Repurposing Language Models Into Embedding Models: Finding The Compute-optimal
  Recipe'
authors: "Alicja Ziarko, Albert Q. Jiang, Bartosz Piotrowski, Wenda Li, Mateja Jamnik,\
  \ Piotr Mi\u0142o\u015B"
conference: Advances in Neural Information Processing Systems 37
year: 2024
bibkey: ziarko2024repurposing
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2406.04165'}]
tags: [Text Retrieval, NeurIPS]
short_authors: Ziarko et al.
---
Text embeddings are essential for many tasks, such as document retrieval,
clustering, and semantic similarity assessment. In this paper, we study how to
contrastively train text embedding models in a compute-optimal fashion, given a
suite of pre-trained decoder-only language models. Our innovation is an
algorithm that produces optimal configurations of model sizes, data quantities,
and fine-tuning methods for text-embedding models at different computational
budget levels. The resulting recipe, which we obtain through extensive
experiments, can be used by practitioners to make informed design choices for
their embedding models. Specifically, our findings suggest that full
fine-tuning and low-rank adaptation fine-tuning produce optimal models at lower
and higher computational budgets respectively.