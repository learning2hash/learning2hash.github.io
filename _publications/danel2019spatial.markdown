---
layout: publication
title: Spatial Graph Convolutional Networks
authors: "Tomasz Danel, Przemys\u0142aw Spurek, Jacek Tabor, Marek \u015Amieja, \u0141\
  ukasz Struski, Agnieszka S\u0142owik, \u0141ukasz Maziarka"
conference: Communications in Computer and Information Science
year: 2020
bibkey: danel2019spatial
citations: 73
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1909.05310'}]
tags: []
short_authors: Danel et al.
---
Graph Convolutional Networks (GCNs) have recently become the primary choice
for learning from graph-structured data, superseding hash fingerprints in
representing chemical compounds. However, GCNs lack the ability to take into
account the ordering of node neighbors, even when there is a geometric
interpretation of the graph vertices that provides an order based on their
spatial positions. To remedy this issue, we propose Spatial Graph Convolutional
Network (SGCN) which uses spatial features to efficiently learn from graphs
that can be naturally located in space. Our contribution is threefold: we
propose a GCN-inspired architecture which (i) leverages node positions, (ii) is
a proper generalization of both GCNs and Convolutional Neural Networks (CNNs),
(iii) benefits from augmentation which further improves the performance and
assures invariance with respect to the desired properties. Empirically, SGCN
outperforms state-of-the-art graph-based methods on image classification and
chemical tasks.