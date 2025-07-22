---
layout: publication
title: Shared Predictive Cross-Modal Deep Quantization
authors: Yang Erkun, Deng Cheng, Li Chao, Liu Wei, Li Jie, Tao Dacheng
conference: IEEE Transactions on Neural Networks and Learning Systems
year: 2018
bibkey: yang2019shared
citations: 151
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1904.07488'}]
tags: ["Similarity-Search", "Supervised", "Hashing-Methods", "Compact-Codes", "Quantization"]
short_authors: Yang et al.
---
With explosive growth of data volume and ever-increasing diversity of data
modalities, cross-modal similarity search, which conducts nearest neighbor
search across different modalities, has been attracting increasing interest.
This paper presents a deep compact code learning solution for efficient
cross-modal similarity search. Many recent studies have proven that
quantization-based approaches perform generally better than hashing-based
approaches on single-modal similarity search. In this paper, we propose a deep
quantization approach, which is among the early attempts of leveraging deep
neural networks into quantization-based cross-modal similarity search. Our
approach, dubbed shared predictive deep quantization (SPDQ), explicitly
formulates a shared subspace across different modalities and two private
subspaces for individual modalities, and representations in the shared subspace
and the private subspaces are learned simultaneously by embedding them to a
reproducing kernel Hilbert space, where the mean embedding of different
modality distributions can be explicitly compared. In addition, in the shared
subspace, a quantizer is learned to produce the semantics preserving compact
codes with the help of label alignment. Thanks to this novel network
architecture in cooperation with supervised quantization training, SPDQ can
preserve intramodal and intermodal similarities as much as possible and greatly
reduce quantization error. Experiments on two popular benchmarks corroborate
that our approach outperforms state-of-the-art methods.