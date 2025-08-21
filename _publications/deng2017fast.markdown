---
layout: publication
title: Fast K-means Based On KNN Graph
authors: Cheng-Hao Deng, Wan-Lei Zhao
conference: Arxiv
year: 2017
bibkey: deng2017fast
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1705.01813'}]
tags: ["Scalability"]
short_authors: Cheng-Hao Deng, Wan-Lei Zhao
---
In the era of big data, k-means clustering has been widely adopted as a basic
processing tool in various contexts. However, its computational cost could be
prohibitively high as the data size and the cluster number are large. It is
well known that the processing bottleneck of k-means lies in the operation of
seeking closest centroid in each iteration. In this paper, a novel solution
towards the scalability issue of k-means is presented. In the proposal, k-means
is supported by an approximate k-nearest neighbors graph. In the k-means
iteration, each data sample is only compared to clusters that its nearest
neighbors reside. Since the number of nearest neighbors we consider is much
less than k, the processing cost in this step becomes minor and irrelevant to
k. The processing bottleneck is therefore overcome. The most interesting thing
is that k-nearest neighbor graph is constructed by iteratively calling the fast
\(k\)-means itself. Comparing with existing fast k-means variants, the proposed
algorithm achieves hundreds to thousands times speed-up while maintaining high
clustering quality. As it is tested on 10 million 512-dimensional data, it
takes only 5.2 hours to produce 1 million clusters. In contrast, to fulfill the
same scale of clustering, it would take 3 years for traditional k-means.