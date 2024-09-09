---
layout: publication
title: "HCLAE: High Capacity Locally Aggregating Encodings for Approximate Nearest Neighbor Search"
authors: Liu Shicong, Shao Junru, Lu Hongtao
conference: Arxiv
year: 2015
bibkey: liu2015hclae
additional_links:
- {name: "Paper", url: "https://arxiv.org/abs/1509.05194"}
tags: ['ARXIV', 'Quantisation']
---
Vector quantization-based approaches are successful to solve Approximate Nearest Neighbor (ANN) problems which are critical to many applications. The idea is to generate effective encodings to allow fast distance approximation. We propose quantization-based methods should partition the data space finely and exhibit locality of the dataset to allow efficient non-exhaustive search. In this paper, we introduce the concept of High Capacity Locality Aggregating Encodings (HCLAE) to this end, and propose Dictionary Annealing (DA) to learn HCLAE by a simulated annealing procedure. The quantization error is lower than other state-of-the-art. The algorithms of DA can be easily extended to an online learning scheme, allowing effective handle of large scale data. Further, we propose Aggregating-Tree (A-Tree), a non-exhaustive search method using HCLAE to perform efficient ANN-Search. A-Tree achieves magnitudes of speed-up on ANN-Search tasks, compared to the state-of-the-art.