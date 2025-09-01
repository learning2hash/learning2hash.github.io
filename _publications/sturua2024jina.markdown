---
layout: publication
title: 'Jina-embeddings-v3: Multilingual Embeddings With Task Lora'
authors: "Saba Sturua, Isabelle Mohr, Mohammad Kalim Akram, Michael G\xFCnther, Bo\
  \ Wang, Markus Krimmel, Feng Wang, Georgios Mastrapas, Andreas Koukounas, Nan Wang,\
  \ Han Xiao"
conference: Arxiv
year: 2024
bibkey: sturua2024jina
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2409.10173'}]
tags: ["Evaluation", "Text Retrieval"]
short_authors: Sturua et al.
---
We introduce jina-embeddings-v3, a novel text embedding model with 570
million parameters, achieves state-of-the-art performance on multilingual data
and long-context retrieval tasks, supporting context lengths of up to 8192
tokens. The model includes a set of task-specific Low-Rank Adaptation (LoRA)
adapters to generate high-quality embeddings for query-document retrieval,
clustering, classification, and text matching. Evaluation on the MTEB benchmark
shows that jina-embeddings-v3 outperforms the latest proprietary embeddings
from OpenAI and Cohere on English tasks, while achieving superior performance
compared to multilingual-e5-large-instruct across all multilingual tasks. With
a default output dimension of 1024, users can flexibly reduce the embedding
dimensions to as low as 32 without compromising performance, enabled by
Matryoshka Representation Learning.