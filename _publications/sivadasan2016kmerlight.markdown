---
layout: publication
title: 'Kmerlight: Fast And Accurate K-mer Abundance Estimation'
authors: Naveen Sivadasan, Rajgopal Srinivasan, Kshama Goyal
conference: Arxiv
year: 2016
bibkey: sivadasan2016kmerlight
citations: 10
additional_links: [{name: Code, url: 'https://github.com/nsivad/kmerlight'}, {name: Paper,
    url: 'https://arxiv.org/abs/1609.05626'}]
tags: ["Memory Efficiency"]
short_authors: Naveen Sivadasan, Rajgopal Srinivasan, Kshama Goyal
---
k-mers (nucleotide strings of length k) form the basis of several algorithms
in computational genomics. In particular, k-mer abundance information in
sequence data is useful in read error correction, parameter estimation for
genome assembly, digital normalization etc. We give a streaming algorithm
Kmerlight for computing the k-mer abundance histogram from sequence data. Our
algorithm is fast and uses very small memory footprint. We provide analytical
bounds on the error guarantees of our algorithm. Kmerlight can efficiently
process genome scale and metagenome scale data using standard desktop machines.
Few applications of abundance histograms computed by Kmerlight are also shown.
We use abundance histogram for de novo estimation of repetitiveness in the
genome based on a simple probabilistic model that we propose. We also show
estimation of k-mer error rate in the sampling using abundance histogram. Our
algorithm can also be used for abundance estimation in a general streaming
setting. The Kmerlight tool is written in C++ and is available for download and
use from https://github.com/nsivad/kmerlight.