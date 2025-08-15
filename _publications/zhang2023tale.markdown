---
layout: publication
title: 'A Tale Of Two Features: Stable Diffusion Complements DINO For Zero-shot Semantic
  Correspondence'
authors: Junyi Zhang, Charles Herrmann, Junhwa Hur, Luisa Polania Cabrera, Varun Jampani,
  Deqing Sun, Ming-Hsuan Yang
conference: Arxiv
year: 2023
bibkey: zhang2023tale
citations: 29
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2305.15347'}]
tags: ["Datasets", "Evaluation", "Few Shot & Zero Shot"]
short_authors: Zhang et al.
---
Text-to-image diffusion models have made significant advances in generating
and editing high-quality images. As a result, numerous approaches have explored
the ability of diffusion model features to understand and process single images
for downstream tasks, e.g., classification, semantic segmentation, and
stylization. However, significantly less is known about what these features
reveal across multiple, different images and objects. In this work, we exploit
Stable Diffusion (SD) features for semantic and dense correspondence and
discover that with simple post-processing, SD features can perform
quantitatively similar to SOTA representations. Interestingly, the qualitative
analysis reveals that SD features have very different properties compared to
existing representation learning features, such as the recently released
DINOv2: while DINOv2 provides sparse but accurate matches, SD features provide
high-quality spatial information but sometimes inaccurate semantic matches. We
demonstrate that a simple fusion of these two features works surprisingly well,
and a zero-shot evaluation using nearest neighbors on these fused features
provides a significant performance gain over state-of-the-art methods on
benchmark datasets, e.g., SPair-71k, PF-Pascal, and TSS. We also show that
these correspondences can enable interesting applications such as instance
swapping in two images.