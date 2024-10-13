---
layout: publication
title: Fast Private Kernel Density Estimation Via Locality Sensitive Quantization
authors: Wagner Tal, Naamad Yonatan, Mishra Nina
conference: "Arxiv"
year: 2023
bibkey: wagner2023fast
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2307.01877"}
tags: ['ARXIV', 'Independent', 'Quantisation']
---
We study efficient mechanisms for differentially private kernel density
estimation (DP-KDE). Prior work for the Gaussian kernel described algorithms
that run in time exponential in the number of dimensions \\{d\\}. This paper breaks
the exponential barrier, and shows how the KDE can privately be approximated in
time linear in \\{d\\}, making it feasible for high-dimensional data. We also
present improved bounds for low-dimensional data.
  Our results are obtained through a general framework, which we term Locality
Sensitive Quantization (LSQ), for constructing private KDE mechanisms where
existing KDE approximation techniques can be applied. It lets us leverage
several efficient non-private KDE methods -- like Random Fourier Features, the
Fast Gauss Transform, and Locality Sensitive Hashing -- and ``privatize'' them
in a black-box manner. Our experiments demonstrate that our resulting DP-KDE
mechanisms are fast and accurate on large datasets in both high and low
dimensions.
