---
layout: publication
title: Learning Dense Representations For Entity Retrieval
authors: Daniel Gillick, Sayali Kulkarni, Larry Lansing, Alessandro Presta, Jason
  Baldridge, Eugene Ie, Diego Garcia-Olano
conference: Proceedings of the 23rd Conference on Computational Natural Language Learning
  (CoNLL)
year: 2019
bibkey: gillick2019learning
citations: 189
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1909.10506'}]
tags: []
short_authors: Gillick et al.
---
We show that it is feasible to perform entity linking by training a dual
encoder (two-tower) model that encodes mentions and entities in the same dense
vector space, where candidate entities are retrieved by approximate nearest
neighbor search. Unlike prior work, this setup does not rely on an alias table
followed by a re-ranker, and is thus the first fully learned entity retrieval
model. We show that our dual encoder, trained using only anchor-text links in
Wikipedia, outperforms discrete alias table and BM25 baselines, and is
competitive with the best comparable results on the standard TACKBP-2010
dataset. In addition, it can retrieve candidates extremely fast, and
generalizes well to a new dataset derived from Wikinews. On the modeling side,
we demonstrate the dramatic value of an unsupervised negative mining algorithm
for this task.