---
layout: publication
title: "Binary Embedding-based Retrieval at Tencent"
authors: Gan Yukang, Ge Yixiao, Zhou Chang, Su Shupeng, Xu Zhouchuan, Xu Xuyuan, Hui Quanchao, Chen Xiang, Wang Yexin, Shan Ying
conference: "Arxiv"
year: 2023
bibkey: gan2023binary
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2302.08714"}
tags: ['ARXIV', 'TIP', 'TOM']
---
Large-scale embedding-based retrieval (EBR) is the cornerstone of search-related
industrial applications. Given a user query, the system of EBR aims to identify
relevant information from a large corpus of documents that may be tens or
hundreds of billions in size. The storage and computation turn out to be
expensive and inefficient with massive documents and high concurrent queries,
making it difficult to further scale up. To tackle the challenge, we propose a
binary embedding-based retrieval (BEBR) engine equipped with a recurrent
binarization algorithm that enables customized bits per dimension. Specifically,
we compress the full-precision query and document embeddings, formulated as
float vectors in general, into a composition of multiple binary vectors using a
lightweight transformation model with residual multilayer perception (MLP)
blocks. We can therefore tailor the number of bits for different applications to
trade off accuracy loss and cost savings. Importantly, we enable task-agnostic
efficient training of the binarization model using a new embedding-to-embedding
strategy. We also exploit the compatible training of binary embeddings so that
the BEBR engine can support indexing among multiple embedding versions within a
unified system. To further realize efficient search, we propose Symmetric
Distance Calculation (SDC) to achieve lower response time than Hamming codes. We
successfully employed the introduced BEBR to Tencent products, including Sogou,
Tencent Video, QQ World, etc. The binarization algorithm can be seamlessly
generalized to various tasks with multiple modalities. Extensive experiments on
offline benchmarks and online A/B tests demonstrate the efficiency and
effectiveness of our method, significantly saving 30%~50% index costs with
almost no loss of accuracy at the system level.
