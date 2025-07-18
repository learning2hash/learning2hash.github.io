---
layout: publication
title: Enabling Fast, Accurate, And Efficient Real-time Genome Analysis Via New Algorithms
  And Techniques
authors: Firtina Can
conference: IEEE Transactions on Computers
year: 2025
bibkey: firtina2025enabling
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2503.02997'}]
tags: [Hashing Methods, Efficiency And Optimization, Similarity Search, Tools & Libraries,
  Evaluation, Robustness]
---
The advent of high-throughput sequencing technologies has revolutionized
genome analysis by enabling the rapid and cost-effective sequencing of large
genomes. Despite these advancements, the increasing complexity and volume of
genomic data present significant challenges related to accuracy, scalability,
and computational efficiency. These challenges are mainly due to various forms
of unwanted and unhandled variations in sequencing data, collectively referred
to as noise. In this dissertation, we address these challenges by providing a
deep understanding of different types of noise in genomic data and developing
techniques to mitigate the impact of noise on genome analysis.
  First, we introduce BLEND, a noise-tolerant hashing mechanism that quickly
identifies both exactly matching and highly similar sequences with arbitrary
differences using a single lookup of their hash values. Second, to enable
scalable and accurate analysis of noisy raw nanopore signals, we propose
RawHash, a novel mechanism that effectively reduces noise in raw nanopore
signals and enables accurate, real-time analysis by proposing the first
hash-based similarity search technique for raw nanopore signals. Third, we
extend the capabilities of RawHash with RawHash2, an improved mechanism that 1)
provides a better understanding of noise in raw nanopore signals to reduce it
more effectively and 2) improves the robustness of mapping decisions. Fourth,
we explore the broader implications and new applications of raw nanopore signal
analysis by introducing Rawsamble, the first mechanism for all-vs-all
overlapping of raw signals using hash-based search. Rawsamble enables the
construction of de novo assemblies directly from raw signals without
basecalling, which opens up new directions and uses for raw nanopore signal
analysis.