---
layout: publication
title: Retrieval-augmented Convolutional Neural Networks For Improved Robustness Against
  Adversarial Examples
authors: Jake Zhao, Kyunghyun Cho
conference: Arxiv
year: 2018
bibkey: zhao2018retrieval
citations: 14
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1802.09502'}]
tags: ["Robustness"]
short_authors: Jake Zhao, Kyunghyun Cho
---
We propose a retrieval-augmented convolutional network and propose to train
it with local mixup, a novel variant of the recently proposed mixup algorithm.
The proposed hybrid architecture combining a convolutional network and an
off-the-shelf retrieval engine was designed to mitigate the adverse effect of
off-manifold adversarial examples, while the proposed local mixup addresses
on-manifold ones by explicitly encouraging the classifier to locally behave
linearly on the data manifold. Our evaluation of the proposed approach against
five readily-available adversarial attacks on three datasets--CIFAR-10, SVHN
and ImageNet--demonstrate the improved robustness compared to the vanilla
convolutional network.