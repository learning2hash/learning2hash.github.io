---
layout: publication
title: Near Input Sparsity Time Kernel Embeddings Via Adaptive Sampling
authors: David P. Woodruff, Amir Zandieh
conference: Arxiv
year: 2020
bibkey: woodruff2020near
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2007.03927'}]
tags: ["Scalability"]
short_authors: David P. Woodruff, Amir Zandieh
---
To accelerate kernel methods, we propose a near input sparsity time algorithm
for sampling the high-dimensional feature space implicitly defined by a kernel
transformation. Our main contribution is an importance sampling method for
subsampling the feature space of a degree \(q\) tensoring of data points in
almost input sparsity time, improving the recent oblivious sketching method of
(Ahle et al., 2020) by a factor of \(q^\{5/2\}/\epsilon^2\). This leads to a
subspace embedding for the polynomial kernel, as well as the Gaussian kernel,
with a target dimension that is only linearly dependent on the statistical
dimension of the kernel and in time which is only linearly dependent on the
sparsity of the input dataset. We show how our subspace embedding bounds imply
new statistical guarantees for kernel ridge regression. Furthermore, we
empirically show that in large-scale regression tasks, our algorithm
outperforms state-of-the-art kernel approximation methods.