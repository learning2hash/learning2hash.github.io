---
layout: publication
title: Scalable Nonlinear Embeddings for Semantic Category-based Image Retrieval
authors: Sharma Gaurav, Schiele Bernt
conference: Arxiv
year: 2015
bibkey: sharma2015scalable
additional_links:
   - {name: "License", url: "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/1509.08902"}
tags: ['Arxiv', 'Image Retrieval', 'CNN', 'Supervised']
---
We propose a novel algorithm for the task of supervised discriminative distance learning by nonlinearly embedding vectors into a low dimensional Euclidean space. We work in the challenging setting where supervision is with constraints on similar and dissimilar pairs while training. The proposed method is derived by an approximate kernelization of a linear Mahalanobis-like distance metric learning algorithm and can also be seen as a kernel neural network. The number of model parameters and test time evaluation complexity of the proposed method are O(dD) where D is the dimensionality of the input features and d is the dimension of the projection space - this is in contrast to the usual kernelization methods as, unlike them, the complexity does not scale linearly with the number of training examples. We propose a stochastic gradient based learning algorithm which makes the method scalable (w.r.t. the number of training examples), while being nonlinear. We train the method with up to half a million training pairs of 4096 dimensional CNN features. We give empirical comparisons with relevant baselines on seven challenging datasets for the task of low dimensional semantic category based image retrieval.
