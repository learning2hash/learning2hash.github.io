---
layout: publication
title: 'Rethinking Chunk Size For Long-document Retrieval: A Multi-dataset Analysis'
authors: Sinchana Ramakanth Bhat, Max Rudat, Jannis Spiekermann, Nicolas Flores-Herr
conference: Arxiv
year: 2025
bibkey: bhat2025rethinking
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2505.21700'}]
tags: ["Datasets", "Evaluation", "Text Retrieval"]
short_authors: Bhat et al.
---
Chunking is a crucial preprocessing step in retrieval-augmented generation (RAG) systems, significantly impacting retrieval effectiveness across diverse datasets. In this study, we systematically evaluate fixed-size chunking strategies and their influence on retrieval performance using multiple embedding models. Our experiments, conducted on both short-form and long-form datasets, reveal that chunk size plays a critical role in retrieval effectiveness -- smaller chunks (64-128 tokens) are optimal for datasets with concise, fact-based answers, whereas larger chunks (512-1024 tokens) improve retrieval in datasets requiring broader contextual understanding. We also analyze the impact of chunking on different embedding models, finding that they exhibit distinct chunking sensitivities. While models like Stella benefit from larger chunks, leveraging global context for long-range retrieval, Snowflake performs better with smaller chunks, excelling at fine-grained, entity-based matching. Our results underscore the trade-offs between chunk size, embedding models, and dataset characteristics, emphasizing the need for improved chunk quality measures, and more comprehensive datasets to advance chunk-based retrieval in long-document Information Retrieval (IR).