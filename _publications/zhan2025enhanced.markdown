---
layout: publication
title: 'ELIP: Enhanced Visual-language Foundation Models For Image Retrieval'
authors: Guanqi Zhan, Yuanpei Liu, Kai Han, Weidi Xie, Andrew Zisserman
conference: "Arxiv"
year: 2025
citations: 0
bibkey: zhan2025enhanced
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2502.15682'}
tags: ['Benchmarks and Datasets', 'Tools and Libraries', 'Evaluation Metrics', 'Applications']
---
The objective in this paper is to improve the performance of text-to-image
retrieval. To this end, we introduce a new framework that can boost the
performance of large-scale pre-trained vision-language models, so that they can
be used for text-to-image re-ranking. The approach, Enhanced Language-Image
Pre-training (ELIP), uses the text query, via a simple MLP mapping network, to
predict a set of visual prompts to condition the ViT image encoding. ELIP can
easily be applied to the commonly used CLIP, SigLIP and BLIP-2 networks. To
train the architecture with limited computing resources, we develop a 'student
friendly' best practice, involving global hard sample mining, and curation of a
large-scale dataset. On the evaluation side, we set up two new
out-of-distribution (OOD) benchmarks, Occluded COCO and ImageNet-R, to assess
the zero-shot generalisation of the models to different domains. The results
demonstrate that ELIP significantly boosts CLIP/SigLIP/SigLIP-2 text-to-image
retrieval performance and outperforms BLIP-2 on several benchmarks, as well as
providing an easy means to adapt to OOD datasets.
