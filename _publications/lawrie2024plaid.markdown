---
layout: publication
title: PLAID SHIRTTT For Large-scale Streaming Dense Retrieval
authors: Dawn Lawrie, Efsun Kayi, Eugene Yang, James Mayfield, Douglas W. Oard
conference: Proceedings of the 47th International ACM SIGIR Conference on Research
  and Development in Information Retrieval
year: 2024
bibkey: lawrie2024plaid
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2405.00975'}]
tags: ["SIGIR", "Scalability", "Text Retrieval"]
short_authors: Lawrie et al.
---
PLAID, an efficient implementation of the ColBERT late interaction bi-encoder
using pretrained language models for ranking, consistently achieves
state-of-the-art performance in monolingual, cross-language, and multilingual
retrieval. PLAID differs from ColBERT by assigning terms to clusters and
representing those terms as cluster centroids plus compressed residual vectors.
While PLAID is effective in batch experiments, its performance degrades in
streaming settings where documents arrive over time because representations of
new tokens may be poorly modeled by the earlier tokens used to select cluster
centroids. PLAID Streaming Hierarchical Indexing that Runs on Terabytes of
Temporal Text (PLAID SHIRTTT) addresses this concern using multi-phase
incremental indexing based on hierarchical sharding. Experiments on ClueWeb09
and the multilingual NeuCLIR collection demonstrate the effectiveness of this
approach both for the largest collection indexed to date by the ColBERT
architecture and in the multilingual setting, respectively.