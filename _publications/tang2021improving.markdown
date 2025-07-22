---
layout: publication
title: Improving Document Representations By Generating Pseudo Query Embeddings For
  Dense Retrieval
authors: Tang Hongyin, Sun Xingwu, Jin Beihong, Wang Jingang, Zhang Fuzheng, Wu Wei
conference: 'Proceedings of the 59th Annual Meeting of the Association for Computational
  Linguistics and the 11th International Joint Conference on Natural Language Processing
  (Volume 1: Long Papers)'
year: 2021
bibkey: tang2021improving
citations: 23
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2105.03599'}]
tags: ["Text-Retrieval", "Efficiency", "Tools-&-Libraries", "Datasets", "Evaluation"]
short_authors: Tang et al.
---
Recently, the retrieval models based on dense representations have been
gradually applied in the first stage of the document retrieval tasks, showing
better performance than traditional sparse vector space models. To obtain high
efficiency, the basic structure of these models is Bi-encoder in most cases.
However, this simple structure may cause serious information loss during the
encoding of documents since the queries are agnostic. To address this problem,
we design a method to mimic the queries on each of the documents by an
iterative clustering process and represent the documents by multiple pseudo
queries (i.e., the cluster centroids). To boost the retrieval process using
approximate nearest neighbor search library, we also optimize the matching
function with a two-step score calculation procedure. Experimental results on
several popular ranking and QA datasets show that our model can achieve
state-of-the-art results.