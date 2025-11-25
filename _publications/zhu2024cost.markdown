---
layout: publication
title: 'Cost: Contrastive Quantization Based Semantic Tokenization For Generative
  Recommendation'
authors: Jieming Zhu, Mengqun Jin, Qijiong Liu, Zexuan Qiu, Zhenhua Dong, Xiu Li
conference: 18th ACM Conference on Recommender Systems
year: 2024
bibkey: zhu2024cost
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2404.14774'}]
tags: ["Quantization", "Recommender Systems"]
short_authors: Zhu et al.
---
Embedding-based retrieval serves as a dominant approach to candidate item
matching for industrial recommender systems. With the success of generative AI,
generative retrieval has recently emerged as a new retrieval paradigm for
recommendation, which casts item retrieval as a generation problem. Its model
consists of two stages: semantic tokenization and autoregressive generation.
The first stage involves item tokenization that constructs discrete semantic
tokens to index items, while the second stage autoregressively generates
semantic tokens of candidate items. Therefore, semantic tokenization serves as
a crucial preliminary step for training generative recommendation models.
Existing research usually employs a vector quantizier with reconstruction loss
(e.g., RQ-VAE) to obtain semantic tokens of items, but this method fails to
capture the essential neighborhood relationships that are vital for effective
item modeling in recommender systems. In this paper, we propose a contrastive
quantization-based semantic tokenization approach, named CoST, which harnesses
both item relationships and semantic information to learn semantic tokens. Our
experimental results highlight the significant impact of semantic tokenization
on generative recommendation performance, with CoST achieving up to a 43%
improvement in Recall@5 and 44% improvement in NDCG@5 on the MIND dataset over
previous baselines.