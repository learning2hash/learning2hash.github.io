---
layout: publication
title: One-bit Supervision For Image Classification
authors: Hengtong Hu, Lingxi Xie, Zewei Du, Richang Hong, Qi Tian
conference: NeurIPS 2020
year: 2020
bibkey: hu2020one
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2009.06168'}]
tags: ["NEURIPS", "Supervised"]
short_authors: Hu et al.
---
This paper presents one-bit supervision, a novel setting of learning from
incomplete annotations, in the scenario of image classification. Instead of
training a model upon the accurate label of each sample, our setting requires
the model to query with a predicted label of each sample and learn from the
answer whether the guess is correct. This provides one bit (yes or no) of
information, and more importantly, annotating each sample becomes much easier
than finding the accurate label from many candidate classes. There are two keys
to training a model upon one-bit supervision: improving the guess accuracy and
making use of incorrect guesses. For these purposes, we propose a multi-stage
training paradigm which incorporates negative label suppression into an
off-the-shelf semi-supervised learning algorithm. In three popular image
classification benchmarks, our approach claims higher efficiency in utilizing
the limited amount of annotations.