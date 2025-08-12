---
layout: publication
title: Dual Graph Embedding For Object-tag Linkprediction On The Knowledge Graph
authors: Chenyang Li, Xu Chen, Ya Zhang, Siheng Chen, Dan Lv, Yanfeng Wang
conference: Arxiv
year: 2020
bibkey: li2020dual
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2007.08304'}]
tags: ["Recommender Systems"]
short_authors: Li et al.
---
Knowledge graphs (KGs) composed of users, objects, and tags are widely used
in web applications ranging from E-commerce, social media sites to news
portals. This paper concentrates on an attractive application which aims to
predict the object-tag links in the KG for better tag recommendation and object
explanation. When predicting the object-tag links, both the first-order and
high-order proximities between entities in the KG propagate essential
similarity information for better prediction. Most existing methods focus on
preserving the first-order proximity between entities in the KG. However, they
cannot capture the high-order proximities in an explicit way, and the adopted
margin-based criterion cannot measure the first-order proximity on the global
structure accurately. In this paper, we propose a novel approach named Dual
Graph Embedding (DGE) that models both the first-order and high-order
proximities in the KG via an auto-encoding architecture to facilitate better
object-tag relation inference. Here the dual graphs contain an object graph and
a tag graph that explicitly depict the high-order object-object and tag-tag
proximities in the KG. The dual graph encoder in DGE then encodes these
high-order proximities in the dual graphs into entity embeddings. The decoder
formulates a skip-gram objective that maximizes the first-order proximity
between observed object-tag pairs over the global proximity structure. With the
supervision of the decoder, the embeddings derived by the encoder will be
refined to capture both the first-order and high-order proximities in the KG
for better link prediction. Extensive experiments on three real-world datasets
demonstrate that DGE outperforms the state-of-the-art methods.