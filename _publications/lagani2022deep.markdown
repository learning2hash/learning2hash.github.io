---
layout: publication
title: Deep Features For CBIR With Scarce Data Using Hebbian Learning
authors: Gabriele Lagani, Davide Bacciu, Claudio Gallicchio, Fabrizio Falchi, Claudio
  Gennaro, Giuseppe Amato
conference: Proceedings of the 19th International Conference on Content-based Multimedia
  Indexing
year: 2022
bibkey: lagani2022deep
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2205.08935'}]
tags: [Evaluation, Supervised, Image Retrieval, Efficiency, Datasets, Unsupervised]
short_authors: Lagani et al.
---
Features extracted from Deep Neural Networks (DNNs) have proven to be very
effective in the context of Content Based Image Retrieval (CBIR). In recent
work, biologically inspired \textit\{Hebbian\} learning algorithms have shown
promises for DNN training. In this contribution, we study the performance of
such algorithms in the development of feature extractors for CBIR tasks.
Specifically, we consider a semi-supervised learning strategy in two steps:
first, an unsupervised pre-training stage is performed using Hebbian learning
on the image dataset; second, the network is fine-tuned using supervised
Stochastic Gradient Descent (SGD) training. For the unsupervised pre-training
stage, we explore the nonlinear Hebbian Principal Component Analysis (HPCA)
learning rule. For the supervised fine-tuning stage, we assume sample
efficiency scenarios, in which the amount of labeled samples is just a small
fraction of the whole dataset. Our experimental analysis, conducted on the
CIFAR10 and CIFAR100 datasets shows that, when few labeled samples are
available, our Hebbian approach provides relevant improvements compared to
various alternative methods.