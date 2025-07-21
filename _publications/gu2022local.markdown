---
layout: publication
title: Local Citation Recommendation with Hierarchical-Attention Text Encoder and
  SciBERT-based Reranking
authors: Gu Nianlong, Gao Yingqiang, Hahnloser Richard H. R.
conference: Lecture Notes in Computer Science
year: 2022
bibkey: gu2022local
citations: 14
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2112.01206'}]
tags: ["Re Ranking", "Recommender Systems"]
---
The goal of local citation recommendation is to recommend a missing reference
from the local citation context and optionally also from the global context. To
balance the tradeoff between speed and accuracy of citation recommendation in
the context of a large-scale paper database, a viable approach is to first
prefetch a limited number of relevant documents using efficient ranking methods
and then to perform a fine-grained reranking using more sophisticated models.
In that vein, BM25 has been found to be a tough-to-beat approach to
prefetching, which is why recent work has focused mainly on the reranking step.
Even so, we explore prefetching with nearest neighbor search among text
embeddings constructed by a hierarchical attention network. When coupled with a
SciBERT reranker fine-tuned on local citation recommendation tasks, our
hierarchical Attention encoder (HAtten) achieves high prefetch recall for a
given number of candidates to be reranked. Consequently, our reranker requires
fewer prefetch candidates to rerank, yet still achieves state-of-the-art
performance on various local citation recommendation datasets such as ACL-200,
FullTextPeerRead, RefSeer, and arXiv.