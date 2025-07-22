---
layout: publication
title: 'Enhanced Discrete Multi-modal Hashing: More Constraints Yet Less Time To Learn'
authors: Chen Yong, Zhang, Tian, Wang, Zhang, Li
conference: IEEE Transactions on Knowledge and Data Engineering
year: 2020
bibkey: chen2020enhanced
citations: 27
additional_links: [{name: Paper, url: 'https://ieeexplore.ieee.org/abstract/document/9095226'}]
tags: ["Compact-Codes", "Hashing-Methods", "Datasets"]
short_authors: Chen et al.
---
Due to the exponential growth of multimedia data, multi-modal hashing as a promising technique to make cross-view retrieval scalable is attracting more and more attention. However, most of the existing multi-modal hashing methods either divide the learning process unnaturally into two separate stages or treat the discrete optimization problem simplistically as a continuous one, which leads to suboptimal results. Recently, a few discrete multi-modal hashing methods that try to address such issues have emerged, but they still ignore several important discrete constraints (such as the balance and decorrelation of hash bits). In this paper, we overcome those limitations by proposing a novel method named “Enhanced Discrete Multi-modal Hashing (EDMH)” which learns binary codes and hashing functions simultaneously from the pairwise similarity matrix of data, under the aforementioned discrete constraints. Although the model of EDMH looks a lot more complex than the other models for multi-modal hashing, we are actually able to develop a fast iterative learning algorithm for it, since the subproblems of its optimization all have closed-form solutions after introducing two auxiliary variables. Our experimental results on three real-world datasets have demonstrated that EDMH not only performs much better than state-of-the-art competitors but also runs much faster than them.