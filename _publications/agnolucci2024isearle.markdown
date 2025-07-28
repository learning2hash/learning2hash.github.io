---
layout: publication
title: 'Isearle: Improving Textual Inversion For Zero-shot Composed Image Retrieval'
authors: Lorenzo Agnolucci, Alberto Baldrati, Marco Bertini, Alberto del Bimbo
conference: Arxiv
year: 2024
bibkey: agnolucci2024isearle
citations: 1
additional_links: [{name: Code, url: 'https://github.com/miccunifi/SEARLE'}, {name: Paper,
    url: 'https://arxiv.org/abs/2405.02951'}]
tags: ["Few Shot & Zero Shot", "Image Retrieval"]
short_authors: Agnolucci et al.
---
Given a query consisting of a reference image and a relative caption,
Composed Image Retrieval (CIR) aims to retrieve target images visually similar
to the reference one while incorporating the changes specified in the relative
caption. The reliance of supervised methods on labor-intensive manually labeled
datasets hinders their broad applicability. In this work, we introduce a new
task, Zero-Shot CIR (ZS-CIR), that addresses CIR without the need for a labeled
training dataset. We propose an approach named iSEARLE (improved zero-Shot
composEd imAge Retrieval with textuaL invErsion) that involves mapping the
visual information of the reference image into a pseudo-word token in CLIP
token embedding space and combining it with the relative caption. To foster
research on ZS-CIR, we present an open-domain benchmarking dataset named CIRCO
(Composed Image Retrieval on Common Objects in context), the first CIR dataset
where each query is labeled with multiple ground truths and a semantic
categorization. The experimental results illustrate that iSEARLE obtains
state-of-the-art performance on three different CIR datasets -- FashionIQ,
CIRR, and the proposed CIRCO -- and two additional evaluation settings, namely
domain conversion and object composition. The dataset, the code, and the model
are publicly available at https://github.com/miccunifi/SEARLE.