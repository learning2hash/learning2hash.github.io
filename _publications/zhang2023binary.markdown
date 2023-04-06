---
layout: publication
title: "Binary Code Ranking with Weighted Hamming Distance"
authors: Lei Zhang, Yongdong Zhang, Jinhui Tang, Ke Lu, Qi Tian
conference: CVPR
year: 2013
bibkey: zhang2023binary
additional_links:
   - {name: "PDF", url: "https://openaccess.thecvf.com/content_cvpr_2013/papers/Zhang_Binary_Code_Ranking_2013_CVPR_paper.pdf"}
tags: ["CVPR", "Unsupervised"]
---
Binary hashing has been widely used for efficient similarity search due to its query and storage efficiency. In most
existing binary hashing methods, the high-dimensional data are embedded into Hamming space and the distance or
similarity of two points are approximated by the Hamming
distance between their binary codes. The Hamming distance calculation is efficient, however, in practice, there are
often lots of results sharing the same Hamming distance to
a query, which makes this distance measure ambiguous and
poses a critical issue for similarity search where ranking is
important. In this paper, we propose a weighted Hamming
distance ranking algorithm (WhRank) to rank the binary
codes of hashing methods. By assigning different bit-level
weights to different hash bits, the returned binary codes
are ranked at a finer-grained binary code level. We give
an algorithm to learn the data-adaptive and query-sensitive
weight for each hash bit. Evaluations on two large-scale
image data sets demonstrate the efficacy of our weighted
Hamming distance for binary code ranking.
