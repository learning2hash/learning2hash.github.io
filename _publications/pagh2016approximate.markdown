---
layout: publication
title: Approximate Furthest Neighbor With Application To Annulus Query
authors: Rasmus Pagh, Francesco Silvestri, Johan Sivertsen, Matthew Skala
conference: Information Systems
year: 2016
bibkey: pagh2016approximate
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1611.07303'}]
tags: ["Efficiency", "Recommender Systems"]
short_authors: Pagh et al.
---
Much recent work has been devoted to approximate nearest neighbor queries.
Motivated by applications in recommender systems, we consider approximate
furthest neighbor (AFN) queries and present a simple, fast, and highly
practical data structure for answering AFN queries in high- dimensional
Euclidean space. The method builds on the technique of In- dyk (SODA 2003),
storing random projections to provide sublinear query time for AFN. However, we
introduce a different query algorithm, improving on Indyk's approximation
factor and reducing the running time by a logarithmic factor. We also present a
variation based on a query- independent ordering of the database points; while
this does not have the provable approximation factor of the query-dependent
data structure, it offers significant improvement in time and space complexity.
We give a theoretical analysis, and experimental results. As an application,
the query-dependent approach is used for deriving a data structure for the
approximate annulus query problem, which is defined as follows: given an input
set S and two parameters r > 0 and w >= 1, construct a data structure that
returns for each query point q a point p in S such that the distance between p
and q is at least r/w and at most wr.