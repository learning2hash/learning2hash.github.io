---
layout: publication
title: 'Mgte: Generalized Long-context Text Representation And Reranking Models For
  Multilingual Text Retrieval'
authors: Xin Zhang, Yanzhao Zhang, Dingkun Long, Wen Xie, Ziqi Dai, Jialong Tang,
  Huan Lin, Baosong Yang, Pengjun Xie, Fei Huang, Meishan Zhang, Wenjie Li, Min Zhang
conference: 'Proceedings of the 2024 Conference on Empirical Methods in Natural Language
  Processing: Industry Track'
year: 2024
bibkey: zhang2024mgte
citations: 43
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2407.19669'}]
tags: ["EMNLP", "Efficiency", "Re-Ranking", "Self-Supervised", "Text Retrieval"]
short_authors: Zhang et al.
---
We present systematic efforts in building long-context multilingual text
representation model (TRM) and reranker from scratch for text retrieval. We
first introduce a text encoder (base size) enhanced with RoPE and unpadding,
pre-trained in a native 8192-token context (longer than 512 of previous
multilingual encoders). Then we construct a hybrid TRM and a cross-encoder
reranker by contrastive learning. Evaluations show that our text encoder
outperforms the same-sized previous state-of-the-art XLM-R. Meanwhile, our TRM
and reranker match the performance of large-sized state-of-the-art BGE-M3
models and achieve better results on long-context retrieval benchmarks. Further
analysis demonstrate that our proposed models exhibit higher efficiency during
both training and inference. We believe their efficiency and effectiveness
could benefit various researches and industrial applications.