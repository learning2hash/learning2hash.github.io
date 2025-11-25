---
layout: publication
title: 'Retrieval For Extremely Long Queries And Documents With RPRS: A Highly Efficient
  And Effective Transformer-based Re-ranker'
authors: Arian Askari, Suzan Verberne, Amin Abolghasemi, Wessel Kraaij, Gabriella
  Pasi
conference: ACM Transactions on Information Systems
year: 2023
bibkey: askari2023retrieval
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2303.01200'}]
tags: ["Datasets", "Efficiency", "Evaluation", "Re-Ranking"]
short_authors: Askari et al.
---
Retrieval with extremely long queries and documents is a well-known and
challenging task in information retrieval and is commonly known as
Query-by-Document (QBD) retrieval. Specifically designed Transformer models
that can handle long input sequences have not shown high effectiveness in QBD
tasks in previous work. We propose a Re-Ranker based on the novel Proportional
Relevance Score (RPRS) to compute the relevance score between a query and the
top-k candidate documents. Our extensive evaluation shows RPRS obtains
significantly better results than the state-of-the-art models on five different
datasets. Furthermore, RPRS is highly efficient since all documents can be
pre-processed, embedded, and indexed before query time which gives our
re-ranker the advantage of having a complexity of O(N) where N is the total
number of sentences in the query and candidate documents. Furthermore, our
method solves the problem of the low-resource training in QBD retrieval tasks
as it does not need large amounts of training data, and has only three
parameters with a limited range that can be optimized with a grid search even
if a small amount of labeled data is available. Our detailed analysis shows
that RPRS benefits from covering the full length of candidate documents and
queries.