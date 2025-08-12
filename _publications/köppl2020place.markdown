---
layout: publication
title: In-place Bijective Burrows-wheeler Transforms
authors: "Dominik K\xF6ppl, Daiki Hashimoto, Diptarama Hendrian, Ayumi Shinohara"
conference: Arxiv
year: 2020
bibkey: "k\xF6ppl2020place"
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2004.12590'}]
tags: []
short_authors: "K\xF6ppl et al."
---
One of the most well-known variants of the Burrows-Wheeler transform (BWT)
[Burrows and Wheeler, 1994] is the bijective BWT (BBWT) [Gil and Scott, arXiv
2012], which applies the extended BWT (EBWT) [Mantaci et al., TCS 2007] to the
multiset of Lyndon factors of a given text. Since the EBWT is invertible, the
BBWT is a bijective transform in the sense that the inverse image of the EBWT
restores this multiset of Lyndon factors such that the original text can be
obtained by sorting these factors in non-increasing order. In this paper, we
present algorithms constructing or inverting the BBWT in-place using quadratic
time. We also present conversions from the BBWT to the BWT, or vice versa,
either (a) in-place using quadratic time, or (b) in the run-length compressed
setting using \(O(n \lg r / \lg \lg r)\) time with \(O(r \lg n)\) bits of words,
where \(r\) is the sum of character runs in the BWT and the BBWT.