---
layout: publication
title: 'LDIR: Low-dimensional Dense And Interpretable Text Embeddings With Relative
  Representations'
authors: Yile Wang, Zhanyu Shen, Hui Huang
conference: 'Findings of the Association for Computational Linguistics: ACL 2025'
year: 2025
bibkey: wang2025ldir
citations: 0
additional_links: [{name: Code, url: 'https://github.com/szu-tera/LDIR'}, {name: Paper,
    url: 'https://arxiv.org/abs/2505.10354'}]
tags: [Evaluation, Similarity Search, ACL]
short_authors: Yile Wang, Zhanyu Shen, Hui Huang
---
Semantic text representation is a fundamental task in the field of natural language processing. Existing text embedding (e.g., SimCSE and LLM2Vec) have demonstrated excellent performance, but the values of each dimension are difficult to trace and interpret. Bag-of-words, as classic sparse interpretable embeddings, suffers from poor performance. Recently, Benara et al. (2024) propose interpretable text embeddings using large language models, which forms "0/1" embeddings based on responses to a series of questions. These interpretable text embeddings are typically high-dimensional (larger than 10,000). In this work, we propose Low-dimensional (lower than 500) Dense and Interpretable text embeddings with Relative representations (LDIR). The numerical values of its dimensions indicate semantic relatedness to different anchor texts through farthest point sampling, offering both semantic representation as well as a certain level of traceability and interpretability. We validate LDIR on multiple semantic textual similarity, retrieval, and clustering tasks. Extensive experimental results show that LDIR performs close to the black-box baseline models and outperforms the interpretable embeddings baselines with much fewer dimensions. Code is available at https://github.com/szu-tera/LDIR.