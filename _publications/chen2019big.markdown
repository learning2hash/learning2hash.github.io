---
layout: publication
title: 'Big-data Clustering: K-means Or K-indicators?'
authors: Feiyu Chen, Yuchen Yang, Liwei Xu, Taiping Zhang, Yin Zhang
conference: Arxiv
year: 2019
bibkey: chen2019big
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1906.00938'}]
tags: ["Scalability"]
short_authors: Chen et al.
---
The K-means algorithm is arguably the most popular data clustering method,
commonly applied to processed datasets in some "feature spaces", as is in
spectral clustering. Highly sensitive to initializations, however, K-means
encounters a scalability bottleneck with respect to the number of clusters K as
this number grows in big data applications. In this work, we promote a closely
related model called K-indicators model and construct an efficient,
semi-convex-relaxation algorithm that requires no randomized initializations.
We present extensive empirical results to show advantages of the new algorithm
when K is large. In particular, using the new algorithm to start the K-means
algorithm, without any replication, can significantly outperform the standard
K-means with a large number of currently state-of-the-art random replications.