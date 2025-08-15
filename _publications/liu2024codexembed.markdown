---
layout: publication
title: 'Codexembed: A Generalist Embedding Model Family For Multiligual And Multi-task
  Code Retrieval'
authors: Ye Liu, Rui Meng, Shafiq Joty, Silvio Savarese, Caiming Xiong, Yingbo Zhou,
  Semih Yavuz
conference: Arxiv
year: 2024
bibkey: liu2024codexembed
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2411.12644'}]
tags: ["Evaluation", "Scalability", "Text Retrieval"]
short_authors: Liu et al.
---
Despite the success of text retrieval in many NLP tasks, code retrieval
remains a largely underexplored area. Most text retrieval systems are tailored
for natural language queries, often neglecting the specific challenges of
retrieving code. This gap leaves existing models unable to effectively capture
the diversity of programming languages and tasks across different domains,
highlighting the need for more focused research in code retrieval. To address
this, we introduce CodeXEmbed, a family of large-scale code embedding models
ranging from 400M to 7B parameters. Our novel training pipeline unifies
multiple programming languages and transforms various code-related tasks into a
common retrieval framework, enhancing model generalizability and retrieval
performance. Our 7B model sets a new state-of-the-art (SOTA) in code retrieval,
outperforming the previous leading model, Voyage-Code, by over 20% on CoIR
benchmark. In addition to excelling in code retrieval, our models demonstrate
competitive performance on the widely adopted BeIR text retrieval benchmark,
offering versatility across domains. Experimental results demonstrate that
improving retrieval performance significantly enhances end-to-end
Retrieval-Augmented Generation (RAG) performance for code-related tasks.