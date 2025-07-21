---
layout: publication
title: Uncertainty-aware Unsupervised Video Hashing
authors: Wang et al.
conference: IEEE Transactions on Image Processing
year: 2025
bibkey: wang2025uncertainty
citations: 48
additional_links: [{name: Paper, url: 'https://proceedings.mlr.press/v206/wang23i.html'}]
tags: ["Hashing Methods", "Unsupervised", "Supervised"]
---
Learning to hash has become popular for video retrieval due to its fast speed and low storage consumption. Previous efforts formulate video hashing as training a binary auto-encoder, for which noncontinuous latent representations are optimized by the biased straight-through (ST) back-propagation heuristic. We propose to formulate video hashing as learning a discrete variational auto-encoder with the factorized Bernoulli latent distribution, termed as Bernoulli variational auto-encoder (BerVAE). The corresponding evidence lower bound (ELBO) in our BerVAE implementation leads to closed-form gradient expression, which can be applied to achieve principled training along with some other unbiased gradient estimators. BerVAE enables uncertainty-aware video hashing by predicting the probability distribution of video hash code-words, thus providing reliable uncertainty quantification. Experiments on both simulated and real-world large-scale video data demonstrate that our BerVAE trained with unbiased gradient estimators can achieve the state-of-the-art retrieval performance. Furthermore, we show that quantified uncertainty is highly correlated to video retrieval performance, which can be leveraged to further improve the retrieval accuracy. Our code is available at https://github.com/wangyucheng1234/BerVAE