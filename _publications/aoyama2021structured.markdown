---
layout: publication
title: Structured Inverted-file K-means Clustering For High-dimensional Sparse Data
authors: Kazuo Aoyama, Kazumi Saito
conference: Arxiv
year: 2021
bibkey: aoyama2021structured
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2103.16141'}]
tags: ["Efficiency", "Scalability"]
short_authors: Kazuo Aoyama, Kazumi Saito
---
This paper presents an architecture-friendly k-means clustering algorithm
called SIVF for a large-scale and high-dimensional sparse data set. Algorithm
efficiency on time is often measured by the number of costly operations such as
similarity calculations. In practice, however, it depends greatly on how the
algorithm adapts to an architecture of the computer system which it is executed
on. Our proposed SIVF employs invariant centroid-pair based filter (ICP) to
decrease the number of similarity calculations between a data object and
centroids of all the clusters. To maximize the ICP performance, SIVF exploits
for a centroid set an inverted-file that is structured so as to reduce pipeline
hazards. We demonstrate in our experiments on real large-scale document data
sets that SIVF operates at higher speed and with lower memory consumption than
existing algorithms. Our performance analysis reveals that SIVF achieves the
higher speed by suppressing performance degradation factors of the number of
cache misses and branch mispredictions rather than less similarity
calculations.