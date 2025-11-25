---
layout: publication
title: 'MEMOIR: Multi-class Extreme Classification With Inexact Margin'
authors: Anton Belyy, Aleksei Sholokhov
conference: Arxiv
year: 2018
bibkey: belyy2018memoir
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1811.09863'}]
tags: ["Datasets", "Evaluation", "Hashing Methods", "Locality-Sensitive-Hashing", "Scalability"]
short_authors: Anton Belyy, Aleksei Sholokhov
---
Multi-class classification with a very large number of classes, or extreme
classification, is a challenging problem from both statistical and
computational perspectives. Most of the classical approaches to multi-class
classification, including one-vs-rest or multi-class support vector machines,
require the exact estimation of the classifier's margin, at both the training
and the prediction steps making them intractable in extreme classification
scenarios. In this paper, we study the impact of computing an approximate
margin using nearest neighbor (ANN) search structures combined with
locality-sensitive hashing (LSH). This approximation allows to dramatically
reduce both the training and the prediction time without a significant loss in
performance. We theoretically prove that this approximation does not lead to a
significant loss of the risk of the model and provide empirical evidence over
five publicly available large scale datasets, showing that the proposed
approach is highly competitive with respect to state-of-the-art approaches on
time, memory and performance measures.