---
layout: publication
title: Burrows-wheeler Transform For Terabases
authors: "Jouni Sir\xE9n"
conference: 2016 Data Compression Conference (DCC)
year: 2016
bibkey: "sir\xE9n2015burrows"
citations: 20
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1511.00898'}]
tags: []
short_authors: "Jouni Sir\xE9n"
---
In order to avoid the reference bias introduced by mapping reads to a
reference genome, bioinformaticians are investigating reference-free methods
for analyzing sequenced genomes. With large projects sequencing thousands of
individuals, this raises the need for tools capable of handling terabases of
sequence data. A key method is the Burrows-Wheeler transform (BWT), which is
widely used for compressing and indexing reads. We propose a practical
algorithm for building the BWT of a large read collection by merging the BWTs
of subcollections. With our 2.4 Tbp datasets, the algorithm can merge 600
Gbp/day on a single system, using 30 gigabytes of memory overhead on top of the
run-length encoded BWTs.