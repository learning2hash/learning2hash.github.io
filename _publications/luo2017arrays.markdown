---
layout: publication
title: 'Arrays Of (locality-sensitive) Count Estimators (ACE): High-speed Anomaly
  Detection Via Cache Lookups'
authors: Chen Luo, Anshumali Shrivastava
conference: Arxiv
year: 2017
citations: 5
bibkey: luo2017arrays
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1706.06664'}]
tags: [Unsupervised, Tools and Libraries, KDD, Evaluation Metrics, Benchmarks and
    Datasets, Hashing Methods, ANN Search]
---
Anomaly detection is one of the frequent and important subroutines deployed
in large-scale data processing systems. Even being a well-studied topic,
existing techniques for unsupervised anomaly detection require storing
significant amounts of data, which is prohibitive from memory and latency
perspective. In the big-data world existing methods fail to address the new set
of memory and latency constraints. In this paper, we propose ACE (Arrays of
(locality-sensitive) Count Estimators) algorithm that can be 60x faster than
the ELKI package~\cite\{DBLP:conf/ssd/AchtertBKSZ09\}, which has the fastest
implementation of the unsupervised anomaly detection algorithms. ACE algorithm
requires less than \\(4MB\\) memory, to dynamically compress the full data
information into a set of count arrays. These tiny \\(4MB\\) arrays of counts are
sufficient for unsupervised anomaly detection. At the core of the ACE
algorithm, there is a novel statistical estimator which is derived from the
sampling view of Locality Sensitive Hashing(LSH). This view is significantly
different and efficient than the widely popular view of LSH for near-neighbor
search. We show the superiority of ACE algorithm over 11 popular baselines on 3
benchmark datasets, including the KDD-Cup99 data which is the largest available
benchmark comprising of more than half a million entries with ground truth
anomaly labels.