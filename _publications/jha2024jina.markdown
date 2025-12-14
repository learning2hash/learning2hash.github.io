---
layout: publication
title: 'Jina-colbert-v2: A General-purpose Multilingual Late Interaction Retriever'
authors: "Rohan Jha, Bo Wang, Michael G\xFCnther, Georgios Mastrapas, Saba Sturua,\
  \ Isabelle Mohr, Andreas Koukounas, Mohammad Kalim Akram, Nan Wang, Han Xiao"
conference: Proceedings of the Fourth Workshop on Multilingual Representation Learning
  (MRL 2024)
year: 2024
bibkey: jha2024jina
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2408.16672'}]
tags: [Evaluation, Efficiency]
short_authors: Jha et al.
---
Multi-vector dense models, such as ColBERT, have proven highly effective in
information retrieval. ColBERT's late interaction scoring approximates the
joint query-document attention seen in cross-encoders while maintaining
inference efficiency closer to traditional dense retrieval models, thanks to
its bi-encoder architecture and recent optimizations in indexing and search. In
this work we propose a number of incremental improvements to the ColBERT model
architecture and training pipeline, using methods shown to work in the more
mature single-vector embedding model training paradigm, particularly those that
apply to heterogeneous multilingual data or boost efficiency with little
tradeoff. Our new model, Jina-ColBERT-v2, demonstrates strong performance
across a range of English and multilingual retrieval tasks.