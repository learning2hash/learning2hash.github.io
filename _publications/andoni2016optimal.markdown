---
layout: publication
title: Optimal Hashing-based Time-space Trade-offs For Approximate Near Neighbors
authors: Andoni Alexandr, Laarhoven Thijs, Razenshteyn Ilya, Waingarten Erik
conference: "Arxiv"
year: 2016
bibkey: andoni2016optimal
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1608.03580"}
tags: ['ARXIV', 'FOCS']
---
[See the paper for the full abstract.] We show tight upper and lower bounds for time-space trade-offs for the \{&#37; raw &#37;\}\\(c\\)\{&#37; endraw &#37;\}-Approximate Near Neighbor Search problem. For the \{&#37; raw &#37;\}\\(d\\)\{&#37; endraw &#37;\}-dimensional Euclidean space and \{&#37; raw &#37;\}\\(n\\)\{&#37; endraw &#37;\}-point datasets, we develop a data structure with space $n^\{1 + \rho\_u + o(1)\} + O(dn)\{&#37; raw &#37;\}\\( and query time \\)\{&#37; endraw &#37;\}n^\{\rho\_q + o(1)\} + d n^\{o(1)\}$ for every \{&#37; raw &#37;\}\\(\rho\_u, \rho\_q \geq 0\\)\{&#37; endraw &#37;\} such that: \begin\{equation\} c^2 \sqrt\{\rho\_q\} + (c^2 - 1) \sqrt\{\rho\_u\} = \sqrt\{2c^2 - 1\}. \end\{equation\} This is the first data structure that achieves sublinear query time and near-linear space for every approximation factor \{&#37; raw &#37;\}\\(c > 1\\)\{&#37; endraw &#37;\}, improving upon [Kapralov, PODS 2015]. The data structure is a culmination of a long line of work on the problem for all space regimes; it builds on Spherical Locality-Sensitive Filtering [Becker, Ducas, Gama, Laarhoven, SODA 2016] and data-dependent hashing [Andoni, Indyk, Nguyen, Razenshteyn, SODA 2014] [Andoni, Razenshteyn, STOC 2015]. Our matching lower bounds are of two types: conditional and unconditional. First, we prove tightness of the whole above trade-off in a restricted model of computation, which captures all known hashing-based approaches. We then show unconditional cell-probe lower bounds for one and two probes that match the above trade-off for \{&#37; raw &#37;\}\\(\rho\_q = 0\\)\{&#37; endraw &#37;\}, improving upon the best known lower bounds from [Panigrahy, Talwar, Wieder, FOCS 2010]. In particular, this is the first space lower bound (for any static data structure) for two probes which is not polynomially smaller than the one-probe bound. To show the result for two probes, we establish and exploit a connection to locally-decodable codes.
