---
layout: publication
title: 'CSCPR: Cross-source-context Indoor RGB-D Place Recognition'
authors: Jing Liang, Zhuo Deng, Zheming Zhou, Min Sun, Omid Ghasemalizadeh, Cheng-hao
  Kuo, Arnie Sen, Dinesh Manocha
conference: IEEE Robotics and Automation Letters
year: 2025
bibkey: liang2024cscpr
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2407.17457'}]
tags: []
short_authors: Liang et al.
---
We extend our previous work, PoCo, and present a new algorithm,
Cross-Source-Context Place Recognition (CSCPR), for RGB-D indoor place
recognition that integrates global retrieval and reranking into an end-to-end
model and keeps the consistency of using Context-of-Clusters (CoCs) for feature
processing. Unlike prior approaches that primarily focus on the RGB domain for
place recognition reranking, CSCPR is designed to handle the RGB-D data. We
apply the CoCs to handle cross-sourced and cross-scaled RGB-D point clouds and
introduce two novel modules for reranking: the Self-Context Cluster (SCC) and
the Cross Source Context Cluster (CSCC), which enhance feature representation
and match query-database pairs based on local features, respectively. We also
release two new datasets, ScanNetIPR and ARKitIPR. Our experiments demonstrate
that CSCPR significantly outperforms state-of-the-art models on these datasets
by at least 29.27% in Recall@1 on the ScanNet-PR dataset and 43.24% in the new
datasets. Code and datasets will be released.