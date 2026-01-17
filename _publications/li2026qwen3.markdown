---
layout: publication
title: 'Qwen3-vl-embedding And Qwen3-vl-reranker: A Unified Framework For State-of-the-art
  Multimodal Retrieval And Ranking'
authors: Mingxin Li, Yanzhao Zhang, Dingkun Long, Keqin Chen, Sibo Song, Shuai Bai,
  Zhibo Yang, Pengjun Xie, An Yang, Dayiheng Liu, Jingren Zhou, Junyang Lin
conference: Arxiv
year: 2026
bibkey: li2026qwen3
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2601.04720'}]
tags: ["Evaluation", "Hybrid ANN Methods", "Multimodal Retrieval", "Re-Ranking", "Text Retrieval"]
short_authors: Li et al.
---
In this report, we introduce the Qwen3-VL-Embedding and Qwen3-VL-Reranker model series, the latest extensions of the Qwen family built on the Qwen3-VL foundation model. Together, they provide an end-to-end pipeline for high-precision multimodal search by mapping diverse modalities, including text, images, document images, and video, into a unified representation space. The Qwen3-VL-Embedding model employs a multi-stage training paradigm, progressing from large-scale contrastive pre-training to reranking model distillation, to generate semantically rich high-dimensional vectors. It supports Matryoshka Representation Learning, enabling flexible embedding dimensions, and handles inputs up to 32k tokens. Complementing this, Qwen3-VL-Reranker performs fine-grained relevance estimation for query-document pairs using a cross-encoder architecture with cross-attention mechanisms. Both model series inherit the multilingual capabilities of Qwen3-VL, supporting more than 30 languages, and are released in \(\textbf\{2B\}\) and \(\textbf\{8B\}\) parameter sizes to accommodate diverse deployment requirements. Empirical evaluations demonstrate that the Qwen3-VL-Embedding series achieves state-of-the-art results across diverse multimodal embedding evaluation benchmarks. Specifically, Qwen3-VL-Embedding-8B attains an overall score of \(\textbf\{77.8\}\) on MMEB-V2, ranking first among all models (as of January 8, 2025). This report presents the architecture, training methodology, and practical capabilities of the series, demonstrating their effectiveness on various multimodal retrieval tasks, including image-text retrieval, visual question answering, and video-text matching.