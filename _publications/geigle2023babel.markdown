---
layout: publication
title: 'Babel-imagenet: Massively Multilingual Evaluation Of Vision-and-language Representations'
authors: "Gregor Geigle, Radu Timofte, Goran Glava\u0161"
conference: 'Proceedings of the 62nd Annual Meeting of the Association for Computational
  Linguistics (Volume 1: Long Papers)'
year: 2024
bibkey: geigle2023babel
citations: 0
additional_links: [{name: Code, url: 'https://github.com/gregor-ge/Babel-ImageNet'},
  {name: Paper, url: 'https://arxiv.org/abs/2306.08658'}]
tags: ["Evaluation", "Few Shot & Zero Shot", "Text Retrieval"]
short_authors: "Gregor Geigle, Radu Timofte, Goran Glava\u0161"
---
Vision-and-language (VL) models with separate encoders for each modality
(e.g., CLIP) have become the go-to models for zero-shot image classification
and image-text retrieval. They are, however, mostly evaluated in English as
multilingual benchmarks are limited in availability. We introduce
Babel-ImageNet, a massively multilingual benchmark that offers (partial)
translations of ImageNet labels to 100 languages, built without machine
translation or manual annotation. We instead automatically obtain reliable
translations by linking them -- via shared WordNet synsets -- to BabelNet, a
massively multilingual lexico-semantic network. We evaluate 11 public
multilingual CLIP models on zero-shot image classification (ZS-IC) on our
benchmark, demonstrating a significant gap between English ImageNet performance
and that of high-resource languages (e.g., German or Chinese), and an even
bigger gap for low-resource languages (e.g., Sinhala or Lao). Crucially, we
show that the models' ZS-IC performance highly correlates with their
performance in image-text retrieval, validating the use of Babel-ImageNet to
evaluate multilingual models for the vast majority of languages without gold
image-text data. Finally, we show that the performance of multilingual CLIP can
be drastically improved for low-resource languages with parameter-efficient
language-specific training. We make our code and data publicly available:
https://github.com/gregor-ge/Babel-ImageNet