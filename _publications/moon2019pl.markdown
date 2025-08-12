---
layout: publication
title: 'PL-NMF: Parallel Locality-optimized Non-negative Matrix Factorization'
authors: Gordon E. Moon, Aravind Sukumaran-Rajam, Srinivasan Parthasarathy, P. Sadayappan
conference: Arxiv
year: 2019
bibkey: moon2019pl
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1904.07935'}]
tags: ["Unsupervised"]
short_authors: Moon et al.
---
Non-negative Matrix Factorization (NMF) is a key kernel for unsupervised
dimension reduction used in a wide range of applications, including topic
modeling, recommender systems and bioinformatics. Due to the compute-intensive
nature of applications that must perform repeated NMF, several parallel
implementations have been developed in the past. However, existing parallel NMF
algorithms have not addressed data locality optimizations, which are critical
for high performance since data movement costs greatly exceed the cost of
arithmetic/logic operations on current computer systems. In this paper, we
devise a parallel NMF algorithm based on the HALS (Hierarchical Alternating
Least Squares) scheme that incorporates algorithmic transformations to enhance
data locality. Efficient realizations of the algorithm on multi-core CPUs and
GPUs are developed, demonstrating significant performance improvement over
existing state-of-the-art parallel NMF algorithms.