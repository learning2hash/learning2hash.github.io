---
layout: publication
title: 'Fuselip: Multimodal Embeddings Via Early Fusion Of Discrete Tokens'
authors: Christian Schlarmann, Francesco Croce, Nicolas Flammarion, Matthias Hein
conference: Arxiv
year: 2025
bibkey: schlarmann2025fuselip
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2506.03096'}]
tags: [Evaluation, Few-shot & Zero-shot, Datasets]
short_authors: Schlarmann et al.
---
Contrastive language-image pre-training aligns the features of text-image pairs in a common latent space via distinct encoders for each modality. While this approach achieves impressive performance in several zero-shot tasks, it cannot natively handle multimodal inputs, i.e., encoding image and text into a single feature vector. As a remedy, it is common practice to use additional modules to merge the features extracted by the unimodal encoders. In this work, we present FuseLIP, an alternative architecture for multimodal embedding. Leveraging recent progress in discrete image tokenizers, we propose to use a single transformer model which operates on an extended vocabulary of text and image tokens. This early fusion approach allows the different modalities to interact at each depth of encoding and obtain richer representations compared to common late fusion. We collect new datasets for multimodal pre-training and evaluation, designing challenging tasks for multimodal encoder models. We show that FuseLIP outperforms other approaches in multimodal embedding tasks such as VQA and text-guided image transformation retrieval, while being comparable to baselines on unimodal tasks.