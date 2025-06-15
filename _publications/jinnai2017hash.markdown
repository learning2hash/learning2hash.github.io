---
layout: publication
title: On Hash-based Work Distribution Methods For Parallel Best-first Search
authors: Jinnai Yuu, Fukunaga Alex
conference: "Yuu Jinnai and Alex Fukunaga."
year: 2017
citations: 3
bibkey: jinnai2017hash
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1706.03254"}
tags: ['Graph', 'Independent', 'Independent']
---
Parallel best-first search algorithms such as Hash Distributed A* (HDA*)
distribute work among the processes using a global hash function. We analyze
the search and communication overheads of state-of-the-art hash-based parallel
best-first search algorithms, and show that although Zobrist hashing, the
standard hash function used by HDA*, achieves good load balance for many
domains, it incurs significant communication overhead since almost all
generated nodes are transferred to a different processor than their parents. We
propose Abstract Zobrist hashing, a new work distribution method for parallel
search which, instead of computing a hash value based on the raw features of a
state, uses a feature projection function to generate a set of abstract
features which results in a higher locality, resulting in reduced
communications overhead. We show that Abstract Zobrist hashing outperforms
previous methods on search domains using hand-coded, domain specific feature
projection functions. We then propose GRAZHDA*, a graph-partitioning based
approach to automatically generating feature projection functions. GRAZHDA*
seeks to approximate the partitioning of the actual search space graph by
partitioning the domain transition graph, an abstraction of the state space
graph. We show that GRAZHDA* outperforms previous methods on domain-independent
planning.
