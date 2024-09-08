---
layout: publication
title: Composite Correlation Quantization for Efficient Multimodal Retrieval
authors: Long Mingsheng, Cao Yue, Wang Jianmin, Yu Philip S.
conference: Arxiv
year: 2015
bibkey: long2015composite
additional_links:
   - {name: "DOI", url: "10.1145/2911451.2911493"}
   - {name: "License", url: "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/1504.04818"}
tags: ['Arxiv', 'TIP', 'Quantisation', 'Cross-Modal']
---
Efficient similarity retrieval from large-scale multimodal database is pervasive in modern search engines and social networks. To support queries across content modalities, the system should enable cross-modal correlation and computation-efficient indexing. While hashing methods have shown great potential in achieving this goal, current attempts generally fail to learn isomorphic hash codes in a seamless scheme, that is, they embed multiple modalities in a continuous isomorphic space and separately threshold embeddings into binary codes, which incurs substantial loss of retrieval accuracy. In this paper, we approach seamless multimodal hashing by proposing a novel Composite Correlation Quantization (CCQ) model. Specifically, CCQ jointly finds correlation-maximal mappings that transform different modalities into isomorphic latent space, and learns composite quantizers that convert the isomorphic latent features into compact binary codes. An optimization framework is devised to preserve both intra-modal similarity and inter-modal correlation through minimizing both reconstruction and quantization errors, which can be trained from both paired and partially paired data in linear time. A comprehensive set of experiments clearly show the superior effectiveness and efficiency of CCQ against the state of the art hashing methods for both unimodal and cross-modal retrieval.
