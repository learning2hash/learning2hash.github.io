---
layout: publication
title: Enhancing Visual Re-ranking Through Denoising Nearest Neighbor Graph Via Continuous
  CRF
authors: Jaeyoon Kim, Yoonki Cho, Taeyoung Kim, Sung-Eui Yoon
conference: Arxiv
year: 2024
bibkey: kim2024enhancing
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.13875'}]
tags: ["Distance Metric Learning", "Evaluation", "Graph Based ANN", "Hybrid ANN Methods", "Re-Ranking"]
short_authors: Kim et al.
---
Nearest neighbor (NN) graph based visual re-ranking has emerged as a powerful approach for improving retrieval accuracy, offering the advantages of effectively exploring high-dimensional manifolds without requiring additional fine-tuning. However, the effectiveness of NN graph-based re-ranking is fundamentally constrained by the quality of its edge connectivity, as incorrect connections between dissimilar (negative) images frequently occur. This is known as a noisy edge problem, which hinders the re-ranking performance of existing techniques and limits their potential. To remedy this issue, we propose a complementary denoising method based on Continuous Conditional Random Fields (C-CRF) that leverages statistical distances derived from similarity-based distributions. As a pre-processing step for enhancing NN graph-based retrieval, our approach constructs fully connected cliques around each anchor image and employs a novel statistical distance metric to robustly alleviate noisy edges before re-ranking while achieving efficient processing through offline computation. Extensive experimental results demonstrate that our method consistently improves three different NN graph-based re-ranking approaches, yielding significant gains in retrieval accuracy.