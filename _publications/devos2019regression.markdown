---
layout: publication
title: Regression Networks For Meta-learning Few-shot Classification
authors: Arnout Devos, Matthias Grossglauser
conference: ICML Workshop on Automated Machine Learning (2020)
year: 2019
bibkey: devos2019regression
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1905.13613'}]
tags: ["Distance Metric Learning", "Few Shot & Zero Shot", "ICML"]
short_authors: Arnout Devos, Matthias Grossglauser
---
We propose regression networks for the problem of few-shot classification,
where a classifier must generalize to new classes not seen in the training set,
given only a small number of examples of each class. In high dimensional
embedding spaces the direction of data generally contains richer information
than magnitude. Next to this, state-of-the-art few-shot metric methods that
compare distances with aggregated class representations, have shown superior
performance. Combining these two insights, we propose to meta-learn
classification of embedded points by regressing the closest approximation in
every class subspace while using the regression error as a distance metric.
Similarly to recent approaches for few-shot learning, regression networks
reflect a simple inductive bias that is beneficial in this limited-data regime
and they achieve excellent results, especially when more aggregate class
representations can be formed with multiple shots.