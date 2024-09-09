---
layout: publication
title: "Asymmetric Transfer Hashing with Adaptive Bipartite Graph Learning"
authors: Lu Jianglin, Zhou Jie, Chen Yudong, Pedrycz Witold, Hung Kwok-Wai
conference: Arxiv
year: 2022
bibkey: lu2022asymmetric
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2206.12592"}
tags: ['ARXIV', 'Graph', 'Semi Supervised', 'Supervised', 'Unsupervised']
---
Thanks to the efficient retrieval speed and low storage consumption, learning to
hash has been widely used in visual retrieval tasks. However, existing hashing
methods assume that the query and retrieval samples lie in homogeneous feature
space within the same domain. As a result, they cannot be directly applied to
heterogeneous cross-domain retrieval. In this paper, we propose a Generalized
Image Transfer Retrieval (GITR) problem, which encounters two crucial
bottlenecks: 1) the query and retrieval samples may come from different domains,
leading to an inevitable {domain distribution gap}; 2) the features of the two
domains may be heterogeneous or misaligned, bringing up an additional {feature
gap}. To address the GITR problem, we propose an Asymmetric Transfer Hashing
(ATH) framework with its unsupervised/semi-supervised/supervised realizations.
Specifically, ATH characterizes the domain distribution gap by the discrepancy
between two asymmetric hash functions, and minimizes the feature gap with the
help of a novel adaptive bipartite graph constructed on cross-domain data. By
jointly optimizing asymmetric hash functions and the bipartite graph, not only
can knowledge transfer be achieved but information loss caused by feature
alignment can also be avoided. Meanwhile, to alleviate negative transfer, the
intrinsic geometrical structure of single-domain data is preserved by involving
a domain affinity graph. Extensive experiments on both single-domain and cross-
domain benchmarks under different GITR subtasks indicate the superiority of our
ATH method in comparison with the state-of-the-art hashing methods.
