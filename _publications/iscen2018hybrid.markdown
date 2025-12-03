---
layout: publication
title: 'Hybrid Diffusion: Spectral-temporal Graph Filtering For Manifold Ranking'
authors: Ahmet Iscen, Yannis Avrithis, Giorgos Tolias, Teddy Furon, Ondrej Chum
conference: Arxiv
year: 2018
bibkey: iscen2018hybrid
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1807.08692'}]
tags: ["Evaluation", "Image Retrieval"]
short_authors: Iscen et al.
---
State of the art image retrieval performance is achieved with CNN features
and manifold ranking using a k-NN similarity graph that is pre-computed
off-line. The two most successful existing approaches are temporal filtering,
where manifold ranking amounts to solving a sparse linear system online, and
spectral filtering, where eigen-decomposition of the adjacency matrix is
performed off-line and then manifold ranking amounts to dot-product search
online. The former suffers from expensive queries and the latter from
significant space overhead. Here we introduce a novel, theoretically
well-founded hybrid filtering approach allowing full control of the space-time
trade-off between these two extremes. Experimentally, we verify that our hybrid
method delivers results on par with the state of the art, with lower memory
demands compared to spectral filtering approaches and faster compared to
temporal filtering.