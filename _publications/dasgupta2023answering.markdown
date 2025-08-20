---
layout: publication
title: Answering Compositional Queries With Set-theoretic Embeddings
authors: Shib Dasgupta, Andrew McCallum, Steffen Rendle, Li Zhang
conference: Arxiv
year: 2023
bibkey: dasgupta2023answering
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2306.04133'}]
tags: [Recommender Systems, Datasets, Evaluation]
short_authors: Dasgupta et al.
---
The need to compactly and robustly represent item-attribute relations arises
in many important tasks, such as faceted browsing and recommendation systems. A
popular machine learning approach for this task denotes that an item has an
attribute by a high dot-product between vectors for the item and attribute -- a
representation that is not only dense, but also tends to correct noisy and
incomplete data. While this method works well for queries retrieving items by a
single attribute (such as *movies that are comedies*), we find that vector
embeddings do not so accurately support compositional queries (such as movies
that are comedies and British but not romances). To address these set-theoretic
compositions, this paper proposes to replace vectors with box embeddings, a
region-based representation that can be thought of as learnable Venn diagrams.
We introduce a new benchmark dataset for compositional queries, and present
experiments and analysis providing insights into the behavior of both. We find
that, while vector and box embeddings are equally suited to single attribute
queries, for compositional queries box embeddings provide substantial
advantages over vectors, particularly at the moderate and larger retrieval set
sizes that are most useful for users' search and browsing.