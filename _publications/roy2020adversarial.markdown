---
layout: publication
title: Adversarial Permutation Guided Node Representations For Link Prediction
authors: Indradyumna Roy, Abir de, Soumen Chakrabarti
conference: Arxiv
year: 2020
bibkey: roy2020adversarial
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2012.08974'}]
tags: [Evaluation, Graph-based ANN, Datasets, Robustness, Tools & Libraries]
short_authors: Indradyumna Roy, Abir de, Soumen Chakrabarti
---
After observing a snapshot of a social network, a link prediction (LP)
algorithm identifies node pairs between which new edges will likely materialize
in future. Most LP algorithms estimate a score for currently non-neighboring
node pairs, and rank them by this score. Recent LP systems compute this score
by comparing dense, low dimensional vector representations of nodes. Graph
neural networks (GNNs), in particular graph convolutional networks (GCNs), are
popular examples. For two nodes to be meaningfully compared, their embeddings
should be indifferent to reordering of their neighbors. GNNs typically use
simple, symmetric set aggregators to ensure this property, but this design
decision has been shown to produce representations with limited expressive
power. Sequence encoders are more expressive, but are permutation sensitive by
design. Recent efforts to overcome this dilemma turn out to be unsatisfactory
for LP tasks. In response, we propose PermGNN, which aggregates neighbor
features using a recurrent, order-sensitive aggregator and directly minimizes
an LP loss while it is `attacked' by adversarial generator of neighbor
permutations. By design, PermGNN\{\} has more expressive power compared to
earlier symmetric aggregators. Next, we devise an optimization framework to map
PermGNN's node embeddings to a suitable locality-sensitive hash, which speeds
up reporting the top-\(K\) most likely edges for the LP task. Our experiments on
diverse datasets show that \our outperforms several state-of-the-art link
predictors by a significant margin, and can predict the most likely edges fast.