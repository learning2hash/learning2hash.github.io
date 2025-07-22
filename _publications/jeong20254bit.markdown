---
layout: publication
title: 4bit-quantization In Vector-embedding For RAG
authors: Jeong Taehee
conference: Arxiv
year: 2025
bibkey: jeong20254bit
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2501.10534'}]
tags: ["Quantization", "Evaluation"]
short_authors: Jeong Taehee
---
Retrieval-augmented generation (RAG) is a promising technique that has shown
great potential in addressing some of the limitations of large language models
(LLMs). LLMs have two major limitations: they can contain outdated information
due to their training data, and they can generate factually inaccurate
responses, a phenomenon known as hallucinations. RAG aims to mitigate these
issues by leveraging a database of relevant documents, which are stored as
embedding vectors in a high-dimensional space. However, one of the challenges
of using high-dimensional embeddings is that they require a significant amount
of memory to store. This can be a major issue, especially when dealing with
large databases of documents. To alleviate this problem, we propose the use of
4-bit quantization to store the embedding vectors. This involves reducing the
precision of the vectors from 32-bit floating-point numbers to 4-bit integers,
which can significantly reduce the memory requirements. Our approach has
several benefits. Firstly, it significantly reduces the memory storage
requirements of the high-dimensional vector database, making it more feasible
to deploy RAG systems in resource-constrained environments. Secondly, it speeds
up the searching process, as the reduced precision of the vectors allows for
faster computation. Our code is available at
https://github.com/taeheej/4bit-Quantization-in-Vector-Embedding-for-RAG