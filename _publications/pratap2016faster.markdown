---
layout: publication
title: Faster Coreset Construction For Projective Clustering Via Low-rank Approximation
authors: Rameshwar Pratap, Sandeep Sen
conference: Lecture Notes in Computer Science
year: 2018
bibkey: pratap2016faster
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1606.07992'}]
tags: []
short_authors: Rameshwar Pratap, Sandeep Sen
---
In this work, we present a randomized coreset construction for projective
clustering, which involves computing a set of \\(k\\) closest \\(j\\)-dimensional
linear (affine) subspaces of a given set of \\(n\\) vectors in \\(d\\) dimensions. Let
\\(A \in \mathbb\{R\}^\{n\times d\}\\) be an input matrix. An earlier deterministic
coreset construction of Feldman \textit\{et. al.\} relied on computing the SVD of
\\(A\\). The best known algorithms for SVD require \\(\min\\{nd^2, n^2d\\}\\) time, which
may not be feasible for large values of \\(n\\) and \\(d\\). We present a coreset
construction by projecting the rows of matrix \\(A\\) on some orthonormal vectors
that closely approximate the right singular vectors of \\(A\\). As a consequence,
when the values of \\(k\\) and \\(j\\) are small, we are able to achieve a faster
algorithm, as compared to the algorithm of Feldman \textit\{et. al.\}, while
maintaining almost the same approximation. We also benefit in terms of space as
well as exploit the sparsity of the input dataset. Another advantage of our
approach is that it can be constructed in a streaming setting quite
efficiently.