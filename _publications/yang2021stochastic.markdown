---
layout: publication
title: Stochastic Cluster Embedding
authors: Zhirong Yang, Yuwei Chen, Denis Sedov, Samuel Kaski, Jukka Corander
conference: Arxiv
year: 2021
bibkey: yang2021stochastic
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2108.08003'}]
tags: ["Scalability"]
short_authors: Yang et al.
---
Neighbor Embedding (NE) aims to preserve pairwise similarities between data
items and has been shown to yield an effective principle for data
visualization. However, even the best existing NE methods such as Stochastic
Neighbor Embedding (SNE) may leave large-scale patterns hidden, for example
clusters, despite strong signals being present in the data. To address this, we
propose a new cluster visualization method based on the Neighbor Embedding
principle. We first present a family of Neighbor Embedding methods that
generalizes SNE by using non-normalized Kullback-Leibler divergence with a
scale parameter. In this family, much better cluster visualizations often
appear with a parameter value different from the one corresponding to SNE. We
also develop an efficient software that employs asynchronous stochastic block
coordinate descent to optimize the new family of objective functions. Our
experimental results demonstrate that the method consistently and substantially
improves the visualization of data clusters compared with the state-of-the-art
NE approaches.