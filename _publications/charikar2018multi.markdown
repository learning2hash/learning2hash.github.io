---
layout: publication
title: Multi-resolution Hashing For Fast Pairwise Summations
authors: Moses Charikar, Paris Siminelakis
conference: 2019 IEEE 60th Annual Symposium on Foundations of Computer Science (FOCS)
year: 2018
bibkey: charikar2018multi
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1807.07635'}]
tags: [Hashing Methods, Tools & Libraries, Datasets, Efficiency]
short_authors: Moses Charikar, Paris Siminelakis
---
A basic computational primitive in the analysis of massive datasets is
summing simple functions over a large number of objects. Modern applications
pose an additional challenge in that such functions often depend on a parameter
vector \(y\) (query) that is unknown a priori. Given a set of points \(X\subset
\mathbb\{R\}^\{d\}\) and a pairwise function \(w:\mathbb\{R\}^\{d\}\times
\mathbb\{R\}^\{d\}\to [0,1]\), we study the problem of designing a data-structure
that enables sublinear-time approximation of the summation
\(Z_\{w\}(y)=\frac\{1\}\{|X|\}\sum_\{x\in X\}w(x,y)\) for any query \(y\in
\mathbb\{R\}^\{d\}\). By combining ideas from Harmonic Analysis (partitions of unity
and approximation theory) with Hashing-Based-Estimators [Charikar, Siminelakis
FOCS'17], we provide a general framework for designing such data structures
through hashing that reaches far beyond what previous techniques allowed.
  A key design principle is a collection of \(T\geq 1\) hashing schemes with
collision probabilities \(p_\{1\},\ldots, p_\{T\}\) such that \(\sup_\{t\in
[T]\}\\{p_\{t\}(x,y)\\} = \Theta(\sqrt\{w(x,y)\})\). This leads to a data-structure
that approximates \(Z_\{w\}(y)\) using a sub-linear number of samples from each
hash family. Using this new framework along with Distance Sensitive Hashing
[Aumuller, Christiani, Pagh, Silvestri PODS'18], we show that such a collection
can be constructed and evaluated efficiently for any log-convex function
\(w(x,y)=e^\{\phi(\langle x,y\rangle)\}\) of the inner product on the unit sphere
\(x,y\in \mathcal\{S\}^\{d-1\}\).
  Our method leads to data structures with sub-linear query time that
significantly improve upon random sampling and can be used for Kernel Density
or Partition Function Estimation. We provide extensions of our result from the
sphere to \(\mathbb\{R\}^\{d\}\) and from scalar functions to vector functions.