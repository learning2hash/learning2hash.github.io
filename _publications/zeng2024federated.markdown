---
layout: publication
title: Federated Recommendation Via Hybrid Retrieval Augmented Generation
authors: Huimin Zeng, Zhenrui Yue, Qian Jiang, Dong Wang
conference: "Arxiv"
year: 2024
bibkey: zeng2024federated
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2403.04256v1"}
tags: ['ARXIV']
---
Federated Recommendation (FR) emerges as a novel paradigm that enables privacy-preserving recommendations. However traditional FR systems usually represent users/items with discrete identities (IDs) suffering from performance degradation due to the data sparsity and heterogeneity in FR. On the other hand Large Language Models (LLMs) as recommenders have proven effective across various recommendation scenarios. Yet LLM-based recommenders encounter challenges such as low inference efficiency and potential hallucination compromising their performance in real-world scenarios. To this end we propose GPT-FedRec a federated recommendation framework leveraging ChatGPT and a novel hybrid Retrieval Augmented Generation (RAG) mechanism. GPT-FedRec is a two-stage solution. The first stage is a hybrid retrieval process mining ID-based user patterns and text-based item features. Next the retrieved results are converted into text prompts and fed into GPT for re-ranking. Our proposed hybrid retrieval mechanism and LLM-based re-rank aims to extract generalized features from data and exploit pretrained knowledge within LLM overcoming data sparsity and heterogeneity in FR. In addition the RAG approach also prevents LLM hallucination improving the recommendation performance for real-world users. Experimental results on diverse benchmark datasets demonstrate the superior performance of GPT-FedRec against state-of-the-art baseline methods.
