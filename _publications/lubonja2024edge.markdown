---
layout: publication
title: Edge-parallel Graph Encoder Embedding
authors: Ariel Lubonja, Cencheng Shen, Carey Priebe, Randal Burns
conference: 2024 IEEE International Parallel and Distributed Processing Symposium
  Workshops (IPDPSW)
year: 2024
bibkey: lubonja2024edge
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2402.04403'}]
tags: ["Efficiency"]
short_authors: Lubonja et al.
---
New algorithms for embedding graphs have reduced the asymptotic complexity of
finding low-dimensional representations. One-Hot Graph Encoder Embedding (GEE)
uses a single, linear pass over edges and produces an embedding that converges
asymptotically to the spectral embedding. The scaling and performance benefits
of this approach have been limited by a serial implementation in an interpreted
language. We refactor GEE into a parallel program in the Ligra graph engine
that maps functions over the edges of the graph and uses lock-free atomic
instrutions to prevent data races. On a graph with 1.8B edges, this results in
a 500 times speedup over the original implementation and a 17 times speedup
over a just-in-time compiled version.