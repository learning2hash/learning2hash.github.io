---
layout: publication
title: Deep Lifelong Cross-modal Hashing
authors: Liming Xu, Hanqi Li, Bochuan Zheng, Weisheng Li, Jiancheng Lv
conference: IEEE Transactions on Circuits and Systems for Video Technology
year: 2024
bibkey: xu2023deep
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2304.13357'}]
tags: ["Datasets", "Evaluation", "Hashing Methods", "Memory Efficiency", "Multimodal Retrieval", "Neural Hashing", "Scalability"]
short_authors: Xu et al.
---
Hashing methods have made significant progress in cross-modal retrieval tasks
with fast query speed and low storage cost. Among them, deep learning-based
hashing achieves better performance on large-scale data due to its excellent
extraction and representation ability for nonlinear heterogeneous features.
However, there are still two main challenges in catastrophic forgetting when
data with new categories arrive continuously, and time-consuming for
non-continuous hashing retrieval to retrain for updating. To this end, we, in
this paper, propose a novel deep lifelong cross-modal hashing to achieve
lifelong hashing retrieval instead of re-training hash function repeatedly when
new data arrive. Specifically, we design lifelong learning strategy to update
hash functions by directly training the incremental data instead of retraining
new hash functions using all the accumulated data, which significantly reduce
training time. Then, we propose lifelong hashing loss to enable original hash
codes participate in lifelong learning but remain invariant, and further
preserve the similarity and dis-similarity among original and incremental hash
codes to maintain performance. Additionally, considering distribution
heterogeneity when new data arriving continuously, we introduce multi-label
semantic similarity to supervise hash learning, and it has been proven that the
similarity improves performance with detailed analysis. Experimental results on
benchmark datasets show that the proposed methods achieves comparative
performance comparing with recent state-of-the-art cross-modal hashing methods,
and it yields substantial average increments over 20% in retrieval accuracy
and almost reduces over 80% training time when new data arrives continuously.