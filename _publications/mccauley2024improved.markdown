---
layout: publication
title: Improved Space-efficient Approximate Nearest Neighbor Search Using Function Inversion
authors: Mccauley Samuel
conference: "Arxiv"
year: 2024
bibkey: mccauley2024improved
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2407.02468"}
tags: ['ARXIV', 'Independent', 'LSH']
---
Approximate nearest neighbor search (ANN) data structures have widespread applications in machine learning, computational biology, and text processing. The goal of ANN is to preprocess a set S so that, given a query q, we can find a point y whose distance from q approximates the smallest distance from q to any point in S. For most distance functions, the best-known ANN bounds for high-dimensional point sets are obtained using techniques based on locality-sensitive hashing (LSH). Unfortunately, space efficiency is a major challenge for LSH-based data structures. Classic LSH techniques require a very large amount of space, oftentimes polynomial in |S|. A long line of work has developed intricate techniques to reduce this space usage, but these techniques suffer from downsides: they must be hand tailored to each specific LSH, are often complicated, and their space reduction comes at the cost of significantly increased query times. In this paper we explore a new way to improve the space efficiency of LSH using function inversion techniques, originally developed in (Fiat and Naor 2000). We begin by describing how function inversion can be used to improve LSH data structures. This gives a fairly simple, black box method to reduce LSH space usage. Then, we give a data structure that leverages function inversion to improve the query time of the best known near-linear space data structure for approximate nearest neighbor search under Euclidean distance: the ALRW data structure of (Andoni, Laarhoven, Razenshteyn, and Waingarten 2017). ALRW was previously shown to be optimal among list-of-points data structures for both Euclidean and Manhattan ANN; thus, in addition to giving improved bounds, our results imply that list-of-points data structures are not optimal for Euclidean or Manhattan ANN.
