---
layout: publication
title: Zero-shot Whole Slide Image Retrieval In Histopathology Using Embeddings Of
  Foundation Models
authors: Saghir Alfasly, Ghazal Alabtah, Sobhan Hemati, Krishna Rani Kalari, H. R.
  Tizhoosh
conference: Arxiv
year: 2024
bibkey: alfasly2024zero
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2409.04631'}]
tags: ["Image Retrieval"]
short_authors: Alfasly et al.
---
We have tested recently published foundation models for histopathology for
image retrieval. We report macro average of F1 score for top-1 retrieval,
majority of top-3 retrievals, and majority of top-5 retrievals. We perform
zero-shot retrievals, i.e., we do not alter embeddings and we do not train any
classifier. As test data, we used diagnostic slides of TCGA, The Cancer Genome
Atlas, consisting of 23 organs and 117 cancer subtypes. As a search platform we
used Yottixel that enabled us to perform WSI search using patches. Achieved F1
scores show low performance, e.g., for top-5 retrievals, 27% +/- 13%
(Yottixel-DenseNet), 42% +/- 14% (Yottixel-UNI), 40%+/-13% (Yottixel-Virchow),
41%+/-13% (Yottixel-GigaPath), and 41%+/-14% (GigaPath WSI).