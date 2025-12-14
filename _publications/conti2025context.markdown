---
layout: publication
title: 'Context Is Gold To Find The Gold Passage: Evaluating And Training Contextual
  Document Embeddings'
authors: "Max Conti, Manuel Faysse, Gautier Viaud, Antoine Bosselut, C\xE9line Hudelot,\
  \ Pierre Colombo"
conference: Proceedings of the 2025 Conference on Empirical Methods in Natural Language
  Processing
year: 2025
bibkey: conti2025context
citations: 0
additional_links: [{name: Code, url: 'https://github.com/illuin-tech/contextual-embeddings'},
  {name: Paper, url: 'https://arxiv.org/abs/2505.24782'}]
tags: [EMNLP, Evaluation, Efficiency, Text Retrieval]
short_authors: Conti et al.
---
A limitation of modern document retrieval embedding methods is that they typically encode passages (chunks) from the same documents independently, often overlooking crucial contextual information from the rest of the document that could greatly improve individual chunk representations.
  In this work, we introduce ConTEB (Context-aware Text Embedding Benchmark), a benchmark designed to evaluate retrieval models on their ability to leverage document-wide context. Our results show that state-of-the-art embedding models struggle in retrieval scenarios where context is required. To address this limitation, we propose InSeNT (In-sequence Negative Training), a novel contrastive post-training approach which combined with late chunking pooling enhances contextual representation learning while preserving computational efficiency. Our method significantly improves retrieval quality on ConTEB without sacrificing base model performance. We further find chunks embedded with our method are more robust to suboptimal chunking strategies and larger retrieval corpus sizes. We open-source all artifacts at https://github.com/illuin-tech/contextual-embeddings.