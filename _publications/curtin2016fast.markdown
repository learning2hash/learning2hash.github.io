---
layout: publication
title: 'Fast Approximate Furthest Neighbors With Data-dependent Hashing'
authors: Ryan R. Curtin, Andrew B. Gardner
conference: "Arxiv"
year: 2016
citations: 0
bibkey: curtin2016fast
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/1605.09784'}
tags: ['Hashing Fundamentals', 'Efficient Learning', 'Hashing Methods', 'Tools and Libraries']
---
We present a novel hashing strategy for approximate furthest neighbor search
that selects projection bases using the data distribution. This strategy leads
to an algorithm, which we call DrusillaHash, that is able to outperform
existing approximate furthest neighbor strategies. Our strategy is motivated by
an empirical study of the behavior of the furthest neighbor search problem,
which lends intuition for where our algorithm is most useful. We also present a
variant of the algorithm that gives an absolute approximation guarantee; to our
knowledge, this is the first such approximate furthest neighbor hashing
approach to give such a guarantee. Performance studies indicate that
DrusillaHash can achieve comparable levels of approximation to other algorithms
while giving up to an order of magnitude speedup. An implementation is
available in the mlpack machine learning library (found at
http://www.mlpack.org).
