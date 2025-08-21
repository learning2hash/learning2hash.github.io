---
layout: publication
title: Elastic Product Quantization For Time Series
authors: Pieter Robberechts, Wannes Meert, Jesse Davis
conference: Arxiv
year: 2022
bibkey: robberechts2022elastic
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2201.01856'}]
tags: ["Datasets", "Efficiency", "Evaluation", "Memory Efficiency", "Quantization", "Similarity Search"]
short_authors: Pieter Robberechts, Wannes Meert, Jesse Davis
---
Analyzing numerous or long time series is difficult in practice due to the
high storage costs and computational requirements. Therefore, techniques have
been proposed to generate compact similarity-preserving representations of time
series, enabling real-time similarity search on large in-memory data
collections. However, the existing techniques are not ideally suited for
assessing similarity when sequences are locally out of phase. In this paper, we
propose the use of product quantization for efficient similarity-based
comparison of time series under time warping. The idea is to first compress the
data by partitioning the time series into equal length sub-sequences which are
represented by a short code. The distance between two time series can then be
efficiently approximated by pre-computed elastic distances between their codes.
The partitioning into sub-sequences forces unwanted alignments, which we
address with a pre-alignment step using the maximal overlap discrete wavelet
transform (MODWT). To demonstrate the efficiency and accuracy of our method, we
perform an extensive experimental evaluation on benchmark datasets in nearest
neighbors classification and clustering applications. Overall, the proposed
solution emerges as a highly efficient (both in terms of memory usage and
computation time) replacement for elastic measures in time series applications.