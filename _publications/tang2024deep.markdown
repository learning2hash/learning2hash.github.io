---
layout: publication
title: Deep Hierarchical Graph Alignment Kernels
authors: Shuhao Tang, Hao Tian, Xiaofeng Cao, Wei Ye
conference: Proceedings of the Thirty-ThirdInternational Joint Conference on Artificial
  Intelligence
year: 2024
bibkey: tang2024deep
citations: 2
additional_links: [{name: Code, url: 'https://github.com/EWesternRa/DHGAK)'}, {name: Paper,
    url: 'https://arxiv.org/abs/2405.05545'}]
tags: []
short_authors: Tang et al.
---
Typical R-convolution graph kernels invoke the kernel functions that
decompose graphs into non-isomorphic substructures and compare them. However,
overlooking implicit similarities and topological position information between
those substructures limits their performances. In this paper, we introduce Deep
Hierarchical Graph Alignment Kernels (DHGAK) to resolve this problem.
Specifically, the relational substructures are hierarchically aligned to
cluster distributions in their deep embedding space. The substructures
belonging to the same cluster are assigned the same feature map in the
Reproducing Kernel Hilbert Space (RKHS), where graph feature maps are derived
by kernel mean embedding. Theoretical analysis guarantees that DHGAK is
positive semi-definite and has linear separability in the RKHS. Comparison with
state-of-the-art graph kernels on various benchmark datasets demonstrates the
effectiveness and efficiency of DHGAK. The code is available at Github
(https://github.com/EWesternRa/DHGAK).