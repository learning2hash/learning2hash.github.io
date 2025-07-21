---
layout: publication
title: Embracing Structure in Data for Billion-Scale Semantic Product Search
authors: Lakshman et al.
conference: Proceedings of the 25th ACM SIGKDD International Conference on Knowledge
  Discovery &amp; Data Mining
year: 2021
bibkey: lakshman2021embracing
citations: 56
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2110.06125'}]
tags: ["KDD", "Large Scale Search", "Scalability"]
---
We present principled approaches to train and deploy dyadic neural embedding
models at the billion scale, focusing our investigation on the application of
semantic product search. When training a dyadic model, one seeks to embed two
different types of entities (e.g., queries and documents or users and movies)
in a common vector space such that pairs with high relevance are positioned
nearby. During inference, given an embedding of one type (e.g., a query or a
user), one seeks to retrieve the entities of the other type (e.g., documents or
movies, respectively) that are highly relevant. In this work, we show that
exploiting the natural structure of real-world datasets helps address both
challenges efficiently. Specifically, we model dyadic data as a bipartite graph
with edges between pairs with positive associations. We then propose to
partition this network into semantically coherent clusters and thus reduce our
search space by focusing on a small subset of these partitions for a given
input. During training, this technique enables us to efficiently mine hard
negative examples while, at inference, we can quickly find the nearest
neighbors for a given embedding. We provide offline experimental results that
demonstrate the efficacy of our techniques for both training and inference on a
billion-scale Amazon.com product search dataset.