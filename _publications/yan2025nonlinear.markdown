---
layout: publication
title: A Nonlinear Hash-based Optimization Method For Spmv On Gpus
authors: Chen Yan, Boyu Diao, Hangda Liu, Zhulin An, Yongjun Xu
conference: 2025 IEEE 25th International Symposium on Cluster, Cloud and Internet
  Computing (CCGrid)
year: 2025
bibkey: yan2025nonlinear
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2504.08860'}]
tags: ["Efficiency"]
short_authors: Yan et al.
---
Sparse matrix-vector multiplication (SpMV) is a fundamental operation with a
wide range of applications in scientific computing and artificial intelligence.
However, the large scale and sparsity of sparse matrix often make it a
performance bottleneck. In this paper, we highlight the effectiveness of
hash-based techniques in optimizing sparse matrix reordering, introducing the
Hash-based Partition (HBP) format, a lightweight SpMV approach. HBP retains the
performance benefits of the 2D-partitioning method while leveraging the hash
transformation's ability to group similar elements, thereby accelerating the
pre-processing phase of sparse matrix reordering. Additionally, we achieve
parallel load balancing across matrix blocks through a competitive method. Our
experiments, conducted on both Nvidia Jetson AGX Orin and Nvidia RTX 4090, show
that in the pre-processing step, our method offers an average speedup of 3.53
times compared to the sorting approach and 3.67 times compared to the dynamic
programming method employed in Regu2D. Furthermore, in SpMV, our method
achieves a maximum speedup of 3.32 times on Orin and 3.01 times on RTX4090
against the CSR format in sparse matrices from the University of Florida Sparse
Matrix Collection.