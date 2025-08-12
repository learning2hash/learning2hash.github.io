---
layout: publication
title: Semantic-aware Graph Matching Mechanism For Multi-label Image Recognition
authors: Yanan Wu, Songhe Feng, Yang Wang
conference: IEEE Transactions on Circuits and Systems for Video Technology
year: 2023
bibkey: wu2023semantic
citations: 11
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2304.11275'}]
tags: []
short_authors: Yanan Wu, Songhe Feng, Yang Wang
---
Multi-label image recognition aims to predict a set of labels that present in
an image. The key to deal with such problem is to mine the associations between
image contents and labels, and further obtain the correct assignments between
images and their labels. In this paper, we treat each image as a bag of
instances, and formulate the task of multi-label image recognition as an
instance-label matching selection problem. To model such problem, we propose an
innovative Semantic-aware Graph Matching framework for Multi-Label image
recognition (ML-SGM), in which Graph Matching mechanism is introduced owing to
its good performance of excavating the instance and label relationship. The
framework explicitly establishes category correlations and instance-label
correspondences by modeling the relation among content-aware (instance) and
semantic-aware (label) category representations, to facilitate multi-label
image understanding and reduce the dependency of large amounts of training
samples for each category. Specifically, we first construct an instance spatial
graph and a label semantic graph respectively and then incorporate them into a
constructed assignment graph by connecting each instance to all labels.
Subsequently, the graph network block is adopted to aggregate and update all
nodes and edges state on the assignment graph to form structured
representations for each instance and label. Our network finally derives a
prediction score for each instance-label correspondence and optimizes such
correspondence with a weighted cross-entropy loss. Empirical results conducted
on generic multi-label image recognition demonstrate the superiority of our
proposed method. Moreover, the proposed method also shows advantages in
multi-label recognition with partial labels and multi-label few-shot learning,
as well as outperforms current state-of-the-art methods with a clear margin.