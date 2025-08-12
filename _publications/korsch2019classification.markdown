---
layout: publication
title: Classification-specific Parts For Improving Fine-grained Visual Categorization
authors: Dimitri Korsch, Paul Bodesheim, Joachim Denzler
conference: Lecture Notes in Computer Science
year: 2019
bibkey: korsch2019classification
citations: 38
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1909.07075'}]
tags: []
short_authors: Dimitri Korsch, Paul Bodesheim, Joachim Denzler
---
Fine-grained visual categorization is a classification task for
distinguishing categories with high intra-class and small inter-class variance.
While global approaches aim at using the whole image for performing the
classification, part-based solutions gather additional local information in
terms of attentions or parts. We propose a novel classification-specific part
estimation that uses an initial prediction as well as back-propagation of
feature importance via gradient computations in order to estimate relevant
image regions. The subsequently detected parts are then not only selected by
a-posteriori classification knowledge, but also have an intrinsic spatial
extent that is determined automatically. This is in contrast to most part-based
approaches and even to available ground-truth part annotations, which only
provide point coordinates and no additional scale information. We show in our
experiments on various widely-used fine-grained datasets the effectiveness of
the mentioned part selection method in conjunction with the extracted part
features.