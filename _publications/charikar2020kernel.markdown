---
layout: publication
title: Kernel Density Estimation Through Density Constrained Near Neighbor Search
authors: Charikar Moses, Kapralov Michael, Nouri Navid, Siminelakis Paris
conference: "Arxiv"
year: 2020
bibkey: charikar2020kernel
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2011.06997"}
tags: ['ARXIV']
---
<p>In this paper we revisit the kernel density estimation problem: given
a kernel <span class="math inline">\(K(x, y)\)</span> and a dataset of
<span class="math inline">\(n\)</span> points in high dimensional
Euclidean space, prepare a data structure that can quickly output, given
a query <span class="math inline">\(q\)</span>, a <span
class="math inline">\((1+\epsilon)\)</span>-approximation to <span
class="math inline">\(\mu:=\frac1{|P|}\sum_{p\in P} K(p, q)\)</span>.
First, we give a single data structure based on classical near neighbor
search techniques that improves upon or essentially matches the query
time and space complexity for all radial kernels considered in the
literature so far. We then show how to improve both the query complexity
and runtime by using recent advances in data-dependent near neighbor
search. We achieve our results by giving a new implementation of the
natural importance sampling scheme. Unlike previous approaches, our
algorithm first samples the dataset uniformly (considering a geometric
sequence of sampling rates), and then uses existing approximate near
neighbor search techniques on the resulting smaller dataset to retrieve
the sampled points that lie at an appropriate distance from the query.
We show that the resulting sampled dataset has strong geometric
structure, making approximate near neighbor search return the required
samples much more efficiently than for worst case datasets of the same
size. As an example application, we show that this approach yields a
data structure that achieves query time <span
class="math inline">\(\mu^{-(1+o(1))/4}\)</span> and space complexity
<span class="math inline">\(\mu^{-(1+o(1))}\)</span> for the Gaussian
kernel. Our data dependent approach achieves query time <span
class="math inline">\(\mu^{-0.173-o(1)}\)</span> and space <span
class="math inline">\(\mu^{-(1+o(1))}\)</span> for the Gaussian kernel.
The data dependent analysis relies on new techniques for tracking the
geometric structure of the input datasets in a recursive hashing process
that we hope will be of interest in other applications in near neighbor
search.</p>
