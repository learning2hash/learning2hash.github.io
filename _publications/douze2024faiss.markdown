---
layout: publication
title: The Faiss Library
authors: Matthijs Douze et al.
conference: Arxiv
year: 2024
citations: 15
bibkey: douze2024faiss
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2401.08281'}]
tags: [Applications, Indexing, Evaluation Metrics, Tools and Libraries]
---
Vector databases typically manage large collections of embedding vectors.
Currently, AI applications are growing rapidly, and so is the number of
embeddings that need to be stored and indexed. The Faiss library is dedicated
to vector similarity search, a core functionality of vector databases. Faiss is
a toolkit of indexing methods and related primitives used to search, cluster,
compress and transform vectors. This paper describes the trade-off space of
vector search and the design principles of Faiss in terms of structure,
approach to optimization and interfacing. We benchmark key features of the
library and discuss a few selected applications to highlight its broad
applicability.