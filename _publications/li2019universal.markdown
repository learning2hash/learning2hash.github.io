---
layout: publication
title: Universal Perturbation Attack Against Image Retrieval
authors: Li et al.
conference: 2019 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2019
bibkey: li2019universal
citations: 102
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1812.00552'}]
tags: ["Image Retrieval", "ICCV"]
---
Universal adversarial perturbations (UAPs), a.k.a. input-agnostic
perturbations, has been proved to exist and be able to fool cutting-edge deep
learning models on most of the data samples. Existing UAP methods mainly focus
on attacking image classification models. Nevertheless, little attention has
been paid to attacking image retrieval systems. In this paper, we make the
first attempt in attacking image retrieval systems. Concretely, image retrieval
attack is to make the retrieval system return irrelevant images to the query at
the top ranking list. It plays an important role to corrupt the neighbourhood
relationships among features in image retrieval attack. To this end, we propose
a novel method to generate retrieval-against UAP to break the neighbourhood
relationships of image features via degrading the corresponding ranking metric.
To expand the attack method to scenarios with varying input sizes or
untouchable network parameters, a multi-scale random resizing scheme and a
ranking distillation strategy are proposed. We evaluate the proposed method on
four widely-used image retrieval datasets, and report a significant performance
drop in terms of different metrics, such as mAP and mP@10. Finally, we test our
attack methods on the real-world visual search engine, i.e., Google Images,
which demonstrates the practical potentials of our methods.