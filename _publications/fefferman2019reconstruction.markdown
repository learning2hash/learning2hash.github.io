---
layout: publication
title: Reconstruction Of A Riemannian Manifold From Noisy Intrinsic Distances
authors: Charles Fefferman, Sergei Ivanov, Matti Lassas, Hariharan Narayanan
conference: SIAM Journal on Mathematics of Data Science
year: 2020
bibkey: fefferman2019reconstruction
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1905.07182'}]
tags: ["Distance Metric Learning"]
short_authors: Fefferman et al.
---
We consider reconstruction of a manifold, or, invariant manifold learning,
where a smooth Riemannian manifold \\(M\\) is determined from intrinsic distances
(that is, geodesic distances) of points in a discrete subset of \\(M\\). In the
studied problem the Riemannian manifold \\((M,g)\\) is considered as an abstract
metric space with intrinsic distances, not as an embedded submanifold of an
ambient Euclidean space. Let \\(\\{X_1,X_2,\dots,X_N\\}\\) bea set of \\(N\\) sample
points sampled randomly from an unknown Riemannian \\(M\\) manifold. We assume that
we are given the numbers \\(D_\{jk\}=d_M(X_j,X_k)+\eta_\{jk\}\\), where \\(j,k\in
\\{1,2,\dots,N\\}\\). Here, \\(d_M(X_j,X_k)\\) are geodesic distances, \\(\eta_\{jk\}\\) are
independent, identically distributed random variables such that \\(\mathbb E
e^\{|\eta_\{jk\}|\}\\) is finite. We show that when \\(N\\) is large enough, it is
possible to construct an approximation of the Riemannian manifold \\((M,g)\\) with
a large probability. This problem is a generalization of the geometric Whitney
problem with random measurement errors. We consider also the case when the
information on noisy distance \\(D_\{jk\}\\) of points \\(X_j\\) and \\(X_k\\) is missing
with some probability. In particular, we consider the case when we have no
information on points that are far away.