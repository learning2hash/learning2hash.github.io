---
layout: publication
title: Lower Bounds On Time-space Trade-offs For Approximate Near Neighbors
authors: Andoni et al.
conference: Proceedings of the Twenty-Eighth Annual ACM-SIAM Symposium on Discrete
  Algorithms
year: 2016
bibkey: andoni2016lower
citations: 30
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1605.02701'}]
tags: [Hashing Methods]
---
We show tight lower bounds for the entire trade-off between space and query
time for the Approximate Near Neighbor search problem. Our lower bounds hold in
a restricted model of computation, which captures all hashing-based approaches.
In articular, our lower bound matches the upper bound recently shown in
[Laarhoven 2015] for the random instance on a Euclidean sphere (which we show
in fact extends to the entire space \\(\mathbb\{R\}^d\\) using the techniques from
[Andoni, Razenshteyn 2015]).
  We also show tight, unconditional cell-probe lower bounds for one and two
probes, improving upon the best known bounds from [Panigrahy, Talwar, Wieder
2010]. In particular, this is the first space lower bound (for any static data
structure) for two probes which is not polynomially smaller than for one probe.
To show the result for two probes, we establish and exploit a connection to
locally-decodable codes.