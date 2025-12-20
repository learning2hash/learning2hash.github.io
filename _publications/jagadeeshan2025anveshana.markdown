---
layout: publication
title: 'Anveshana: A New Benchmark Dataset For Cross-lingual Information Retrieval
  On English Queries And Sanskrit Documents'
authors: Manoj Balaji Jagadeeshan, Prince Raj, Pawan Goyal
conference: Arxiv
year: 2025
bibkey: jagadeeshan2025anveshana
citations: 0
additional_links: [{name: Code, url: 'https://huggingface.co/datasets/manojbalaji1/anveshana'},
  {name: Paper, url: 'https://arxiv.org/abs/2505.19494'}]
tags: ["Datasets", "Evaluation", "Tools & Libraries"]
short_authors: Manoj Balaji Jagadeeshan, Prince Raj, Pawan Goyal
---
The study presents a comprehensive benchmark for retrieving Sanskrit documents using English queries, focusing on the chapters of the Srimadbhagavatam. It employs a tripartite approach: Direct Retrieval (DR), Translation-based Retrieval (DT), and Query Translation (QT), utilizing shared embedding spaces and advanced translation methods to enhance retrieval systems in a RAG framework. The study fine-tunes state-of-the-art models for Sanskrit's linguistic nuances, evaluating models such as BM25, REPLUG, mDPR, ColBERT, Contriever, and GPT-2. It adapts summarization techniques for Sanskrit documents to improve QA processing. Evaluation shows DT methods outperform DR and QT in handling the cross-lingual challenges of ancient texts, improving accessibility and understanding. A dataset of 3,400 English-Sanskrit query-document pairs underpins the study, aiming to preserve Sanskrit scriptures and share their philosophical importance widely. Our dataset is publicly available at https://huggingface.co/datasets/manojbalaji1/anveshana