---
layout: publication
title: Hebbian Graph Embeddings
authors: Shalin Shah, Venkataramana Kini
conference: Arxiv
year: 2019
bibkey: shah2019hebbian
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1908.08037'}]
tags: ["Evaluation", "Graph Based ANN", "Recommender Systems"]
short_authors: Shalin Shah, Venkataramana Kini
---
Representation learning has recently been successfully used to create vector
representations of entities in language learning, recommender systems and in
similarity learning. Graph embeddings exploit the locality structure of a graph
and generate embeddings for nodes which could be words in a language, products
of a retail website; and the nodes are connected based on a context window. In
this paper, we consider graph embeddings with an error-free associative
learning update rule, which models the embedding vector of node as a non-convex
Gaussian mixture of the embeddings of the nodes in its immediate vicinity with
some constant variance that is reduced as iterations progress. It is very easy
to parallelize our algorithm without any form of shared memory, which makes it
possible to use it on very large graphs with a much higher dimensionality of
the embeddings. We study the efficacy of proposed method on several benchmark
data sets and favorably compare with state of the art methods. Further,
proposed method is applied to generate relevant recommendations for a large
retailer.