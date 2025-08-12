---
layout: publication
title: 'Graph DNA: Deep Neighborhood Aware Graph Encoding For Collaborative Filtering'
authors: Liwei Wu, Hsiang-Fu Yu, Nikhil Rao, James Sharpnack, Cho-Jui Hsieh
conference: Arxiv
year: 2019
bibkey: wu2019graph
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1905.12217'}]
tags: ["Recommender Systems"]
short_authors: Wu et al.
---
In this paper, we consider recommender systems with side information in the
form of graphs. Existing collaborative filtering algorithms mainly utilize only
immediate neighborhood information and have a hard time taking advantage of
deeper neighborhoods beyond 1-2 hops. The main caveat of exploiting deeper
graph information is the rapidly growing time and space complexity when
incorporating information from these neighborhoods. In this paper, we propose
using Graph DNA, a novel Deep Neighborhood Aware graph encoding algorithm, for
exploiting deeper neighborhood information. DNA encoding computes approximate
deep neighborhood information in linear time using Bloom filters, a
space-efficient probabilistic data structure and results in a per-node encoding
that is logarithmic in the number of nodes in the graph. It can be used in
conjunction with both feature-based and graph-regularization-based
collaborative filtering algorithms. Graph DNA has the advantages of being
memory and time efficient and providing additional regularization when compared
to directly using higher order graph information. We conduct experiments on
real-world datasets, showing graph DNA can be easily used with 4 popular
collaborative filtering algorithms and consistently leads to a performance
boost with little computational and memory overhead.