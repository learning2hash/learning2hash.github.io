---
layout: publication
title: Parallel Decompression Of Gzip-compressed Files And Random Access To DNA Sequences
authors: "Ma\xEBl Kerbiriou, Rayan Chikhi"
conference: 2019 IEEE International Parallel and Distributed Processing Symposium
  Workshops (IPDPSW)
year: 2019
bibkey: kerbiriou2019parallel
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1905.07224'}]
tags: []
short_authors: "Ma\xEBl Kerbiriou, Rayan Chikhi"
---
Decompressing a file made by the gzip program at an arbitrary location is in
principle impossible, due to the nature of the DEFLATE compression algorithm.
Consequently, no existing program can take advantage of parallelism to rapidly
decompress large gzip-compressed files. This is an unsatisfactory bottleneck,
especially for the analysis of large sequencing data experiments. Here we
propose a parallel algorithm and an implementation, pugz, that performs fast
and exact decompression of any text file. We show that pugz is an order of
magnitude faster than gunzip, and 5x faster than a highly-optimized sequential
implementation (libdeflate). We also study the related problem of random access
to compressed data. We give simple models and experimental results that shed
light on the structure of gzip-compressed files containing DNA sequences.
Preliminary results show that random access to sequences within a
gzip-compressed FASTQ file is almost always feasible at low compression levels,
yet is approximate at higher compression levels.