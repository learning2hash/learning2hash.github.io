---
layout: publication
title: A Fast Nearest Neighbor Search Algorithm Based On Vector Quantization
authors: Sylvain Lpma Corlay
conference: Arxiv
year: 2011
citations: 4
bibkey: corlay2011fast
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1105.4953'}]
tags: [ANN Search, Quantization]
---
In this article, we propose a new fast nearest neighbor search algorithm,
based on vector quantization. Like many other branch and bound search
algorithms [1,10], a preprocessing recursively partitions the data set into
disjointed subsets until the number of points in each part is small enough. In
doing so, a search-tree data structure is built. This preliminary recursive
data-set partition is based on the vector quantization of the empirical
distribution of the initial data-set. Unlike previously cited methods, this
kind of partitions does not a priori allow to eliminate several brother nodes
in the search tree with a single test. To overcome this difficulty, we propose
an algorithm to reduce the number of tested brother nodes to a minimal list
that we call "friend Voronoi cells". The complete description of the method
requires a deeper insight into the properties of Delaunay triangulations and
Voronoi diagrams