---
layout: publication
title: 'CITADEL: Conditional Token Interaction Via Dynamic Lexical Routing For Efficient
  And Effective Multi-vector Retrieval'
authors: Li et al.
conference: 'Proceedings of the 61st Annual Meeting of the Association for Computational
  Linguistics (Volume 1: Long Papers)'
year: 2023
bibkey: li2023citadel
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2211.10411'}]
tags: [ACL]
---
Multi-vector retrieval methods combine the merits of sparse (e.g. BM25) and
dense (e.g. DPR) retrievers and have achieved state-of-the-art performance on
various retrieval tasks. These methods, however, are orders of magnitude slower
and need much more space to store their indices compared to their single-vector
counterparts. In this paper, we unify different multi-vector retrieval models
from a token routing viewpoint and propose conditional token interaction via
dynamic lexical routing, namely CITADEL, for efficient and effective
multi-vector retrieval. CITADEL learns to route different token vectors to the
predicted lexical ``keys'' such that a query token vector only interacts with
document token vectors routed to the same key. This design significantly
reduces the computation cost while maintaining high accuracy. Notably, CITADEL
achieves the same or slightly better performance than the previous state of the
art, ColBERT-v2, on both in-domain (MS MARCO) and out-of-domain (BEIR)
evaluations, while being nearly 40 times faster. Code and data are available at
https://github.com/facebookresearch/dpr-scale.