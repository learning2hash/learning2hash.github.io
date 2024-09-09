---
layout: publication
title: "Pairwise Supervised Hashing with Bernoulli Variational Auto-Encoder and Self-Control Gradient Estimator"
authors: Dadaneh Siamak Zamani, Boluki Shahin, Yin Mingzhang, Zhou Mingyuan, Qian Xiaoning
conference: Uncertainty in Artificial Intelligence Conference
year: 2020
bibkey: dadaneh2020pairwise
additional_links:
- {name: "Paper", url: "https://arxiv.org/abs/2005.10477"}
tags: ['Supervised']
---
Semantic hashing has become a crucial component of fast similarity search in many large-scale information retrieval systems, in particular, for text data. Variational auto-encoders (VAEs) with binary latent variables as hashing codes provide state-of-the-art performance in terms of precision for document retrieval. We propose a pairwise loss function with discrete latent VAE to reward within-class similarity and between-class dissimilarity for supervised hashing. Instead of solving the optimization relying on existing biased gradient estimators, an unbiased low-variance gradient estimator is adopted to optimize the hashing function by evaluating the non-differentiable loss function over two correlated sets of binary hashing codes to control the variance of gradient estimates. This new semantic hashing framework achieves superior performance compared to the state-of-the-arts, as demonstrated by our comprehensive experiments.