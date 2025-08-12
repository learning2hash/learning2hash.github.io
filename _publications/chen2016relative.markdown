---
layout: publication
title: Relative Error Embeddings For The Gaussian Kernel Distance
authors: di Chen, Jeff M. Phillips
conference: Arxiv
year: 2016
bibkey: chen2016relative
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1602.05350'}]
tags: ["Distance Metric Learning"]
short_authors: di Chen, Jeff M. Phillips
---
A reproducing kernel can define an embedding of a data point into an infinite
dimensional reproducing kernel Hilbert space (RKHS). The norm in this space
describes a distance, which we call the kernel distance. The random Fourier
features (of Rahimi and Recht) describe an oblivious approximate mapping into
finite dimensional Euclidean space that behaves similar to the RKHS. We show in
this paper that for the Gaussian kernel the Euclidean norm between these mapped
to features has \((1+\epsilon)\)-relative error with respect to the kernel
distance. When there are \(n\) data points, we show that \(O((1/\epsilon^2)
log(n))\) dimensions of the approximate feature space are sufficient and
necessary.
  Without a bound on \(n\), but when the original points lie in \(\mathbb\{R\}^d\)
and have diameter bounded by \(\mathcal\{M\}\), then we show that \(O((d/\epsilon^2)
log(\mathcal\{M\}))\) dimensions are sufficient, and that this many are required,
up to \(log(1/\epsilon)\) factors.