---
layout: publication
title: 'CPS-MEBR: Click Feedback-aware Web Page Summarization For Multi-embedding-based
  Retrieval'
authors: Wenbiao Li, Pan Tang, Zhengfan Wu, Weixue Lu, Minghua Zhang, Zhenlei Tian,
  Daiting Shi, Yu Sun, Simiu Gu, Dawei Yin
conference: Arxiv
year: 2022
bibkey: li2022cps
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2210.09787'}]
tags: [Tools & Libraries]
short_authors: Li et al.
---
Embedding-based retrieval (EBR) is a technique to use embeddings to represent
query and document, and then convert the retrieval problem into a nearest
neighbor search problem in the embedding space. Some previous works have mainly
focused on representing the web page with a single embedding, but in real web
search scenarios, it is difficult to represent all the information of a long
and complex structured web page as a single embedding. To address this issue,
we design a click feedback-aware web page summarization for
multi-embedding-based retrieval (CPS-MEBR) framework which is able to generate
multiple embeddings for web pages to match different potential queries.
Specifically, we use the click data of users in search logs to train a summary
model to extract those sentences in web pages that are frequently clicked by
users, which are more likely to answer those potential queries. Meanwhile, we
introduce sentence-level semantic interaction to design a multi-embedding-based
retrieval (MEBR) model, which can generate multiple embeddings to deal with
different potential queries by using frequently clicked sentences in web pages.
Offline experiments show that it can perform high quality candidate retrieval
compared to single-embedding-based retrieval (SEBR) model.