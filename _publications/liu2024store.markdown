---
layout: publication
title: 'STORE: Streamlining Semantic Tokenization And Generative Recommendation With
  A Single LLM'
authors: Qijiong Liu, Jieming Zhu, Lu Fan, Zhou Zhao, Xiao-Ming Wu
conference: Arxiv
year: 2024
bibkey: liu2024store
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2409.07276'}]
tags: ["Recommender Systems"]
short_authors: Liu et al.
---
Traditional recommendation models often rely on unique item identifiers (IDs)
to distinguish between items, which can hinder their ability to effectively
leverage item content information and generalize to long-tail or cold-start
items. Recently, semantic tokenization has been proposed as a promising
solution that aims to tokenize each item's semantic representation into a
sequence of discrete tokens. In this way, it preserves the item's semantics
within these tokens and ensures that semantically similar items are represented
by similar tokens. These semantic tokens have become fundamental in training
generative recommendation models. However, existing generative recommendation
methods typically involve multiple sub-models for embedding, quantization, and
recommendation, leading to an overly complex system. In this paper, we propose
to streamline the semantic tokenization and generative recommendation process
with a unified framework, dubbed STORE, which leverages a single large language
model (LLM) for both tasks. Specifically, we formulate semantic tokenization as
a text-to-token task and generative recommendation as a token-to-token task,
supplemented by a token-to-text reconstruction task and a text-to-token
auxiliary task. All these tasks are framed in a generative manner and trained
using a single LLM backbone. Extensive experiments have been conducted to
validate the effectiveness of our STORE framework across various recommendation
tasks and datasets. We will release the source code and configurations for
reproducible research.