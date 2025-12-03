---
layout: publication
title: 'Deepssn: A Deep Convolutional Neural Network To Assess Spatial Scene Similarity'
authors: Danhuai Guo, Shiyin Ge, Shu Zhang, Song Gao, Ran Tao, Yangang Wang
conference: Transactions in GIS
year: 2022
bibkey: guo2022deepssn
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2202.04755'}]
tags: ["Distance Metric Learning", "Evaluation", "Neural Hashing"]
short_authors: Guo et al.
---
Spatial-query-by-sketch is an intuitive tool to explore human spatial
knowledge about geographic environments and to support communication with scene
database queries. However, traditional sketch-based spatial search methods
perform insufficiently due to their inability to find hidden multi-scale map
features from mental sketches. In this research, we propose a deep
convolutional neural network, namely Deep Spatial Scene Network (DeepSSN), to
better assess the spatial scene similarity. In DeepSSN, a triplet loss function
is designed as a comprehensive distance metric to support the similarity
assessment. A positive and negative example mining strategy using qualitative
constraint networks in spatial reasoning is designed to ensure a consistently
increasing distinction of triplets during the training process. Moreover, we
develop a prototype spatial scene search system using the proposed DeepSSN, in
which the users input spatial query via sketch maps and the system can
automatically augment the sketch training data. The proposed model is validated
using multi-source conflated map data including 131,300 labeled scene samples
after data augmentation. The empirical results demonstrate that the DeepSSN
outperforms baseline methods including k-nearest-neighbors, multilayer
perceptron, AlexNet, DenseNet, and ResNet using mean reciprocal rank and
precision metrics. This research advances geographic information retrieval
studies by introducing a novel deep learning method tailored to spatial scene
queries.