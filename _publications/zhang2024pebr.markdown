---
layout: publication
title: 'Pebr: A Probabilistic Approach To Embedding Based Retrieval'
authors: Han Zhang, Yunjing Jiang, Mingming Li, Haowei Yuan, Wen-Yun Yang
conference: Arxiv
year: 2024
bibkey: zhang2024pebr
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2410.19349'}]
tags: ["Distance Metric Learning", "Evaluation"]
short_authors: Zhang et al.
---
Embedding retrieval aims to learn a shared semantic representation space for
both queries and items, thus enabling efficient and effective item retrieval
using approximate nearest neighbor (ANN) algorithms. In current industrial
practice, retrieval systems typically retrieve a fixed number of items for
different queries, which actually leads to insufficient retrieval (low recall)
for head queries and irrelevant retrieval (low precision) for tail queries.
Mostly due to the trend of frequentist approach to loss function designs, till
now there is no satisfactory solution to holistically address this challenge in
the industry. In this paper, we move away from the frequentist approach, and
take a novel \textbf\{p\}robabilistic approach to \textbf\{e\}mbedding
\textbf\{b\}ased \textbf\{r\}etrieval (namely \textbf\{pEBR\}) by learning the item
distribution for different queries, which enables a dynamic cosine similarity
threshold calculated by the probabilistic cumulative distribution function
(CDF) value. The experimental results show that our approach improves both the
retrieval precision and recall significantly. Ablation studies also illustrate
how the probabilistic approach is able to capture the differences between head
and tail queries.