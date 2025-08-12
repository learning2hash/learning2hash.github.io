---
layout: publication
title: Enhance Hyperbolic Representation Learning Via Second-order Pooling
authors: Kun Song, Ruben Solozabal, Li Hao, Lu Ren, Moloud Abdar, Qing Li, Fakhri
  Karray, Martin Takac
conference: Arxiv
year: 2024
bibkey: song2024enhance
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2410.22026'}]
tags: []
short_authors: Song et al.
---
Hyperbolic representation learning is well known for its ability to capture
hierarchical information. However, the distance between samples from different
levels of hierarchical classes can be required large. We reveal that the
hyperbolic discriminant objective forces the backbone to capture this
hierarchical information, which may inevitably increase the Lipschitz constant
of the backbone. This can hinder the full utilization of the backbone's
generalization ability. To address this issue, we introduce second-order
pooling into hyperbolic representation learning, as it naturally increases the
distance between samples without compromising the generalization ability of the
input features. In this way, the Lipschitz constant of the backbone does not
necessarily need to be large. However, current off-the-shelf low-dimensional
bilinear pooling methods cannot be directly employed in hyperbolic
representation learning because they inevitably reduce the distance expansion
capability. To solve this problem, we propose a kernel approximation
regularization, which enables the low-dimensional bilinear features to
approximate the kernel function well in low-dimensional space. Finally, we
conduct extensive experiments on graph-structured datasets to demonstrate the
effectiveness of the proposed method.