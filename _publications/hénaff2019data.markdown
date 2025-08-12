---
layout: publication
title: Data-efficient Image Recognition With Contrastive Predictive Coding
authors: "Olivier J. H\xE9naff, Aravind Srinivas, Jeffrey de Fauw, Ali Razavi, Carl\
  \ Doersch, S. M. Ali Eslami, Aaron van Den Oord"
conference: Arxiv
year: 2019
bibkey: "h\xE9naff2019data"
citations: 874
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1905.09272'}]
tags: []
short_authors: "H\xE9naff et al."
---
Human observers can learn to recognize new categories of images from a
handful of examples, yet doing so with artificial ones remains an open
challenge. We hypothesize that data-efficient recognition is enabled by
representations which make the variability in natural signals more predictable.
We therefore revisit and improve Contrastive Predictive Coding, an unsupervised
objective for learning such representations. This new implementation produces
features which support state-of-the-art linear classification accuracy on the
ImageNet dataset. When used as input for non-linear classification with deep
neural networks, this representation allows us to use 2-5x less labels than
classifiers trained directly on image pixels. Finally, this unsupervised
representation substantially improves transfer learning to object detection on
the PASCAL VOC dataset, surpassing fully supervised pre-trained ImageNet
classifiers.