---
layout: publication
title: Similarity Join Size Estimation Using Locality Sensitive Hashing
authors: Lee Hongrae University Of British Columbia, Ng Raymond T. University Of British Columbia, Shim Kyuseok Seoul National University
conference: "Proceedings of the VLDB Endowment"
year: 2011
bibkey: lee2011similarity
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1104.3212"}
tags: ['Independent', 'LSH', 'VLDB']
---
Similarity joins are important operations with a broad range of applications. In this paper we study the problem of vector similarity join size estimation (VSJ). It is a generalization of the previously studied set similarity join size estimation (SSJ) problem and can handle more interesting cases such as TF45;IDF vectors. One of the key challenges in similarity join size estimation is that the join size can change dramatically depending on the input similarity threshold. We propose a sampling based algorithm that uses the Locality45;Sensitive45;Hashing (LSH) scheme. The proposed algorithm LSH45;SS uses an LSH index to enable effective sampling even at high thresholds. We compare the proposed technique with random sampling and the state45;of45;the45;art technique for SSJ (adapted to VSJ) and demonstrate LSH45;SS offers more accurate estimates at both high and low similarity thresholds and small variance using real45;world data sets.
