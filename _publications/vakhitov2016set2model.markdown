---
layout: publication
title: 'Set2model Networks: Learning Discriminatively To Learn Generative Models'
authors: A. Vakhitov, A. Kuzmin, V. Lempitsky
conference: Arxiv
year: 2016
bibkey: vakhitov2016set2model
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1612.07697'}]
tags: ["Image Retrieval"]
short_authors: A. Vakhitov, A. Kuzmin, V. Lempitsky
---
We present a new "learning-to-learn"-type approach that enables rapid
learning of concepts from small-to-medium sized training sets and is primarily
designed for web-initialized image retrieval. At the core of our approach is a
deep architecture (a Set2Model network) that maps sets of examples to simple
generative probabilistic models such as Gaussians or mixtures of Gaussians in
the space of high-dimensional descriptors. The parameters of the embedding into
the descriptor space are trained in the end-to-end fashion in the meta-learning
stage using a set of training learning problems. The main technical novelty of
our approach is the derivation of the backprop process through the mixture
model fitting, which makes the likelihood of the resulting models
differentiable with respect to the positions of the input descriptors.
  While the meta-learning process for a Set2Model network is discriminative, a
trained Set2Model network performs generative learning of generative models in
the descriptor space, which facilitates learning in the cases when no negative
examples are available, and whenever the concept being learned is polysemous or
represented by noisy training sets. Among other experiments, we demonstrate
that these properties allow Set2Model networks to pick visual concepts from the
raw outputs of Internet image search engines better than a set of strong
baselines.