---
layout: publication
title: Random Projections On Manifolds Of Symmetric Positive Definite Matrices For
  Image Classification
authors: Azadeh Alavi, Arnold Wiliem, Kun Zhao, Brian C. Lovell, Conrad Sanderson
conference: IEEE Winter Conference on Applications of Computer Vision
year: 2014
bibkey: alavi2014random
citations: 13
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1403.0700'}]
tags: ["Evaluation"]
short_authors: Alavi et al.
---
Recent advances suggest that encoding images through Symmetric Positive
Definite (SPD) matrices and then interpreting such matrices as points on
Riemannian manifolds can lead to increased classification performance. Taking
into account manifold geometry is typically done via (1) embedding the
manifolds in tangent spaces, or (2) embedding into Reproducing Kernel Hilbert
Spaces (RKHS). While embedding into tangent spaces allows the use of existing
Euclidean-based learning algorithms, manifold shape is only approximated which
can cause loss of discriminatory information. The RKHS approach retains more of
the manifold structure, but may require non-trivial effort to kernelise
Euclidean-based learning algorithms. In contrast to the above approaches, in
this paper we offer a novel solution that allows SPD matrices to be used with
unmodified Euclidean-based learning algorithms, with the true manifold shape
well-preserved. Specifically, we propose to project SPD matrices using a set of
random projection hyperplanes over RKHS into a random projection space, which
leads to representing each matrix as a vector of projection coefficients.
Experiments on face recognition, person re-identification and texture
classification show that the proposed approach outperforms several recent
methods, such as Tensor Sparse Coding, Histogram Plus Epitome, Riemannian
Locality Preserving Projection and Relational Divergence Classification.