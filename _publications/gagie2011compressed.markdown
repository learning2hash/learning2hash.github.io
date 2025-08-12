---
layout: publication
title: A Compressed Self-index For Genomic Databases
authors: "Travis Gagie, Juha K\xE4rkk\xE4inen, Yakov Nekrich, Simon J. Puglisi"
conference: Arxiv
year: 2011
bibkey: gagie2011compressed
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1111.1355'}]
tags: []
short_authors: Gagie et al.
---
Advances in DNA sequencing technology will soon result in databases of
thousands of genomes. Within a species, individuals' genomes are almost exact
copies of each other; e.g., any two human genomes are 99.9% the same. Relative
Lempel-Ziv (RLZ) compression takes advantage of this property: it stores the
first genome uncompressed or as an FM-index, then compresses the other genomes
with a variant of LZ77 that copies phrases only from the first genome. RLZ
achieves good compression and supports fast random access; in this paper we
show how to support fast search as well, thus obtaining an efficient compressed
self-index.