---
layout: publication
title: Deep Distributional Sequence Embeddings Based On A Wasserstein Loss
authors: Ahmed Abdelwahab, Niels Landwehr
conference: Neural Processing Letters
year: 2022
bibkey: abdelwahab2019deep
citations: 13
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1912.01933'}]
tags: ["Distance Metric Learning"]
short_authors: Ahmed Abdelwahab, Niels Landwehr
---
Deep metric learning employs deep neural networks to embed instances into a
metric space such that distances between instances of the same class are small
and distances between instances from different classes are large. In most
existing deep metric learning techniques, the embedding of an instance is given
by a feature vector produced by a deep neural network and Euclidean distance or
cosine similarity defines distances between these vectors. In this paper, we
study deep distributional embeddings of sequences, where the embedding of a
sequence is given by the distribution of learned deep features across the
sequence. This has the advantage of capturing statistical information about the
distribution of patterns within the sequence in the embedding. When embeddings
are distributions rather than vectors, measuring distances between embeddings
involves comparing their respective distributions. We propose a distance metric
based on Wasserstein distances between the distributions and a corresponding
loss function for metric learning, which leads to a novel end-to-end trainable
embedding model. We empirically observe that distributional embeddings
outperform standard vector embeddings and that training with the proposed
Wasserstein metric outperforms training with other distance functions.