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
Given a set of points \{&#37; raw &#37;\}\\(P\subset \mathbb\{R\}^\{d\}\\)\{&#37; endraw &#37;\} and a kernel \{&#37; raw &#37;\}\\(k\\)\{&#37; endraw &#37;\}, the Kernel Density Estimate at a point \{&#37; raw &#37;\}\\(x\in\mathbb\{R\}^\{d\}\\)\{&#37; endraw &#37;\} is defined as \{&#37; raw &#37;\}\\(\mathrm\{KDE\}\_\{P\}(x)=\frac\{1\}\{|P|\}\sum\_\{y\in P\} k(x,y)\\)\{&#37; endraw &#37;\}. We study the problem of designing a data structure that given a data set \{&#37; raw &#37;\}\\(P\\)\{&#37; endraw &#37;\} and a kernel function, returns *approximations to the kernel density* of a query point in *sublinear time*. We introduce a class of unbiased estimators for kernel density implemented through locality-sensitive hashing, and give general theorems bounding the variance of such estimators. These estimators give rise to efficient data structures for estimating the kernel density in high dimensions for a variety of commonly used kernels. Our work is the first to provide data-structures with theoretical guarantees that improve upon simple random sampling in high dimensions.
