---
layout: publication
title: Security Analysis Of A Self-embedding Fragile Image Watermark Scheme
authors: Xinhui Gong, Feng Yu, Xiaohong Zhao, Shihong Wang
conference: Arxiv
year: 2018
bibkey: gong2018security
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1812.11735'}]
tags: []
short_authors: Gong et al.
---
Recently, a self-embedding fragile watermark scheme based on reference-bits
interleaving and adaptive selection of embedding mode was proposed. Reference
bits are derived from the scrambled MSB bits of a cover image, and then are
combined with authentication bits to form the watermark bits for LSB embedding.
We find this algorithm has a feature of block independence of embedding
watermark such that it is vulnerable to a collage attack. In addition, because
the generation of authentication bits via hash function operations is not
related to secret keys, we analyze this algorithm by a multiple stego-image
attack. We find that the cost of obtaining all the permutation relations of
\(l\cdot b^2\) watermark bits of each block (i.e., equivalent permutation keys)
is about \((l\cdot b^2)!\) for the embedding mode \((m, l)\), where \(m\) MSB layers
of a cover image are used for generating reference bits and \(l\) LSB layers for
embedding watermark, and \(b\times b\) is the size of image block. The simulation
results and the statistical results demonstrate our analysis is effective.