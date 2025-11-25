---
layout: publication
title: Federated Graph-based Networks With Shared Embedding
authors: Tianyi Yu, Pei Lai, Fei Teng
conference: Arxiv
year: 2022
bibkey: yu2022federated
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2210.01803'}]
tags: ["Efficiency", "Graph Based ANN", "Privacy & Security", "Recommender Systems"]
short_authors: Tianyi Yu, Pei Lai, Fei Teng
---
Nowadays, user privacy is becoming an issue that cannot be bypassed for
system developers, especially for that of web applications where data can be
easily transferred through internet. Thankfully, federated learning proposes an
innovative method to train models with distributed devices while data are kept
in local storage. However, unlike general neural networks, although graph-based
networks have achieved great success in classification tasks and advanced
recommendation system, its high performance relies on the rich context provided
by a graph structure, which is vulnerable when data attributes are incomplete.
Therefore, the latter becomes a realistic problem when implementing federated
learning for graph-based networks. Knowing that data embedding is a
representation in a different space, we propose our Federated Graph-based
Networks with Shared Embedding (Feras), which uses shared embedding data to
train the network and avoids the direct sharing of original data. A solid
theoretical proof of the convergence of Feras is given in this work.
Experiments on different datasets (PPI, Flickr, Reddit) are conducted to show
the efficiency of Feras for centralized learning. Finally, Feras enables the
training of current graph-based models in the federated learning framework for
privacy concern.