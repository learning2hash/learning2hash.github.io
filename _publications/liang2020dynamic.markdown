---
layout: publication
title: Dynamic Sampling for Deep Metric Learning
authors: Liang Chang-hui, Zhao Wan-lei, Chen Run-qing
conference: Pattern Recognition Letters
year: 2021
bibkey: liang2020dynamic
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2004.11624'}]
tags: ["Distance-Metric-Learning"]
---
Deep metric learning maps visually similar images onto nearby locations and
visually dissimilar images apart from each other in an embedding manifold. The
learning process is mainly based on the supplied image negative and positive
training pairs. In this paper, a dynamic sampling strategy is proposed to
organize the training pairs in an easy-to-hard order to feed into the network.
It allows the network to learn general boundaries between categories from the
easy training pairs at its early stages and finalize the details of the model
mainly relying on the hard training samples in the later. Compared to the
existing training sample mining approaches, the hard samples are mined with
little harm to the learned general model. This dynamic sampling strategy is
formularized as two simple terms that are compatible with various loss
functions. Consistent performance boost is observed when it is integrated with
several popular loss functions on fashion search, fine-grained classification,
and person re-identification tasks.