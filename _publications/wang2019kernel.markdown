---
layout: publication
title: A Kernel-independent Treecode Based On Barycentric Lagrange Interpolation
authors: Lei Wang, Robert Krasny, Svetlana Tlupova
conference: Communications in Computational Physics
year: 2020
bibkey: wang2019kernel
citations: 28
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1902.02250'}]
tags: []
short_authors: Lei Wang, Robert Krasny, Svetlana Tlupova
---
A kernel-independent treecode (KITC) is presented for fast summation of
particle interactions. The method employs barycentric Lagrange interpolation at
Chebyshev points to approximate well-separated particle-cluster interactions.
The KITC requires only kernel evaluations, is suitable for non-oscillatory
kernels, and it utilizes a scale-invariance property of barycentric Lagrange
interpolation. For a given level of accuracy, the treecode reduces the
operation count for pairwise interactions from \\(O(N^2)\\) to \\(O(Nlog N)\\), where
\\(N\\) is the number of particles in the system. The algorithm is demonstrated for
systems of regularized Stokeslets and rotlets in 3D, and numerical results show
the treecode performance in terms of error, CPU time, and memory consumption.
The KITC is a relatively simple algorithm with low memory consumption, and this
enables a straightforward OpenMP parallelization.