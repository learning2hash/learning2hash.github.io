---
layout: publication
title: Communication-efficient Jaccard Similarity For High-performance Distributed
  Genome Comparisons
authors: "Maciej Besta, Raghavendra Kanakagiri, Harun Mustafa, Mikhail Karasikov,\
  \ Gunnar R\xE4tsch, Torsten Hoefler, Edgar Solomonik"
conference: 2020 IEEE International Parallel and Distributed Processing Symposium
  (IPDPS)
year: 2020
bibkey: besta2019communication
citations: 63
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1911.04200'}]
tags: ["Scalability"]
short_authors: Besta et al.
---
The Jaccard similarity index is an important measure of the overlap of two
sets, widely used in machine learning, computational genomics, information
retrieval, and many other areas. We design and implement SimilarityAtScale, the
first communication-efficient distributed algorithm for computing the Jaccard
similarity among pairs of large datasets. Our algorithm provides an efficient
encoding of this problem into a multiplication of sparse matrices. Both the
encoding and sparse matrix product are performed in a way that minimizes data
movement in terms of communication and synchronization costs. We apply our
algorithm to obtain similarity among all pairs of a set of large samples of
genomes. This task is a key part of modern metagenomics analysis and an
evergrowing need due to the increasing availability of high-throughput DNA
sequencing data. The resulting scheme is the first to enable accurate Jaccard
distance derivations for massive datasets, using largescale distributed-memory
systems. We package our routines in a tool, called GenomeAtScale, that combines
the proposed algorithm with tools for processing input sequences. Our
evaluation on real data illustrates that one can use GenomeAtScale to
effectively employ tens of thousands of processors to reach new frontiers in
large-scale genomic and metagenomic analysis. While GenomeAtScale can be used
to foster DNA research, the more general underlying SimilarityAtScale algorithm
may be used for high-performance distributed similarity computations in other
data analytics application domains.