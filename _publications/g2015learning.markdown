---
layout: publication
title: Learning Local Image Descriptors With Deep Siamese And Triplet Convolutional
  Networks By Minimising Global Loss Functions
authors: Vijay Kumar B G, Gustavo Carneiro, Ian Reid
conference: Arxiv
year: 2015
bibkey: g2015learning
citations: 134
additional_links: [{name: Code, url: 'https://github.com/vijaykbg/deep-patchmatch'},
  {name: Paper, url: 'https://arxiv.org/abs/1512.09272'}]
tags: ["Datasets", "Evaluation"]
short_authors: Vijay Kumar B G, Gustavo Carneiro, Ian Reid
---
Recent innovations in training deep convolutional neural network (ConvNet)
models have motivated the design of new methods to automatically learn local
image descriptors. The latest deep ConvNets proposed for this task consist of a
siamese network that is trained by penalising misclassification of pairs of
local image patches. Current results from machine learning show that replacing
this siamese by a triplet network can improve the classification accuracy in
several problems, but this has yet to be demonstrated for local image
descriptor learning. Moreover, current siamese and triplet networks have been
trained with stochastic gradient descent that computes the gradient from
individual pairs or triplets of local image patches, which can make them prone
to overfitting. In this paper, we first propose the use of triplet networks for
the problem of local image descriptor learning. Furthermore, we also propose
the use of a global loss that minimises the overall classification error in the
training set, which can improve the generalisation capability of the model.
Using the UBC benchmark dataset for comparing local image descriptors, we show
that the triplet network produces a more accurate embedding than the siamese
network in terms of the UBC dataset errors. Moreover, we also demonstrate that
a combination of the triplet and global losses produces the best embedding in
the field, using this triplet network. Finally, we also show that the use of
the central-surround siamese network trained with the global loss produces the
best result of the field on the UBC dataset. Pre-trained models are available
online at https://github.com/vijaykbg/deep-patchmatch