---
layout: publication
title: Prefix-free Parsing For Building Big Bwts
authors: Christina Boucher, Travis Gagie, Alan Kuhnle, Ben Langmead, Giovanni Manzini,
  Taher Mun
conference: Algorithms for Molecular Biology
year: 2019
bibkey: boucher2018prefix
citations: 59
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1803.11245'}]
tags: []
short_authors: Boucher et al.
---
High-throughput sequencing technologies have led to explosive growth of
genomic databases; one of which will soon reach hundreds of terabytes. For many
applications we want to build and store indexes of these databases but
constructing such indexes is a challenge. Fortunately, many of these genomic
databases are highly-repetitive---a characteristic that can be exploited to
ease the computation of the Burrows-Wheeler Transform (BWT), which underlies
many popular indexes. In this paper, we introduce a preprocessing algorithm,
referred to as \{\em prefix-free parsing\}, that takes a text \\(T\\) as input, and
in one-pass generates a dictionary \\(D\\) and a parse \\(P\\) of \\(T\\) with the property
that the BWT of \\(T\\) can be constructed from \\(D\\) and \\(P\\) using workspace
proportional to their total size and \\(O (|T|)\\)-time. Our experiments show that
\\(D\\) and \\(P\\) are significantly smaller than \\(T\\) in practice, and thus, can fit
in a reasonable internal memory even when \\(T\\) is very large. In particular, we
show that with prefix-free parsing we can build an 131-megabyte run-length
compressed FM-index (restricted to support only counting and not locating) for
1000 copies of human chromosome 19 in 2 hours using 21 gigabytes of memory,
suggesting that we can build a 6.73 gigabyte index for 1000 complete
human-genome haplotypes in approximately 102 hours using about 1 terabyte of
memory.