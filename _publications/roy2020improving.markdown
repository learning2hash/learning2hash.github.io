---
layout: publication
title: Improving Zero Shot Learning Baselines With Commonsense Knowledge
authors: Abhinaba Roy, Deepanway Ghosal, Erik Cambria, Navonil Majumder, Rada Mihalcea,
  Soujanya Poria
conference: Cognitive Computation
year: 2022
bibkey: roy2020improving
citations: 18
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2012.06236'}]
tags: []
short_authors: Roy et al.
---
Zero shot learning -- the problem of training and testing on a completely
disjoint set of classes -- relies greatly on its ability to transfer knowledge
from train classes to test classes. Traditionally semantic embeddings
consisting of human defined attributes (HA) or distributed word embeddings
(DWE) are used to facilitate this transfer by improving the association between
visual and semantic embeddings. In this paper, we take advantage of explicit
relations between nodes defined in ConceptNet, a commonsense knowledge graph,
to generate commonsense embeddings of the class labels by using a graph
convolution network-based autoencoder. Our experiments performed on three
standard benchmark datasets surpass the strong baselines when we fuse our
commonsense embeddings with existing semantic embeddings i.e. HA and DWE.