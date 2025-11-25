---
layout: publication
title: Dynamic Adapter With Semantics Disentangling For Cross-lingual Cross-modal
  Retrieval
authors: Rui Cai, Zhiyu Dong, Jianfeng Dong, Xun Wang
conference: Arxiv
year: 2024
bibkey: cai2024dynamic
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.13510'}]
tags: ["Datasets", "Multimodal Retrieval"]
short_authors: Cai et al.
---
Existing cross-modal retrieval methods typically rely on large-scale
vision-language pair data. This makes it challenging to efficiently develop a
cross-modal retrieval model for under-resourced languages of interest.
Therefore, Cross-lingual Cross-modal Retrieval (CCR), which aims to align
vision and the low-resource language (the target language) without using any
human-labeled target-language data, has gained increasing attention. As a
general parameter-efficient way, a common solution is to utilize adapter
modules to transfer the vision-language alignment ability of Vision-Language
Pretraining (VLP) models from a source language to a target language. However,
these adapters are usually static once learned, making it difficult to adapt to
target-language captions with varied expressions. To alleviate it, we propose
Dynamic Adapter with Semantics Disentangling (DASD), whose parameters are
dynamically generated conditioned on the characteristics of the input captions.
Considering that the semantics and expression styles of the input caption
largely influence how to encode it, we propose a semantic disentangling module
to extract the semantic-related and semantic-agnostic features from the input,
ensuring that generated adapters are well-suited to the characteristics of
input caption. Extensive experiments on two image-text datasets and one
video-text dataset demonstrate the effectiveness of our model for cross-lingual
cross-modal retrieval, as well as its good compatibility with various VLP
models.