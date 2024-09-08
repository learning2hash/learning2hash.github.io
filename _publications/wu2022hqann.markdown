---
layout: publication
title: HQANN: Efficient and Robust Similarity Search for Hybrid Queries with Structured and Unstructured Constraints
authors: Wu Wei, He Junlin, Qiao Yu, Fu Guoheng, Liu Li, Yu Jin
conference: Arxiv
year: 2022
bibkey: wu2022hqann
additional_links:
   - {name: "License", url: "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/2207.07940"}
tags: ['Arxiv', 'Graph']
---
The in-memory approximate nearest neighbor search (ANNS) algorithms have achieved great success for fast high-recall query processing, but are extremely inefficient when handling hybrid queries with unstructured (i.e., feature vectors) and structured (i.e., related attributes) constraints. In this paper, we present HQANN, a simple yet highly efficient hybrid query processing framework which can be easily embedded into existing proximity graph-based ANNS algorithms. We guarantee both low latency and high recall by leveraging navigation sense among attributes and fusing vector similarity search with attribute filtering. Experimental results on both public and in-house datasets demonstrate that HQANN is 10x faster than the state-of-the-art hybrid ANNS solutions to reach the same recall quality and its performance is hardly affected by the complexity of attributes. It can reach 99\% recall@10 in just around 50 microseconds On GLOVE-1.2M with thousands of attribute constraints.
