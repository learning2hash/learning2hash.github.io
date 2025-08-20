---
layout: publication
title: 'Retreever: Tree-based Coarse-to-fine Representations For Retrieval'
authors: Shubham Gupta, Zichao Li, Tianyi Chen, Cem Subakan, Siva Reddy, Perouz Taslakian,
  Valentina Zantedeschi
conference: Arxiv
year: 2025
bibkey: gupta2025retreever
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2502.07971'}]
tags: [Text Retrieval, Tree-based ANN, Scalability, Evaluation, Similarity Search]
short_authors: Gupta et al.
---
Document retrieval is a core component of question-answering systems, as it
enables conditioning answer generation on new and large-scale corpora. While
effective, the standard practice of encoding documents into high-dimensional
embeddings for similarity search entails large memory and compute footprints,
and also makes it hard to inspect the inner workings of the system. In this
paper, we propose a tree-based method for organizing and representing reference
documents at various granular levels, which offers the flexibility to balance
cost and utility, and eases the inspection of the corpus content and retrieval
operations. Our method, called ReTreever, jointly learns a routing function per
internal node of a binary tree such that query and reference documents are
assigned to similar tree branches, hence directly optimizing for retrieval
performance. Our evaluations show that ReTreever generally preserves full
representation accuracy. Its hierarchical structure further provides strong
coarse representations and enhances transparency by indirectly learning
meaningful semantic groupings. Among hierarchical retrieval methods, ReTreever
achieves the best retrieval accuracy at the lowest latency, proving that this
family of techniques can be viable in practical applications.