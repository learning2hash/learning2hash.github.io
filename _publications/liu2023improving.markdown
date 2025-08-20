---
layout: publication
title: Improving Deep Representation Learning Via Auxiliary Learnable Target Coding
authors: Kangjun Liu, Ke Chen, Kui Jia, Yaowei Wang
conference: Pattern Recognition
year: 2024
bibkey: liu2023improving
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2305.18680'}]
tags: [Distance Metric Learning, CVPR]
short_authors: Liu et al.
---
Deep representation learning is a subfield of machine learning that focuses
on learning meaningful and useful representations of data through deep neural
networks. However, existing methods for semantic classification typically
employ pre-defined target codes such as the one-hot and the Hadamard codes,
which can either fail or be less flexible to model inter-class correlation. In
light of this, this paper introduces a novel learnable target coding as an
auxiliary regularization of deep representation learning, which can not only
incorporate latent dependency across classes but also impose geometric
properties of target codes into representation space. Specifically, a
margin-based triplet loss and a correlation consistency loss on the proposed
target codes are designed to encourage more discriminative representations
owing to enlarging between-class margins in representation space and favoring
equal semantic correlation of learnable target codes respectively. Experimental
results on several popular visual classification and retrieval benchmarks can
demonstrate the effectiveness of our method on improving representation
learning, especially for imbalanced data. Source codes are made publicly
available at
\href\{https://github.com/AkonLau/LTC\}\{https://github.com/AkonLau/LTC\}.