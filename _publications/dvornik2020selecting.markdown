---
layout: publication
title: Selecting Relevant Features From A Multi-domain Representation For Few-shot
  Classification
authors: Nikita Dvornik, Cordelia Schmid, Julien Mairal
conference: Lecture Notes in Computer Science
year: 2020
bibkey: dvornik2020selecting
citations: 95
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2003.09338'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Nikita Dvornik, Cordelia Schmid, Julien Mairal
---
Popular approaches for few-shot classification consist of first learning a
generic data representation based on a large annotated dataset, before adapting
the representation to new classes given only a few labeled samples. In this
work, we propose a new strategy based on feature selection, which is both
simpler and more effective than previous feature adaptation approaches. First,
we obtain a multi-domain representation by training a set of semantically
different feature extractors. Then, given a few-shot learning task, we use our
multi-domain feature bank to automatically select the most relevant
representations. We show that a simple non-parametric classifier built on top
of such features produces high accuracy and generalizes to domains never seen
during training, which leads to state-of-the-art results on MetaDataset and
improved accuracy on mini-ImageNet.