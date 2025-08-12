---
layout: publication
title: 'Alibi: An Alignment-based Index For Genomic Datasets'
authors: Hector Ferrada, Travis Gagie, Tommi Hirvola, Simon J. Puglisi
conference: Arxiv
year: 2013
bibkey: ferrada2013alibi
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1307.6462'}]
tags: ["Datasets"]
short_authors: Ferrada et al.
---
With current hardware and software, a standard computer can now hold in RAM
an index for approximate pattern matching on about half a dozen human genomes.
Sequencing technologies have improved so quickly, however, that scientists will
soon demand indexes for thousands of genomes. Whereas most researchers who have
addressed this problem have proposed completely new kinds of indexes, we
recently described a simple technique that scales standard indexes to work on
more genomes. Our main idea was to filter the dataset with LZ77, build a
standard index for the filtered file, and then create a hybrid of that standard
index and an LZ77-based index. In this paper we describe how to our technique
to use alignments instead of LZ77, in order to simplify and speed up both
preprocessing and random access.