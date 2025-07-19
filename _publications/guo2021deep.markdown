---
layout: publication
title: Deep Kernel Supervised Hashing for Node Classification in Structural Networks
authors: Guo et al.
conference: Information Sciences
year: 2021
bibkey: guo2021deep
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2010.13582'}]
tags: [Supervised, Neural Hashing, Hashing Methods]
---
Node classification in structural networks has been proven to be useful in
many real world applications. With the development of network embedding, the
performance of node classification has been greatly improved. However, nearly
all the existing network embedding based methods are hard to capture the actual
category features of a node because of the linearly inseparable problem in
low-dimensional space; meanwhile they cannot incorporate simultaneously network
structure information and node label information into network embedding. To
address the above problems, in this paper, we propose a novel Deep Kernel
Supervised Hashing (DKSH) method to learn the hashing representations of nodes
for node classification. Specifically, a deep multiple kernel learning is first
proposed to map nodes into suitable Hilbert space to deal with linearly
inseparable problem. Then, instead of only considering structural similarity
between two nodes, a novel similarity matrix is designed to merge both network
structure information and node label information. Supervised by the similarity
matrix, the learned hashing representations of nodes simultaneously preserve
the two kinds of information well from the learned Hilbert space. Extensive
experiments show that the proposed method significantly outperforms the
state-of-the-art baselines over three real world benchmark datasets.