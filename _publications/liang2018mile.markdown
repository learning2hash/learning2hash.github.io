---
layout: publication
title: 'MILE: A Multi-level Framework For Scalable Graph Embedding'
authors: Jiongqian Liang, Saket Gurukar, Srinivasan Parthasarathy
conference: Proceedings of the International AAAI Conference on Web and Social Media
year: 2018
bibkey: liang2018mile
citations: 38
additional_links: [{name: Code, url: 'https://github.com/jiongqian/MILE'}, {name: Paper,
    url: 'https://arxiv.org/abs/1802.09612'}]
tags: ["AAAI", "Datasets", "Scalability", "Tools & Libraries"]
short_authors: Jiongqian Liang, Saket Gurukar, Srinivasan Parthasarathy
---
Recently there has been a surge of interest in designing graph embedding
methods. Few, if any, can scale to a large-sized graph with millions of nodes
due to both computational complexity and memory requirements. In this paper, we
relax this limitation by introducing the MultI-Level Embedding (MILE) framework
-- a generic methodology allowing contemporary graph embedding methods to scale
to large graphs. MILE repeatedly coarsens the graph into smaller ones using a
hybrid matching technique to maintain the backbone structure of the graph. It
then applies existing embedding methods on the coarsest graph and refines the
embeddings to the original graph through a graph convolution neural network
that it learns. The proposed MILE framework is agnostic to the underlying graph
embedding techniques and can be applied to many existing graph embedding
methods without modifying them. We employ our framework on several popular
graph embedding techniques and conduct embedding for real-world graphs.
Experimental results on five large-scale datasets demonstrate that MILE
significantly boosts the speed (order of magnitude) of graph embedding while
generating embeddings of better quality, for the task of node classification.
MILE can comfortably scale to a graph with 9 million nodes and 40 million
edges, on which existing methods run out of memory or take too long to compute
on a modern workstation. Our code and data are publicly available with detailed
instructions for adding new base embedding methods:
https://github.com/jiongqian/MILE.