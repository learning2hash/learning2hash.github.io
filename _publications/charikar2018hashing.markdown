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
<p>Given a set of points <span class="math inline">\(P\subset
\mathbb{R}^{d}\)</span> and a kernel <span
class="math inline">\(k\)</span>, the Kernel Density Estimate at a point
<span class="math inline">\(x\in\mathbb{R}^{d}\)</span> is defined as
<span class="math inline">\(\mathrm{KDE}_{P}(x)=\frac{1}{|P|}\sum_{y\in
P} k(x,y)\)</span>. We study the problem of designing a data structure
that given a data set <span class="math inline">\(P\)</span> and a
kernel function, returns <em>approximations to the kernel density</em>
of a query point in <em>sublinear time</em>. We introduce a class of
unbiased estimators for kernel density implemented through
locality-sensitive hashing, and give general theorems bounding the
variance of such estimators. These estimators give rise to efficient
data structures for estimating the kernel density in high dimensions for
a variety of commonly used kernels. Our work is the first to provide
data-structures with theoretical guarantees that improve upon simple
random sampling in high dimensions.</p>
