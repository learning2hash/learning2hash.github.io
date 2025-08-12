---
layout: publication
title: On Optimally Partitioning Variable-byte Codes
authors: Giulio Ermanno Pibiri, Rossano Venturini
conference: IEEE Transactions on Knowledge and Data Engineering
year: 2019
bibkey: pibiri2018optimally
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1804.10949'}]
tags: ["Evaluation"]
short_authors: Giulio Ermanno Pibiri, Rossano Venturini
---
The ubiquitous Variable-Byte encoding is one of the fastest compressed
representation for integer sequences. However, its compression ratio is usually
not competitive with other more sophisticated encoders, especially when the
integers to be compressed are small that is the typical case for inverted
indexes. This paper shows that the compression ratio of Variable-Byte can be
improved by 2x by adopting a partitioned representation of the inverted lists.
This makes Variable-Byte surprisingly competitive in space with the best
bit-aligned encoders, hence disproving the folklore belief that Variable-Byte
is space-inefficient for inverted index compression. Despite the significant
space savings, we show that our optimization almost comes for free, given that:
we introduce an optimal partitioning algorithm that does not affect indexing
time because of its linear-time complexity; we show that the query processing
speed of Variable-Byte is preserved, with an extensive experimental analysis
and comparison with several other state-of-the-art encoders.