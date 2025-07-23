---
layout: publication
title: Improving Deep Metric Learning By Divide And Conquer
authors: "Sanakoyeu Artsiom, Ma Pingchuan, Tschernezki Vadim, Ommer Bj\xF6rn"
conference: IEEE Transactions on Pattern Analysis and Machine Intelligence
year: 2021
bibkey: sanakoyeu2021improving
citations: 16
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2109.04003'}]
tags: ["Distance Metric Learning", "Efficiency", "Image Retrieval", "Scalability"]
short_authors: Sanakoyeu et al.
---
Deep metric learning (DML) is a cornerstone of many computer vision
applications. It aims at learning a mapping from the input domain to an
embedding space, where semantically similar objects are located nearby and
dissimilar objects far from another. The target similarity on the training data
is defined by user in form of ground-truth class labels. However, while the
embedding space learns to mimic the user-provided similarity on the training
data, it should also generalize to novel categories not seen during training.
Besides user-provided groundtruth training labels, a lot of additional visual
factors (such as viewpoint changes or shape peculiarities) exist and imply
different notions of similarity between objects, affecting the generalization
on the images unseen during training. However, existing approaches usually
directly learn a single embedding space on all available training data,
struggling to encode all different types of relationships, and do not
generalize well. We propose to build a more expressive representation by
jointly splitting the embedding space and the data hierarchically into smaller
sub-parts. We successively focus on smaller subsets of the training data,
reducing its variance and learning a different embedding subspace for each data
subset. Moreover, the subspaces are learned jointly to cover not only the
intricacies, but the breadth of the data as well. Only after that, we build the
final embedding from the subspaces in the conquering stage. The proposed
algorithm acts as a transparent wrapper that can be placed around arbitrary
existing DML methods. Our approach significantly improves upon the
state-of-the-art on image retrieval, clustering, and re-identification tasks
evaluated using CUB200-2011, CARS196, Stanford Online Products, In-shop
Clothes, and PKU VehicleID datasets.