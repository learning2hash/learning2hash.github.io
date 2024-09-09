---
layout: publication
title: "Near-Isometric Binary Hashing for Large-scale Datasets"
authors: Aghazadeh Amirali, Lan Andrew, Shrivastava Anshumali, Baraniuk Richard
conference: Arxiv
year: 2016
bibkey: aghazadeh2016near
additional_links:
- {name: "Paper", url: "https://arxiv.org/abs/1603.03836"}
tags: ['ARXIV']
---
We develop a scalable algorithm to learn binary hash codes for indexing large-scale datasets. Near-isometric binary hashing (NIBH) is a data-dependent hashing scheme that quantizes the output of a learned low-dimensional embedding to obtain a binary hash code. In contrast to conventional hashing schemes, which typically rely on an $\ell_2$-norm (i.e., average distortion) minimization, NIBH is based on a $\ell_\{\infty\}$-norm (i.e., worst-case distortion) minimization that provides several benefits, including superior distance, ranking, and near-neighbor preservation performance. We develop a practical and efficient algorithm for NIBH based on column generation that scales well to large datasets. A range of experimental evaluations demonstrate the superiority of NIBH over ten state-of-the-art binary hashing schemes.