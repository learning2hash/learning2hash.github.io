---
layout: publication
title: 'AH-UGC: Adaptive And Heterogeneous-universal Graph Coarsening'
authors: Mohit Kataria, Shreyash Bhilwade, Sandeep Kumar, Jayadeva
conference: Arxiv
year: 2025
bibkey: kataria2025ah
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2505.15842'}]
tags: ["Hashing Methods", "Locality-Sensitive-Hashing", "Scalability"]
short_authors: Kataria et al.
---
\(\textbf\{Graph Coarsening (GC)\}\) is a prominent graph reduction technique that compresses large graphs to enable efficient learning and inference. However, existing GC methods generate only one coarsened graph per run and must recompute from scratch for each new coarsening ratio, resulting in unnecessary overhead. Moreover, most prior approaches are tailored to \(\textit\{homogeneous\}\) graphs and fail to accommodate the semantic constraints of \(\textit\{heterogeneous\}\) graphs, which comprise multiple node and edge types. To overcome these limitations, we introduce a novel framework that combines Locality Sensitive Hashing (LSH) with Consistent Hashing to enable \(\textit\{adaptive graph coarsening\}\). Leveraging hashing techniques, our method is inherently fast and scalable. For heterogeneous graphs, we propose a \(\textit\{type isolated coarsening\}\) strategy that ensures semantic consistency by restricting merges to nodes of the same type. Our approach is the first unified framework to support both adaptive and heterogeneous coarsening. Extensive evaluations on 23 real-world datasets including homophilic, heterophilic, homogeneous, and heterogeneous graphs demonstrate that our method achieves superior scalability while preserving the structural and semantic integrity of the original graph.