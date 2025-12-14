---
layout: publication
title: Satellite Image Search In Agoraeo
authors: "Ahmet Kerem Aksoy, Pavel Dushev, Eleni Tzirita Zacharatou, Holmer Hemsen,\
  \ Marcela Charfuelan, Jorge-Arnulfo Quian\xE9-Ruiz, Beg\xFCm Demir, Volker Markl"
conference: Proceedings of the VLDB Endowment
year: 2022
bibkey: aksoy2022satellite
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2208.10830'}]
tags: [Image Retrieval, Efficiency, Neural Hashing, Similarity Search, Distance Metric
    Learning, Scalability, Hashing Methods]
short_authors: Aksoy et al.
---
The growing operational capability of global Earth Observation (EO) creates
new opportunities for data-driven approaches to understand and protect our
planet. However, the current use of EO archives is very restricted due to the
huge archive sizes and the limited exploration capabilities provided by EO
platforms. To address this limitation, we have recently proposed MiLaN, a
content-based image retrieval approach for fast similarity search in satellite
image archives. MiLaN is a deep hashing network based on metric learning that
encodes high-dimensional image features into compact binary hash codes. We use
these codes as keys in a hash table to enable real-time nearest neighbor search
and highly accurate retrieval. In this demonstration, we showcase the
efficiency of MiLaN by integrating it with EarthQube, a browser and search
engine within AgoraEO. EarthQube supports interactive visual exploration and
Query-by-Example over satellite image repositories. Demo visitors will interact
with EarthQube playing the role of different users that search images in a
large-scale remote sensing archive by their semantic content and apply other
filters.