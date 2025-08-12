---
layout: publication
title: A Data-dependent Algorithm For Querying Earth Mover's Distance With Low Doubling
  Dimensions
authors: Hu Ding, Tan Chen, Fan Yang, Mingyue Wang
conference: Proceedings of the 2021 SIAM International Conference on Data Mining (SDM)
year: 2021
bibkey: ding2020data
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2002.12354'}]
tags: []
short_authors: Ding et al.
---
In this paper, we consider the following query problem: given two weighted
point sets \\(A\\) and \\(B\\) in the Euclidean space \\(\mathbb\{R\}^d\\), we want to
quickly determine that whether their earth mover's distance (EMD) is larger or
smaller than a pre-specified threshold \\(T\geq 0\\). The problem finds a number of
important applications in the fields of machine learning and data mining. In
particular, we assume that the dimensionality \\(d\\) is not fixed and the sizes
\\(|A|\\) and \\(|B|\\) are large. Therefore, most of existing EMD algorithms are not
quite efficient to solve this problem due to their high complexities. Here, we
consider the problem under the assumption that \\(A\\) and \\(B\\) have low doubling
dimensions, which is common for high-dimensional data in real world. Inspired
by the geometric method \{\em net tree\}, we propose a novel ``data-dependent''
algorithm to avoid directly computing the EMD between \\(A\\) and \\(B\\), so as to
solve this query problem more efficiently. We also study the performance of our
method on synthetic and real datasets. The experimental results suggest that
our method can save a large amount of running time comparing with existing EMD
algorithms.