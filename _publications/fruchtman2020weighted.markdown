---
layout: publication
title: Weighted Adaptive Coding
authors: Aharon Fruchtman, Yoav Gross, Shmuel T. Klein, Dana Shapira
conference: Arxiv
year: 2020
bibkey: fruchtman2020weighted
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2005.08232'}]
tags: []
short_authors: Fruchtman et al.
---
Huffman coding is known to be optimal, yet its dynamic version may be even
more efficient in practice. A new variant of Huffman encoding has been proposed
recently, that provably always performs better than static Huffman coding by at
least \(m-1\) bits, where \(m\) denotes the size of the alphabet, and has a better
worst case than the standard dynamic Huffman coding. This paper introduces a
new generic coding method, extending the known static and dynamic variants and
including them as special cases. In fact, the generalization is applicable to
all statistical methods, including arithmetic coding. This leads then to the
formalization of a new adaptive coding method, which is provably always at
least as good as the best dynamic variant known to date. Moreover, we present
empirical results that show improvements over static and dynamic Huffman and
arithmetic coding achieved by the proposed method, even when the encoded file
includes the model description.