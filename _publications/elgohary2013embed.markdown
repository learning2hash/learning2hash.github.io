---
layout: publication
title: "Embed and Conquer: Scalable Embeddings for Kernel k-Means on MapReduce"
authors: Elgohary Ahmed, Farahat Ahmed K., Kamel Mohamed S., Karray Fakhri
conference: Arxiv
year: 2013
bibkey: elgohary2013embed
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1311.2334"}
tags: ['ARXIV']
---
The kernel $k$-means is an effective method for data clustering which extends the commonly-used $k$-means algorithm to work on a similarity matrix over complex data structures. The kernel $k$-means algorithm is however computationally very complex as it requires the complete data matrix to be calculated and stored. Further, the kernelized nature of the kernel $k$-means algorithm hinders the parallelization of its computations on modern infrastructures for distributed computing. In this paper, we are defining a family of kernel-based low-dimensional embeddings that allows for scaling kernel $k$-means on MapReduce via an efficient and unified parallelization strategy. Afterwards, we propose two methods for low-dimensional embedding that adhere to our definition of the embedding family. Exploiting the proposed parallelization strategy, we present two scalable MapReduce algorithms for kernel $k$-means. We demonstrate the effectiveness and efficiency of the proposed algorithms through an empirical evaluation on benchmark data sets.