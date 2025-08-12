---
layout: publication
title: Convolutional Fine-grained Classification With Self-supervised Target Relation
  Regularization
authors: Kangjun Liu, Ke Chen, Kui Jia
conference: IEEE Transactions on Image Processing
year: 2022
bibkey: liu2022convolutional
citations: 32
additional_links: [{name: Code, url: 'https://github.com/AkonLau/DTRG'}, {name: Paper,
    url: 'https://arxiv.org/abs/2208.01997'}]
tags: ["Self-Supervised"]
short_authors: Kangjun Liu, Ke Chen, Kui Jia
---
Fine-grained visual classification can be addressed by deep representation
learning under supervision of manually pre-defined targets (e.g., one-hot or
the Hadamard codes). Such target coding schemes are less flexible to model
inter-class correlation and are sensitive to sparse and imbalanced data
distribution as well. In light of this, this paper introduces a novel target
coding scheme -- dynamic target relation graphs (DTRG), which, as an auxiliary
feature regularization, is a self-generated structural output to be mapped from
input images. Specifically, online computation of class-level feature centers
is designed to generate cross-category distance in the representation space,
which can thus be depicted by a dynamic graph in a non-parametric manner.
Explicitly minimizing intra-class feature variations anchored on those
class-level centers can encourage learning of discriminative features.
Moreover, owing to exploiting inter-class dependency, the proposed target
graphs can alleviate data sparsity and imbalanceness in representation
learning. Inspired by recent success of the mixup style data augmentation, this
paper introduces randomness into soft construction of dynamic target relation
graphs to further explore relation diversity of target classes. Experimental
results can demonstrate the effectiveness of our method on a number of diverse
benchmarks of multiple visual classification tasks, especially achieving the
state-of-the-art performance on popular fine-grained object benchmarks and
superior robustness against sparse and imbalanced data. Source codes are made
publicly available at https://github.com/AkonLau/DTRG.