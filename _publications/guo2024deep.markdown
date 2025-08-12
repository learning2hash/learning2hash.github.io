---
layout: publication
title: Deep Spectral Clustering Via Joint Spectral Embedding And Kmeans
authors: Wengang Guo, Wei Ye
conference: 2024 IEEE International Conference on Systems, Man, and Cybernetics (SMC)
year: 2024
bibkey: guo2024deep
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.11080'}]
tags: []
short_authors: Wengang Guo, Wei Ye
---
Spectral clustering is a popular clustering method. It first maps data into
the spectral embedding space and then uses Kmeans to find clusters. However,
the two decoupled steps prohibit joint optimization for the optimal solution.
In addition, it needs to construct the similarity graph for samples, which
suffers from the curse of dimensionality when the data are high-dimensional. To
address these two challenges, we introduce \textbf\{D\}eep \textbf\{S\}pectral
\textbf\{C\}lustering (\textbf\{DSC\}), which consists of two main modules: the
spectral embedding module and the greedy Kmeans module. The former module
learns to efficiently embed raw samples into the spectral embedding space using
deep neural networks and power iteration. The latter module improves the
cluster structures of Kmeans on the learned spectral embeddings by a greedy
optimization strategy, which iteratively reveals the direction of the worst
cluster structures and optimizes embeddings in this direction. To jointly
optimize spectral embeddings and clustering, we seamlessly integrate the two
modules and optimize them in an end-to-end manner. Experimental results on
seven real-world datasets demonstrate that DSC achieves state-of-the-art
clustering performance.