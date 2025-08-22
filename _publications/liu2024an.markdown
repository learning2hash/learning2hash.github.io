---
layout: publication
title: An Analysis On Matching Mechanisms And Token Pruning For Late-interaction Models
authors: Qi Liu, Gang Guo, Jiaxin Mao, Zhicheng Dou, Ji-Rong Wen, Hao Jiang, Xinyu
  Zhang, Zhao Cao
conference: ACM Transactions on Information Systems
year: 2024
bibkey: liu2024an
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2403.13291'}]
tags: ["Datasets", "Efficiency"]
short_authors: Liu et al.
---
With the development of pre-trained language models, the dense retrieval
models have become promising alternatives to the traditional retrieval models
that rely on exact match and sparse bag-of-words representations. Different
from most dense retrieval models using a bi-encoder to encode each query or
document into a dense vector, the recently proposed late-interaction
multi-vector models (i.e., ColBERT and COIL) achieve state-of-the-art retrieval
effectiveness by using all token embeddings to represent documents and queries
and modeling their relevance with a sum-of-max operation. However, these
fine-grained representations may cause unacceptable storage overhead for
practical search systems. In this study, we systematically analyze the matching
mechanism of these late-interaction models and show that the sum-of-max
operation heavily relies on the co-occurrence signals and some important words
in the document. Based on these findings, we then propose several simple
document pruning methods to reduce the storage overhead and compare the
effectiveness of different pruning methods on different late-interaction
models. We also leverage query pruning methods to further reduce the retrieval
latency. We conduct extensive experiments on both in-domain and out-domain
datasets and show that some of the used pruning methods can significantly
improve the efficiency of these late-interaction models without substantially
hurting their retrieval effectiveness.