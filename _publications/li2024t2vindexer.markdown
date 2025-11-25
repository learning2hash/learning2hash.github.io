---
layout: publication
title: 'T2vindexer: A Generative Video Indexer For Efficient Text-video Retrieval'
authors: Yili Li, Jing Yu, Keke Gai, Bang Liu, Gang Xiong, Qi Wu
conference: Proceedings of the 32nd ACM International Conference on Multimedia
year: 2024
bibkey: li2024t2vindexer
citations: 3
additional_links: [{name: Code, url: 'https://github.com/Lilidamowang/T2VIndexer-generativeSearch'},
  {name: Paper, url: 'https://arxiv.org/abs/2408.11432'}]
tags: ["Efficiency", "Multimodal Retrieval", "Video Retrieval"]
short_authors: Li et al.
---
Current text-video retrieval methods mainly rely on cross-modal matching
between queries and videos to calculate their similarity scores, which are then
sorted to obtain retrieval results. This method considers the matching between
each candidate video and the query, but it incurs a significant time cost and
will increase notably with the increase of candidates. Generative models are
common in natural language processing and computer vision, and have been
successfully applied in document retrieval, but their application in multimodal
retrieval remains unexplored. To enhance retrieval efficiency, in this paper,
we introduce a model-based video indexer named T2VIndexer, which is a
sequence-to-sequence generative model directly generating video identifiers and
retrieving candidate videos with constant time complexity. T2VIndexer aims to
reduce retrieval time while maintaining high accuracy. To achieve this goal, we
propose video identifier encoding and query-identifier augmentation approaches
to represent videos as short sequences while preserving their semantic
information. Our method consistently enhances the retrieval efficiency of
current state-of-the-art models on four standard datasets. It enables baselines
with only 30%-50% of the original retrieval time to achieve better retrieval
performance on MSR-VTT (+1.0%), MSVD (+1.8%), ActivityNet (+1.5%), and DiDeMo
(+0.2%). The code is available at
https://github.com/Lilidamowang/T2VIndexer-generativeSearch.