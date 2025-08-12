---
layout: publication
title: Vectorized Vbyte Decoding
authors: Jeff Plaisance, Nathan Kurz, Daniel Lemire
conference: Arxiv
year: 2015
bibkey: plaisance2015vectorized
citations: 24
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1503.07387'}]
tags: []
short_authors: Jeff Plaisance, Nathan Kurz, Daniel Lemire
---
We consider the ubiquitous technique of VByte compression, which represents
each integer as a variable length sequence of bytes. The low 7 bits of each
byte encode a portion of the integer, and the high bit of each byte is reserved
as a continuation flag. This flag is set to 1 for all bytes except the last,
and the decoding of each integer is complete when a byte with a high bit of 0
is encountered. VByte decoding can be a performance bottleneck especially when
the unpredictable lengths of the encoded integers cause frequent branch
mispredictions. Previous attempts to accelerate VByte decoding using SIMD
vector instructions have been disappointing, prodding search engines such as
Google to use more complicated but faster-to-decode formats for
performance-critical code. Our decoder (Masked VByte) is 2 to 4 times faster
than a conventional scalar VByte decoder, making the format once again
competitive with regard to speed.