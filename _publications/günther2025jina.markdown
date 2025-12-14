---
layout: publication
title: 'Jina-embeddings-v4: Universal Embeddings For Multimodal Multilingual Retrieval'
authors: "Michael G\xFCnther, Saba Sturua, Mohammad Kalim Akram, Isabelle Mohr, Andrei\
  \ Ungureanu, Bo Wang, Sedigheh Eslami, Scott Martens, Maximilian Werk, Nan Wang,\
  \ Han Xiao"
conference: Proceedings of the 5th Workshop on Multilingual Representation Learning
  (MRL 2025)
year: 2025
bibkey: "g\xFCnther2025jina"
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2506.18902'}]
tags: [Text Retrieval, Evaluation, Image Retrieval, Multimodal Retrieval]
short_authors: "G\xFCnther et al."
---
We introduce jina-embeddings-v4, a 3.8 billion parameter multimodal embedding model that unifies text and image representations through a novel architecture supporting both single-vector and multi-vector embeddings in the late interaction style. The model incorporates task-specific Low-Rank Adaptation (LoRA) adapters to optimize performance across diverse retrieval scenarios, including query-document retrieval, semantic text similarity, and code search. Comprehensive evaluations demonstrate that jina-embeddings-v4 achieves state-of-the-art performance on both single-modal and cross-modal retrieval tasks, with particular strength in processing visually rich content such as tables, charts, diagrams, and mixed-media formats. To facilitate evaluation of this capability, we also introduce Jina-VDR, a novel benchmark specifically designed for visually rich image retrieval.