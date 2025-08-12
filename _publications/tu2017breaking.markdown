---
layout: publication
title: Breaking Locality Accelerates Block Gauss-seidel
authors: Stephen Tu, Shivaram Venkataraman, Ashia C. Wilson, Alex Gittens, Michael
  I. Jordan, Benjamin Recht
conference: Arxiv
year: 2017
bibkey: tu2017breaking
citations: 15
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1701.03863'}]
tags: []
short_authors: Tu et al.
---
Recent work by Nesterov and Stich showed that momentum can be used to
accelerate the rate of convergence for block Gauss-Seidel in the setting where
a fixed partitioning of the coordinates is chosen ahead of time. We show that
this setting is too restrictive, constructing instances where breaking locality
by running non-accelerated Gauss-Seidel with randomly sampled coordinates
substantially outperforms accelerated Gauss-Seidel with any fixed partitioning.
Motivated by this finding, we analyze the accelerated block Gauss-Seidel
algorithm in the random coordinate sampling setting. Our analysis captures the
benefit of acceleration with a new data-dependent parameter which is well
behaved when the matrix sub-blocks are well-conditioned. Empirically, we show
that accelerated Gauss-Seidel with random coordinate sampling provides speedups
for large scale machine learning tasks when compared to non-accelerated
Gauss-Seidel and the classical conjugate-gradient algorithm.