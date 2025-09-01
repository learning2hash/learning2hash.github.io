---
layout: publication
title: Knn Hashing With Factorized Neighborhood Representation
authors: Kun Ding, Huo, Fan, Pan
conference: 2015 IEEE International Conference on Computer Vision (ICCV)
year: 2015
bibkey: ding2025knn
citations: 14
additional_links: [{name: Paper, url: 'http://www.cv-foundation.org/openaccess/content_iccv_2015/papers/Ding_kNN_Hashing_With_ICCV_2015_paper.pdf'}]
tags: ["Evaluation", "Hashing Methods", "ICCV", "Memory Efficiency", "Supervised"]
short_authors: Ding et al.
---
Hashing is very effective for many tasks in reducing the
processing time and in compressing massive databases. Although lots of approaches have been developed to learn
data-dependent hash functions in recent years, how to learn
hash functions to yield good performance with acceptable
computational and memory cost is still a challenging problem. Based on the observation that retrieval precision is
highly related to the kNN classification accuracy, this paper
proposes a novel kNN-based supervised hashing method,
which learns hash functions by directly maximizing the kNN
accuracy of the Hamming-embedded training data. To make
it scalable well to large problem, we propose a factorized
neighborhood representation to parsimoniously model the
neighborhood relationships inherent in training data. Considering that real-world data are often linearly inseparable,
we further kernelize this basic model to improve its performance. As a result, the proposed method is able to learn
accurate hashing functions with tolerable computation and
storage cost. Experiments on four benchmarks demonstrate
that our method outperforms the state-of-the-arts.