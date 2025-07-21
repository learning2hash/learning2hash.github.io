---
layout: publication
title: 'Quari: Query Adaptive Retrieval Improvement'
authors: Xing et al.
conference: Journal of Systems and Software
year: 2025
bibkey: xing2025quari
citations: 15
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2505.21647'}]
---
Massive-scale pretraining has made vision-language models increasingly popular for image-to-image and text-to-image retrieval across a broad collection of domains. However, these models do not perform well when used for challenging retrieval tasks, such as instance retrieval in very large-scale image collections. Recent work has shown that linear transformations of VLM features trained for instance retrieval can improve performance by emphasizing subspaces that relate to the domain of interest. In this paper, we explore a more extreme version of this specialization by learning to map a given query to a query-specific feature space transformation. Because this transformation is linear, it can be applied with minimal computational cost to millions of image embeddings, making it effective for large-scale retrieval or re-ranking. Results show that this method consistently outperforms state-of-the-art alternatives, including those that require many orders of magnitude more computation at query time.