---
layout: publication
title: Learning Discrete Structured Representations By Adversarially Maximizing Mutual
  Information
authors: Karl Stratos, Sam Wiseman
conference: Arxiv
year: 2020
bibkey: stratos2020learning
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2004.03991'}]
tags: ["Hashing Methods", "Neural Hashing", "Unsupervised"]
short_authors: Karl Stratos, Sam Wiseman
---
We propose learning discrete structured representations from unlabeled data
by maximizing the mutual information between a structured latent variable and a
target variable. Calculating mutual information is intractable in this setting.
Our key technical contribution is an adversarial objective that can be used to
tractably estimate mutual information assuming only the feasibility of cross
entropy calculation. We develop a concrete realization of this general
formulation with Markov distributions over binary encodings. We report critical
and unexpected findings on practical aspects of the objective such as the
choice of variational priors. We apply our model on document hashing and show
that it outperforms current best baselines based on discrete and vector
quantized variational autoencoders. It also yields highly compressed
interpretable representations.