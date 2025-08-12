---
layout: publication
title: Improving Run Length Encoding By Preprocessing
authors: Sven Fiergolla, Petra Wolf
conference: 2021 Data Compression Conference (DCC)
year: 2021
bibkey: fiergolla2021improving
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2101.05329'}]
tags: ["Efficiency", "Memory Efficiency"]
short_authors: Sven Fiergolla, Petra Wolf
---
The Run Length Encoding (RLE) compression method is a long standing simple
lossless compression scheme which is easy to implement and achieves a good
compression on input data which contains repeating consecutive symbols. In its
pure form RLE is not applicable on natural text or other input data with short
sequences of identical symbols. We present a combination of preprocessing steps
that turn arbitrary input data in a byte-wise encoding into a bit-string which
is highly suitable for RLE compression. The main idea is to first read all most
significant bits of the input byte-string, followed by the second most
significant bit, and so on. We combine this approach by a dynamic byte
remapping as well as a Burrows-Wheeler-Scott transform on a byte level.
Finally, we apply a Huffman Encoding on the output of the bit-wise RLE encoding
to allow for more dynamic lengths of code words encoding runs of the RLE. With
our technique we can achieve a lossless average compression which is better
than the standard RLE compression by a factor of 8 on average.