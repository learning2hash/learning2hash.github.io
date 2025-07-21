---
layout: publication
title: Multi-modal Transformer for Video Retrieval
authors: Gabeur et al.
conference: Lecture Notes in Computer Science
year: 2020
bibkey: gabeur2020multi
citations: 486
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2007.10639'}]
tags: ["Video-Retrieval"]
---
The task of retrieving video content relevant to natural language queries
plays a critical role in effectively handling internet-scale datasets. Most of
the existing methods for this caption-to-video retrieval problem do not fully
exploit cross-modal cues present in video. Furthermore, they aggregate
per-frame visual features with limited or no temporal information. In this
paper, we present a multi-modal transformer to jointly encode the different
modalities in video, which allows each of them to attend to the others. The
transformer architecture is also leveraged to encode and model the temporal
information. On the natural language side, we investigate the best practices to
jointly optimize the language embedding together with the multi-modal
transformer. This novel framework allows us to establish state-of-the-art
results for video retrieval on three datasets. More details are available at
http://thoth.inrialpes.fr/research/MMT.