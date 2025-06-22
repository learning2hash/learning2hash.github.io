---
layout: publication
title: Confirmation Sampling For Exact Nearest Neighbor Search
authors: Tobias Christiani, Rasmus Pagh, Mikkel Thorup
conference: Arxiv
year: 2018
citations: 1
bibkey: christiani2018confirmation
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1812.02603'}]
tags: [Tools and Libraries, ANN Search, Hashing Methods]
---
Locality-sensitive hashing (LSH), introduced by Indyk and Motwani in STOC
'98, has been an extremely influential framework for nearest neighbor search in
high-dimensional data sets. While theoretical work has focused on the
approximate nearest neighbor problems, in practice LSH data structures with
suitably chosen parameters are used to solve the exact nearest neighbor problem
(with some error probability). Sublinear query time is often possible in
practice even for exact nearest neighbor search, intuitively because the
nearest neighbor tends to be significantly closer than other data points.
However, theory offers little advice on how to choose LSH parameters outside of
pre-specified worst-case settings.
  We introduce the technique of confirmation sampling for solving the exact
nearest neighbor problem using LSH. First, we give a general reduction that
transforms a sequence of data structures that each find the nearest neighbor
with a small, unknown probability, into a data structure that returns the
nearest neighbor with probability \\(1-\delta\\), using as few queries as possible.
Second, we present a new query algorithm for the LSH Forest data structure with
\\(L\\) trees that is able to return the exact nearest neighbor of a query point
within the same time bound as an LSH Forest of \\(Ω(L)\\) trees with internal
parameters specifically tuned to the query and data.