---
layout: publication
title: Sequence Covering For Efficient Host-based Intrusion Detection
authors: "Pierre-fran\xE7ois Marteau"
conference: IEEE Transactions on Information Forensics and Security
year: 2018
bibkey: marteau2017sequence
citations: 40
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1712.02084'}]
tags: []
short_authors: "Pierre-fran\xE7ois Marteau"
---
This paper introduces a new similarity measure, the covering similarity, that
we formally define for evaluating the similarity between a symbolic sequence
and a set of symbolic sequences. A pair-wise similarity can also be directly
derived from the covering similarity to compare two symbolic sequences. An
efficient implementation to compute the covering similarity is proposed that
uses a suffix tree data-structure, but other implementations, based on suffix
array for instance, are possible and possibly necessary for handling large
scale problems. We have used this similarity to isolate attack sequences from
normal sequences in the scope of Host-based Intrusion Detection. We have
assessed the covering similarity on two well-known benchmarks in the field. In
view of the results reported on these two datasets for the state of the art
methods, and according to the comparative study we have carried out based on
three challenging similarity measures commonly used for string processing or in
bioinformatics, we show that the covering similarity is particularly relevant
to address the detection of anomalies in sequences of system calls