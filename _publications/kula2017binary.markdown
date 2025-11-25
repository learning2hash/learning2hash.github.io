---
layout: publication
title: 'Binary Latent Representations For Efficient Ranking: Empirical Assessment'
authors: MacIej Kula
conference: Arxiv
year: 2017
bibkey: kula2017binary
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1706.07479'}]
tags: ["Recommender Systems", "Scalability"]
short_authors: MacIej Kula
---
Large-scale recommender systems often face severe latency and storage
constraints at prediction time. These are particularly acute when the number of
items that could be recommended is large, and calculating predictions for the
full set is computationally intensive. In an attempt to relax these
constraints, we train recommendation models that use binary rather than
real-valued user and item representations, and show that while they are
substantially faster to evaluate, the gains in speed come at a large cost in
accuracy. In our Movielens 1M experiments, we show that reducing the latent
dimensionality of traditional models offers a more attractive accuracy/speed
trade-off than using binary representations.