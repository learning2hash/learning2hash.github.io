---
layout: publication
title: 'Vlmo: Unified Vision-language Pre-training With Mixture-of-modality-experts'
authors: Hangbo Bao, Wenhui Wang, Li Dong, Qiang Liu, Owais Khan Mohammed, Kriti Aggarwal,
  Subhojit Som, Furu Wei
conference: Arxiv
year: 2021
bibkey: bao2021vlmo
citations: 288
additional_links: [{name: Code, url: 'https://aka.ms/vlmo'}, {name: Paper, url: 'https://arxiv.org/abs/2111.02358'}]
tags: ["Image Retrieval", "Multimodal Retrieval", "Scalability"]
short_authors: Bao et al.
---
We present a unified Vision-Language pretrained Model (VLMo) that jointly
learns a dual encoder and a fusion encoder with a modular Transformer network.
Specifically, we introduce Mixture-of-Modality-Experts (MoME) Transformer,
where each block contains a pool of modality-specific experts and a shared
self-attention layer. Because of the modeling flexibility of MoME, pretrained
VLMo can be fine-tuned as a fusion encoder for vision-language classification
tasks, or used as a dual encoder for efficient image-text retrieval. Moreover,
we propose a stagewise pre-training strategy, which effectively leverages
large-scale image-only and text-only data besides image-text pairs.
Experimental results show that VLMo achieves state-of-the-art results on
various vision-language tasks, including VQA, NLVR2 and image-text retrieval.
The code and pretrained models are available at https://aka.ms/vlmo.