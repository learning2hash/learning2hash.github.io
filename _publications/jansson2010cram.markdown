---
layout: publication
title: 'CRAM: Compressed Random Access Memory'
authors: Jesper Jansson, Kunihiko Sadakane, Wing-kin Sung
conference: Lecture Notes in Computer Science
year: 2012
bibkey: jansson2010cram
citations: 15
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1011.1708'}]
tags: ["Memory Efficiency"]
short_authors: Jesper Jansson, Kunihiko Sadakane, Wing-kin Sung
---
We present a new data structure called the *Compressed Random Access
Memory* (CRAM) that can store a dynamic string \\(T\\) of characters, e.g.,
representing the memory of a computer, in compressed form while achieving
asymptotically almost-optimal bounds (in terms of empirical entropy) on the
compression ratio. It allows short substrings of \\(T\\) to be decompressed and
retrieved efficiently and, significantly, characters at arbitrary positions of
\\(T\\) to be modified quickly during execution *without decompressing the
entire string*. This can be regarded as a new type of data compression that can
update a compressed file directly. Moreover, at the cost of slightly increasing
the time spent per operation, the CRAM can be extended to also support
insertions and deletions. Our key observation that the empirical entropy of a
string does not change much after a small change to the string, as well as our
simple yet efficient method for maintaining an array of variable-length blocks
under length modifications, may be useful for many other applications as well.