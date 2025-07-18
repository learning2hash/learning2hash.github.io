---
layout: publication
title: 'SEINE: Segment-based Indexing For Neural Information Retrieval'
authors: Dong Sibo, Goldstein Justin, Yang Grace Hui
conference: International Journal of Computer Science and Information Technology
year: 2023
bibkey: dong2023seine
citations: 13
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2311.15923'}]
tags: [DATASETS, Tools & Libraries, Efficiency And Optimization]
---
Many early neural Information Retrieval (NeurIR) methods are re-rankers that
rely on a traditional first-stage retriever due to expensive query time
computations. Recently, representation-based retrievers have gained much
attention, which learns query representation and document representation
separately, making it possible to pre-compute document representations offline
and reduce the workload at query time. Both dense and sparse
representation-based retrievers have been explored. However, these methods
focus on finding the representation that best represents a text (aka metric
learning) and the actual retrieval function that is responsible for similarity
matching between query and document is kept at a minimum by using dot product.
One drawback is that unlike traditional term-level inverted index, the index
formed by these embeddings cannot be easily re-used by another retrieval
method. Another drawback is that keeping the interaction at minimum hurts
retrieval effectiveness. On the contrary, interaction-based retrievers are
known for their better retrieval effectiveness. In this paper, we propose a
novel SEgment-based Neural Indexing method, SEINE, which provides a general
indexing framework that can flexibly support a variety of interaction-based
neural retrieval methods. We emphasize on a careful decomposition of common
components in existing neural retrieval methods and propose to use
segment-level inverted index to store the atomic query-document interaction
values. Experiments on LETOR MQ2007 and MQ2008 datasets show that our indexing
method can accelerate multiple neural retrieval methods up to 28-times faster
without sacrificing much effectiveness.