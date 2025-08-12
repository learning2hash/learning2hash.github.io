---
layout: publication
title: Efficient Compression Of Long Arbitrary Sequences With No Reference At The
  Encoder
authors: Yuval Cassuto, Jacob Ziv
conference: IEEE Transactions on Information Theory
year: 2020
bibkey: cassuto2020efficient
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2002.09893'}]
tags: ["Efficiency", "Memory Efficiency"]
short_authors: Yuval Cassuto, Jacob Ziv
---
In a distributed information application an encoder compresses an arbitrary
vector while a similar reference vector is available to the decoder as side
information. For the Hamming-distance similarity measure, and when guaranteed
perfect reconstruction is required, we present two contributions to the
solution of this problem. One result shows that when a set of potential
reference vectors is available to the encoder, lower compression rates can be
achieved when the set satisfies a certain clustering property. Another result
reduces the best known decoding complexity from exponential in the vector
length \(n\) to \(O(n^\{1.5\})\) by generalized concatenation of inner coset codes
and outer error-correcting codes. One potential application of the results is
the compression of DNA sequences, where similar (but not identical) reference
vectors are shared among senders and receivers.