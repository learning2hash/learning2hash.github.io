---
layout: publication
title: Locality-sensitive Hashing Scheme Based On Longest Circular Co-substring
authors: Yifan Lei, Qiang Huang, Mohan Kankanhalli, Anthony K. H. Tung
conference: Proceedings of the 2020 ACM SIGMOD International Conference on Management
  of Data
year: 2020
bibkey: lei2020locality
citations: 27
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2004.05345'}]
tags: [Distance Metric Learning, Datasets, Tools & Libraries, Hashing Methods, Locality
    Sensitive Hashing]
short_authors: Lei et al.
---
Locality-Sensitive Hashing (LSH) is one of the most popular methods for
\(c\)-Approximate Nearest Neighbor Search (\(c\)-ANNS) in high-dimensional spaces.
In this paper, we propose a novel LSH scheme based on the Longest Circular
Co-Substring (LCCS) search framework (LCCS-LSH) with a theoretical guarantee.
We introduce a novel concept of LCCS and a new data structure named Circular
Shift Array (CSA) for \(k\)-LCCS search. The insight of LCCS search framework is
that close data objects will have a longer LCCS than the far-apart ones with
high probability. LCCS-LSH is *LSH-family-independent*, and it supports
\(c\)-ANNS with different kinds of distance metrics. We also introduce a
multi-probe version of LCCS-LSH and conduct extensive experiments over five
real-life datasets. The experimental results demonstrate that LCCS-LSH
outperforms state-of-the-art LSH schemes.