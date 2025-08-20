---
layout: publication
title: Position-based Hash Embeddings For Scaling Graph Neural Networks
authors: Maria Kalantzi, George Karypis
conference: 2021 IEEE International Conference on Big Data (Big Data)
year: 2021
bibkey: kalantzi2021position
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2109.00101'}]
tags: [Hashing Methods, Recommender Systems, Datasets, Evaluation]
short_authors: Maria Kalantzi, George Karypis
---
Graph Neural Networks (GNNs) bring the power of deep representation learning
to graph and relational data and achieve state-of-the-art performance in many
applications. GNNs compute node representations by taking into account the
topology of the node's ego-network and the features of the ego-network's nodes.
When the nodes do not have high-quality features, GNNs learn an embedding layer
to compute node embeddings and use them as input features. However, the size of
the embedding layer is linear to the product of the number of nodes in the
graph and the dimensionality of the embedding and does not scale to big data
and graphs with hundreds of millions of nodes. To reduce the memory associated
with this embedding layer, hashing-based approaches, commonly used in
applications like NLP and recommender systems, can potentially be used.
However, a direct application of these ideas fails to exploit the fact that in
many real-world graphs, nodes that are topologically close will tend to be
related to each other (homophily) and as such their representations will be
similar.
  In this work, we present approaches that take advantage of the nodes'
position in the graph to dramatically reduce the memory required, with minimal
if any degradation in the quality of the resulting GNN model. Our approaches
decompose a node's embedding into two components: a position-specific component
and a node-specific component. The position-specific component models homophily
and the node-specific component models the node-to-node variation. Extensive
experiments using different datasets and GNN models show that our methods are
able to reduce the memory requirements by 88% to 97% while achieving, in nearly
all cases, better classification accuracy than other competing approaches,
including the full embeddings.