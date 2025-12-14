---
layout: publication
title: The Faiss Library
authors: "Matthijs Douze, Alexandr Guzhva, Chengqi Deng, Jeff Johnson, Gergely Szilvasy,\
  \ Pierre-Emmanuel Mazar\xE9, Maria Lomeli, Lucas Hosseini, Herv\xE9 J\xE9gou"
conference: Arxiv
year: 2024
bibkey: douze2024the
citations: 43
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2401.08281'}]
tags: [Evaluation, Tools & Libraries, Similarity Search]
short_authors: Douze et al.
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