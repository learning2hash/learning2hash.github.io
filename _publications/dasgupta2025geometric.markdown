---
layout: publication
title: A Geometric Approach To Personalized Recommendation With Set-theoretic Constraints
  Using Box Embeddings
authors: Shib Dasgupta, Michael Boratko, Andrew McCallum
conference: Arxiv
year: 2025
bibkey: dasgupta2025geometric
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2502.10875'}]
tags: ["Recommender Systems"]
short_authors: Shib Dasgupta, Michael Boratko, Andrew McCallum
---
Personalized item recommendation typically suffers from data sparsity, which
is most often addressed by learning vector representations of users and items
via low-rank matrix factorization. While this effectively densifies the matrix
by assuming users and movies can be represented by linearly dependent latent
features, it does not capture more complicated interactions. For example,
vector representations struggle with set-theoretic relationships, such as
negation and intersection, e.g. recommending a movie that is "comedy and
action, but not romance". In this work, we formulate the problem of
personalized item recommendation as matrix completion where rows are
set-theoretically dependent. To capture this set-theoretic dependence we
represent each user and attribute by a hyper-rectangle or box (i.e. a Cartesian
product of intervals). Box embeddings can intuitively be understood as
trainable Venn diagrams, and thus not only inherently represent similarity (via
the Jaccard index), but also naturally and faithfully support arbitrary
set-theoretic relationships. Queries involving set-theoretic constraints can be
efficiently computed directly on the embedding space by performing geometric
operations on the representations. We empirically demonstrate the superiority
of box embeddings over vector-based neural methods on both simple and complex
item recommendation queries by up to 30 % overall.