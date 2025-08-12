---
layout: publication
title: Distributed Hybrid Sketching For \(\ell_2\)-embeddings
authors: Neophytos Charalambides, Arya Mazumdar
conference: Arxiv
year: 2024
bibkey: charalambides2024distributed
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.20301'}]
tags: []
short_authors: Neophytos Charalambides, Arya Mazumdar
---
Linear algebraic operations are ubiquitous in engineering applications, and
arise often in a variety of fields including statistical signal processing and
machine learning. With contemporary large datasets, to perform linear algebraic
methods and regression tasks, it is necessary to resort to both distributed
computations as well as data compression. In this paper, we study
\textit\{distributed\} \(ℓ₂\)-subspace embeddings, a common technique used to
efficiently perform linear regression. In our setting, data is distributed
across multiple computing nodes and a goal is to minimize communication between
the nodes and the coordinator in the distributed centralized network, while
maintaining the geometry of the dataset. Furthermore, there is also the concern
of keeping the data private and secure from potential adversaries. In this
work, we address these issues through randomized sketching, where the key idea
is to apply distinct sketching matrices on the local datasets. A novelty of
this work is that we also consider \textit\{hybrid sketching\}, \textit\{i.e.\} a
second sketch is applied on the aggregated locally sketched datasets, for
enhanced embedding results. One of the main takeaways of this work is that by
hybrid sketching, we can interpolate between the trade-offs that arise in
off-the-shelf sketching matrices. That is, we can obtain gains in terms of
embedding dimension or multiplication time. Our embedding arguments are also
justified numerically.