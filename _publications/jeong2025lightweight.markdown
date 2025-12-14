---
layout: publication
title: Lightweight Relevance Grader In RAG
authors: Taehee Jeong
conference: 2025 8th International Conference on Information and Computer Technologies
  (ICICT)
year: 2025
bibkey: jeong2025lightweight
citations: 0
additional_links: [{name: Code, url: 'https://github.com/taeheej/Lightweight-Relevance-Grader-in-RAG'},
  {name: Paper, url: 'https://arxiv.org/abs/2506.14084'}]
tags: [Evaluation]
short_authors: Taehee Jeong
---
Retrieval-Augmented Generation (RAG) addresses limitations of large language models (LLMs) by leveraging a vector database to provide more accurate and up-to-date information. When a user submits a query, RAG executes a vector search to find relevant documents, which are then used to generate a response. However, ensuring the relevance of retrieved documents with a query would be a big challenge. To address this, a secondary model, known as a relevant grader, can be served to verify its relevance. To reduce computational requirements of a relevant grader, a lightweight small language model is preferred. In this work, we finetuned llama-3.2-1b as a relevant grader and achieved a significant increase in precision from 0.1301 to 0.7750. Its precision is comparable to that of llama-3.1-70b. Our code is available at https://github.com/taeheej/Lightweight-Relevance-Grader-in-RAG.