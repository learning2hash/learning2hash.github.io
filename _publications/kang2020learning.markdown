---
layout: publication
title: Learning to Embed Categorical Features without Embedding Tables for Recommendation
authors: Kang et al.
conference: Companion Proceedings of the Web Conference 2020
year: 2020
bibkey: kang2020learning
citations: 32
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2010.10784'}]
tags: ["Recommender-Systems"]
---
Embedding learning of categorical features (e.g. user/item IDs) is at the
core of various recommendation models including matrix factorization and neural
collaborative filtering. The standard approach creates an embedding table where
each row represents a dedicated embedding vector for every unique feature
value. However, this method fails to efficiently handle high-cardinality
features and unseen feature values (e.g. new video ID) that are prevalent in
real-world recommendation systems. In this paper, we propose an alternative
embedding framework Deep Hash Embedding (DHE), replacing embedding tables by a
deep embedding network to compute embeddings on the fly. DHE first encodes the
feature value to a unique identifier vector with multiple hashing functions and
transformations, and then applies a DNN to convert the identifier vector to an
embedding. The encoding module is deterministic, non-learnable, and free of
storage, while the embedding network is updated during the training time to
learn embedding generation. Empirical results show that DHE achieves comparable
AUC against the standard one-hot full embedding, with smaller model sizes. Our
work sheds light on the design of DNN-based alternative embedding schemes for
categorical features without using embedding table lookup.