---
layout: publication
title: 'Co-embedding: Discovering Communities On Bipartite Graphs Through Projection'
authors: "Ga\xEBlle Candel, David Naccache"
conference: Arxiv
year: 2021
bibkey: candel2021co
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2109.07135'}]
tags: ["Recommender Systems"]
short_authors: "Ga\xEBlle Candel, David Naccache"
---
Many datasets take the form of a bipartite graph where two types of nodes are
connected by relationships, like the movies watched by a user or the tags
associated with a file. The partitioning of the bipartite graph could be used
to fasten recommender systems, or reduce the information retrieval system's
index size, by identifying groups of items with similar properties. This type
of graph is often processed by algorithms using the Vector Space Model
representation, where a binary vector represents an item with 0 and 1. The main
problem with this representation is the dimension relatedness, like words'
synonymity, which is not considered. This article proposes a co-clustering
algorithm using items projection, allowing the measurement of features
similarity. We evaluated our algorithm on a cluster retrieval task. Over
various datasets, our algorithm produced well balanced clusters with coherent
items in, leading to high retrieval scores on this task..