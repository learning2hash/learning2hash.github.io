---
layout: publication
title: 'Universal Vision-language Dense Retrieval: Learning A Unified Representation
  Space For Multi-modal Retrieval'
authors: Zhenghao Liu, Chenyan Xiong, Yuanhuiyi Lv, Zhiyuan Liu, Ge Yu
conference: Arxiv
year: 2022
bibkey: liu2022universal
citations: 6
additional_links: [{name: Code, url: 'https://github.com/OpenMatch/UniVL-DR'}, {name: Paper,
    url: 'https://arxiv.org/abs/2209.00179'}]
tags: ["Evaluation", "Image Retrieval", "Multimodal Retrieval", "Text Retrieval"]
short_authors: Liu et al.
---
This paper presents Universal Vision-Language Dense Retrieval (UniVL-DR),
which builds a unified model for multi-modal retrieval. UniVL-DR encodes
queries and multi-modality resources in an embedding space for searching
candidates from different modalities. To learn a unified embedding space for
multi-modal retrieval, UniVL-DR proposes two techniques: 1) Universal embedding
optimization strategy, which contrastively optimizes the embedding space using
the modality-balanced hard negatives; 2) Image verbalization method, which
bridges the modality gap between images and texts in the raw data space.
UniVL-DR achieves the state-of-the-art on the multi-modal open-domain question
answering benchmark, WebQA, and outperforms all retrieval models on the two
subtasks, text-text retrieval and text-image retrieval. It demonstrates that
universal multi-modal search is feasible to replace the divide-and-conquer
pipeline with a united model and also benefits single/cross modality tasks. All
source codes of this work are available at
https://github.com/OpenMatch/UniVL-DR.