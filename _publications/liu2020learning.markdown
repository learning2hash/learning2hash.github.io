---
layout: publication
title: Learning Diverse Fashion Collocation By Neural Graph Filtering
authors: Xin Liu, Yongbin Sun, Ziwei Liu, Dahua Lin
conference: IEEE Transactions on Multimedia
year: 2020
bibkey: liu2020learning
citations: 27
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2003.04888'}]
tags: ["Recommender Systems"]
short_authors: Liu et al.
---
Fashion recommendation systems are highly desired by customers to find
visually-collocated fashion items, such as clothes, shoes, bags, etc. While
existing methods demonstrate promising results, they remain lacking in
flexibility and diversity, e.g. assuming a fixed number of items or favoring
safe but boring recommendations. In this paper, we propose a novel fashion
collocation framework, Neural Graph Filtering, that models a flexible set of
fashion items via a graph neural network. Specifically, we consider the visual
embeddings of each garment as a node in the graph, and describe the
inter-garment relationship as the edge between nodes. By applying symmetric
operations on the edge vectors, this framework allows varying numbers of
inputs/outputs and is invariant to their ordering. We further include a style
classifier augmented with focal loss to enable the collocation of significantly
diverse styles, which are inherently imbalanced in the training set. To
facilitate a comprehensive study on diverse fashion collocation, we reorganize
Amazon Fashion dataset with carefully designed evaluation protocols. We
evaluate the proposed approach on three popular benchmarks, the Polyvore
dataset, the Polyvore-D dataset, and our reorganized Amazon Fashion dataset.
Extensive experimental results show that our approach significantly outperforms
the state-of-the-art methods with over 10% improvements on the standard AUC
metric on the established tasks. More importantly, 82.5% of the users prefer
our diverse-style recommendations over other alternatives in a real-world
perception study.