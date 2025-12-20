---
layout: publication
title: Efficient Training On Very Large Corpora Via Gramian Estimation
authors: Walid Krichene, Nicolas Mayoraz, Steffen Rendle, Li Zhang, Xinyang Yi, Lichan
  Hong, Ed Chi, John Anderson
conference: Arxiv
year: 2018
bibkey: krichene2018efficient
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1807.07187'}]
tags: ["Efficiency", "Scalability"]
short_authors: Krichene et al.
---
We study the problem of learning similarity functions over very large corpora
using neural network embedding models. These models are typically trained using
SGD with sampling of random observed and unobserved pairs, with a number of
samples that grows quadratically with the corpus size, making it expensive to
scale to very large corpora. We propose new efficient methods to train these
models without having to sample unobserved pairs. Inspired by matrix
factorization, our approach relies on adding a global quadratic penalty to all
pairs of examples and expressing this term as the matrix-inner-product of two
generalized Gramians. We show that the gradient of this term can be efficiently
computed by maintaining estimates of the Gramians, and develop variance
reduction schemes to improve the quality of the estimates. We conduct
large-scale experiments that show a significant improvement in training time
and generalization quality compared to traditional sampling methods.