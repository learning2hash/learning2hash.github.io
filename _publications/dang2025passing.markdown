---
layout: publication
title: 'Passing The Baton: High Throughput Distributed Disk-based Vector Search With
  Batann'
authors: Nam Anh Dang, Ben Landrum, Ken Birman
conference: Arxiv
year: 2025
bibkey: dang2025passing
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2512.09331'}]
tags: ["Datasets", "Efficiency", "Evaluation"]
short_authors: Nam Anh Dang, Ben Landrum, Ken Birman
---
Vector search underpins modern information-retrieval systems, including retrieval-augmented generation (RAG) pipelines and search engines over unstructured text and images. As datasets scale to billions of vectors, disk-based vector search has emerged as a practical solution. However, looking to the future, we need to anticipate datasets too large for any single server. We present BatANN, a distributed disk-based approximate nearest neighbor (ANN) system that retains the logarithmic search efficiency of a single global graph while achieving near-linear throughput scaling in the number of servers. Our core innovation is that when accessing a neighborhood which is stored on another machine, we send the full state of the query to the other machine to continue executing there for improved locality. On 100M- and 1B-point datasets at 0.95 recall using 10 servers, BatANN achieves 6.21-6.49x and 2.5-5.10x the throughput of the scatter-gather baseline, respectively, while maintaining mean latency below 6 ms. Moreover, we get these results on standard TCP. To our knowledge, BatANN is the first open-source distributed disk-based vector search system to operate over a single global graph.