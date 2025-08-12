---
layout: publication
title: Efficient OCR For Building A Diverse Digital History
authors: Jacob Carlson, Tom Bryan, Melissa Dell
conference: 'Proceedings of the 62nd Annual Meeting of the Association for Computational
  Linguistics (Volume 1: Long Papers)'
year: 2024
bibkey: carlson2023efficient
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2304.02737'}]
tags: ["Image Retrieval"]
short_authors: Jacob Carlson, Tom Bryan, Melissa Dell
---
Thousands of users consult digital archives daily, but the information they
can access is unrepresentative of the diversity of documentary history. The
sequence-to-sequence architecture typically used for optical character
recognition (OCR) - which jointly learns a vision and language model - is
poorly extensible to low-resource document collections, as learning a
language-vision model requires extensive labeled sequences and compute. This
study models OCR as a character level image retrieval problem, using a
contrastively trained vision encoder. Because the model only learns characters'
visual features, it is more sample efficient and extensible than existing
architectures, enabling accurate OCR in settings where existing solutions fail.
Crucially, the model opens new avenues for community engagement in making
digital history more representative of documentary history.