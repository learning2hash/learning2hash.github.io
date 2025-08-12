---
layout: publication
title: Robust Clustering Using Hyperdimensional Computing
authors: Lulu Ge, Keshab K. Parhi
conference: IEEE Open Journal of Circuits and Systems
year: 2024
bibkey: ge2023robust
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2312.02407'}]
tags: []
short_authors: Lulu Ge, Keshab K. Parhi
---
This paper addresses the clustering of data in the hyperdimensional computing
(HDC) domain. In prior work, an HDC-based clustering framework, referred to as
HDCluster, has been proposed. However, the performance of the existing
HDCluster is not robust. The performance of HDCluster is degraded as the
hypervectors for the clusters are chosen at random during the initialization
step. To overcome this bottleneck, we assign the initial cluster hypervectors
by exploring the similarity of the encoded data, referred to as \textit\{query\}
hypervectors. Intra-cluster hypervectors have a higher similarity than
inter-cluster hypervectors. Harnessing the similarity results among query
hypervectors, this paper proposes four HDC-based clustering algorithms:
similarity-based k-means, equal bin-width histogram, equal bin-height
histogram, and similarity-based affinity propagation. Experimental results
illustrate that: (i) Compared to the existing HDCluster, our proposed HDC-based
clustering algorithms can achieve better accuracy, more robust performance,
fewer iterations, and less execution time. Similarity-based affinity
propagation outperforms the other three HDC-based clustering algorithms on
eight datasets by 2~38% in clustering accuracy. (ii) Even for one-pass
clustering, i.e., without any iterative update of the cluster hypervectors, our
proposed algorithms can provide more robust clustering accuracy than HDCluster.
(iii) Over eight datasets, five out of eight can achieve higher or comparable
accuracy when projected onto the hyperdimensional space. Traditional clustering
is more desirable than HDC when the number of clusters, \\(k\\), is large.