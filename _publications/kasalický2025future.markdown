---
layout: publication
title: 'The Future Is Sparse: Embedding Compression For Scalable Retrieval In Recommender
  Systems'
authors: "Kasalick\xFD et al."
conference: ACM Computing Surveys
year: 2025
bibkey: "kasalick\xFD2025future"
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2505.11388'}]
tags: ["Large-Scale-Search", "Survey-Paper", "Recommender-Systems"]
---
Industry-scale recommender systems face a core challenge: representing entities with high cardinality, such as users or items, using dense embeddings that must be accessible during both training and inference. However, as embedding sizes grow, memory constraints make storage and access increasingly difficult. We describe a lightweight, learnable embedding compression technique that projects dense embeddings into a high-dimensional, sparsely activated space. Designed for retrieval tasks, our method reduces memory requirements while preserving retrieval performance, enabling scalable deployment under strict resource constraints. Our results demonstrate that leveraging sparsity is a promising approach for improving the efficiency of large-scale recommenders. We release our code at https://github.com/recombee/CompresSAE.