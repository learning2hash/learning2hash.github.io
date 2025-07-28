---
layout: publication
title: 'SWAG: Item Recommendations Using Convolutions On Weighted Graphs'
authors: Amit Pande, Kai Ni, Venkataramani Kini
conference: 2019 IEEE International Conference on Big Data (Big Data)
year: 2019
bibkey: pande2019swag
citations: 12
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1911.10232'}]
tags: ["Recommender Systems"]
short_authors: Amit Pande, Kai Ni, Venkataramani Kini
---
Recent advancements in deep neural networks for graph-structured data have
led to state-of-the-art performance on recommender system benchmarks. In this
work, we present a Graph Convolutional Network (GCN) algorithm SWAG (Sample
Weight and AGgregate), which combines efficient random walks and graph
convolutions on weighted graphs to generate embeddings for nodes (items) that
incorporate both graph structure as well as node feature information such as
item-descriptions and item-images. The three important SWAG operations that
enable us to efficiently generate node embeddings based on graph structures are
(a) Sampling of graph to homogeneous structure, (b) Weighting the sampling,
walks and convolution operations, and (c) using AGgregation functions for
generating convolutions. The work is an adaptation of graphSAGE over weighted
graphs. We deploy SWAG at Target and train it on a graph of more than 500K
products sold online with over 50M edges. Offline and online evaluations reveal
the benefit of using a graph-based approach and the benefits of weighing to
produce high quality embeddings and product recommendations.