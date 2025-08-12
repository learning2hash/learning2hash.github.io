---
layout: publication
title: 'Clustem4ano: Clustering Text Embeddings Of Nominal Textual Attributes For
  Microdata Anonymization'
authors: "Robert Aufschl\xE4ger, Sebastian Wilhelm, Michael Heigl, Martin Schramm"
conference: Lecture Notes in Computer Science
year: 2025
bibkey: "aufschl\xE4ger2024clustem4ano"
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.12649'}]
tags: []
short_authors: "Aufschl\xE4ger et al."
---
This work introduces ClustEm4Ano, an anonymization pipeline that can be used
for generalization and suppression-based anonymization of nominal textual
tabular data. It automatically generates value generalization hierarchies
(VGHs) that, in turn, can be used to generalize attributes in
quasi-identifiers. The pipeline leverages embeddings to generate semantically
close value generalizations through iterative clustering. We applied KMeans and
Hierarchical Agglomerative Clustering on \\(13\\) different predefined text
embeddings (both open and closed-source (via APIs)). Our approach is
experimentally tested on a well-known benchmark dataset for anonymization: The
UCI Machine Learning Repository's Adult dataset. ClustEm4Ano supports
anonymization procedures by offering more possibilities compared to using
arbitrarily chosen VGHs. Experiments demonstrate that these VGHs can outperform
manually constructed ones in terms of downstream efficacy (especially for small
\\(k\\)-anonymity (\\(2 \leq k \leq 30\\))) and therefore can foster the quality of
anonymized datasets. Our implementation is made public.