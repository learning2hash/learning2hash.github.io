---
layout: publication
title: Efficient Approximation Of Earth Mover's Distance Based On Nearest Neighbor
  Search
authors: Meng Guangyu, Zhou Ruyu, Liu Liu, Liang Peixian, Liu Fang, Chen Danny, Niemier
  Michael, Hu X. Sharon
conference: Arxiv
year: 2024
bibkey: meng2024efficient
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2401.07378'}]
tags: ["Distance Metric Learning", "Efficiency", "Memory Efficiency", "Scalability"]
short_authors: Meng et al.
---
Earth Mover's Distance (EMD) is an important similarity measure between two distributions, used in computer vision and many other application domains. However, its exact calculation is computationally and memory intensive, which hinders its scalability and applicability for large-scale problems. Various approximate EMD algorithms have been proposed to reduce computational costs, but they suffer lower accuracy and may require additional memory usage or manual parameter tuning. In this paper, we present a novel approach, NNS-EMD, to approximate EMD using Nearest Neighbor Search (NNS), in order to achieve high accuracy, low time complexity, and high memory efficiency. The NNS operation reduces the number of data points compared in each NNS iteration and offers opportunities for parallel processing. We further accelerate NNS-EMD via vectorization on GPU, which is especially beneficial for large datasets. We compare NNS-EMD with both the exact EMD and state-of-the-art approximate EMD algorithms on image classification and retrieval tasks. We also apply NNS-EMD to calculate transport mapping and realize color transfer between images. NNS-EMD can be 44x to 135x faster than the exact EMD implementation, and achieves superior accuracy, speedup, and memory efficiency over existing approximate EMD methods.