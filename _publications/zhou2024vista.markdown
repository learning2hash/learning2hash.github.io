---
layout: publication
title: 'VISTA: Visualized Text Embedding For Universal Multi-modal Retrieval'
authors: Zhou Junjie, Liu Zheng, Xiao Shitao, Zhao Bo, Xiong Yongping
conference: 'Proceedings of the 62nd Annual Meeting of the Association for Computational
  Linguistics (Volume 1: Long Papers)'
year: 2024
bibkey: zhou2024vista
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2406.04292'}]
tags: ["Image Retrieval", "Multimodal Retrieval", "Similarity Search", "Supervised", "Text Retrieval"]
short_authors: Zhou et al.
---
Multi-modal retrieval becomes increasingly popular in practice. However, the
existing retrievers are mostly text-oriented, which lack the capability to
process visual information. Despite the presence of vision-language models like
CLIP, the current methods are severely limited in representing the text-only
and image-only data. In this work, we present a new embedding model VISTA for
universal multi-modal retrieval. Our work brings forth threefold technical
contributions. Firstly, we introduce a flexible architecture which extends a
powerful text encoder with the image understanding capability by introducing
visual token embeddings. Secondly, we develop two data generation strategies,
which bring high-quality composed image-text to facilitate the training of the
embedding model. Thirdly, we introduce a multi-stage training algorithm, which
first aligns the visual token embedding with the text encoder using massive
weakly labeled data, and then develops multi-modal representation capability
using the generated composed image-text data. In our experiments, VISTA
achieves superior performances across a variety of multi-modal retrieval tasks
in both zero-shot and supervised settings. Our model, data, and source code are
available at https://github.com/FlagOpen/FlagEmbedding.