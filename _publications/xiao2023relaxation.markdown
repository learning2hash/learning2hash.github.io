---
layout: publication
title: A Relaxation Method For Binary Optimizations On Constrained Stiefel Manifold
authors: Lianghai Xiao, Yitian Qian, Shaohua Pan
conference: Arxiv
year: 2023
citations: 0
bibkey: xiao2023relaxation
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2308.10506'}]
tags: [Unsupervised, Supervised, Hashing Methods, ANN Search, Evaluation Metrics,
  Benchmarks and Datasets]
---
This paper focuses on a class of binary orthogonal optimization problems
frequently arising in semantic hashing. Consider that this class of problems
may have an empty feasible set, rendering them not well-defined. We introduce
an equivalent model involving a restricted Stiefel manifold and a matrix box
set, and then investigate its penalty problems induced by the \\(\ell_1\\)-distance
from the box set and its Moreau envelope. The two penalty problems are always
well-defined. Moreover, they serve as the global exact penalties provided that
the original feasible set is non-empty. Notably, the penalty problem induced by
the Moreau envelope is a smooth optimization over an embedded submanifold with
a favorable structure. We develop a retraction-based line-search Riemannian
gradient method to address the penalty problem. Finally, the proposed method is
applied to supervised and unsupervised hashing tasks and is compared with
several popular methods on the MNIST and CIFAR-10 datasets. The numerical
comparisons reveal that our algorithm is significantly superior to other
solvers in terms of feasibility violation, and it is comparable even superior
to others in terms of evaluation metrics related to the Hamming distance.