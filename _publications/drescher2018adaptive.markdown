---
layout: publication
title: The Adaptive Sampling Revisited
authors: Matthew Drescher, Guy Louchard, Yvik Swan
conference: Arxiv
year: 2018
bibkey: drescher2018adaptive
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1805.08043'}]
tags: []
short_authors: Matthew Drescher, Guy Louchard, Yvik Swan
---
The problem of estimating the number \(n\) of distinct keys of a large
collection of \(N\) data is well known in computer science. A classical algorithm
is the adaptive sampling (AS). \(n\) can be estimated by \(R.2^D\), where \(R\) is
the final bucket (cache) size and \(D\) is the final depth at the end of the
process. Several new interesting questions can be asked about AS (some of them
were suggested by P.Flajolet and popularized by J.Lumbroso). The distribution
of \(W=log (R2^D/n)\) is known, we rederive this distribution in a simpler way.
We provide new results on the moments of \(D\) and \(W\). We also analyze the final
cache size \(R\) distribution. We consider colored keys: assume that among the
\(n\) distinct keys, \(n_C\) do have color \(C\). We show how to estimate
\(p=\frac\{n_C\}\{n\}\). We also study colored keys with some multiplicity given by
some distribution function. We want to estimate mean an variance of this
distribution. Finally, we consider the case where neither colors nor
multiplicities are known. There we want to estimate the related parameters. An
appendix is devoted to the case where the hashing function provides bits with
probability different from \(1/2\).