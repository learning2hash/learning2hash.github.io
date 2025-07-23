---
layout: publication
title: Efficient Large-scale Approximate Nearest Neighbor Search On The GPU
authors: Wieschollek Patrick, Wang Oliver, Sorkine-hornung Alexander, Lensch Hendrik
  P. A.
conference: 2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2016
bibkey: wieschollek2017efficient
citations: 55
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1702.05911'}]
tags: ["CVPR", "Efficiency", "Hybrid ANN Methods", "Large Scale Search", "Memory Efficiency", "Quantization", "Scalability"]
short_authors: Wieschollek et al.
---
We present a new approach for efficient approximate nearest neighbor (ANN)
search in high dimensional spaces, extending the idea of Product Quantization.
We propose a two-level product and vector quantization tree that reduces the
number of vector comparisons required during tree traversal. Our approach also
includes a novel highly parallelizable re-ranking method for candidate vectors
by efficiently reusing already computed intermediate values. Due to its small
memory footprint during traversal, the method lends itself to an efficient,
parallel GPU implementation. This Product Quantization Tree (PQT) approach
significantly outperforms recent state of the art methods for high dimensional
nearest neighbor queries on standard reference datasets. Ours is the first work
that demonstrates GPU performance superior to CPU performance on high
dimensional, large scale ANN problems in time-critical real-world applications,
like loop-closing in videos.