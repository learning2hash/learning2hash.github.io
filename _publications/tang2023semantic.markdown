---
layout: publication
title: Semantic-enhanced Differentiable Search Index Inspired By Learning Strategies
authors: Yubao Tang, Ruqing Zhang, Jiafeng Guo, Jiangui Chen, Zuowei Zhu, Shuaiqiang
  Wang, Dawei Yin, Xueqi Cheng
conference: Proceedings of the 29th ACM SIGKDD Conference on Knowledge Discovery and
  Data Mining
year: 2023
bibkey: tang2023semantic
citations: 26
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2305.15115'}]
tags: ["Evaluation", "KDD", "Text Retrieval"]
short_authors: Tang et al.
---
Recently, a new paradigm called Differentiable Search Index (DSI) has been
proposed for document retrieval, wherein a sequence-to-sequence model is
learned to directly map queries to relevant document identifiers. The key idea
behind DSI is to fully parameterize traditional ``index-retrieve'' pipelines
within a single neural model, by encoding all documents in the corpus into the
model parameters. In essence, DSI needs to resolve two major questions: (1) how
to assign an identifier to each document, and (2) how to learn the associations
between a document and its identifier. In this work, we propose a
Semantic-Enhanced DSI model (SE-DSI) motivated by Learning Strategies in the
area of Cognitive Psychology. Our approach advances original DSI in two ways:
(1) For the document identifier, we take inspiration from Elaboration
Strategies in human learning. Specifically, we assign each document an
Elaborative Description based on the query generation technique, which is more
meaningful than a string of integers in the original DSI; and (2) For the
associations between a document and its identifier, we take inspiration from
Rehearsal Strategies in human learning. Specifically, we select fine-grained
semantic features from a document as Rehearsal Contents to improve document
memorization. Both the offline and online experiments show improved retrieval
performance over prevailing baselines.