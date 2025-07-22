---
layout: publication
title: Deep Hashing for Compact Binary Codes Learning
authors: Liong V., Lu, Wang, Moulin, Zhou
conference: 2015 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2015
bibkey: liong2025deep
citations: 579
additional_links: [{name: Paper, url: 'http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.707.72&rep=rep1&type=pdf'}]
tags: ["CVPR", "Neural-Hashing", "Compact-Codes", "Hashing-Methods", "Evaluation", "Supervised"]
short_authors: Liong et al.
---
In this paper, we propose a new deep hashing (DH) approach
to learn compact binary codes for large scale visual
search. Unlike most existing binary codes learning methods
which seek a single linear projection to map each sample
into a binary vector, we develop a deep neural network
to seek multiple hierarchical non-linear transformations to
learn these binary codes, so that the nonlinear relationship
of samples can be well exploited. Our model is learned under
three constraints at the top layer of the deep network:
1) the loss between the original real-valued feature descriptor
and the learned binary vector is minimized, 2) the binary
codes distribute evenly on each bit, and 3) different bits
are as independent as possible. To further improve the discriminative
power of the learned binary codes, we extend
DH into supervised DH (SDH) by including one discriminative
term into the objective function of DH which simultaneously
maximizes the inter-class variations and minimizes
the intra-class variations of the learned binary codes. Experimental
results show the superiority of the proposed approach
over the state-of-the-arts.