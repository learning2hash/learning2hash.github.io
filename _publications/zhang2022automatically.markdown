---
layout: publication
title: Automatically Discovering Novel Visual Categories With Self-supervised Prototype
  Learning
authors: Lu Zhang, Lu Qi, Xu Yang, Hong Qiao, Ming-Hsuan Yang, Zhiyong Liu
conference: Arxiv
year: 2022
bibkey: zhang2022automatically
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2208.00979'}]
tags: ["Self-Supervised"]
short_authors: Zhang et al.
---
This paper tackles the problem of novel category discovery (NCD), which aims
to discriminate unknown categories in large-scale image collections. The NCD
task is challenging due to the closeness to the real-world scenarios, where we
have only encountered some partial classes and images. Unlike other works on
the NCD, we leverage the prototypes to emphasize the importance of category
discrimination and alleviate the issue of missing annotations of novel classes.
Concretely, we propose a novel adaptive prototype learning method consisting of
two main stages: prototypical representation learning and prototypical
self-training. In the first stage, we obtain a robust feature extractor, which
could serve for all images with base and novel categories. This ability of
instance and category discrimination of the feature extractor is boosted by
self-supervised learning and adaptive prototypes. In the second stage, we
utilize the prototypes again to rectify offline pseudo labels and train a final
parametric classifier for category clustering. We conduct extensive experiments
on four benchmark datasets and demonstrate the effectiveness and robustness of
the proposed method with state-of-the-art performance.