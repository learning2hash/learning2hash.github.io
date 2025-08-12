---
layout: publication
title: Infinite Mixture Prototypes For Few-shot Learning
authors: Kelsey R. Allen, Evan Shelhamer, Hanul Shin, Joshua B. Tenenbaum
conference: Arxiv
year: 2019
bibkey: allen2019infinite
citations: 82
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1902.04552'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Allen et al.
---
We propose infinite mixture prototypes to adaptively represent both simple
and complex data distributions for few-shot learning. Our infinite mixture
prototypes represent each class by a set of clusters, unlike existing
prototypical methods that represent each class by a single cluster. By
inferring the number of clusters, infinite mixture prototypes interpolate
between nearest neighbor and prototypical representations, which improves
accuracy and robustness in the few-shot regime. We show the importance of
adaptive capacity for capturing complex data distributions such as alphabets,
with 25% absolute accuracy improvements over prototypical networks, while still
maintaining or improving accuracy on the standard Omniglot and mini-ImageNet
benchmarks. In clustering labeled and unlabeled data by the same clustering
rule, infinite mixture prototypes achieves state-of-the-art semi-supervised
accuracy. As a further capability, we show that infinite mixture prototypes can
perform purely unsupervised clustering, unlike existing prototypical methods.