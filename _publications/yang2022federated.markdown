---
layout: publication
title: 'Fedhap: Federated Hashing With Global Prototypes For Cross-silo Retrieval'
authors: Meilin Yang, Jian Xu, Yang Liu, Wenbo Ding
conference: "Arxiv"
year: 2022
citations: 2
bibkey: yang2022federated
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2207.05525'}
tags: ['Cross-Modal', 'Deep', 'Independent', 'Efficiency', 'Retrieval Models', 'Datasets', 'Vector Indexing', 'Deep Hashing', 'Training Strategy', 'Similarity Learning', 'Hashing']
---
Deep hashing has been widely applied in large-scale data retrieval due to its
superior retrieval efficiency and low storage cost. However, data are often
scattered in data silos with privacy concerns, so performing centralized data
storage and retrieval is not always possible. Leveraging the concept of
federated learning (FL) to perform deep hashing is a recent research trend.
However, existing frameworks mostly rely on the aggregation of the local deep
hashing models, which are trained by performing similarity learning with local
skewed data only. Therefore, they cannot work well for non-IID clients in a
real federated environment. To overcome these challenges, we propose a novel
federated hashing framework that enables participating clients to jointly train
the shared deep hashing model by leveraging the prototypical hash codes for
each class. Globally, the transmission of global prototypes with only one
prototypical hash code per class will minimize the impact of communication cost
and privacy risk. Locally, the use of global prototypes are maximized by
jointly training a discriminator network and the local hashing network.
Extensive experiments on benchmark datasets are conducted to demonstrate that
our method can significantly improve the performance of the deep hashing model
in the federated environments with non-IID data distributions.
