---
layout: publication
title: 'Gloss: Generative Language Models With Semantic Search For Sequential Recommendation'
authors: Acharya Krishna, Petrov Aleksandr V., Ziani Juba
conference: Proceedings of the 17th ACM Conference on Recommender Systems
year: 2025
bibkey: acharya2025gloss
citations: 56
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2506.01910'}]
tags: [RecSys, Recommender Systems]
---
We propose Generative Low-rank language model with Semantic Search (GLoSS), a generative recommendation framework that combines large language models with dense retrieval for sequential recommendation. Unlike prior methods such as GPT4Rec, which rely on lexical matching via BM25, GLoSS uses semantic search to retrieve relevant items beyond lexical matching. For query generation, we employ 4-bit quantized LlaMA-3 models fine-tuned with low-rank adaptation (LoRA), enabling efficient training and inference on modest hardware. We evaluate GLoSS on three real-world Amazon review datasets: Beauty, Toys, and Sports, and find that it achieves state-of-the-art performance. Compared to traditional ID-based baselines, GLoSS improves Recall@5 by 33.3%, 52.8%, and 15.2%, and NDCG@5 by 30.0%, 42.6%, and 16.1%, respectively. It also outperforms LLM-based recommenders such as P5, GPT4Rec, LlamaRec and E4SRec with Recall@5 gains of 4.3%, 22.8%, and 29.5%. Additionally, user segment evaluations show that GLoSS performs particularly well for cold-start users in the Amazon Toys and Sports datasets, and benefits from longer user histories in Amazon Beauty dataset, demonstrating robustness across different levels of interaction lengths.