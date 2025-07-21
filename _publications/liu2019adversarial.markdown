---
layout: publication
title: Adversarial Binary Coding for Efficient Person Re-identification
authors: Liu et al.
conference: 2019 IEEE International Conference on Multimedia and Expo (ICME)
year: 2019
bibkey: liu2019adversarial
citations: 36
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1803.10914'}]
tags: ["Robustness"]
---
Person re-identification (ReID) aims at matching persons across different
views/scenes. In addition to accuracy, the matching efficiency has received
more and more attention because of demanding applications using large-scale
data. Several binary coding based methods have been proposed for efficient
ReID, which either learn projections to map high-dimensional features to
compact binary codes, or directly adopt deep neural networks by simply
inserting an additional fully-connected layer with tanh-like activations.
However, the former approach requires time-consuming hand-crafted feature
extraction and complicated (discrete) optimizations; the latter lacks the
necessary discriminative information greatly due to the straightforward
activation functions. In this paper, we propose a simple yet effective
framework for efficient ReID inspired by the recent advances in adversarial
learning. Specifically, instead of learning explicit projections or adding
fully-connected mapping layers, the proposed Adversarial Binary Coding (ABC)
framework guides the extraction of binary codes implicitly and effectively. The
discriminability of the extracted codes is further enhanced by equipping the
ABC with a deep triplet network for the ReID task. More importantly, the ABC
and triplet network are simultaneously optimized in an end-to-end manner.
Extensive experiments on three large-scale ReID benchmarks demonstrate the
superiority of our approach over the state-of-the-art methods.