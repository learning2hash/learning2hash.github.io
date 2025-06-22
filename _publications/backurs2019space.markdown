---
layout: publication
title: Space And Time Efficient Kernel Density Estimation In High Dimensions
authors: Arturs Backurs, Piotr Indyk, Tal Wagner
conference: Neural Information Processing Systems
year: 2019
citations: 27
bibkey: backurs2019space
additional_links: [{name: Paper, url: 'https://papers.nips.cc/paper/2019/hash/a2ce8f1706e52936dfad516c23904e3e-Abstract.html'}]
tags: [Hashing Methods, ANN Search, Has Code, NeurIPS]
---
Recently, Charikar and Siminelakis (2017) presented a framework for kernel density estimation in provably sublinear query time, for kernels that possess a certain hashing-based property. However, their data structure requires a significantly increased super-linear storage space, as well as super-linear preprocessing time. These limitations inhibit the practical applicability of their approach on large datasets.
In this work, we present an improvement to their framework that retains the same query time, while requiring only linear space and linear preprocessing time. We instantiate our framework with the Laplacian and Exponential kernels, two popular kernels which possess the aforementioned property. Our experiments on various datasets verify that our approach attains accuracy and query time similar to Charikar and Siminelakis (2017), with significantly improved space and preprocessing time.