---
layout: publication
title: Explaining And Mitigating The Modality Gap In Contrastive Multimodal Learning
authors: Can Yaras, Siyi Chen, Peng Wang, Qing Qu
conference: Arxiv
year: 2024
bibkey: yaras2024explaining
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.07909'}]
tags: ["Evaluation", "Few Shot & Zero Shot", "Self-Supervised", "Text Retrieval"]
short_authors: Yaras et al.
---
Multimodal learning has recently gained significant popularity, demonstrating
impressive performance across various zero-shot classification tasks and a
range of perceptive and generative applications. Models such as Contrastive
Language-Image Pretraining (CLIP) are designed to bridge different modalities,
such as images and text, by learning a shared representation space through
contrastive learning. Despite their success, the working mechanisms underlying
multimodal learning are not yet well understood. Notably, these models often
exhibit a modality gap, where different modalities occupy distinct regions
within the shared representation space. In this work, we conduct an in-depth
analysis of the emergence of modality gap by characterizing the gradient flow
learning dynamics. Specifically, we identify the critical roles of mismatched
data pairs and a learnable temperature parameter in causing and perpetuating
the modality gap during training. Furthermore, our theoretical insights are
validated through experiments on practical CLIP models. These findings provide
principled guidance for mitigating the modality gap, including strategies such
as appropriate temperature scheduling and modality swapping. Additionally, we
demonstrate that closing the modality gap leads to improved performance on
tasks such as image-text retrieval.