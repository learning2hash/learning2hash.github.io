---
layout: publication
title: Unsupervised Deep Metric Learning Via Auxiliary Rotation Loss
authors: Xuefei Cao, Bor-chun Chen, Ser-nam Lim
conference: Arxiv
year: 2019
bibkey: cao2019unsupervised
citations: 12
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1911.07072'}]
tags: ["Distance Metric Learning", "Unsupervised"]
short_authors: Xuefei Cao, Bor-chun Chen, Ser-nam Lim
---
Deep metric learning is an important area due to its applicability to many
domains such as image retrieval and person re-identification. The main drawback
of such models is the necessity for labeled data. In this work, we propose to
generate pseudo-labels for deep metric learning directly from clustering
assignment and we introduce unsupervised deep metric learning (UDML)
regularized by a self-supervision (SS) task. In particular, we propose to
regularize the training process by predicting image rotations. Our method
(UDML-SS) jointly learns discriminative embeddings, unsupervised clustering
assignments of the embeddings, as well as a self-supervised pretext task.
UDML-SS iteratively cluster embeddings using traditional clustering algorithm
(e.g., k-means), and sampling training pairs based on the cluster assignment
for metric learning, while optimizing self-supervised pretext task in a
multi-task fashion. The role of self-supervision is to stabilize the training
process and encourages the model to learn meaningful feature representations
that are not distorted due to unreliable clustering assignments. The proposed
method performs well on standard benchmarks for metric learning, where it
outperforms current state-of-the-art approaches by a large margin and it also
shows competitive performance with various metric learning loss functions.