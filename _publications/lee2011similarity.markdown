---
layout: publication
title: 'Similarity Join Size Estimation Using Locality Sensitive Hashing'
authors: Hongrae University Of British Columbia Lee, Raymond T. University Of British Columbia Ng, Kyuseok Seoul National University Shim
conference: "Proceedings of the VLDB Endowment (PVLDB) Vol. 4 No. 6 pp. 338-349 (2011)"
year: 2011
citations: 26
bibkey: lee2011similarity
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/1104.3212'}
tags: ['Independent', 'Unimodal', 'Shallow', 'Hashing', 'Applications']
---
Similarity joins are important operations with a broad range of applications.
In this paper, we study the problem of vector similarity join size estimation
(VSJ). It is a generalization of the previously studied set similarity join
size estimation (SSJ) problem and can handle more interesting cases such as
TF-IDF vectors. One of the key challenges in similarity join size estimation is
that the join size can change dramatically depending on the input similarity
threshold.
  We propose a sampling based algorithm that uses the
Locality-Sensitive-Hashing (LSH) scheme. The proposed algorithm LSH-SS uses an
LSH index to enable effective sampling even at high thresholds. We compare the
proposed technique with random sampling and the state-of-the-art technique for
SSJ (adapted to VSJ) and demonstrate LSH-SS offers more accurate estimates at
both high and low similarity thresholds and small variance using real-world
data sets.
