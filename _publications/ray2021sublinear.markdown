---
layout: publication
title: Sublinear Time Approximation Of Text Similarity Matrices
authors: Archan Ray, Nicholas Monath, Andrew Mccallum, Cameron Musco
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2022
bibkey: ray2021sublinear
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2112.09631'}]
tags: ["AAAI"]
short_authors: Ray et al.
---
We study algorithms for approximating pairwise similarity matrices that arise
in natural language processing. Generally, computing a similarity matrix for
\\(n\\) data points requires \\(Ω(n^2)\\) similarity computations. This quadratic
scaling is a significant bottleneck, especially when similarities are computed
via expensive functions, e.g., via transformer models. Approximation methods
reduce this quadratic complexity, often by using a small subset of exactly
computed similarities to approximate the remainder of the complete pairwise
similarity matrix.
  Significant work focuses on the efficient approximation of positive
semidefinite (PSD) similarity matrices, which arise e.g., in kernel methods.
However, much less is understood about indefinite (non-PSD) similarity
matrices, which often arise in NLP. Motivated by the observation that many of
these matrices are still somewhat close to PSD, we introduce a generalization
of the popular Nystr\"\{o\}m method to the indefinite setting. Our algorithm can
be applied to any similarity matrix and runs in sublinear time in the size of
the matrix, producing a rank-\\(s\\) approximation with just \\(O(ns)\\) similarity
computations.
  We show that our method, along with a simple variant of CUR decomposition,
performs very well in approximating a variety of similarity matrices arising in
NLP tasks. We demonstrate high accuracy of the approximated similarity matrices
in the downstream tasks of document classification, sentence similarity, and
cross-document coreference.