---
layout: publication
title: 'Stream Vbyte: Faster Byte-oriented Integer Compression'
authors: Daniel Lemire, Nathan Kurz, Christoph Rupp
conference: Information Processing Letters
year: 2017
bibkey: lemire2017stream
citations: 41
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1709.08990'}]
tags: ["Efficiency", "Memory Efficiency"]
short_authors: Daniel Lemire, Nathan Kurz, Christoph Rupp
---
Arrays of integers are often compressed in search engines. Though there are
many ways to compress integers, we are interested in the popular byte-oriented
integer compression techniques (e.g., VByte or Google's Varint-GB). They are
appealing due to their simplicity and engineering convenience. Amazon's
varint-G8IU is one of the fastest byte-oriented compression technique published
so far. It makes judicious use of the powerful single-instruction-multiple-data
(SIMD) instructions available in commodity processors. To surpass varint-G8IU,
we present Stream VByte, a novel byte-oriented compression technique that
separates the control stream from the encoded data. Like varint-G8IU, Stream
VByte is well suited for SIMD instructions. We show that Stream VByte decoding
can be up to twice as fast as varint-G8IU decoding over real data sets. In this
sense, Stream VByte establishes new speed records for byte-oriented integer
compression, at times exceeding the speed of the memcpy function. On a 3.4GHz
Haswell processor, it decodes more than 4 billion differentially-coded integers
per second from RAM to L1 cache.