---
layout: publication
title: Sign Stable Projections, Sign Cauchy Projections And Chi-square Kernels
authors: Li Ping, Samorodnitsky Gennady, Hopcroft John
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2013
bibkey: li2013sign
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1308.1009'}]
tags: [AAAI, Locality Sensitive Hashing]
---
The method of stable random projections is popular for efficiently computing
the Lp distances in high dimension (where 0<p<=2), using small space. Because
it adopts nonadaptive linear projections, this method is naturally suitable
when the data are collected in a dynamic streaming fashion (i.e., turnstile
data streams). In this paper, we propose to use only the signs of the projected
data and analyze the probability of collision (i.e., when the two signs
differ). We derive a bound of the collision probability which is exact when p=2
and becomes less sharp when p moves away from 2. Interestingly, when p=1 (i.e.,
Cauchy random projections), we show that the probability of collision can be
accurately approximated as functions of the chi-square similarity. For example,
when the (un-normalized) data are binary, the maximum approximation error of
the collision probability is smaller than 0.0192. In text and vision
applications, the chi-square similarity is a popular measure for nonnegative
data when the features are generated from histograms. Our experiments confirm
that the proposed method is promising for large-scale learning applications.