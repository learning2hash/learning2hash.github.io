---
layout: publication
title: 'EDIN: An End-to-end Benchmark And Pipeline For Unknown Entity Discovery And
  Indexing'
authors: Nora Kassner, Fabio Petroni, Mikhail Plekhanov, Sebastian Riedel, Nicola
  Cancedda
conference: Proceedings of the 2022 Conference on Empirical Methods in Natural Language
  Processing
year: 2022
bibkey: kassner2022edin
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2205.12570'}]
tags: ["EMNLP"]
short_authors: Kassner et al.
---
Existing work on Entity Linking mostly assumes that the reference knowledge
base is complete, and therefore all mentions can be linked. In practice this is
hardly ever the case, as knowledge bases are incomplete and because novel
concepts arise constantly. This paper created the Unknown Entity Discovery and
Indexing (EDIN) benchmark where unknown entities, that is entities without a
description in the knowledge base and labeled mentions, have to be integrated
into an existing entity linking system. By contrasting EDIN with zero-shot
entity linking, we provide insight on the additional challenges it poses.
Building on dense-retrieval based entity linking, we introduce the end-to-end
EDIN pipeline that detects, clusters, and indexes mentions of unknown entities
in context. Experiments show that indexing a single embedding per entity
unifying the information of multiple mentions works better than indexing
mentions independently.