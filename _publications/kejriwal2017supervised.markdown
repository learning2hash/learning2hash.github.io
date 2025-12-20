---
layout: publication
title: Supervised Typing Of Big Graphs Using Semantic Embeddings
authors: Mayank Kejriwal, Pedro Szekely
conference: Proceedings of The International Workshop on Semantic Big Data
year: 2017
bibkey: kejriwal2017supervised
citations: 11
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1703.07805'}]
tags: ["Efficiency", "Memory Efficiency", "Recommender Systems", "Supervised", "Unsupervised"]
short_authors: Mayank Kejriwal, Pedro Szekely
---
We propose a supervised algorithm for generating type embeddings in the same
semantic vector space as a given set of entity embeddings. The algorithm is
agnostic to the derivation of the underlying entity embeddings. It does not
require any manual feature engineering, generalizes well to hundreds of types
and achieves near-linear scaling on Big Graphs containing many millions of
triples and instances by virtue of an incremental execution. We demonstrate the
utility of the embeddings on a type recommendation task, outperforming a
non-parametric feature-agnostic baseline while achieving 15x speedup and
near-constant memory usage on a full partition of DBpedia. Using
state-of-the-art visualization, we illustrate the agreement of our
extensionally derived DBpedia type embeddings with the manually curated domain
ontology. Finally, we use the embeddings to probabilistically cluster about 4
million DBpedia instances into 415 types in the DBpedia ontology.