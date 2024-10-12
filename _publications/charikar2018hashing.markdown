---
layout: publication
title: Hashing-based-estimators For Kernel Density In High Dimensions
authors: Charikar Moses, Siminelakis Paris
conference: "Arxiv"
year: 2018
bibkey: charikar2018hashing
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1808.10530"}
tags: ['ARXIV', 'Independent']
---
Given a set of points \(P\subset \mathbb\&amp;\#123;R\&amp;\#125;^\&amp;\#123;d\&amp;\#125;\) and a kernel \(k\), the Kernel Density Estimate at a point \(x\in\mathbb\&amp;\#123;R\&amp;\#125;^\&amp;\#123;d\&amp;\#125;\) is defined as \(\mathrm\&amp;\#123;KDE\&amp;\#125;\_\&amp;\#123;P\&amp;\#125;(x)=\frac\&amp;\#123;1\&amp;\#125;\&amp;\#123;|P|\&amp;\#125;\sum\_\&amp;\#123;y\in P\&amp;\#125; k(x,y)\). We study the problem of designing a data structure that given a data set \(P\) and a kernel function, returns *approximations to the kernel density* of a query point in *sublinear time*. We introduce a class of unbiased estimators for kernel density implemented through locality-sensitive hashing, and give general theorems bounding the variance of such estimators. These estimators give rise to efficient data structures for estimating the kernel density in high dimensions for a variety of commonly used kernels. Our work is the first to provide data-structures with theoretical guarantees that improve upon simple random sampling in high dimensions.
