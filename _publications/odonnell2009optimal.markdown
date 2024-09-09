---
layout: publication
title: Optimal lower bounds for locality sensitive hashing (except when q is tiny)
authors: O'Donnell Ryan, Wu Yi, Zhou Yuan
conference: "Arxiv"
year: 2009
bibkey: odonnell2009optimal
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/0912.0250"}
tags: ['ARXIV', 'LSH']
---
We study lower bounds for Locality Sensitive Hashing (LSH) in the strongest setting point sets in 0,1^d under the Hamming distance. Recall that here H is said to be an (r, cr, p, q)-sensitive hash family if all pairs x, y in 0,1^d with dist(x,y) at most r have probability at least p of collision under a randomly chosen h in H, whereas all pairs x, y in 0,1^d with dist(x,y) at least cr have probability at most q of collision. Typically, one considers d tending to infinity, with c fixed and q bounded away from 0. For its applications to approximate nearest neighbor search in high dimensions, the quality of an LSH family H is governed by how small its rho parameter rho = ln(1/p)/ln(1/q) is as a function of the parameter c. The seminal paper of Indyk and Motwani showed that for each c, the extremely simple family H = x -> x_i i in d achieves rho at most 1/c. The only known lower bound, due to Motwani, Naor, and Panigrahy, is that rho must be at least .46/c (minus o_d(1)). In this paper we show an optimal lower bound rho must be at least 1/c (minus o_d(1)). This lower bound for Hamming space yields a lower bound of 1/c^2 for Euclidean space (or the unit sphere) and 1/c for the Jaccard distance on sets; both of these match known upper bounds. Our proof is simple; the essence is that the noise stability of a boolean function at e^-t is a log-convex function of t.
