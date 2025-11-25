---
layout: publication
title: Lstm-based Selective Dense Text Retrieval Guided By Sparse Lexical Retrieval
authors: Yingrui Yang, Parker Carlson, Yifan Qiao, Wentai Xie, Shanxiu He, Tao Yang
conference: Lecture Notes in Computer Science
year: 2025
bibkey: yang2025lstm
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2502.10639'}]
tags: ["Datasets", "Large Scale Search", "Memory Efficiency", "Similarity Search", "Text Retrieval"]
short_authors: Yang et al.
---
This paper studies fast fusion of dense retrieval and sparse lexical
retrieval, and proposes a cluster-based selective dense retrieval method called
CluSD guided by sparse lexical retrieval. CluSD takes a lightweight
cluster-based approach and exploits the overlap of sparse retrieval results and
embedding clusters in a two-stage selection process with an LSTM model to
quickly identify relevant clusters while incurring limited extra memory space
overhead. CluSD triggers partial dense retrieval and performs cluster-based
block disk I/O if needed. This paper evaluates CluSD and compares it with
several baselines for searching in-memory and on-disk MS MARCO and BEIR
datasets.