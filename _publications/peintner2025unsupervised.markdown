---
layout: publication
title: Unsupervised Graph Embeddings For Session-based Recommendation With Item Features
authors: Andreas Peintner, Marta Moscati, Emilia Parada-Cabaleiro, Markus Schedl,
  Eva Zangerle
conference: Arxiv
year: 2025
bibkey: peintner2025unsupervised
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2502.13763'}]
tags: ["Datasets", "Evaluation", "Recommender Systems", "Supervised", "Unsupervised"]
short_authors: Peintner et al.
---
In session-based recommender systems, predictions are based on the user's
preceding behavior in the session. State-of-the-art sequential recommendation
algorithms either use graph neural networks to model sessions in a graph or
leverage the similarity of sessions by exploiting item features. In this paper,
we combine these two approaches and propose a novel method, Graph Convolutional
Network Extension (GCNext), which incorporates item features directly into the
graph representation via graph convolutional networks. GCNext creates a
feature-rich item co-occurrence graph and learns the corresponding item
embeddings in an unsupervised manner. We show on three datasets that
integrating GCNext into sequential recommendation algorithms significantly
boosts the performance of nearest-neighbor methods as well as neural network
models. Our flexible extension is easy to incorporate in state-of-the-art
methods and increases the MRR@20 by up to 12.79%.