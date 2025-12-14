---
layout: publication
title: 'Beyond The Visible: Multispectral Vision-language Learning For Earth Observation'
authors: Clive Tinashe Marimo, Benedikt Blumenstiel, Maximilian Nitsche, Johannes
  Jakubik, Thomas Brunschwiler
conference: Arxiv
year: 2025
bibkey: marimo2025beyond
citations: 0
additional_links: [{name: Code, url: 'https://github.com/IBM/MS-CLIP'}, {name: Paper,
    url: 'https://arxiv.org/abs/2503.15969'}]
tags: [Evaluation, Few-shot & Zero-shot, Self-Supervised, Datasets, Scalability]
short_authors: Marimo et al.
---
Vision-language models for Earth observation (EO) typically rely on the visual spectrum of data as the only model input, thus failing to leverage the rich spectral information available in the multispectral channels recorded by satellites. Therefore, we introduce Llama3-MS-CLIP, the first vision-language model pre-trained with contrastive learning on a large-scale multispectral dataset and report on the performance gains due to the extended spectral range. Furthermore, we present the largest-to-date image-caption dataset for multispectral data, consisting of one million Sentinel-2 samples and corresponding textual descriptions generated using Llama3-LLaVA-Next and Overture Maps data. We develop a scalable captioning pipeline, which is validated by domain experts. We evaluate Llama3-MS-CLIP on multispectral zero-shot image classification and retrieval using three datasets of varying complexity. Our results demonstrate that Llama3-MS-CLIP significantly outperforms other RGB-based approaches, improving classification accuracy by +6.77% on average and retrieval performance by +4.63% mAP compared to the second-best model. Our results emphasize the relevance of multispectral vision-language learning. The image-caption dataset, code, and model weights are available at https://github.com/IBM/MS-CLIP.