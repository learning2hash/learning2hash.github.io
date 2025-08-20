---
layout: publication
title: 'PECANN: Parallel Efficient Clustering With Graph-based Approximate Nearest
  Neighbor Search'
authors: Shangdi Yu, Joshua Engels, Yihao Huang, Julian Shun
conference: Arxiv
year: 2023
bibkey: yu2023pecann
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2312.03940'}]
tags: [Tools & Libraries, Datasets, Graph-based ANN]
short_authors: Yu et al.
---
This paper studies density-based clustering of point sets. These methods use dense regions of points to detect clusters of arbitrary shapes. In particular, we study variants of density peaks clustering, a popular type of algorithm that has been shown to work well in practice. Our goal is to cluster large high-dimensional datasets, which are prevalent in practice. Prior solutions are either sequential, and cannot scale to large data, or are specialized for low-dimensional data.
  This paper unifies the different variants of density peaks clustering into a single framework, PECANN, by abstracting out several key steps common to this class of algorithms. One such key step is to find nearest neighbors that satisfy a predicate function, and one of the main contributions of this paper is an efficient way to do this predicate search using graph-based approximate nearest neighbor search (ANNS). To provide ample parallelism, we propose a doubling search technique that enables points to find an approximate nearest neighbor satisfying the predicate in a small number of rounds. Our technique can be applied to many existing graph-based ANNS algorithms, which can all be plugged into PECANN.
  We implement five clustering algorithms with PECANN and evaluate them on synthetic and real-world datasets with up to 1.28 million points and up to 1024 dimensions on a 30-core machine with two-way hyper-threading. Compared to the state-of-the-art FASTDP algorithm for high-dimensional density peaks clustering, which is sequential, our best algorithm is 45x-734x faster while achieving competitive ARI scores. Compared to the state-of-the-art parallel DPC-based algorithm, which is optimized for low dimensions, we show that PECANN is two orders of magnitude faster. As far as we know, our work is the first to evaluate DPC variants on large high-dimensional real-world image and text embedding datasets.