---
layout: publication
title: Encoding Of Probability Distributions For Asymmetric Numeral Systems
authors: Jarek Duda
conference: Arxiv
year: 2021
bibkey: duda2021encoding
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2106.06438'}]
tags: []
short_authors: Jarek Duda
---
Many data compressors regularly encode probability distributions for entropy
coding - requiring minimal description length type of optimizations. Canonical
prefix/Huffman coding usually just writes lengths of bit sequences, this way
approximating probabilities with powers-of-2. Operating on more accurate
probabilities usually allows for better compression ratios, and is possible
e.g. using arithmetic coding and Asymmetric Numeral Systems family. Especially
the multiplication-free tabled variant of the latter (tANS) builds automaton
often replacing Huffman coding due to better compression at similar
computational cost - e.g. in popular Facebook Zstandard and Apple LZFSE
compressors. There is discussed encoding of probability distributions for such
applications, especially using Pyramid Vector Quantizer(PVQ)-based approach
with deformation, bucket approximation, prefix trees, improving accuracy with
additional bits, also tuned symbol spread for tANS.