---
layout: publication
title: 'Filling In The Gaps: Efficient Event Coreference Resolution Using Graph Autoencoder
  Networks'
authors: "Loic de Langhe, Orph\xE9e de Clercq, Veronique Hoste"
conference: Proceedings of The Sixth Workshop on Computational Models of Reference,
  Anaphora and Coreference (CRAC 2023)
year: 2023
bibkey: delanghe2023filling
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2310.11965'}]
tags: ["Efficiency"]
short_authors: "Loic de Langhe, Orph\xE9e de Clercq, Veronique Hoste"
---
We introduce a novel and efficient method for Event Coreference Resolution
(ECR) applied to a lower-resourced language domain. By framing ECR as a graph
reconstruction task, we are able to combine deep semantic embeddings with
structural coreference chain knowledge to create a parameter-efficient family
of Graph Autoencoder models (GAE). Our method significantly outperforms
classical mention-pair methods on a large Dutch event coreference corpus in
terms of overall score, efficiency and training speed. Additionally, we show
that our models are consistently able to classify more difficult coreference
links and are far more robust in low-data settings when compared to
transformer-based mention-pair coreference algorithms.