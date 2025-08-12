---
layout: publication
title: 'Random Fourier Features For Kernel Ridge Regression: Approximation Bounds
  And Statistical Guarantees'
authors: Haim Avron, Michael Kapralov, Cameron Musco, Christopher Musco, Ameya Velingker,
  Amir Zandieh
conference: Arxiv
year: 2017
bibkey: avron2017random
citations: 72
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1804.09893'}]
tags: []
short_authors: Avron et al.
---
Random Fourier features is one of the most popular techniques for scaling up
kernel methods, such as kernel ridge regression. However, despite impressive
empirical results, the statistical properties of random Fourier features are
still not well understood. In this paper we take steps toward filling this gap.
Specifically, we approach random Fourier features from a spectral matrix
approximation point of view, give tight bounds on the number of Fourier
features required to achieve a spectral approximation, and show how spectral
matrix approximation bounds imply statistical guarantees for kernel ridge
regression.
  Qualitatively, our results are twofold: on the one hand, we show that random
Fourier feature approximation can provably speed up kernel ridge regression
under reasonable assumptions. At the same time, we show that the method is
suboptimal, and sampling from a modified distribution in Fourier space, given
by the leverage function of the kernel, yields provably better performance. We
study this optimal sampling distribution for the Gaussian kernel, achieving a
nearly complete characterization for the case of low-dimensional bounded
datasets. Based on this characterization, we propose an efficient sampling
scheme with guarantees superior to random Fourier features in this regime.