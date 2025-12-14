---
layout: publication
title: Retrieval-enhanced Visual Prompt Learning For Few-shot Classification
authors: Jintao Rong, Hao Chen, Linlin Ou, Tianxiao Chen, Xinyi Yu, Yifan Liu
conference: Arxiv
year: 2023
bibkey: rong2023retrieval
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2306.02243'}]
tags: [Evaluation, Few-shot & Zero-shot, Datasets]
short_authors: Rong et al.
---
The Contrastive Language-Image Pretraining (CLIP) model has been widely used
in various downstream vision tasks. The few-shot learning paradigm has been
widely adopted to augment its capacity for these tasks. However, current
paradigms may struggle with fine-grained classification, such as satellite
image recognition, due to widening domain gaps. To address this limitation, we
propose retrieval-enhanced visual prompt learning (RePrompt), which introduces
retrieval mechanisms to cache and reuse the knowledge of downstream tasks.
RePrompt constructs a retrieval database from either training examples or
external data if available, and uses a retrieval mechanism to enhance multiple
stages of a simple prompt learning baseline, thus narrowing the domain gap.
During inference, our enhanced model can reference similar samples brought by
retrieval to make more accurate predictions. A detailed analysis reveals that
retrieval helps to improve the distribution of late features, thus, improving
generalization for downstream tasks. Reprompt attains state-of-the-art
performance on a wide range of vision datasets, including 11 image datasets, 3
video datasets, 1 multi-view dataset, and 4 domain generalization benchmarks.