---
layout: publication
title: Improving Query Representations For Dense Retrieval With Pseudo Relevance Feedback
authors: Hongchien Yu, Chenyan Xiong, Jamie Callan
conference: Proceedings of the 30th ACM International Conference on Information &amp;
  Knowledge Management
year: 2021
bibkey: yu2021improving
citations: 44
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2108.13454'}]
tags: []
short_authors: Hongchien Yu, Chenyan Xiong, Jamie Callan
---
Dense retrieval systems conduct first-stage retrieval using embedded
representations and simple similarity metrics to match a query to documents.
Its effectiveness depends on encoded embeddings to capture the semantics of
queries and documents, a challenging task due to the shortness and ambiguity of
search queries. This paper proposes ANCE-PRF, a new query encoder that uses
pseudo relevance feedback (PRF) to improve query representations for dense
retrieval. ANCE-PRF uses a BERT encoder that consumes the query and the top
retrieved documents from a dense retrieval model, ANCE, and it learns to
produce better query embeddings directly from relevance labels. It also keeps
the document index unchanged to reduce overhead. ANCE-PRF significantly
outperforms ANCE and other recent dense retrieval systems on several datasets.
Analysis shows that the PRF encoder effectively captures the relevant and
complementary information from PRF documents, while ignoring the noise with its
learned attention mechanism.