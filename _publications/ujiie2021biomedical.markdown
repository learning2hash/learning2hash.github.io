---
layout: publication
title: Biomedical Entity Linking With Contrastive Context Matching
authors: Ujiie Shogo, Iso Hayate, Aramaki Eiji
conference: Arxiv
year: 2021
bibkey: ujiie2021biomedical
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2106.07583'}]
tags: ["Self-Supervised", "Tools-&-Libraries"]
short_authors: Ujiie Shogo, Iso Hayate, Aramaki Eiji
---
We introduce BioCoM, a contrastive learning framework for biomedical entity
linking that uses only two resources: a small-sized dictionary and a large
number of raw biomedical articles. Specifically, we build the training
instances from raw PubMed articles by dictionary matching and use them to train
a context-aware entity linking model with contrastive learning. We predict the
normalized biomedical entity at inference time through a nearest-neighbor
search. Results found that BioCoM substantially outperforms state-of-the-art
models, especially in low-resource settings, by effectively using the context
of the entities.