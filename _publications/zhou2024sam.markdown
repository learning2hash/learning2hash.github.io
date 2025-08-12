---
layout: publication
title: 'SAM-IF: Leveraging SAM For Incremental Few-shot Instance Segmentation'
authors: Xudong Zhou, Wenhao He
conference: Arxiv
year: 2024
bibkey: zhou2024sam
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.11034'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Xudong Zhou, Wenhao He
---
We propose SAM-IF, a novel method for incremental few-shot instance
segmentation leveraging the Segment Anything Model (SAM). SAM-IF addresses the
challenges of class-agnostic instance segmentation by introducing a multi-class
classifier and fine-tuning SAM to focus on specific target objects. To enhance
few-shot learning capabilities, SAM-IF employs a cosine-similarity-based
classifier, enabling efficient adaptation to novel classes with minimal data.
Additionally, SAM-IF supports incremental learning by updating classifier
weights without retraining the decoder. Our method achieves competitive but
more reasonable results compared to existing approaches, particularly in
scenarios requiring specific object segmentation with limited labeled data.