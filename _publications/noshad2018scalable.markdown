---
layout: publication
title: Scalable Hash-based Estimation Of Divergence Measures
authors: Morteza Noshad, Alfred O. Hero
conference: 2018 Information Theory and Applications Workshop (ITA)
year: 2018
bibkey: noshad2018scalable
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1801.00398'}]
tags: [Hashing Methods]
short_authors: Morteza Noshad, Alfred O. Hero
---
We propose a scalable divergence estimation method based on hashing. Consider
two continuous random variables \(X\) and \(Y\) whose densities have bounded
support. We consider a particular locality sensitive random hashing, and
consider the ratio of samples in each hash bin having non-zero numbers of Y
samples. We prove that the weighted average of these ratios over all of the
hash bins converges to f-divergences between the two samples sets. We show that
the proposed estimator is optimal in terms of both MSE rate and computational
complexity. We derive the MSE rates for two families of smooth functions; the
H\"\{o\}lder smoothness class and differentiable functions. In particular, it is
proved that if the density functions have bounded derivatives up to the order
\(d/2\), where \(d\) is the dimension of samples, the optimal parametric MSE rate
of \(O(1/N)\) can be achieved. The computational complexity is shown to be
\(O(N)\), which is optimal. To the best of our knowledge, this is the first
empirical divergence estimator that has optimal computational complexity and
achieves the optimal parametric MSE estimation rate.