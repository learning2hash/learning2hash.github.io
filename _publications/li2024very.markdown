---
layout: publication
title: Very Sparse Random Projections
authors: Li Ping, Hastie, Church
conference: "Arxiv"
year: 2024
bibkey: li2024very
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/li2006sparse"}
tags: ['ARXIV', 'Independent']
---
There has been considerable interest in random projections an approximate algorithm for estimating distances between pairs of points in a high-dimensional vector space. Let A in Rn x D be our n points in D dimensions. The method multiplies A by a random matrix R in RD x k reducing the D dimensions down to just k for speeding up the computation. R typically consists of entries of standard normal N(01). It is well known that random projections preserve pairwise distances (in the expectation). Achlioptas proposed sparse random projections by replacing the N(01) entries in R with entries in -101 with probabilities 1/6 2/3 1/6 achieving a threefold speedup in processing time.We recommend using R of entries in -101 with probabilities 1/2√D 1-1√D 1/2√D for achieving a significant √D-fold speedup with little loss in accuracy.
