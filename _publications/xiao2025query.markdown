---
layout: publication
title: Query-based Adaptive Aggregation For Multi-dataset Joint Training Toward Universal
  Visual Place Recognition
authors: Jiuhong Xiao, Yang Zhou, Giuseppe Loianno
conference: Arxiv
year: 2025
bibkey: xiao2025query
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2507.03831'}]
tags: [Scalability, Evaluation, Datasets, Neural Hashing]
short_authors: Jiuhong Xiao, Yang Zhou, Giuseppe Loianno
---
Deep learning methods for Visual Place Recognition (VPR) have advanced significantly, largely driven by large-scale datasets. However, most existing approaches are trained on a single dataset, which can introduce dataset-specific inductive biases and limit model generalization. While multi-dataset joint training offers a promising solution for developing universal VPR models, divergences among training datasets can saturate limited information capacity in feature aggregation layers, leading to suboptimal performance. To address these challenges, we propose Query-based Adaptive Aggregation (QAA), a novel feature aggregation technique that leverages learned queries as reference codebooks to effectively enhance information capacity without significant computational or parameter complexity. We show that computing the Cross-query Similarity (CS) between query-level image features and reference codebooks provides a simple yet effective way to generate robust descriptors. Our results demonstrate that QAA outperforms state-of-the-art models, achieving balanced generalization across diverse datasets while maintaining peak performance comparable to dataset-specific models. Ablation studies further explore QAA's mechanisms and scalability. Visualizations reveal that the learned queries exhibit diverse attention patterns across datasets. Code will be publicly released.