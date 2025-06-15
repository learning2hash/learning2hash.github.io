---
layout: publication
title: 'Coarse2fine: Two-layer Fusion For Image Retrieval'
authors: Gaipeng Kong, Le Dong, Wenpu Dong, Liang Zheng, Qi Tian
conference: "Arxiv"
year: 2016
citations: 4
bibkey: kong2016two
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/1607.00719'}
tags: ['Cross-Modal', 'Deep', 'Quantisation', 'Retrieval Models', 'Datasets', 'Applications']
---
This paper addresses the problem of large-scale image retrieval. We propose a
two-layer fusion method which takes advantage of global and local cues and
ranks database images from coarse to fine (C2F). Departing from the previous
methods fusing multiple image descriptors simultaneously, C2F is featured by a
layered procedure composed by filtering and refining. In particular, C2F
consists of three components. 1) Distractor filtering. With holistic
representations, noise images are filtered out from the database, so the number
of candidate images to be used for comparison with the query can be greatly
reduced. 2) Adaptive weighting. For a certain query, the similarity of
candidate images can be estimated by holistic similarity scores in
complementary to the local ones. 3) Candidate refining. Accurate retrieval is
conducted via local features, combining the pre-computed adaptive weights.
Experiments are presented on two benchmarks, *i.e.,* Holidays and Ukbench
datasets. We show that our method outperforms recent fusion methods in terms of
storage consumption and computation complexity, and that the accuracy is
competitive to the state-of-the-arts.
