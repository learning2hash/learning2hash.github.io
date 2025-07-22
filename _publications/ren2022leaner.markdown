---
layout: publication
title: 'Leaner And Faster: Two-stage Model Compression For Lightweight Text-image
  Retrieval'
authors: Ren Siyu, Zhu Kenny Q.
conference: 'Proceedings of the 2022 Conference of the North American Chapter of the
  Association for Computational Linguistics: Human Language Technologies'
year: 2022
bibkey: ren2022leaner
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2204.13913'}]
tags: ["Tools-&-Libraries", "Image-Retrieval"]
short_authors: Ren Siyu, Zhu Kenny Q.
---
Current text-image approaches (e.g., CLIP) typically adopt dual-encoder
architecture using pre-trained vision-language representation. However, these
models still pose non-trivial memory requirements and substantial incremental
indexing time, which makes them less practical on mobile devices. In this
paper, we present an effective two-stage framework to compress large
pre-trained dual-encoder for lightweight text-image retrieval. The resulting
model is smaller (39% of the original), faster (1.6x/2.9x for processing
image/text respectively), yet performs on par with or better than the original
full model on Flickr30K and MSCOCO benchmarks. We also open-source an
accompanying realistic mobile image search application.