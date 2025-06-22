---
layout: publication
title: Stochastic Graphlet Embedding
authors: Anjan Dutta, Hichem Sahbi
conference: IEEE TNNLS pages 1-14 2018
year: 2017
citations: 11
bibkey: dutta2017stochastic
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1702.00156'}]
tags: [ANN Search, Hashing Methods, Evaluation Metrics]
---
Graph-based methods are known to be successful in many machine learning and
pattern classification tasks. These methods consider semi-structured data as
graphs where nodes correspond to primitives (parts, interest points, segments,
etc.) and edges characterize the relationships between these primitives.
However, these non-vectorial graph data cannot be straightforwardly plugged
into off-the-shelf machine learning algorithms without a preliminary step of --
explicit/implicit -- graph vectorization and embedding. This embedding process
should be resilient to intra-class graph variations while being highly
discriminant. In this paper, we propose a novel high-order stochastic graphlet
embedding (SGE) that maps graphs into vector spaces. Our main contribution
includes a new stochastic search procedure that efficiently parses a given
graph and extracts/samples unlimitedly high-order graphlets. We consider these
graphlets, with increasing orders, to model local primitives as well as their
increasingly complex interactions. In order to build our graph representation,
we measure the distribution of these graphlets into a given graph, using
particular hash functions that efficiently assign sampled graphlets into
isomorphic sets with a very low probability of collision. When combined with
maximum margin classifiers, these graphlet-based representations have positive
impact on the performance of pattern comparison and recognition as corroborated
through extensive experiments using standard benchmark databases.