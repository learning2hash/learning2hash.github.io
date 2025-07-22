---
layout: publication
title: Highly-economized Multi-view Binary Compression For Scalable Image Clustering
authors: Zhang Zheng, Liu Li, Qin Jie, Zhu Fan, Shen Fumin, Xu Yong, Shao Ling, Shen
  Heng Tao
conference: Lecture Notes in Computer Science
year: 2018
bibkey: zhang2018highly
citations: 49
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1809.05992'}]
tags: ["Hashing-Methods", "Distance-Metric-Learning", "Scalability", "Memory-Efficiency", "Tools-&-Libraries", "Datasets"]
short_authors: Zhang et al.
---
How to economically cluster large-scale multi-view images is a long-standing
problem in computer vision. To tackle this challenge, we introduce a novel
approach named Highly-economized Scalable Image Clustering (HSIC) that
radically surpasses conventional image clustering methods via binary
compression. We intuitively unify the binary representation learning and
efficient binary cluster structure learning into a joint framework. In
particular, common binary representations are learned by exploiting both
sharable and individual information across multiple views to capture their
underlying correlations. Meanwhile, cluster assignment with robust binary
centroids is also performed via effective discrete optimization under L21-norm
constraint. By this means, heavy continuous-valued Euclidean distance
computations can be successfully reduced by efficient binary XOR operations
during the clustering procedure. To our best knowledge, HSIC is the first
binary clustering work specifically designed for scalable multi-view image
clustering. Extensive experimental results on four large-scale image datasets
show that HSIC consistently outperforms the state-of-the-art approaches, whilst
significantly reducing computational time and memory footprint.