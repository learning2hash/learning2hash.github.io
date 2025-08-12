---
layout: publication
title: A Distributed Block Chebyshev-davidson Algorithm For Parallel Spectral Clustering
authors: Qiyuan Pang, Haizhao Yang
conference: Arxiv
year: 2022
bibkey: pang2022distributed
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2212.04443'}]
tags: ["Efficiency", "Scalability"]
short_authors: Qiyuan Pang, Haizhao Yang
---
We develop a distributed Block Chebyshev-Davidson algorithm to solve
large-scale leading eigenvalue problems for spectral analysis in spectral
clustering. First, the efficiency of the Chebyshev-Davidson algorithm relies on
the prior knowledge of the eigenvalue spectrum, which could be expensive to
estimate. This issue can be lessened by the analytic spectrum estimation of the
Laplacian or normalized Laplacian matrices in spectral clustering, making the
proposed algorithm very efficient for spectral clustering. Second, to make the
proposed algorithm capable of analyzing big data, a distributed and parallel
version has been developed with attractive scalability. The speedup by parallel
computing is approximately equivalent to \(\sqrt\{p\}\), where \(p\) denotes the
number of processes. \{Numerical results will be provided to demonstrate its
efficiency in spectral clustering and scalability advantage over existing
eigensolvers used for spectral clustering in parallel computing environments.\}