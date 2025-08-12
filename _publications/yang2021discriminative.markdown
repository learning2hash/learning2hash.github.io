---
layout: publication
title: Discriminative Similarity For Data Clustering
authors: Yingzhen Yang, Ping Li
conference: Arxiv
year: 2021
bibkey: yang2021discriminative
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2109.08675'}]
tags: ["Unsupervised"]
short_authors: Yingzhen Yang, Ping Li
---
Similarity-based clustering methods separate data into clusters according to
the pairwise similarity between the data, and the pairwise similarity is
crucial for their performance. In this paper, we propose \{\em Clustering by
Discriminative Similarity (CDS)\}, a novel method which learns discriminative
similarity for data clustering. CDS learns an unsupervised similarity-based
classifier from each data partition, and searches for the optimal partition of
the data by minimizing the generalization error of the learnt classifiers
associated with the data partitions. By generalization analysis via Rademacher
complexity, the generalization error bound for the unsupervised
similarity-based classifier is expressed as the sum of discriminative
similarity between the data from different classes. It is proved that the
derived discriminative similarity can also be induced by the integrated squared
error bound for kernel density classification. In order to evaluate the
performance of the proposed discriminative similarity, we propose a new
clustering method using a kernel as the similarity function, CDS via
unsupervised kernel classification (CDSK), with its effectiveness demonstrated
by experimental results.