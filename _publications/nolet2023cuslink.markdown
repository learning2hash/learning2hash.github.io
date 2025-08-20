---
layout: publication
title: 'Cuslink: Single-linkage Agglomerative Clustering On The GPU'
authors: Corey J. Nolet, Divye Gala, Alex Fender, Mahesh Doijade, Joe Eaton, Edward
  Raff, John Zedlewski, Brad Rees, Tim Oates
conference: Lecture Notes in Computer Science
year: 2023
bibkey: nolet2023cuslink
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2306.16354'}]
tags: [Tools & Libraries, Graph-based ANN]
short_authors: Nolet et al.
---
In this paper, we propose cuSLINK, a novel and state-of-the-art reformulation
of the SLINK algorithm on the GPU which requires only \(O(Nk)\) space and uses a
parameter \(k\) to trade off space and time. We also propose a set of novel and
reusable building blocks that compose cuSLINK. These building blocks include
highly optimized computational patterns for \(k\)-NN graph construction, spanning
trees, and dendrogram cluster extraction. We show how we used our primitives to
implement cuSLINK end-to-end on the GPU, further enabling a wide range of
real-world data mining and machine learning applications that were once
intractable. In addition to being a primary computational bottleneck in the
popular HDBSCAN algorithm, the impact of our end-to-end cuSLINK algorithm spans
a large range of important applications, including cluster analysis in social
and computer networks, natural language processing, and computer vision. Users
can obtain cuSLINK at
https://docs.rapids.ai/api/cuml/latest/api/%23agglomerative-clustering