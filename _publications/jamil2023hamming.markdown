---
layout: publication
title: Hamming Similarity And Graph Laplacians For Class Partitioning And Adversarial
  Image Detection
authors: Huma Jamil, Yajing Liu, Turgay Caglar, Christina M. Cole, Nathaniel Blanchard,
  Christopher Peterson, Michael Kirby
conference: 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops
  (CVPRW)
year: 2023
bibkey: jamil2023hamming
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2305.01808'}]
tags: ["CVPR"]
short_authors: Jamil et al.
---
Researchers typically investigate neural network representations by examining
activation outputs for one or more layers of a network. Here, we investigate
the potential for ReLU activation patterns (encoded as bit vectors) to aid in
understanding and interpreting the behavior of neural networks. We utilize
Representational Dissimilarity Matrices (RDMs) to investigate the coherence of
data within the embedding spaces of a deep neural network. From each layer of a
network, we extract and utilize bit vectors to construct similarity scores
between images. From these similarity scores, we build a similarity matrix for
a collection of images drawn from 2 classes. We then apply Fiedler partitioning
to the associated Laplacian matrix to separate the classes. Our results
indicate, through bit vector representations, that the network continues to
refine class detectability with the last ReLU layer achieving better than 95%
separation accuracy. Additionally, we demonstrate that bit vectors aid in
adversarial image detection, again achieving over 95% accuracy in separating
adversarial and non-adversarial images using a simple classifier.