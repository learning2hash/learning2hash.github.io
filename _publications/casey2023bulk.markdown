---
layout: publication
title: Bulk Johnson-lindenstrauss Lemmas
authors: Michael P. Casey
conference: Arxiv
year: 2023
bibkey: casey2023bulk
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2307.07704'}]
tags: ["Distance Metric Learning", "Hashing Methods", "Locality Sensitive Hashing", "Scalability"]
short_authors: Michael P. Casey
---
For a set \(X\) of \(N\) points in \(\mathbb\{R\}^D\), the Johnson-Lindenstrauss
lemma provides random linear maps that approximately preserve all pairwise
distances in \(X\) -- up to multiplicative error \((1\pm \epsilon)\) with high
probability -- using a target dimension of \(O(\epsilon^\{-2\}log(N))\). Certain
known point sets actually require a target dimension this large -- any smaller
dimension forces at least one distance to be stretched or compressed too much.
What happens to the remaining distances? If we only allow a fraction \(\eta\) of
the distances to be distorted beyond tolerance \((1\pm \epsilon)\), we show a
target dimension of \(O(\epsilon^\{-2\}log(4e/\eta)log(N)/R)\) is sufficient for
the remaining distances. With the stable rank of a matrix \(A\) as
\(\lVert\{A\rVert\}_F^2/\lVert\{A\rVert\}^2\), the parameter \(R\) is the minimal
stable rank over certain \(log(N)\) sized subsets of \(X-X\) or their unit
normalized versions, involving each point of \(X\) exactly once. The linear maps
may be taken as random matrices with i.i.d. zero-mean unit-variance
sub-gaussian entries. When the data is sampled i.i.d. as a given random vector
\(\xi\), refined statements are provided; the most improvement happens when \(\xi\)
or the unit normalized \(\widehat\{\xi-\xi'\}\) is isotropic, with \(\xi'\) an
independent copy of \(\xi\), and includes the case of i.i.d. coordinates.