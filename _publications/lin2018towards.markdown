---
layout: publication
title: Towards A Theoretical Understanding Of Hashing-based Neural Nets
authors: Yibo Lin, Zhao Song, Lin F. Yang
conference: Arxiv
year: 2018
bibkey: lin2018towards
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1812.10244'}]
tags: [Hashing Methods, Neural Hashing]
short_authors: Yibo Lin, Zhao Song, Lin F. Yang
---
Parameter reduction has been an important topic in deep learning due to the
ever-increasing size of deep neural network models and the need to train and
run them on resource limited machines. Despite many efforts in this area, there
were no rigorous theoretical guarantees on why existing neural net compression
methods should work. In this paper, we provide provable guarantees on some
hashing-based parameter reduction methods in neural nets. First, we introduce a
neural net compression scheme based on random linear sketching (which is
usually implemented efficiently via hashing), and show that the sketched
(smaller) network is able to approximate the original network on all input data
coming from any smooth and well-conditioned low-dimensional manifold. The
sketched network can also be trained directly via back-propagation. Next, we
study the previously proposed HashedNets architecture and show that the
optimization landscape of one-hidden-layer HashedNets has a local strong
convexity property similar to a normal fully connected neural network. We
complement our theoretical results with empirical verifications.