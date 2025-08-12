---
layout: publication
title: Lyric Document Embeddings For Music Tagging
authors: Matt McVicar, Bruno di Giorgi, Baris Dundar, Matthias Mauch
conference: Arxiv
year: 2021
bibkey: mcvicar2021lyric
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2112.11436'}]
tags: ["Datasets"]
short_authors: McVicar et al.
---
We present an empirical study on embedding the lyrics of a song into a
fixed-dimensional feature for the purpose of music tagging. Five methods of
computing token-level and four methods of computing document-level
representations are trained on an industrial-scale dataset of tens of millions
of songs. We compare simple averaging of pretrained embeddings to modern
recurrent and attention-based neural architectures. Evaluating on a wide range
of tagging tasks such as genre classification, explicit content identification
and era detection, we find that averaging word embeddings outperform more
complex architectures in many downstream metrics.