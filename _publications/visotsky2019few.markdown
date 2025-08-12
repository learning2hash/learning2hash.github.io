---
layout: publication
title: Few-shot Learning With Per-sample Rich Supervision
authors: Roman Visotsky, Yuval Atzmon, Gal Chechik
conference: Arxiv
year: 2019
bibkey: visotsky2019few
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1906.03859'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Roman Visotsky, Yuval Atzmon, Gal Chechik
---
Learning with few samples is a major challenge for parameter-rich models like
deep networks. In contrast, people learn complex new concepts even from very
few examples, suggesting that the sample complexity of learning can often be
reduced. Many approaches to few-shot learning build on transferring a
representation from well-sampled classes, or using meta learning to favor
architectures that can learn with few samples. Unfortunately, such approaches
often struggle when learning in an online way or with non-stationary data
streams. Here we describe a new approach to learn with fewer samples, by using
additional information that is provided per sample. Specifically, we show how
the sample complexity can be reduced by providing semantic information about
the relevance of features per sample, like information about the presence of
objects in a scene or confidence of detecting attributes in an image. We
provide an improved generalization error bound for this case. We cast the
problem of using per-sample feature relevance by using a new ellipsoid-margin
loss, and develop an online algorithm that minimizes this loss effectively.
Empirical evaluation on two machine vision benchmarks for scene classification
and fine-grain bird classification demonstrate the benefits of this approach
for few-shot learning.