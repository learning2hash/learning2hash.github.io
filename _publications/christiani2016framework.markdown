---
layout: publication
title: A Framework For Similarity Search With Space-time Tradeoffs Using Locality-sensitive Filtering
authors: Christiani Tobias
conference: "Arxiv"
year: 2016
bibkey: christiani2016framework
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1605.02687"}
tags: ['ARXIV', 'Independent', 'LSH']
---
We present a framework for similarity search based on Locality-Sensitive Filtering (LSF), generalizing the Indyk-Motwani (STOC 1998) Locality-Sensitive Hashing (LSH) framework to support space-time tradeoffs. Given a family of filters, defined as a distribution over pairs of subsets of space with certain locality-sensitivity properties, we can solve the approximate near neighbor problem in \(d\)-dimensional space for an \(n\)-point data set with query time \(dn^\&amp;\#123;\rho\_q+o(1)\&amp;\#125;\), update time \(dn^\&amp;\#123;\rho\_u+o(1)\&amp;\#125;\), and space usage $dn + n^&amp;\#123;1 + \rho\_u + o(1)&amp;\#125;$. The space-time tradeoff is tied to the tradeoff between query time and update time, controlled by the exponents \(\rho\_q, \rho\_u\) that are determined by the filter family. Locality-sensitive filtering was introduced by Becker et al. (SODA 2016) together with a framework yielding a single, balanced, tradeoff between query time and space, further relying on the assumption of an efficient oracle for the filter evaluation algorithm. We extend the LSF framework to support space-time tradeoffs and through a combination of existing techniques we remove the oracle assumption. Building on a filter family for the unit sphere by Laarhoven (arXiv 2015) we use a kernel embedding technique by Rahimi &amp; Recht (NIPS 2007) to show a solution to the \((r,cr)\)-near neighbor problem in \(\ell\_s^d\)-space for $0 < s \leq 2$ with query and update exponents \(\rho\_q=\frac\&amp;\#123;c^s(1+\lambda)^2\&amp;\#125;\&amp;\#123;(c^s+\lambda)^2\&amp;\#125;\) and \(\rho\_u=\frac\&amp;\#123;c^s(1-\lambda)^2\&amp;\#125;\&amp;\#123;(c^s+\lambda)^2\&amp;\#125;\) where \(\lambda\in[-1,1]\) is a tradeoff parameter. This result improves upon the space-time tradeoff of Kapralov (PODS 2015) and is shown to be optimal in the case of a balanced tradeoff. Finally, we show a lower bound for the space-time tradeoff on the unit sphere that matches Laarhoven's and our own upper bound in the case of random data.
