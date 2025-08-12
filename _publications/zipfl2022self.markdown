---
layout: publication
title: Self Supervised Clustering Of Traffic Scenes Using Graph Representations
authors: "Maximilian Zipfl, Moritz Jarosch, J. Marius Z\xF6llner"
conference: 2022 International Conference on Electrical, Computer, Communications
  and Mechatronics Engineering (ICECCME)
year: 2022
bibkey: zipfl2022self
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2211.15508'}]
tags: ["Self-Supervised"]
short_authors: "Maximilian Zipfl, Moritz Jarosch, J. Marius Z\xF6llner"
---
Examining graphs for similarity is a well-known challenge, but one that is
mandatory for grouping graphs together. We present a data-driven method to
cluster traffic scenes that is self-supervised, i.e. without manual labelling.
We leverage the semantic scene graph model to create a generic graph embedding
of the traffic scene, which is then mapped to a low-dimensional embedding space
using a Siamese network, in which clustering is performed. In the training
process of our novel approach, we augment existing traffic scenes in the
Cartesian space to generate positive similarity samples. This allows us to
overcome the challenge of reconstructing a graph and at the same time obtain a
representation to describe the similarity of traffic scenes. We could show,
that the resulting clusters possess common semantic characteristics. The
approach was evaluated on the INTERACTION dataset.