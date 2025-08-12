---
layout: publication
title: Discriminative K-shot Learning Using Probabilistic Models
authors: "Matthias Bauer, Mateo Rojas-Carulla, Jakub Bart\u0142omiej \u015Awi\u0105\
  tkowski, Bernhard Sch\xF6lkopf, Richard E. Turner"
conference: Arxiv
year: 2017
bibkey: bauer2017discriminative
citations: 47
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1706.00326'}]
tags: []
short_authors: Bauer et al.
---
This paper introduces a probabilistic framework for k-shot image
classification. The goal is to generalise from an initial large-scale
classification task to a separate task comprising new classes and small numbers
of examples. The new approach not only leverages the feature-based
representation learned by a neural network from the initial task
(representational transfer), but also information about the classes (concept
transfer). The concept information is encapsulated in a probabilistic model for
the final layer weights of the neural network which acts as a prior for
probabilistic k-shot learning. We show that even a simple probabilistic model
achieves state-of-the-art on a standard k-shot learning dataset by a large
margin. Moreover, it is able to accurately model uncertainty, leading to well
calibrated classifiers, and is easily extensible and flexible, unlike many
recent approaches to k-shot learning.