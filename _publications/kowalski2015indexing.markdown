---
layout: publication
title: Indexing Arbitrary-length \(k\)-mers In Sequencing Reads
authors: Tomasz Kowalski, Szymon Grabowski, Sebastian Deorowicz
conference: PLOS ONE
year: 2015
bibkey: kowalski2015indexing
citations: 17
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1502.01861'}]
tags: ["Efficiency"]
short_authors: Tomasz Kowalski, Szymon Grabowski, Sebastian Deorowicz
---
We propose a lightweight data structure for indexing and querying collections
of NGS reads data in main memory. The data structure supports the interface
proposed in the pioneering work by Philippe et al. for counting and locating
\(k\)-mers in sequencing reads. Our solution, PgSA (pseudogenome suffix array),
based on finding overlapping reads, is competitive to the existing algorithms
in the space use, query times, or both. The main applications of our index
include variant calling, error correction and analysis of reads from RNA-seq
experiments.