---
layout: publication
title: Entity Embeddings Of Categorical Variables
authors: Cheng Guo, Felix Berkhahn
conference: Arxiv
year: 2016
bibkey: guo2016entity
citations: 300
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1604.06737'}]
tags: []
short_authors: Cheng Guo, Felix Berkhahn
---
We map categorical variables in a function approximation problem into
Euclidean spaces, which are the entity embeddings of the categorical variables.
The mapping is learned by a neural network during the standard supervised
training process. Entity embedding not only reduces memory usage and speeds up
neural networks compared with one-hot encoding, but more importantly by mapping
similar values close to each other in the embedding space it reveals the
intrinsic properties of the categorical variables. We applied it successfully
in a recent Kaggle competition and were able to reach the third position with
relative simple features. We further demonstrate in this paper that entity
embedding helps the neural network to generalize better when the data is sparse
and statistics is unknown. Thus it is especially useful for datasets with lots
of high cardinality features, where other methods tend to overfit. We also
demonstrate that the embeddings obtained from the trained neural network boost
the performance of all tested machine learning methods considerably when used
as the input features instead. As entity embedding defines a distance measure
for categorical variables it can be used for visualizing categorical data and
for data clustering.