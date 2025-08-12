---
layout: publication
title: Impact Of Base Dataset Design On Few-shot Image Classification
authors: Othman Sbai, Camille Couprie, Mathieu Aubry
conference: Lecture Notes in Computer Science
year: 2020
bibkey: sbai2020impact
citations: 18
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2007.08872'}]
tags: ["Datasets", "Evaluation", "Few Shot & Zero Shot"]
short_authors: Othman Sbai, Camille Couprie, Mathieu Aubry
---
The quality and generality of deep image features is crucially determined by
the data they have been trained on, but little is known about this often
overlooked effect. In this paper, we systematically study the effect of
variations in the training data by evaluating deep features trained on
different image sets in a few-shot classification setting. The experimental
protocol we define allows to explore key practical questions. What is the
influence of the similarity between base and test classes? Given a fixed
annotation budget, what is the optimal trade-off between the number of images
per class and the number of classes? Given a fixed dataset, can features be
improved by splitting or combining different classes? Should simple or diverse
classes be annotated? In a wide range of experiments, we provide clear answers
to these questions on the miniImageNet, ImageNet and CUB-200 benchmarks. We
also show how the base dataset design can improve performance in few-shot
classification more drastically than replacing a simple baseline by an advanced
state of the art algorithm.