---
layout: publication
title: Sparse Convolution For Approximate Sparse Instance
authors: Xiaoxiao Li, Zhao Song, Guangyi Zhang
conference: Arxiv
year: 2023
bibkey: li2023sparse
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2306.02381'}]
tags: []
short_authors: Xiaoxiao Li, Zhao Song, Guangyi Zhang
---
Computing the convolution \(A \star B\) of two vectors of dimension \(n\) is one
of the most important computational primitives in many fields. For the
non-negative convolution scenario, the classical solution is to leverage the
Fast Fourier Transform whose time complexity is \(O(n log n)\). However, the
vectors \(A\) and \(B\) could be very sparse and we can exploit such property to
accelerate the computation to obtain the result. In this paper, we show that
when \(\|A \star B\|_\{\geq c_1\} = k\) and \(\|A \star B\|_\{\leq c_2\} = n-k\) holds,
we can approximately recover the all index in \(\mathrm\{supp\}_\{\geq c_1\}(A \star
B)\) with point-wise error of \(o(1)\) in \(O(k log (n) log(k)log(k/\delta))\)
time. We further show that we can iteratively correct the error and recover all
index in \(\mathrm\{supp\}_\{\geq c_1\}(A \star B)\) correctly in \(O(k log(n)
log^2(k) (log(1/\delta) + loglog(k)))\) time.