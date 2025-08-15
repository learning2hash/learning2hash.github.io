---
layout: publication
title: 'Sketchne: Embedding Billion-scale Networks Accurately In One Hour'
authors: Yuyang Xie, Yuxiao Dong, Jiezhong Qiu, Wenjian Yu, Xu Feng, Jie Tang
conference: IEEE Transactions on Knowledge and Data Engineering
year: 2023
bibkey: xie2023sketchne
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2110.12782'}]
tags: ["Datasets", "Efficiency", "Scalability"]
short_authors: Xie et al.
---
We study large-scale network embedding with the goal of generating
high-quality embeddings for networks with more than 1 billion vertices and 100
billion edges. Recent attempts LightNE and NetSMF propose to sparsify and
factorize the (dense) NetMF matrix for embedding large networks, where NetMF is
a theoretically-grounded network embedding method. However, there is a
trade-off between their embeddings' quality and scalability due to their
expensive memory requirements, making embeddings less effective under
real-world memory constraints. Therefore, we present the SketchNE model, a
scalable, effective, and memory-efficient network embedding solution developed
for a single machine with CPU only. The main idea of SketchNE is to avoid the
explicit construction and factorization of the NetMF matrix either sparsely or
densely when producing the embeddings through the proposed sparse-sign
randomized single-pass SVD algorithm. We conduct extensive experiments on nine
datasets of various sizes for vertex classification and link prediction,
demonstrating the consistent outperformance of SketchNE over state-of-the-art
baselines in terms of both effectiveness and efficiency. SketchNE costs only
1.0 hours to embed the Hyperlink2012 network with 3.5 billion vertices and 225
billion edges on a CPU-only single machine with embedding superiority (e.g., a
282% relative HITS@10 gain over LightNE).