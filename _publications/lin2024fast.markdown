---
layout: publication
title: Fast Supervised Hashing With Decision Trees For High-dimensional Data
authors: Lin Guosheng, Shen, Shi, Hengel, Suter.
conference: "Arxiv"
year: 2024
bibkey: lin2024fast
additional_links:
  - {name: "Paper", url: "https://bitbucket.org/chhshen/fasthash/src"}
tags: ['ARXIV', 'Graph', 'Supervised']
---
Supervised hashing aims to map the original features to compact binary codes that are able to preserve label based similarity in the Hamming space. Non-linear hash functions have demonstrated their advantage over linear ones due to their powerful generalization capability. In the literature, kernel functions are typically used to achieve non-linearity in hashing, which achieve encouraging retrieval performance at the price of slow evaluation and training time. Here we propose to use boosted decision trees for achieving non-linearity in hashing, which are fast to train and evaluate, hence more suitable for hashing with high dimensional data. In our approach, we first propose sub-modular formulations for the hashing binary code inference problem and an efficient GraphCut based block search method for solving large-scale inference. Then we learn hash functions by training boosted decision trees to fit the binary codes. Experiments demonstrate that our proposed method significantly outperforms most state-of-the-art methods in retrieval precision and training time. Especially for highdimensional data, our method is orders of magnitude faster than many methods in terms of training time.
