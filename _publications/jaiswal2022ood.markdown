---
layout: publication
title: Ood-diskann Efficient And Scalable Graph ANNS For Out-of-distribution Queries
authors: Jaiswal Shikhar, Krishnaswamy Ravishankar, Garg Ankit, Simhadri Harsha Vardhan, Agrawal Sheshansh
conference: "Arxiv"
year: 2022
bibkey: jaiswal2022ood
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2211.12850"}
tags: ['ARXIV', 'Graph']
---
State-of-the-art algorithms for Approximate Nearest Neighbor Search (ANNS) such as DiskANN, FAISS-IVF, and HNSW build data dependent indices that offer substantially better accuracy and search efficiency over data-agnostic indices by overfitting to the index data distribution. When the query data is drawn from a different distribution - e.g., when index represents image embeddings and query represents textual embeddings - such algorithms lose much of this performance advantage. On a variety of datasets, for a fixed recall target, latency is worse by an order of magnitude or more for Out-Of-Distribution (OOD) queries as compared to In-Distribution (ID) queries. The question we address in this work is whether ANNS algorithms can be made efficient for OOD queries if the index construction is given access to a small sample set of these queries. We answer positively by presenting OOD-DiskANN, which uses a sparing sample (1&#37; of index set size) of OOD queries, and provides up to 40&#37; improvement in mean query latency over SoTA algorithms of a similar memory footprint. OOD-DiskANN is scalable and has the efficiency of graph-based ANNS indices. Some of our contributions can improve query efficiency for ID queries as well.
