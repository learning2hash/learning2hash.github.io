---
layout: publication
title: 'Genoogle: An Indexed And Parallelized Search Engine For Similar DNA Sequences'
authors: Albrecht Felipe
conference: Nucleic Acids Research
year: 2015
bibkey: albrecht2015genoogle
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1507.02987'}]
tags: [Evaluation, Efficiency And Optimization]
---
The search for similar genetic sequences is one of the main bioinformatics
tasks. The genetic sequences data banks are growing exponentially and the
searching techniques that use linear time are not capable to do the search in
the required time anymore. Another problem is that the clock speed of the
modern processors are not growing as it did before, instead, the processing
capacity is growing with the addiction of more processing cores and the
techniques which does not use parallel computing does not have benefits from
these extra cores. This work aims to use data indexing techniques to reduce the
searching process computation cost united with the parallelization of the
searching techniques to use the computational capacity of the multi core
processors. To verify the viability of using these two techniques
simultaneously, a software which uses parallelization techniques with inverted
indexes was developed.
  Experiments were executed to analyze the performance gain when parallelism is
utilized, the search time gain, and also the quality of the results when it
compared with others searching tools. The results of these experiments were
promising, the parallelism gain overcame the expected speedup, the searching
time was 20 times faster than the parallelized NCBI BLAST, and the searching
results showed a good quality when compared with this tool.
  The software source code is available at
https://github.com/felipealbrecht/Genoogle .