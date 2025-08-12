---
layout: publication
title: Episode Adaptive Embedding Networks For Few-shot Learning
authors: Fangbing Liu, Qing Wang
conference: Lecture Notes in Computer Science
year: 2021
bibkey: liu2021episode
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2106.09398'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Fangbing Liu, Qing Wang
---
Few-shot learning aims to learn a classifier using a few labelled instances
for each class. Metric-learning approaches for few-shot learning embed
instances into a high-dimensional space and conduct classification based on
distances among instance embeddings. However, such instance embeddings are
usually shared across all episodes and thus lack the discriminative power to
generalize classifiers according to episode-specific features. In this paper,
we propose a novel approach, namely *Episode Adaptive Embedding Network*
(EAEN), to learn episode-specific embeddings of instances. By leveraging the
probability distributions of all instances in an episode at each channel-pixel
embedding dimension, EAEN can not only alleviate the overfitting issue
encountered in few-shot learning tasks, but also capture discriminative
features specific to an episode. To empirically verify the effectiveness and
robustness of EAEN, we have conducted extensive experiments on three widely
used benchmark datasets, under various combinations of different generic
embedding backbones and different classifiers. The results show that EAEN
significantly improves classification accuracy about \(10%\) to \(20%\) in
different settings over the state-of-the-art methods.