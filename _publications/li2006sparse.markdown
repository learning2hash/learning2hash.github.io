---
layout: publication
title: "Very Sparse Random Projections"
authors: Ping Li, Trevor J Hastie, Kenneth W. Church
conference: KDD
year: 2006
bibkey: li2006sparse
additional_links:
   - {name: "PDF", url: "https://web.stanford.edu/~hastie/Papers/Ping/KDD06_rp.pdf/"}
tags: ['Unsupervised']
---
There has been considerable interest in random projections, an approximate algorithm for estimating distances between pairs of points in a high-dimensional vector space. Let A in Rn x D be our n points in D dimensions. The method multiplies A by a random matrix R in RD x k, reducing the D dimensions down to just k for speeding up the computation. R typically consists of entries of standard normal N(0,1). It is well known that random projections preserve pairwise distances (in the expectation). Achlioptas proposed sparse random projections by replacing the N(0,1) entries in R with entries in -1,0,1 with probabilities 1/6, 2/3, 1/6, achieving a threefold speedup in processing time.We recommend using R of entries in -1,0,1 with probabilities 1/2√D, 1-1√D, 1/2√D for achieving a significant √D-fold speedup, with little loss in accuracy.
