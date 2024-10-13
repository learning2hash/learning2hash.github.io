---
layout: publication
title: SPANN Highly-efficient Billion-scale Approximate Nearest Neighborhood Search
authors: Qi Chen, Bing Zhao, Haidong Wang, Mingqin Li, Chuanjie Liu, Zhiyong Zheng, Mao Yang, Jingdong Wang
conference: "Neural Information Processing Systems"
year: 2021
bibkey: chen2021spann
additional_links:
  - {name: "Paper", url: "https://papers.nips.cc/paper/2021/hash/299dc35e747eb77177d9cea10a802da2-Abstract.html"}
  - {name: "Code", url: "https://github.com/microsoft/SPTAG"}
tags: ['Has Code', 'NEURIPS', 'Unsupervised']
---
<p>The in-memory algorithms for approximate nearest neighbor search
(ANNS) have achieved great success for fast high-recall search, but are
extremely expensive when handling very large scale database. Thus, there
is an increasing request for the hybrid ANNS solutions with small memory
and inexpensive solid-state drive (SSD). In this paper, we present a
simple but efficient memory-disk hybrid indexing and search system,
named SPANN, that follows the inverted index methodology. It stores the
centroid points of the posting lists in the memory and the large posting
lists in the disk. We guarantee both disk-access efficiency (low
latency) and high recall by effectively reducing the disk-access number
and retrieving high-quality posting lists. In the index-building stage,
we adopt a hierarchical balanced clustering algorithm to balance the
length of posting lists and augment the posting list by adding the
points in the closure of the corresponding clusters. In the search
stage, we use a query-aware scheme to dynamically prune the access of
unnecessary posting lists. Experiment results demonstrate that SPANN is
2X faster than the state-of-the-art ANNS solution DiskANN to reach the
same recall quality 90% with same memory cost in three billion-scale
datasets. It can reach 90% recall@1 and recall@10 in just around one
millisecond with only 32GB memory cost. Code is available at:
https://github.com/microsoft/SPTAG.</p>
