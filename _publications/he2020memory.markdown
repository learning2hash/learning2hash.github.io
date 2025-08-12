---
layout: publication
title: Memory-augmented Relation Network For Few-shot Learning
authors: Jun He, Richang Hong, Xueliang Liu, Mingliang Xu, Zhengjun Zha, Meng Wang
conference: Proceedings of the 28th ACM International Conference on Multimedia
year: 2020
bibkey: he2020memory
citations: 44
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2005.04414'}]
tags: ["Few Shot & Zero Shot"]
short_authors: He et al.
---
Metric-based few-shot learning methods concentrate on learning transferable
feature embedding that generalizes well from seen categories to unseen
categories under the supervision of limited number of labelled instances.
However, most of them treat each individual instance in the working context
separately without considering its relationships with the others. In this work,
we investigate a new metric-learning method, Memory-Augmented Relation Network
(MRN), to explicitly exploit these relationships. In particular, for an
instance, we choose the samples that are visually similar from the working
context, and perform weighted information propagation to attentively aggregate
helpful information from the chosen ones to enhance its representation. In MRN,
we also formulate the distance metric as a learnable relation module which
learns to compare for similarity measurement, and augment the working context
with memory slots, both contributing to its generality. We empirically
demonstrate that MRN yields significant improvement over its ancestor and
achieves competitive or even better performance when compared with other
few-shot learning approaches on the two major benchmark datasets, i.e.
miniImagenet and tieredImagenet.