---
layout: publication
title: 'Meta\(^\mathbf{2}\): Memory-efficient Taxonomic Classification And Abundance
  Estimation For Metagenomics With Deep Learning'
authors: "Andreas Georgiou, Vincent Fortuin, Harun Mustafa, Gunnar R\xE4tsch"
conference: Arxiv
year: 2019
bibkey: georgiou2019meta
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1909.13146'}]
tags: ["Hashing Methods", "Memory Efficiency", "Neural Hashing"]
short_authors: Georgiou et al.
---
Metagenomic studies have increasingly utilized sequencing technologies in
order to analyze DNA fragments found in environmental samples.One important
step in this analysis is the taxonomic classification of the DNA fragments.
Conventional read classification methods require large databases and vast
amounts of memory to run, with recent deep learning methods suffering from very
large model sizes. We therefore aim to develop a more memory-efficient
technique for taxonomic classification. A task of particular interest is
abundance estimation in metagenomic samples. Current attempts rely on
classifying single DNA reads independently from each other and are therefore
agnostic to co-occurence patterns between taxa. In this work, we also attempt
to take these patterns into account. We develop a novel memory-efficient read
classification technique, combining deep learning and locality-sensitive
hashing. We show that this approach outperforms conventional mapping-based and
other deep learning methods for single-read taxonomic classification when
restricting all methods to a fixed memory footprint. Moreover, we formulate the
task of abundance estimation as a Multiple Instance Learning (MIL) problem and
we extend current deep learning architectures with two different types of
permutation-invariant MIL pooling layers: a) deepsets and b) attention-based
pooling. We illustrate that our architectures can exploit the co-occurrence of
species in metagenomic read sets and outperform the single-read architectures
in predicting the distribution over taxa at higher taxonomic ranks.