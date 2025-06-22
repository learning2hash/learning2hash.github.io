---
layout: publication
title: A Scalable Optimization Mechanism For Pairwise Based Discrete Hashing
authors: Xiaoshuang Shi et al.
conference: Arxiv
year: 2018
citations: 10
bibkey: shi2018scalable
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1811.10810'}]
tags: [Hashing Methods, Evaluation Metrics]
---
Maintaining the pair similarity relationship among originally
high-dimensional data into a low-dimensional binary space is a popular strategy
to learn binary codes. One simiple and intutive method is to utilize two
identical code matrices produced by hash functions to approximate a pairwise
real label matrix. However, the resulting quartic problem is difficult to
directly solve due to the non-convex and non-smooth nature of the objective. In
this paper, unlike previous optimization methods using various relaxation
strategies, we aim to directly solve the original quartic problem using a novel
alternative optimization mechanism to linearize the quartic problem by
introducing a linear regression model. Additionally, we find that gradually
learning each batch of binary codes in a sequential mode, i.e. batch by batch,
is greatly beneficial to the convergence of binary code learning. Based on this
significant discovery and the proposed strategy, we introduce a scalable
symmetric discrete hashing algorithm that gradually and smoothly updates each
batch of binary codes. To further improve the smoothness, we also propose a
greedy symmetric discrete hashing algorithm to update each bit of batch binary
codes. Moreover, we extend the proposed optimization mechanism to solve the
non-convex optimization problems for binary code learning in many other
pairwise based hashing algorithms. Extensive experiments on benchmark
single-label and multi-label databases demonstrate the superior performance of
the proposed mechanism over recent state-of-the-art methods.