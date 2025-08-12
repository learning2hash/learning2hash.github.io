---
layout: publication
title: Geordf2vec Learning Location-aware Entity Representations In Knowledge Graphs
authors: Martin Boeckling, Heiko Paulheim, Sarah Detzler
conference: Lecture Notes in Computer Science
year: 2025
bibkey: boeckling2025geordf2vec
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2504.17099'}]
tags: []
short_authors: Martin Boeckling, Heiko Paulheim, Sarah Detzler
---
Many knowledge graphs contain a substantial number of spatial entities, such
as cities, buildings, and natural landmarks. For many of these entities, exact
geometries are stored within the knowledge graphs. However, most existing
approaches for learning entity representations do not take these geometries
into account. In this paper, we introduce a variant of RDF2Vec that
incorporates geometric information to learn location-aware embeddings of
entities. Our approach expands different nodes by flooding the graph from
geographic nodes, ensuring that each reachable node is considered. Based on the
resulting flooded graph, we apply a modified version of RDF2Vec that biases
graph walks using spatial weights. Through evaluations on multiple benchmark
datasets, we demonstrate that our approach outperforms both non-location-aware
RDF2Vec and GeoTransE.