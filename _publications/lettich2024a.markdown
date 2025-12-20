---
layout: publication
title: A Surprisingly Simple Method For Distributed Euclidean-minimum Spanning Tree
  / Single Linkage Dendrogram Construction From High Dimensional Embeddings Via Distance
  Decomposition
authors: Richard Lettich
conference: Arxiv
year: 2024
bibkey: lettich2024a
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2406.01739'}]
tags: ["Uncategorized"]
short_authors: Richard Lettich
---
We introduce a decomposition method for the distributed calculation of exact
Euclidean Minimum Spanning Trees in high dimensions (where sub-quadratic
algorithms are not effective), or more generalized geometric-minimum spanning
trees of complete graphs, where for each vertex \(v\in V\) in the graph \(G=(V,E)\)
is represented by a vector in \(\vec\{v\}\in \mathbb\{R\}^n\), and each for any edge,
the the weight of the edge in the graph is given by a symmetric binary
`distance' function between the representative vectors \(w(\\{x,y\\}) =
d(\vec\{x\},\vec\{y\})\). This is motivated by the task of clustering high
dimensional embeddings produced by neural networks, where low-dimensional
algorithms are ineffective; such geometric-minimum spanning trees find
applications as a subroutine in the construction of single linkage dendrograms,
as the two structures can be converted between each other efficiently.