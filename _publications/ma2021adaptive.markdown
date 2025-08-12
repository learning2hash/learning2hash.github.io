---
layout: publication
title: Adaptive Poincar\'e Point To Set Distance For Few-shot Classification
authors: Rongkai Ma, Pengfei Fang, Tom Drummond, Mehrtash Harandi
conference: Arxiv
year: 2021
bibkey: ma2021adaptive
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2112.01719'}]
tags: ["Few Shot & Zero Shot", "Robustness"]
short_authors: Ma et al.
---
Learning and generalizing from limited examples, i,e, few-shot learning, is
of core importance to many real-world vision applications. A principal way of
achieving few-shot learning is to realize an embedding where samples from
different classes are distinctive. Recent studies suggest that embedding via
hyperbolic geometry enjoys low distortion for hierarchical and structured data,
making it suitable for few-shot learning. In this paper, we propose to learn a
context-aware hyperbolic metric to characterize the distance between a point
and a set associated with a learned set to set distance. To this end, we
formulate the metric as a weighted sum on the tangent bundle of the hyperbolic
space and develop a mechanism to obtain the weights adaptively and based on the
constellation of the points. This not only makes the metric local but also
dependent on the task in hand, meaning that the metric will adapt depending on
the samples that it compares. We empirically show that such metric yields
robustness in the presence of outliers and achieves a tangible improvement over
baseline models. This includes the state-of-the-art results on five popular
few-shot classification benchmarks, namely mini-ImageNet, tiered-ImageNet,
Caltech-UCSD Birds-200-2011 (CUB), CIFAR-FS, and FC100.