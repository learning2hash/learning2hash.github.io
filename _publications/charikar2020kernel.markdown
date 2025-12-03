---
layout: publication
title: Kernel Density Estimation Through Density Constrained Near Neighbor Search
authors: Moses Charikar, Michael Kapralov, Navid Nouri, Paris Siminelakis
conference: 2020 IEEE 61st Annual Symposium on Foundations of Computer Science (FOCS)
year: 2020
bibkey: charikar2020kernel
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2011.06997'}]
tags: ["Datasets", "Efficiency", "Hashing Methods"]
short_authors: Charikar et al.
---
In this paper we revisit the kernel density estimation problem: given a
kernel \(K(x, y)\) and a dataset of \(n\) points in high dimensional Euclidean
space, prepare a data structure that can quickly output, given a query \(q\), a
\((1+\epsilon)\)-approximation to \(\mu:=\frac1\{|P|\}\sum_\{p\in P\} K(p, q)\). First,
we give a single data structure based on classical near neighbor search
techniques that improves upon or essentially matches the query time and space
complexity for all radial kernels considered in the literature so far. We then
show how to improve both the query complexity and runtime by using recent
advances in data-dependent near neighbor search.
  We achieve our results by giving a new implementation of the natural
importance sampling scheme. Unlike previous approaches, our algorithm first
samples the dataset uniformly (considering a geometric sequence of sampling
rates), and then uses existing approximate near neighbor search techniques on
the resulting smaller dataset to retrieve the sampled points that lie at an
appropriate distance from the query. We show that the resulting sampled dataset
has strong geometric structure, making approximate near neighbor search return
the required samples much more efficiently than for worst case datasets of the
same size. As an example application, we show that this approach yields a data
structure that achieves query time \(\mu^\{-(1+o(1))/4\}\) and space complexity
\(\mu^\{-(1+o(1))\}\) for the Gaussian kernel. Our data dependent approach achieves
query time \(\mu^\{-0.173-o(1)\}\) and space \(\mu^\{-(1+o(1))\}\) for the Gaussian
kernel. The data dependent analysis relies on new techniques for tracking the
geometric structure of the input datasets in a recursive hashing process that
we hope will be of interest in other applications in near neighbor search.