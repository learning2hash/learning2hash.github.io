---
layout: publication
title: Weighted Minwise Hashing Beats Linear Sketching For Inner Product Estimation
authors: "Aline Bessa, Majid Daliri, Juliana Freire, Cameron Musco, Christopher Musco,\
  \ A\xE9cio Santos, Haoxiang Zhang"
conference: Proceedings of the 42nd ACM SIGMOD-SIGACT-SIGAI Symposium on Principles
  of Database Systems
year: 2023
bibkey: bessa2023weighted
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2301.05811'}]
tags: ["Datasets", "Hashing Methods", "Locality-Sensitive-Hashing"]
short_authors: Bessa et al.
---
We present a new approach for computing compact sketches that can be used to
approximate the inner product between pairs of high-dimensional vectors. Based
on the Weighted MinHash algorithm, our approach admits strong accuracy
guarantees that improve on the guarantees of popular linear sketching
approaches for inner product estimation, such as CountSketch and
Johnson-Lindenstrauss projection. Specifically, while our method admits
guarantees that exactly match linear sketching for dense vectors, it yields
significantly lower error for sparse vectors with limited overlap between
non-zero entries. Such vectors arise in many applications involving sparse
data. They are also important in increasingly popular dataset search
applications, where inner product sketches are used to estimate data
covariance, conditional means, and other quantities involving columns in
unjoined tables. We complement our theoretical results by showing that our
approach empirically outperforms existing linear sketches and unweighted
hashing-based sketches for sparse vectors.