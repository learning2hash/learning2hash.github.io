---
layout: publication
title: A Hybrid Parallel Implementation Of The Aho-corasick And Wu-manber Algorithms
  Using NVIDIA CUDA And MPI Evaluated On A Biological Sequence Database
authors: Charalampos S. Kouzinopoulos, John-alexander M. Assael, Themistoklis K. Pyrgiotis,
  Konstantinos G. Margaritis
conference: International Journal on Artificial Intelligence Tools
year: 2015
bibkey: kouzinopoulos2014hybrid
citations: 14
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1407.2889'}]
tags: ["Efficiency"]
short_authors: Kouzinopoulos et al.
---
Multiple matching algorithms are used to locate the occurrences of patterns
from a finite pattern set in a large input string. Aho-Corasick and Wu-Manber,
two of the most well known algorithms for multiple matching require an
increased computing power, particularly in cases where large-size datasets must
be processed, as is common in computational biology applications. Over the past
years, Graphics Processing Units (GPUs) have evolved to powerful parallel
processors outperforming Central Processing Units (CPUs) in scientific
calculations. Moreover, multiple GPUs can be used in parallel, forming hybrid
computer cluster configurations to achieve an even higher processing
throughput. This paper evaluates the speedup of the parallel implementation of
the Aho-Corasick and Wu-Manber algorithms on a hybrid GPU cluster, when used to
process a snapshot of the Expressed Sequence Tags of the human genome and for
different problem parameters.