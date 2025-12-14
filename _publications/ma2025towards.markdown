---
layout: publication
title: 'Towards Storage-efficient Visual Document Retrieval: An Empirical Study On
  Reducing Patch-level Embeddings'
authors: Yubo Ma, Jinsong Li, Yuhang Zang, Xiaobao Wu, Xiaoyi Dong, Pan Zhang, Yuhang
  Cao, Haodong Duan, Jiaqi Wang, Yixin Cao, Aixin Sun
conference: 'Findings of the Association for Computational Linguistics: ACL 2025'
year: 2025
bibkey: ma2025towards
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2506.04997'}]
tags: [Text Retrieval, Evaluation, Memory Efficiency, ACL]
short_authors: Ma et al.
---
Despite the strong performance of ColPali/ColQwen2 in Visualized Document Retrieval (VDR), it encodes each page into multiple patch-level embeddings and leads to excessive memory usage. This empirical study investigates methods to reduce patch embeddings per page at minimum performance degradation. We evaluate two token-reduction strategies: token pruning and token merging. Regarding token pruning, we surprisingly observe that a simple random strategy outperforms other sophisticated pruning methods, though still far from satisfactory. Further analysis reveals that pruning is inherently unsuitable for VDR as it requires removing certain page embeddings without query-specific information. Turning to token merging (more suitable for VDR), we search for the optimal combinations of merging strategy across three dimensions and develop Light-ColPali/ColQwen2. It maintains 98.2% of retrieval performance with only 11.8% of original memory usage, and preserves 94.6% effectiveness at 2.8% memory footprint. We expect our empirical findings and resulting Light-ColPali/ColQwen2 offer valuable insights and establish a competitive baseline for future research towards efficient VDR.