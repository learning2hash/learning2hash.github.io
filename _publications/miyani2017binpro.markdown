---
layout: publication
title: 'Binpro: A Tool For Binary Source Code Provenance'
authors: Dhaval Miyani, Zhen Huang, David Lie
conference: Arxiv
year: 2017
bibkey: miyani2017binpro
citations: 16
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1711.00830'}]
tags: []
short_authors: Dhaval Miyani, Zhen Huang, David Lie
---
Enforcing open source licenses such as the GNU General Public License (GPL),
analyzing a binary for possible vulnerabilities, and code maintenance are all
situations where it is useful to be able to determine the source code
provenance of a binary. While previous work has either focused on computing
binary-to-binary similarity or source-to-source similarity, BinPro is the first
work we are aware of to tackle the problem of source-to-binary similarity.
BinPro can match binaries with their source code even without knowing which
compiler was used to produce the binary, or what optimization level was used
with the compiler. To do this, BinPro utilizes machine learning to compute
optimal code features for determining binary-to-source similarity and a static
analysis pipeline to extract and compute similarity based on those features.
Our experiments show that on average BinPro computes a similarity of 81% for
matching binaries and source code of the same applications, and an average
similarity of 25% for binaries and source code of similar but different
applications. This shows that BinPro's similarity score is useful for
determining if a binary was derived from a particular source code.