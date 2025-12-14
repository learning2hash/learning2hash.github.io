---
layout: publication
title: A Comparison Of Similarity Based Instance Selection Methods For Cross Project
  Defect Prediction
authors: Seyedrebvar Hosseini, Burak Turhan
conference: Proceedings of the 36th Annual ACM Symposium on Applied Computing
year: 2021
bibkey: hosseini2021a
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2104.01024'}]
tags: [Hashing Methods, Locality Sensitive Hashing, Evaluation, Datasets]
short_authors: Seyedrebvar Hosseini, Burak Turhan
---
Context: Previous studies have shown that training data instance selection
based on nearest neighborhood (NN) information can lead to better performance
in cross project defect prediction (CPDP) by reducing heterogeneity in training
datasets. However, neighborhood calculation is computationally expensive and
approximate methods such as Locality Sensitive Hashing (LSH) can be as
effective as exact methods. Aim: We aim at comparing instance selection methods
for CPDP, namely LSH, NN-filter, and Genetic Instance Selection (GIS). Method:
We conduct experiments with five base learners, optimizing their hyper
parameters, on 13 datasets from PROMISE repository in order to compare the
performance of LSH with benchmark instance selection methods NN-Filter and GIS.
Results: The statistical tests show six distinct groups for F-measure
performance. The top two group contains only LSH and GIS benchmarks whereas the
bottom two groups contain only NN-Filter variants. LSH and GIS favor recall
more than precision. In fact, for precision performance only three
significantly distinct groups are detected by the tests where the top group is
comprised of NN-Filter variants only. Recall wise, 16 different groups are
identified where the top three groups contain only LSH methods, four of the
next six are GIS only and the bottom five contain only NN-Filter. Finally,
NN-Filter benchmarks never outperform the LSH counterparts with the same base
learner, tuned or non-tuned. Further, they never even belong to the same rank
group, meaning that LSH is always significantly better than NN-Filter with the
same learner and settings. Conclusions: The increase in performance and the
decrease in computational overhead and runtime make LSH a promising approach.
However, the performance of LSH is based on high recall and in environments
where precision is considered more important NN-Filter should be considered.