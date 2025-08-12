---
layout: publication
title: 'Linear Dimensionality Reduction In Linear Time: Johnson-lindenstrauss-type
  Guarantees For Random Subspace'
authors: Nick Lim, Robert J. Durrant
conference: Arxiv
year: 2017
bibkey: lim2017linear
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1705.06408'}]
tags: []
short_authors: Nick Lim, Robert J. Durrant
---
We consider the problem of efficient randomized dimensionality reduction with
norm-preservation guarantees. Specifically we prove data-dependent
Johnson-Lindenstrauss-type geometry preservation guarantees for Ho's random
subspace method: When data satisfy a mild regularity condition -- the extent of
which can be estimated by sampling from the data -- then random subspace
approximately preserves the Euclidean geometry of the data with high
probability. Our guarantees are of the same order as those for random
projection, namely the required dimension for projection is logarithmic in the
number of data points, but have a larger constant term in the bound which
depends upon this regularity. A challenging situation is when the original data
have a sparse representation, since this implies a very large projection
dimension is required: We show how this situation can be improved for sparse
binary data by applying an efficient `densifying' preprocessing, which neither
changes the Euclidean geometry of the data nor requires an explicit
matrix-matrix multiplication. We corroborate our theoretical findings with
experiments on both dense and sparse high-dimensional datasets from several
application domains.