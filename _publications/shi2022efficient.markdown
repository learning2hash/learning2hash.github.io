---
layout: publication
title: 'Efficient Cross-modal Retrieval Via Deep Binary Hashing And Quantization'
authors: Yang Shi, Young-joo Chung
conference: "BMVC 2021"
year: 2022
citations: 0
bibkey: shi2022efficient
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2202.10232'}
tags: ['Cross-Modal', 'Quantisation', 'Retrieval Models', 'Shallow', 'Datasets', 'Deep Hashing', 'Quantization', 'Hashing']
---
Cross-modal retrieval aims to search for data with similar semantic meanings
across different content modalities. However, cross-modal retrieval requires
huge amounts of storage and retrieval time since it needs to process data in
multiple modalities. Existing works focused on learning single-source compact
features such as binary hash codes that preserve similarities between different
modalities. In this work, we propose a jointly learned deep hashing and
quantization network (HQ) for cross-modal retrieval. We simultaneously learn
binary hash codes and quantization codes to preserve semantic information in
multiple modalities by an end-to-end deep learning architecture. At the
retrieval step, binary hashing is used to retrieve a subset of items from the
search space, then quantization is used to re-rank the retrieved items. We
theoretically and empirically show that this two-stage retrieval approach
provides faster retrieval results while preserving accuracy. Experimental
results on the NUS-WIDE, MIR-Flickr, and Amazon datasets demonstrate that HQ
achieves boosts of more than 7% in precision compared to supervised neural
network-based compact coding models.
