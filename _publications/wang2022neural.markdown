---
layout: publication
title: A Neural Corpus Indexer For Document Retrieval
authors: Yujing Wang, Yingyan Hou, Haonan Wang, Ziming Miao, Shibin Wu, Hao Sun, Qi
  Chen, Yuqing Xia, Chengmin Chi, Guoshuai Zhao, Zheng Liu, Xing Xie, Hao Allen Sun,
  Weiwei Deng, Qi Zhang, Mao Yang
conference: Arxiv
year: 2022
bibkey: wang2022neural
citations: 46
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2206.02743'}]
tags: [Evaluation, Datasets, Text Retrieval]
short_authors: Wang et al.
---
Current state-of-the-art document retrieval solutions mainly follow an
index-retrieve paradigm, where the index is hard to be directly optimized for
the final retrieval target. In this paper, we aim to show that an end-to-end
deep neural network unifying training and indexing stages can significantly
improve the recall performance of traditional methods. To this end, we propose
Neural Corpus Indexer (NCI), a sequence-to-sequence network that generates
relevant document identifiers directly for a designated query. To optimize the
recall performance of NCI, we invent a prefix-aware weight-adaptive decoder
architecture, and leverage tailored techniques including query generation,
semantic document identifiers, and consistency-based regularization. Empirical
studies demonstrated the superiority of NCI on two commonly used academic
benchmarks, achieving +21.4% and +16.8% relative enhancement for Recall@1 on
NQ320k dataset and R-Precision on TriviaQA dataset, respectively, compared to
the best baseline method.