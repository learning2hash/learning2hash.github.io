---
layout: publication
title: Multi-view Document Representation Learning For Open-domain Dense Retrieval
authors: Zhang Shunyu, Liang Yaobo, Gong Ming, Jiang Daxin, Duan Nan
conference: IEEE Transactions on Multimedia
year: 2022
bibkey: zhang2022multi
citations: 38
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2203.08372'}]
tags: ["Large-Scale Search", "Neural Hashing", "Scalability", "Similarity Search", "Text Retrieval"]
short_authors: Zhang et al.
---
Dense retrieval has achieved impressive advances in first-stage retrieval
from a large-scale document collection, which is built on bi-encoder
architecture to produce single vector representation of query and document.
However, a document can usually answer multiple potential queries from
different views. So the single vector representation of a document is hard to
match with multi-view queries, and faces a semantic mismatch problem. This
paper proposes a multi-view document representation learning framework, aiming
to produce multi-view embeddings to represent documents and enforce them to
align with different queries. First, we propose a simple yet effective method
of generating multiple embeddings through viewers. Second, to prevent
multi-view embeddings from collapsing to the same one, we further propose a
global-local loss with annealed temperature to encourage the multiple viewers
to better align with different potential queries. Experiments show our method
outperforms recent works and achieves state-of-the-art results.