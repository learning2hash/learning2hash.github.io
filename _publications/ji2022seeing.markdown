---
layout: publication
title: 'Seeing What You Miss: Vision-language Pre-training With Semantic Completion
  Learning'
authors: Yatai Ji, Rongcheng Tu, Jie Jiang, Weijie Kong, Chengfei Cai, Wenzhe Zhao,
  Hongfa Wang, Yujiu Yang, Wei Liu
conference: Arxiv
year: 2022
bibkey: ji2022seeing
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2211.13437'}]
tags: ["Multimodal Retrieval"]
short_authors: Ji et al.
---
Cross-modal alignment is essential for vision-language pre-training (VLP)
models to learn the correct corresponding information across different
modalities. For this purpose, inspired by the success of masked language
modeling (MLM) tasks in the NLP pre-training area, numerous masked modeling
tasks have been proposed for VLP to further promote cross-modal interactions.
The core idea of previous masked modeling tasks is to focus on reconstructing
the masked tokens based on visible context for learning local-to-local
alignment. However, most of them pay little attention to the global semantic
features generated for the masked data, resulting in a limited cross-modal
alignment ability of global representations. Therefore, in this paper, we
propose a novel Semantic Completion Learning (SCL) task, complementary to
existing masked modeling tasks, to facilitate global-to-local alignment.
Specifically, the SCL task complements the missing semantics of masked data by
capturing the corresponding information from the other modality, promoting
learning more representative global features which have a great impact on the
performance of downstream tasks. Moreover, we present a flexible vision
encoder, which enables our model to perform image-text and video-text
multimodal tasks simultaneously. Experimental results show that our proposed
method obtains state-of-the-art performance on various vision-language
benchmarks, such as visual question answering, image-text retrieval, and
video-text retrieval.