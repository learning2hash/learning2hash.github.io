---
layout: publication
title: Rd-optimized Trit-plane Coding Of Deep Compressed Image Latent Tensors
authors: Seungmin Jeon, Jae-Han Lee, Chang-Su Kim
conference: Arxiv
year: 2022
bibkey: jeon2022rd
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2203.13467'}]
tags: []
short_authors: Seungmin Jeon, Jae-Han Lee, Chang-Su Kim
---
DPICT is the first learning-based image codec supporting fine granular
scalability. In this paper, we describe how to implement two key components of
DPICT efficiently: trit-plane slicing and rate-distortion-optimized
(RD-optimized) coding. In DPICT, we transform an image into a latent tensor,
represent the tensor in ternary digits (trits), and encode the trits in the
decreasing order of significance. For entropy encoding, it is necessary to
compute the probability of each trit, which demands high time complexity in
both the encoder and the decoder. To reduce the complexity, we develop a
parallel computing scheme for the probabilities, which is described in detail
with pseudo-codes. Moreover, we compare the trit-plane slicing in DPICT with
the alternative bit-plane slicing. Experimental results show that the time
complexity is reduced significantly by the parallel computing and that the
trit-plane slicing provides better RD performances than the bit-plane slicing.