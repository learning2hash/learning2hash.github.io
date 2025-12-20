---
layout: publication
title: 'Refit: Relevance Feedback From A Reranker During Inference'
authors: Revanth Gangi Reddy, Pradeep Dasigi, Md Arafat Sultan, Arman Cohan, Avirup
  Sil, Heng Ji, Hannaneh Hajishirzi
conference: Arxiv
year: 2023
bibkey: reddy2023refit
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2305.11744'}]
tags: ["Evaluation", "Re-Ranking", "Tools & Libraries"]
short_authors: Reddy et al.
---
Retrieve-and-rerank is a prevalent framework in neural information retrieval,
wherein a bi-encoder network initially retrieves a pre-defined number of
candidates (e.g., K=100), which are then reranked by a more powerful
cross-encoder model. While the reranker often yields improved candidate scores
compared to the retriever, its scope is confined to only the top K retrieved
candidates. As a result, the reranker cannot improve retrieval performance in
terms of Recall@K. In this work, we propose to leverage the reranker to improve
recall by making it provide relevance feedback to the retriever at inference
time. Specifically, given a test instance during inference, we distill the
reranker's predictions for that instance into the retriever's query
representation using a lightweight update mechanism. The aim of the
distillation loss is to align the retriever's candidate scores more closely
with those produced by the reranker. The algorithm then proceeds by executing a
second retrieval step using the updated query vector. We empirically
demonstrate that this method, applicable to various retrieve-and-rerank
frameworks, substantially enhances retrieval recall across multiple domains,
languages, and modalities.