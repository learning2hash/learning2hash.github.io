---
layout: publication
title: Weighted Embeddings For Low-dimensional Graph Representation
authors: "Thomas Bl\xE4sius, Jean-pierre von Der Heydt, Maximilian Katzmann, Nikolai\
  \ Maas"
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2025
bibkey: "bl\xE4sius2024weighted"
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2410.06042'}]
tags: ["AAAI"]
short_authors: "Bl\xE4sius et al."
---
Learning low-dimensional numerical representations from symbolic data, e.g.,
embedding the nodes of a graph into a geometric space, is an important concept
in machine learning. While embedding into Euclidean space is common, recent
observations indicate that hyperbolic geometry is better suited to represent
hierarchical information and heterogeneous data (e.g., graphs with a scale-free
degree distribution). Despite their potential for more accurate
representations, hyperbolic embeddings also have downsides like being more
difficult to compute and harder to use in downstream tasks.
  We propose embedding into a weighted space, which is closely related to
hyperbolic geometry but mathematically simpler. We provide the embedding
algorithm WEmbed and demonstrate, based on generated as well as over 2000
real-world graphs, that our weighted embeddings heavily outperform
state-of-the-art Euclidean embeddings for heterogeneous graphs while using
fewer dimensions. The running time of WEmbed and embedding quality for the
remaining instances is on par with state-of-the-art Euclidean embedders.