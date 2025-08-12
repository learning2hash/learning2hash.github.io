---
layout: publication
title: Learning Robust Visual Representations Using Data Augmentation Invariance
authors: "Alex Hern\xE1ndez-Garc\xEDa, Peter K\xF6nig, Tim C. Kietzmann"
conference: 2019 Conference on Cognitive Computational Neuroscience
year: 2019
bibkey: "hern\xE1ndezgarc\xEDa2019learning"
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1906.04547'}]
tags: ["Robustness"]
short_authors: "Alex Hern\xE1ndez-Garc\xEDa, Peter K\xF6nig, Tim C. Kietzmann"
---
Deep convolutional neural networks trained for image object categorization
have shown remarkable similarities with representations found across the
primate ventral visual stream. Yet, artificial and biological networks still
exhibit important differences. Here we investigate one such property:
increasing invariance to identity-preserving image transformations found along
the ventral stream. Despite theoretical evidence that invariance should emerge
naturally from the optimization process, we present empirical evidence that the
activations of convolutional neural networks trained for object categorization
are not robust to identity-preserving image transformations commonly used in
data augmentation. As a solution, we propose data augmentation invariance, an
unsupervised learning objective which improves the robustness of the learned
representations by promoting the similarity between the activations of
augmented image samples. Our results show that this approach is a simple, yet
effective and efficient (10 % increase in training time) way of increasing the
invariance of the models while obtaining similar categorization performance.