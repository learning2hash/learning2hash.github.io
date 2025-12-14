---
layout: publication
title: Fast Online K-nn Graph Building
authors: Thibault Debatty, Pietro Michiardi, Wim Mees
conference: Arxiv
year: 2016
bibkey: debatty2016fast
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1602.06819'}]
tags: [Evaluation]
short_authors: Thibault Debatty, Pietro Michiardi, Wim Mees
---
In this paper we propose an online approximate k-nn graph building algorithm,
which is able to quickly update a k-nn graph using a flow of data points. One
very important step of the algorithm consists in using the current distributed
graph to search for the neighbors of a new node. Hence we also propose a
distributed partitioning method based on balanced k-medoids clustering, that we
use to optimize the distributed search process. Finally, we present the
improved sequential search procedure that is used inside each partition.
  We also perform an experimental evaluation of the different algorithms, where
we study the influence of the parameters and compare the result of our
algorithms to existing state of the art. This experimental evaluation confirms
that the fast online k-nn graph building algorithm produces a graph that is
highly similar to the graph produced by an offline exhaustive algorithm, while
it requires less similarity computations.