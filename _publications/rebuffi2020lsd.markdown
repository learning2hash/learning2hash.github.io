---
layout: publication
title: 'LSD-C: Linearly Separable Deep Clusters'
authors: Sylvestre-alvise Rebuffi, Sebastien Ehrhardt, Kai Han, Andrea Vedaldi, Andrew
  Zisserman
conference: 2021 IEEE/CVF International Conference on Computer Vision Workshops (ICCVW)
year: 2021
bibkey: rebuffi2020lsd
citations: 23
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2006.10039'}]
tags: ["ICCV"]
short_authors: Rebuffi et al.
---
We present LSD-C, a novel method to identify clusters in an unlabeled
dataset. Our algorithm first establishes pairwise connections in the feature
space between the samples of the minibatch based on a similarity metric. Then
it regroups in clusters the connected samples and enforces a linear separation
between clusters. This is achieved by using the pairwise connections as targets
together with a binary cross-entropy loss on the predictions that the
associated pairs of samples belong to the same cluster. This way, the feature
representation of the network will evolve such that similar samples in this
feature space will belong to the same linearly separated cluster. Our method
draws inspiration from recent semi-supervised learning practice and proposes to
combine our clustering algorithm with self-supervised pretraining and strong
data augmentation. We show that our approach significantly outperforms
competitors on popular public image benchmarks including CIFAR 10/100, STL 10
and MNIST, as well as the document classification dataset Reuters 10K.