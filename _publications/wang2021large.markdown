---
layout: publication
title: Large-scale Approximate K-nn Graph Construction On GPU
authors: Hui Wang, Wan-Lei Zhao, Xiangxiang Zeng
conference: Arxiv
year: 2021
bibkey: wang2021large
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2103.15386'}]
tags: ["Graph Based ANN", "Scalability"]
short_authors: Hui Wang, Wan-Lei Zhao, Xiangxiang Zeng
---
k-nearest neighbor graph is a key data structure in many disciplines such as
manifold learning, machine learning and information retrieval, etc. NN-Descent
was proposed as an effective solution for the graph construction problem.
However, it cannot be directly transplanted to GPU due to the intensive memory
accesses required in the approach. In this paper, NN-Descent has been
redesigned to adapt to the GPU architecture. In particular, the number of
memory accesses has been reduced significantly. The redesign fully exploits the
parallelism of the GPU hardware. In the meantime, the genericness as well as
the simplicity of NN-Descent are well-preserved. In addition, a simple but
effective k-NN graph merge approach is presented. It allows two graphs to be
merged efficiently on GPUs. More importantly, it makes the construction of
high-quality k-NN graphs for out-of-GPU-memory datasets tractable. The results
show that our approach is 100-250x faster than single-thread NN-Descent and is
2.5-5x faster than existing GPU-based approaches.