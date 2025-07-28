---
layout: publication
title: Scalable Nearest Neighbor Search For Optimal Transport
authors: Arturs Backurs, Yihe Dong, Piotr Indyk, Ilya Razenshteyn, Tal Wagner
conference: Arxiv
year: 2019
bibkey: backurs2019scalable
citations: 12
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1910.04126'}]
tags: []
short_authors: Backurs et al.
---
The Optimal Transport (a.k.a. Wasserstein) distance is an increasingly
popular similarity measure for rich data domains, such as images or text
documents. This raises the necessity for fast nearest neighbor search
algorithms according to this distance, which poses a substantial computational
bottleneck on massive datasets. In this work we introduce Flowtree, a fast and
accurate approximation algorithm for the Wasserstein-\\(1\\) distance. We formally
analyze its approximation factor and running time. We perform extensive
experimental evaluation of nearest neighbor search algorithms in the \\(W_1\\)
distance on real-world dataset. Our results show that compared to previous
state of the art, Flowtree achieves up to \\(7.4\\) times faster running time.