---
layout: publication
title: Multi-modal Generative Embedding Model
authors: Feipeng Ma, Hongwei Xue, Guangting Wang, Yizhou Zhou, Fengyun Rao, Shilin
  Yan, Yueyi Zhang, Siying Wu, Mike Zheng Shou, Xiaoyan Sun
conference: Arxiv
year: 2024
bibkey: ma2024multi
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2405.19333'}]
tags: ["Efficiency", "Few Shot & Zero Shot", "Image Retrieval", "Multimodal Retrieval"]
short_authors: Ma et al.
---
Most multi-modal tasks can be formulated into problems of either generation
or embedding. Existing models usually tackle these two types of problems by
decoupling language modules into a text decoder for generation, and a text
encoder for embedding. To explore the minimalism of multi-modal paradigms, we
attempt to achieve only one model per modality in this work. We propose a
Multi-Modal Generative Embedding Model (MM-GEM), whereby the generative and
embedding objectives are encapsulated in one Large Language Model. We also
propose a PoolAggregator to boost efficiency and enable the ability of
fine-grained embedding and generation. A surprising finding is that these two
objectives do not significantly conflict with each other. For example, MM-GEM
instantiated from ViT-Large and TinyLlama shows competitive performance on
benchmarks for multimodal embedding models such as cross-modal retrieval and
zero-shot classification, while has good ability of image captioning.
Additionally, MM-GEM can seamlessly execute region-level image caption
generation and retrieval tasks. Besides, the advanced text model in MM-GEM
brings over 5% improvement in Recall@1 for long text and image retrieval.