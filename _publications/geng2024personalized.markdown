---
layout: publication
title: Personalized Clustering Via Targeted Representation Learning
authors: Xiwen Geng, Suyun Zhao, Yixin Yu, Borui Peng, Pan Du, Hong Chen, Cuiping
  Li, Mengdie Wang
conference: Geng X. Zhao S. Yu Y. Peng B. Du P. Chen H. Li C. Wang M. (2025). Personalized
  Clustering via Targeted Representation Learning. Proceedings of the AAAI Conference
  on Artificial Intelligence 39(16) 16790-16798
year: 2024
bibkey: geng2024personalized
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.13690'}]
tags: ["Distance Metric Learning"]
short_authors: Geng et al.
---
Clustering traditionally aims to reveal a natural grouping structure within unlabeled data. However, this structure may not always align with users' preferences. In this paper, we propose a personalized clustering method that explicitly performs targeted representation learning by interacting with users via modicum task information (e.g., \(\textit\{must-link\}\) or \(\textit\{cannot-link\}\) pairs) to guide the clustering direction. We query users with the most informative pairs, i.e., those pairs most hard to cluster and those most easy to miscluster, to facilitate the representation learning in terms of the clustering preference. Moreover, by exploiting attention mechanism, the targeted representation is learned and augmented. By leveraging the targeted representation and constrained contrastive loss as well, personalized clustering is obtained. Theoretically, we verify that the risk of personalized clustering is tightly bounded, guaranteeing that active queries to users do mitigate the clustering risk. Experimentally, extensive results show that our method performs well across different clustering tasks and datasets, even when only a limited number of queries are available.