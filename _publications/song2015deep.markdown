---
layout: publication
title: Deep Metric Learning Via Lifted Structured Feature Embedding
authors: Hyun Oh Song, Yu Xiang, Stefanie Jegelka, Silvio Savarese
conference: 2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2016
bibkey: song2015deep
citations: 1656
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1511.06452'}]
tags: ["CVPR", "Datasets", "Distance Metric Learning"]
short_authors: Song et al.
---
Learning the distance metric between pairs of examples is of great importance
for learning and visual recognition. With the remarkable success from the state
of the art convolutional neural networks, recent works have shown promising
results on discriminatively training the networks to learn semantic feature
embeddings where similar examples are mapped close to each other and dissimilar
examples are mapped farther apart. In this paper, we describe an algorithm for
taking full advantage of the training batches in the neural network training by
lifting the vector of pairwise distances within the batch to the matrix of
pairwise distances. This step enables the algorithm to learn the state of the
art feature embedding by optimizing a novel structured prediction objective on
the lifted problem. Additionally, we collected Online Products dataset: 120k
images of 23k classes of online products for metric learning. Our experiments
on the CUB-200-2011, CARS196, and Online Products datasets demonstrate
significant improvement over existing deep feature embedding methods on all
experimented embedding sizes with the GoogLeNet network.