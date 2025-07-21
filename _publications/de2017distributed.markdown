---
layout: publication
title: Distributed Stratified Locality Sensitive Hashing for Critical Event Prediction
  in the Cloud
authors: de Palma Alessandro, Hemberg Erik, O'reilly Una-may
conference: Proceedings of the 21st ACM international conference on Information and
  knowledge management
year: 2017
bibkey: de2017distributed
citations: 52
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1712.00206'}]
tags: ["CIKM", "Hashing-Methods", "Locality-Sensitive-Hashing"]
---
The availability of massive healthcare data repositories calls for efficient
tools for data-driven medicine. We introduce a distributed system for
Stratified Locality Sensitive Hashing to perform fast similarity-based
prediction on large medical waveform datasets. Our implementation, for an ICU
use case, prioritizes latency over throughput and is targeted at a cloud
environment. We demonstrate our system on Acute Hypotensive Episode prediction
from Arterial Blood Pressure waveforms. On a dataset of \\(1.37\\) million points,
we show scaling up to \\(40\\) processors and a \\(21\times\\) speedup in number of
comparisons to parallel exhaustive search at the price of a \\(10%\\) Matthews
correlation coefficient (MCC) loss. Furthermore, if additional MCC loss can be
tolerated, our system achieves speedups up to two orders of magnitude.