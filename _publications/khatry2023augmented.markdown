---
layout: publication
title: Augmented Embeddings For Custom Retrievals
authors: Anirudh Khatry, Yasharth Bajpai, Priyanshu Gupta, Sumit Gulwani, Ashish Tiwari
conference: Arxiv
year: 2023
bibkey: khatry2023augmented
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2310.05380'}]
tags: []
short_authors: Khatry et al.
---
Information retrieval involves selecting artifacts from a corpus that are
most relevant to a given search query. The flavor of retrieval typically used
in classical applications can be termed as homogeneous and relaxed, where
queries and corpus elements are both natural language (NL) utterances
(homogeneous) and the goal is to pick most relevant elements from the corpus in
the Top-K, where K is large, such as 10, 25, 50 or even 100 (relaxed).
Recently, retrieval is being used extensively in preparing prompts for large
language models (LLMs) to enable LLMs to perform targeted tasks. These new
applications of retrieval are often heterogeneous and strict -- the queries and
the corpus contain different kinds of entities, such as NL and code, and there
is a need for improving retrieval at Top-K for small values of K, such as K=1
or 3 or 5. Current dense retrieval techniques based on pretrained embeddings
provide a general-purpose and powerful approach for retrieval, but they are
oblivious to task-specific notions of similarity of heterogeneous artifacts. We
introduce Adapted Dense Retrieval, a mechanism to transform embeddings to
enable improved task-specific, heterogeneous and strict retrieval. Adapted
Dense Retrieval works by learning a low-rank residual adaptation of the
pretrained black-box embedding. We empirically validate our approach by showing
improvements over the state-of-the-art general-purpose embeddings-based
baseline.