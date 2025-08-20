---
layout: publication
title: K-nearest Neighbor Approximation Via The Friend-of-a-friend Principle
authors: Jacob D. Baron, R. W. R. Darling
conference: Arxiv
year: 2019
bibkey: baron2019k
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1908.07645'}]
tags: [Uncategorized]
short_authors: Jacob D. Baron, R. W. R. Darling
---
Suppose \(V\) is an \(n\)-element set where for each \(x \in V\), the elements of
\(V \setminus \\{x\\}\) are ranked by their similarity to \(x\). The \(K\)-nearest
neighbor graph is a directed graph including an arc from each \(x\) to the \(K\)
points of \(V \setminus \\{x\\}\) most similar to \(x\). Constructive approximation
to this graph using far fewer than \(n^2\) comparisons is important for the
analysis of large high-dimensional data sets. \(K\)-Nearest Neighbor Descent is a
parameter-free heuristic where a sequence of graph approximations is
constructed, in which second neighbors in one approximation are proposed as
neighbors in the next. Run times in a test case fit an \(O(n K^2 log\{n\})\)
pattern. This bound is rigorously justified for a similar algorithm, using
range queries, when applied to a homogeneous Poisson process in suitable
dimension. However the basic algorithm fails to achieve subquadratic complexity
on sets whose similarity rankings arise from a ``generic'' linear order on the
\(\binom\{n\}\{2\}\) inter-point distances in a metric space.