---
layout: publication
title: 'Oasis: Adaptive Column Sampling For Kernel Matrix Approximation'
authors: Raajen Patel, Thomas A. Goldstein, Eva L. Dyer, Azalia Mirhoseini, Richard
  G. Baraniuk
conference: Arxiv
year: 2015
bibkey: patel2015oasis
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1505.05208'}]
tags: []
short_authors: Patel et al.
---
Kernel matrices (e.g. Gram or similarity matrices) are essential for many
state-of-the-art approaches to classification, clustering, and dimensionality
reduction. For large datasets, the cost of forming and factoring such kernel
matrices becomes intractable. To address this challenge, we introduce a new
adaptive sampling algorithm called Accelerated Sequential Incoherence Selection
(oASIS) that samples columns without explicitly computing the entire kernel
matrix. We provide conditions under which oASIS is guaranteed to exactly
recover the kernel matrix with an optimal number of columns selected. Numerical
experiments on both synthetic and real-world datasets demonstrate that oASIS
achieves performance comparable to state-of-the-art adaptive sampling methods
at a fraction of the computational cost. The low runtime complexity of oASIS
and its low memory footprint enable the solution of large problems that are
simply intractable using other adaptive methods.