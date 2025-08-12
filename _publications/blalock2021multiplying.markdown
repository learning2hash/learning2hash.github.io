---
layout: publication
title: Multiplying Matrices Without Multiplying
authors: Davis Blalock, John Guttag
conference: PMLR 139992-1004 2021
year: 2021
bibkey: blalock2021multiplying
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2106.10860'}]
tags: []
short_authors: Davis Blalock, John Guttag
---
Multiplying matrices is among the most fundamental and compute-intensive
operations in machine learning. Consequently, there has been significant work
on efficiently approximating matrix multiplies. We introduce a learning-based
algorithm for this task that greatly outperforms existing methods. Experiments
using hundreds of matrices from diverse domains show that it often runs
\(100\times\) faster than exact matrix products and \(10\times\) faster than
current approximate methods. In the common case that one matrix is known ahead
of time, our method also has the interesting property that it requires zero
multiply-adds. These results suggest that a mixture of hashing, averaging, and
byte shuffling\(-\)the core operations of our method\(-\)could be a more promising
building block for machine learning than the sparsified, factorized, and/or
scalar quantized matrix products that have recently been the focus of
substantial research and hardware investment.