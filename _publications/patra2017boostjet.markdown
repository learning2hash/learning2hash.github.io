---
layout: publication
title: 'Boostjet: Towards Combining Statistical Aggregates With Neural Embeddings
  For Recommendations'
authors: Rhicheek Patra, Egor Samosvat, Michael Roizner, Andrei Mishchenko
conference: Arxiv
year: 2017
bibkey: patra2017boostjet
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1711.05828'}]
tags: [Recommender Systems, Evaluation, Datasets, Scalability]
short_authors: Patra et al.
---
Recommenders have become widely popular in recent years because of their
broader applicability in many e-commerce applications. These applications rely
on recommenders for generating advertisements for various offers or providing
content recommendations. However, the quality of the generated recommendations
depends on user features (like demography, temporality), offer features (like
popularity, price), and user-offer features (like implicit or explicit
feedback). Current state-of-the-art recommenders do not explore such diverse
features concurrently while generating the recommendations.
  In this paper, we first introduce the notion of Trackers which enables us to
capture the above-mentioned features and thus incorporate users' online
behaviour through statistical aggregates of different features (demography,
temporality, popularity, price). We also show how to capture offer-to-offer
relations, based on their consumption sequence, leveraging neural embeddings
for offers in our Offer2Vec algorithm. We then introduce BoostJet, a novel
recommender which integrates the Trackers along with the neural embeddings
using MatrixNet, an efficient distributed implementation of gradient boosted
decision tree, to improve the recommendation quality significantly. We provide
an in-depth evaluation of BoostJet on Yandex's dataset, collecting online
behaviour from tens of millions of online users, to demonstrate the
practicality of BoostJet in terms of recommendation quality as well as
scalability.