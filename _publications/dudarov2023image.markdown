---
layout: publication
title: On The Image Of Graph Distance Matrices
authors: William Dudarov, Noah Feinberg, Raymond Guo, Ansel Goh, Andrea Ottolini,
  Alicia Stepin, Raghavenda Tripathi, Joia Zhang
conference: Arxiv
year: 2023
bibkey: dudarov2023image
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2307.04740'}]
tags: ["Distance Metric Learning", "Graph Based ANN"]
short_authors: Dudarov et al.
---
Let \(G=(V,E)\) be a finite, simple, connected, combinatorial graph on \(n\)
vertices and let \(D \in \mathbb\{R\}^\{n \times n\}\) be its graph distance matrix
\(D_\{ij\} = d(v_i, v_j)\). Steinerberger (J. Graph Theory, 2023) empirically
observed that the linear system of equations \(Dx =\mathbf\{1\}\), where
\(\mathbf\{1\} = (1,1,\dots, 1)^\{T\}\), very frequently has a solution (even in
cases where \(D\) is not invertible). The smallest nontrivial example of a graph
where the linear system is not solvable are two graphs on 7 vertices. We prove
that, in fact, counterexamples exists for all \(n\geq 7\). The construction is
somewhat delicate and further suggests that such examples are perhaps rare. We
also prove that for Erd\H\{o\}s-R\'enyi random graphs the graph distance matrix
\(D\) is invertible with high probability. We conclude with some structural
results on the Perron-Frobenius eigenvector for a distance matrix.