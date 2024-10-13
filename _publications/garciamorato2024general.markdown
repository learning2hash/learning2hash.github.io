---
layout: publication
title: A General Framework For Distributed Approximate Similarity Search With Arbitrary Distances
authors: Garcia-morato Elena, Algar Maria Jesus, Alfaro Cesar, Ortega Felipe, Gomez Javier, Moguerza Javier M.
conference: "Arxiv"
year: 2024
bibkey: garciamorato2024general
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2405.13795"}
tags: ['ARXIV', 'Unsupervised']
---
Similarity search is a central problem in domains such as information
management and retrieval or data analysis. Many similarity search algorithms
are designed or specifically adapted to metric distances. Thus, they are
unsuitable for alternatives like the cosine distance, which has become quite
common, for example, with embeddings and in text mining. This paper presents
GDASC (General Distributed Approximate Similarity search with Clustering), a
general framework for distributed approximate similarity search that accepts
arbitrary distances. This framework can build a multilevel index structure, by
selecting a clustering algorithm, the number of prototypes in each cluster and
any arbitrary distance function. As a result, this framework effectively
overcomes the limitation of using metric distances and can address situations
involving cosine similarity or other non-standard similarity measures.
Experimental results using k-medoids clustering in GDASC with real datasets
confirm the applicability of this approach for approximate similarity search,
improving the performance of extant algorithms for this purpose.
