---
layout: publication
title: Model-enhanced Vector Index
authors: Hailin Zhang, Yujing Wang, Qi Chen, Ruiheng Chang, Ting Zhang, Ziming Miao,
  Yingyan Hou, Yang Ding, Xupeng Miao, Haonan Wang, Bochen Pang, Yuefeng Zhan, Hao
  Sun, Weiwei Deng, Qi Zhang, Fan Yang, Xing Xie, Mao Yang, Bin Cui
conference: Arxiv
year: 2023
bibkey: zhang2023model
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2309.13335'}]
tags: ["Efficiency", "Evaluation", "Quantization", "Text Retrieval", "Vector Indexing"]
short_authors: Zhang et al.
---
Embedding-based retrieval methods construct vector indices to search for
document representations that are most similar to the query representations.
They are widely used in document retrieval due to low latency and decent recall
performance. Recent research indicates that deep retrieval solutions offer
better model quality, but are hindered by unacceptable serving latency and the
inability to support document updates. In this paper, we aim to enhance the
vector index with end-to-end deep generative models, leveraging the
differentiable advantages of deep retrieval models while maintaining desirable
serving efficiency. We propose Model-enhanced Vector Index (MEVI), a
differentiable model-enhanced index empowered by a twin-tower representation
model. MEVI leverages a Residual Quantization (RQ) codebook to bridge the
sequence-to-sequence deep retrieval and embedding-based models. To
substantially reduce the inference time, instead of decoding the unique
document ids in long sequential steps, we first generate some semantic virtual
cluster ids of candidate documents in a small number of steps, and then
leverage the well-adapted embedding vectors to further perform a fine-grained
search for the relevant documents in the candidate virtual clusters. We
empirically show that our model achieves better performance on the commonly
used academic benchmarks MSMARCO Passage and Natural Questions, with comparable
serving latency to dense retrieval solutions.