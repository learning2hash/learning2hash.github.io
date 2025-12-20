---
layout: publication
title: On Leveraging Variational Graph Embeddings For Open World Compositional Zero-shot
  Learning
authors: Muhammad Umer Anwaar, Zhihui Pan, Martin Kleinsteuber
conference: Proceedings of the 30th ACM International Conference on Multimedia
year: 2022
bibkey: anwaar2022on
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2204.11848'}]
tags: ["Datasets", "Distance Metric Learning", "Evaluation", "Few Shot & Zero Shot", "Image Retrieval"]
short_authors: Muhammad Umer Anwaar, Zhihui Pan, Martin Kleinsteuber
---
Humans are able to identify and categorize novel compositions of known
concepts. The task in Compositional Zero-Shot learning (CZSL) is to learn
composition of primitive concepts, i.e. objects and states, in such a way that
even their novel compositions can be zero-shot classified. In this work, we do
not assume any prior knowledge on the feasibility of novel compositions
i.e.open-world setting, where infeasible compositions dominate the search
space. We propose a Compositional Variational Graph Autoencoder (CVGAE)
approach for learning the variational embeddings of the primitive concepts
(nodes) as well as feasibility of their compositions (via edges). Such
modelling makes CVGAE scalable to real-world application scenarios. This is in
contrast to SOTA method, CGE, which is computationally very expensive. e.g.for
benchmark C-GQA dataset, CGE requires 3.94 x 10^5 nodes, whereas CVGAE requires
only 1323 nodes. We learn a mapping of the graph and image embeddings onto a
common embedding space. CVGAE adopts a deep metric learning approach and learns
a similarity metric in this space via bi-directional contrastive loss between
projected graph and image embeddings. We validate the effectiveness of our
approach on three benchmark datasets.We also demonstrate via an image retrieval
task that the representations learnt by CVGAE are better suited for
compositional generalization.