---
layout: publication
title: Graph-based Multi-view Binary Learning For Image Clustering
authors: Guangqi Jiang, Huibing Wang, Jinjia Peng, Dongyan Chen, Xianping Fu
conference: Neurocomputing
year: 2020
bibkey: jiang2019graph
citations: 28
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1912.05159'}]
tags: ["Compact Codes", "Datasets", "Evaluation", "Graph Based ANN", "Hashing Methods", "Scalability"]
short_authors: Jiang et al.
---
Hashing techniques, also known as binary code learning, have recently gained
increasing attention in large-scale data analysis and storage. Generally, most
existing hash clustering methods are single-view ones, which lack complete
structure or complementary information from multiple views. For cluster tasks,
abundant prior researches mainly focus on learning discrete hash code while few
works take original data structure into consideration. To address these
problems, we propose a novel binary code algorithm for clustering, which adopts
graph embedding to preserve the original data structure, called (Graph-based
Multi-view Binary Learning) GMBL in this paper. GMBL mainly focuses on encoding
the information of multiple views into a compact binary code, which explores
complementary information from multiple views. In particular, in order to
maintain the graph-based structure of the original data, we adopt a Laplacian
matrix to preserve the local linear relationship of the data and map it to the
Hamming space. Considering different views have distinctive contributions to
the final clustering results, GMBL adopts a strategy of automatically assign
weights for each view to better guide the clustering. Finally, An alternating
iterative optimization method is adopted to optimize discrete binary codes
directly instead of relaxing the binary constraint in two steps. Experiments on
five public datasets demonstrate the superiority of our proposed method
compared with previous approaches in terms of clustering performance.