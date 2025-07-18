---
layout: publication
title: Instance-based Learning Using The Half-space Proximal Graph
authors: Talamantes Ariana, Chavez Edgar
conference: Pattern Recognition Letters
year: 2021
bibkey: talamantes2021instance
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2102.02755'}]
tags: [DATASETS]
---
The primary example of instance-based learning is the \\(k\\)-nearest neighbor
rule (kNN), praised for its simplicity and the capacity to adapt to new unseen
data and toss away old data. The main disadvantages often mentioned are the
classification complexity, which is \\(O(n)\\), and the estimation of the parameter
\\(k\\), the number of nearest neighbors to be used. The use of indexes at
classification time lifts the former disadvantage, while there is no conclusive
method for the latter.
  This paper presents a parameter-free instance-based learning algorithm using
the \{\em Half-Space Proximal\} (HSP) graph. The HSP neighbors simultaneously
possess proximity and variety concerning the center node. To classify a given
query, we compute its HSP neighbors and apply a simple majority rule over them.
In our experiments, the resulting classifier bettered \\(KNN\\) for any \\(k\\) in a
battery of datasets. This improvement sticks even when applying weighted
majority rules to both kNN and HSP classifiers.
  Surprisingly, when using a probabilistic index to approximate the HSP graph
and consequently speeding-up the classification task, our method could \{\em
improve\} its accuracy in stark contrast with the kNN classifier, which worsens
with a probabilistic index.