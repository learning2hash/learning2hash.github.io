---
layout: publication
title: Large-scale Compression Of Genomic Sequence Databases With The Burrows-wheeler
  Transform
authors: Anthony J. Cox, Markus J. Bauer, Tobias Jakobi, Giovanna Rosone
conference: Bioinformatics
year: 2012
bibkey: cox2012large
citations: 141
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1205.0192'}]
tags: ["Datasets", "Scalability"]
short_authors: Cox et al.
---
Motivation
  The Burrows-Wheeler transform (BWT) is the foundation of many algorithms for
compression and indexing of text data, but the cost of computing the BWT of
very large string collections has prevented these techniques from being widely
applied to the large sets of sequences often encountered as the outcome of DNA
sequencing experiments. In previous work, we presented a novel algorithm that
allows the BWT of human genome scale data to be computed on very moderate
hardware, thus enabling us to investigate the BWT as a tool for the compression
of such datasets.
  Results
  We first used simulated reads to explore the relationship between the level
of compression and the error rate, the length of the reads and the level of
sampling of the underlying genome and compare choices of second-stage
compression algorithm.
  We demonstrate that compression may be greatly improved by a particular
reordering of the sequences in the collection and give a novel `implicit
sorting' strategy that enables these benefits to be realised without the
overhead of sorting the reads. With these techniques, a 45x coverage of real
human genome sequence data compresses losslessly to under 0.5 bits per base,
allowing the 135.3Gbp of sequence to fit into only 8.2Gbytes of space (trimming
a small proportion of low-quality bases from the reads improves the compression
still further).
  This is more than 4 times smaller than the size achieved by a standard
BWT-based compressor (bzip2) on the untrimmed reads, but an important further
advantage of our approach is that it facilitates the building of compressed
full text indexes such as the FM-index on large-scale DNA sequence collections.