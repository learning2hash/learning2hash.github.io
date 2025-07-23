---
layout: publication
title: Document Hashing With Mixture-prior Generative Models
authors: Dong Wei, Su Qinliang, Shen Dinghan, Chen Changyou
conference: Proceedings of the 2019 Conference on Empirical Methods in Natural Language
  Processing and the 9th International Joint Conference on Natural Language Processing
  (EMNLP-IJCNLP)
year: 2019
bibkey: dong2019document
citations: 19
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1908.11078'}]
tags: ["Compact Codes", "Efficiency", "Evaluation", "Hashing Methods", "Scalability", "Unsupervised"]
short_authors: Dong et al.
---
Hashing is promising for large-scale information retrieval tasks thanks to
the efficiency of distance evaluation between binary codes. Generative hashing
is often used to generate hashing codes in an unsupervised way. However,
existing generative hashing methods only considered the use of simple priors,
like Gaussian and Bernoulli priors, which limits these methods to further
improve their performance. In this paper, two mixture-prior generative models
are proposed, under the objective to produce high-quality hashing codes for
documents. Specifically, a Gaussian mixture prior is first imposed onto the
variational auto-encoder (VAE), followed by a separate step to cast the
continuous latent representation of VAE into binary code. To avoid the
performance loss caused by the separate casting, a model using a Bernoulli
mixture prior is further developed, in which an end-to-end training is admitted
by resorting to the straight-through (ST) discrete gradient estimator.
Experimental results on several benchmark datasets demonstrate that the
proposed methods, especially the one using Bernoulli mixture priors,
consistently outperform existing ones by a substantial margin.