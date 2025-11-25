---
layout: publication
title: 'Synerise At Recsys 2021: Twitter User Engagement Prediction With A Fast Neural
  Model'
authors: "Micha\u0142 Daniluk, Jacek D\u0105browski, Barbara Rychalska, Konrad Go\u0142\
  uchowski"
conference: 'RecSysChallenge ''21: Proceedings of the Recommender Systems Challenge
  2021'
year: 2021
bibkey: daniluk2021synerise
citations: 0
additional_links: [{name: Code, url: 'https://github.com/Synerise/recsys-challenge-2021'},
  {name: Paper, url: 'https://arxiv.org/abs/2109.12985'}]
tags: ["Evaluation", "Locality-Sensitive-Hashing", "Recommender Systems"]
short_authors: Daniluk et al.
---
In this paper we present our 2nd place solution to ACM RecSys 2021 Challenge
organized by Twitter. The challenge aims to predict user engagement for a set
of tweets, offering an exceptionally large data set of 1 billion data points
sampled from over four weeks of real Twitter interactions. Each data point
contains multiple sources of information, such as tweet text along with
engagement features, user features, and tweet features. The challenge brings
the problem close to a real production environment by introducing strict
latency constraints in the model evaluation phase: the average inference time
for single tweet engagement prediction is limited to 6ms on a single CPU core
with 64GB memory. Our proposed model relies on extensive feature engineering
performed with methods such as the Efficient Manifold Density Estimator (EMDE)
- our previously introduced algorithm based on Locality Sensitive Hashing
method, and novel Fourier Feature Encoding, among others. In total, we create
numerous features describing a user's Twitter account status and the content of
a tweet. In order to adhere to the strict latency constraints, the underlying
model is a simple residual feed-forward neural network. The system is a
variation of our previous methods which proved successful in KDD Cup 2021, WSDM
Challenge 2021, and SIGIR eCom Challenge 2020. We release the source code at:
https://github.com/Synerise/recsys-challenge-2021