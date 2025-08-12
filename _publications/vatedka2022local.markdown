---
layout: publication
title: Local Decoding In Distributed Compression
authors: Shashank Vatedka, Venkat Chandar, Aslan Tchamkerten
conference: IEEE Journal on Selected Areas in Information Theory
year: 2022
bibkey: vatedka2022local
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2204.07518'}]
tags: []
short_authors: Shashank Vatedka, Venkat Chandar, Aslan Tchamkerten
---
It was recently shown that the lossless compression of a single source \(X^n\)
is achievable with a notion of strong locality; any \(X_i\) can be decoded from a
constant number of compressed bits, with a vanishing in \(n\) probability of
error. By contrast, we show that for two separately encoded sources
\((X^n,Y^n)\), lossless compression and strong locality is generally not
possible. Specifically, we show that for the class of ``confusable'' sources,
strong locality cannot be achieved whenever one of the sources is compressed
below its entropy. Irrespective of \(n\), for some index \(i\) the probability of
error of decoding \((X_i,Y_i)\) is lower bounded by \(2^\{-O(d)\}\), where \(d\)
denotes the number of compressed bits accessed by the local decoder.
Conversely, if the source is not confusable, strong locality is possible even
if one of the sources is compressed below its entropy. Results extend to an
arbitrary number of sources.