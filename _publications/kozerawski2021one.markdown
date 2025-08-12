---
layout: publication
title: 'One-class Meta-learning: Towards Generalizable Few-shot Open-set Classification'
authors: Jedrzej Kozerawski, Matthew Turk
conference: Arxiv
year: 2021
bibkey: kozerawski2021one
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2109.06859'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Jedrzej Kozerawski, Matthew Turk
---
Real-world classification tasks are frequently required to work in an
open-set setting. This is especially challenging for few-shot learning problems
due to the small sample size for each known category, which prevents existing
open-set methods from working effectively; however, most multiclass few-shot
methods are limited to closed-set scenarios. In this work, we address the
problem of few-shot open-set classification by first proposing methods for
few-shot one-class classification and then extending them to few-shot
multiclass open-set classification. We introduce two independent few-shot
one-class classification methods: Meta Binary Cross-Entropy (Meta-BCE), which
learns a separate feature representation for one-class classification, and
One-Class Meta-Learning (OCML), which learns to generate one-class classifiers
given standard multiclass feature representation. Both methods can augment any
existing few-shot learning method without requiring retraining to work in a
few-shot multiclass open-set setting without degrading its closed-set
performance. We demonstrate the benefits and drawbacks of both methods in
different problem settings and evaluate them on three standard benchmark
datasets, miniImageNet, tieredImageNet, and Caltech-UCSD-Birds-200-2011, where
they surpass the state-of-the-art methods in the few-shot multiclass open-set
and few-shot one-class tasks.