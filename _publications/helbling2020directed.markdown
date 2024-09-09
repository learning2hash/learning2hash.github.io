---
layout: publication
title: "Directed Graph Hashing"
authors: Helbling Caleb
conference: Arxiv
year: 2020
bibkey: helbling2020directed
additional_links:
- {name: "Paper", url: "https://arxiv.org/abs/2002.06653"}
tags: ['ARXIV', 'Graph', 'TOM']
---
This paper presents several algorithms for hashing directed graphs. The algorithms given are capable of hashing entire graphs as well as assigning hash values to specific nodes in a given graph. The notion of node symmetry is made precise via computation of vertex orbits and the graph automorphism group, and nodes that are symmetrically identical are assigned equal hashes. We also present a novel Merkle-style hashing algorithm that seeks to fulfill the recursive principle that a hash of a node should depend only on the hash of its neighbors. This algorithm works even in the presence of cycles, which would not be possible with a naive approach. Structurally hashing trees has seen widespread use in blockchain, source code version control, and web applications. Despite the popularity of tree hashing, directed graph hashing remains unstudied in the literature. Our algorithms open new possibilities to hashing both directed graphs and more complex data structures that can be reduced to directed graphs such as hypergraphs.