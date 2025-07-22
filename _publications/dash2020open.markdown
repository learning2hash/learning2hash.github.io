---
layout: publication
title: Open Knowledge Graphs Canonicalization Using Variational Autoencoders
authors: Dash Sarthak, Rossiello Gaetano, Mihindukulasooriya Nandana, Bagchi Sugato,
  Gliozzo Alfio
conference: Proceedings of the 2021 Conference on Empirical Methods in Natural Language
  Processing
year: 2021
bibkey: dash2020open
citations: 12
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2012.04780'}]
tags: ["Evaluation", "EMNLP", "Datasets"]
short_authors: Dash et al.
---
Noun phrases and Relation phrases in open knowledge graphs are not
canonicalized, leading to an explosion of redundant and ambiguous
subject-relation-object triples. Existing approaches to solve this problem take
a two-step approach. First, they generate embedding representations for both
noun and relation phrases, then a clustering algorithm is used to group them
using the embeddings as features. In this work, we propose Canonicalizing Using
Variational Autoencoders (CUVA), a joint model to learn both embeddings and
cluster assignments in an end-to-end approach, which leads to a better vector
representation for the noun and relation phrases. Our evaluation over multiple
benchmarks shows that CUVA outperforms the existing state-of-the-art
approaches. Moreover, we introduce CanonicNell, a novel dataset to evaluate
entity canonicalization systems.