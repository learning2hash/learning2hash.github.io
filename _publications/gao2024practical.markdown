---
layout: publication
title: 'Practical And Asymptotically Optimal Quantization Of High-dimensional Vectors In Euclidean Space For Approximate Nearest Neighbor Search'
authors: Jianyang Gao et al.
conference: "Arxiv"
year: 2024
citations: 0
bibkey: gao2024practical
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2409.09913'}
tags: ['Approximate Nearest Neighbor Search', 'Quantization and Compression', 'Tools and Libraries', 'ANN Search', 'Quantization']
---
Approximate nearest neighbor (ANN) query in high-dimensional Euclidean space
is a key operator in database systems. For this query, quantization is a
popular family of methods developed for compressing vectors and reducing memory
consumption. Recently, a method called RaBitQ achieves the state-of-the-art
performance among these methods. It produces better empirical performance in
both accuracy and efficiency when using the same compression rate and provides
rigorous theoretical guarantees. However, the method is only designed for
compressing vectors at high compression rates (32x) and lacks support for
achieving higher accuracy by using more space. In this paper, we introduce a
new quantization method to address this limitation by extending RaBitQ. The new
method inherits the theoretical guarantees of RaBitQ and achieves the
asymptotic optimality in terms of the trade-off between space and error bounds
as to be proven in this study. Additionally, we present efficient
implementations of the method, enabling its application to ANN queries to
reduce both space and time consumption. Extensive experiments on real-world
datasets confirm that our method consistently outperforms the state-of-the-art
baselines in both accuracy and efficiency when using the same amount of memory.
