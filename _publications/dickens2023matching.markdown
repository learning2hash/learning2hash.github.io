---
layout: publication
title: "Matching Noisy Keys for Obfuscation"
authors: Dickens Charlie, Bax Eric
conference: Arxiv
year: 2023
bibkey: dickens2023matching
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2312.08981"}
tags: ['ARXIV']
---
Data sketching has emerged as a key infrastructure for large-scale data analysis
on streaming and distributed data. Merging sketches enables efficient estimation
of cardinalities and frequency histograms over distributed data. However,
merging sketches can require that each sketch stores hash codes for identifiers
in different data sets or partitions, in order to perform effective matching.
This can reveal identifiers during merging or across different data set or
partition owners. This paper presents a framework to use noisy hash codes, with
the noise level selected to obfuscate identifiers while allowing matching, with
high probability. We give probabilistic error bounds on simultaneous obfuscation
and matching, concluding that this is a viable approach.
