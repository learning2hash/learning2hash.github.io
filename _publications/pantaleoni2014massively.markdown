---
layout: publication
title: A Massively Parallel Algorithm For Constructing The BWT Of Large String Sets
authors: Jacopo Pantaleoni
conference: Arxiv
year: 2014
bibkey: pantaleoni2014massively
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1410.0562'}]
tags: []
short_authors: Jacopo Pantaleoni
---
We present a new scalable, lightweight algorithm to incrementally construct
the BWT and FM-index of large string sets such as those produced by Next
Generation Sequencing. The algorithm is designed for massive parallelism and
can effectively exploit the combination of low capacity high bandwidth memory
and slower external system memory typical of GPU accelerated systems.
Particularly, for a string set of n characters from an alphabet with \sigma
symbols, it uses a constant amount of high-bandwidth memory and at most 3n
log(\sigma) bits of system memory. Given that deep memory hierarchies are
becoming a pervasive trait of high performance computing architectures, we
believe this to be a relevant feature. The implementation can handle reads of
arbitrary length and is up to 2 and respectively 6.5 times faster than
state-of-the-art for short and long genomic reads