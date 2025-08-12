---
layout: publication
title: Matching Reads To Many Genomes With The \(r\)-index
authors: Taher Mun, Alan Kuhnle, Christina Boucher, Travis Gagie, Ben Langmead, Giovanni
  Manzini
conference: Journal of Computational Biology
year: 2020
bibkey: mun2019matching
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1908.01263'}]
tags: []
short_authors: Mun et al.
---
The \\(r\\)-index is a tool for compressed indexing of genomic databases for
exact pattern matching, which can be used to completely align reads that
perfectly match some part of a genome in the database or to find seeds for
reads that do not. This paper shows how to download and install the programs
ri-buildfasta and ri-align; how to call ri-buildfasta on a FASTA file to build
an \\(r\\)-index for that file; and how to query that index with ri-align.
  Availability: The source code for these programs is released under GPLv3 and
available at https://github.com/alshai/r-index .