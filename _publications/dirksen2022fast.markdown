---
layout: publication
title: Fast Metric Embedding Into The Hamming Cube
authors: Sjoerd Dirksen, Shahar Mendelson, Alexander Stollenwerk
conference: SIAM Journal on Computing
year: 2024
bibkey: dirksen2022fast
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2204.04109'}]
tags: [Evaluation]
short_authors: Sjoerd Dirksen, Shahar Mendelson, Alexander Stollenwerk
---
We consider the problem of embedding a subset of \\(\mathbb\{R\}^n\\) into a
low-dimensional Hamming cube in an almost isometric way. We construct a simple,
data-oblivious, and computationally efficient map that achieves this task with
high probability: we first apply a specific structured random matrix, which we
call the double circulant matrix; using that matrix requires linear storage and
matrix-vector multiplication can be performed in near-linear time. We then
binarize each vector by comparing each of its entries to a random threshold,
selected uniformly at random from a well-chosen interval.
  We estimate the number of bits required for this encoding scheme in terms of
two natural geometric complexity parameters of the set - its Euclidean covering
numbers and its localized Gaussian complexity. The estimate we derive turns out
to be the best that one can hope for - up to logarithmic terms.
  The key to the proof is a phenomenon of independent interest: we show that
the double circulant matrix mimics the behavior of a Gaussian matrix in two
important ways. First, it maps an arbitrary set in \\(\mathbb\{R\}^n\\) into a set of
well-spread vectors. Second, it yields a fast near-isometric embedding of any
finite subset of \\(ℓ₂^n\\) into \\(\ell_1^m\\). This embedding achieves the same
dimension reduction as a Gaussian matrix in near-linear time, under an optimal
condition - up to logarithmic factors - on the number of points to be embedded.
This improves a well-known construction due to Ailon and Chazelle.