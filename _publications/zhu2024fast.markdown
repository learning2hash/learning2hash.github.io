---
layout: publication
title: "Fast Exact Retrieval for Nearest-neighbor Lookup (FERN)"
authors: Zhu Richard
conference: Arxiv
year: 2024
bibkey: zhu2024fast
additional_links:
- {name: "Paper", url: "https://arxiv.org/abs/2405.04435"}
  - {name: "Code", url: "https://github.com/RichardZhu123/ferns}"}
tags: ['ARXIV', 'GAN']
---
Exact nearest neighbor search is a computationally intensive process, and even its simpler sibling -- vector retrieval -- can be computationally complex. This is exacerbated when retrieving vectors which have high-dimension $d$ relative to the number of vectors, $N$, in the database. Exact nearest neighbor retrieval has been generally acknowledged to be a $O(Nd)$ problem with no sub-linear solutions. Attention has instead shifted towards Approximate Nearest-Neighbor (ANN) retrieval techniques, many of which have sub-linear or even logarithmic time complexities. However, if our intuition from binary search problems (e.g. $d=1$ vector retrieval) carries, there ought to be a way to retrieve an organized representation of vectors without brute-forcing our way to a solution. For low dimension (e.g. $d=2$ or $d=3$ cases), \texttt{kd-trees} provide a $O(d\log N)$ algorithm for retrieval. Unfortunately the algorithm deteriorates rapidly to a $O(dN)$ solution at high dimensions (e.g. $k=128$), in practice. We propose a novel algorithm for logarithmic Fast Exact Retrieval for Nearest-neighbor lookup (FERN), inspired by \texttt{kd-trees}. The algorithm achieves $O(d\log N)$ look-up with 100\% recall on 10 million $d=128$ uniformly randomly generated vectors.\footnote{Code available at https://github.com/RichardZhu123/ferns}