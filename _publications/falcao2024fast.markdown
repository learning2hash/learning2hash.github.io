---
layout: publication
title: Fast Mutual Information Computation For Large Binary Datasets
authors: Andre O. Falcao
conference: Arxiv
year: 2024
bibkey: falcao2024fast
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2411.19702'}]
tags: ["Datasets"]
short_authors: Andre O. Falcao
---
Mutual Information (MI) is a powerful statistical measure that quantifies
shared information between random variables, particularly valuable in
high-dimensional data analysis across fields like genomics, natural language
processing, and network science. However, computing MI becomes computationally
prohibitive for large datasets where it is typically required a pairwise
computational approach where each column is compared to others. This work
introduces a matrix-based algorithm that accelerates MI computation by
leveraging vectorized operations and optimized matrix calculations. By
transforming traditional pairwise computational approaches into bulk matrix
operations, the proposed method enables efficient MI calculation across all
variable pairs. Experimental results demonstrate significant performance
improvements, with computation times reduced up to 50,000 times in the largest
dataset using optimized implementations, particularly when utilizing hardware
optimized frameworks. The approach promises to expand MI's applicability in
data-driven research by overcoming previous computational limitations.