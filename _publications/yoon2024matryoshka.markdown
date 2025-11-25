---
layout: publication
title: 'Matryoshka-adaptor: Unsupervised And Supervised Tuning For Smaller Embedding
  Dimensions'
authors: Jinsung Yoon, Raj Sinha, Sercan O Arik, Tomas Pfister
conference: Proceedings of the 2024 Conference on Empirical Methods in Natural Language
  Processing
year: 2024
bibkey: yoon2024matryoshka
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2407.20243'}]
tags: ["Datasets", "EMNLP", "Efficiency", "Supervised", "Unsupervised"]
short_authors: Yoon et al.
---
Embeddings from Large Language Models (LLMs) have emerged as critical
components in various applications, particularly for information retrieval.
While high-dimensional embeddings generally demonstrate superior performance as
they contain more salient information, their practical application is
frequently hindered by elevated computational latency and the associated higher
cost. To address these challenges, we propose Matryoshka-Adaptor, a novel
tuning framework designed for the customization of LLM embeddings.
Matryoshka-Adaptor facilitates substantial dimensionality reduction while
maintaining comparable performance levels, thereby achieving a significant
enhancement in computational efficiency and cost-effectiveness. Our framework
directly modifies the embeddings from pre-trained LLMs which is designed to be
seamlessly integrated with any LLM architecture, encompassing those accessible
exclusively through black-box APIs. Also, it exhibits efficacy in both
unsupervised and supervised learning settings. A rigorous evaluation conducted
across a diverse corpus of English, multilingual, and multimodal datasets
consistently reveals substantial gains with Matryoshka-Adaptor. Notably, with
Google and OpenAI Embedding APIs, Matryoshka-Adaptor achieves a reduction in
dimensionality ranging from two- to twelve-fold without compromising
performance across multiple BEIR datasets.