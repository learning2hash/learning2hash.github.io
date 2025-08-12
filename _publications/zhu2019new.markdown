---
layout: publication
title: A New Capacity-achieving Private Information Retrieval Scheme With (almost)
  Optimal File Length For Coded Servers
authors: Jinbao Zhu, Qifa Yan, Chao Qi, Xiaohu Tang
conference: IEEE Transactions on Information Forensics and Security
year: 2019
bibkey: zhu2019new
citations: 38
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1903.06921'}]
tags: ["Privacy & Security"]
short_authors: Zhu et al.
---
In a distributed storage system, private information retrieval (PIR)
guarantees that a user retrieves one file from the system without revealing any
information about the identity of its interested file to any individual server.
In this paper, we investigate \((N,K,M)\) coded sever model of PIR, where each of
\(M\) files is distributed to the \(N\) servers in the form of \((N,K)\) maximum
distance separable (MDS) code for some \(N>K\) and \(M>1\). As a result, we propose
a new capacity-achieving \((N,K,M)\) coded linear PIR scheme such that it can be
implemented with file length \(\frac\{K(N-K)\}\{\gcd(N,K)\}\), which is much smaller
than the previous best result \(K\big(\frac\{N\}\{\gcd(N,K)\}\big)^\{M-1\}\). Notably,
among all the capacity-achieving coded linear PIR schemes, we show that the
file length is optimal if \(M>\big\lfloor
\frac\{K\}\{\gcd(N,K)\}-\frac\{K\}\{N-K\}\big\rfloor+1\), and within a multiplicative
gap \(\frac\{K\}\{\gcd(N,K)\}\) of a lower bound on the minimum file length
otherwise.