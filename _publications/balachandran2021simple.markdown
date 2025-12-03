---
layout: publication
title: Simple And Efficient Ways To Improve REALM
authors: Vidhisha Balachandran, Ashish Vaswani, Yulia Tsvetkov, Niki Parmar
conference: Proceedings of the 3rd Workshop on Machine Reading for Question Answering
year: 2021
bibkey: balachandran2021simple
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2104.08710'}]
tags: ["Datasets", "Efficiency", "Evaluation", "Graph Based ANN"]
short_authors: Balachandran et al.
---
Dense retrieval has been shown to be effective for retrieving relevant
documents for Open Domain QA, surpassing popular sparse retrieval methods like
BM25. REALM (Guu et al., 2020) is an end-to-end dense retrieval system that
relies on MLM based pretraining for improved downstream QA efficiency across
multiple datasets. We study the finetuning of REALM on various QA tasks and
explore the limits of various hyperparameter and supervision choices. We find
that REALM was significantly undertrained when finetuning and simple
improvements in the training, supervision, and inference setups can
significantly benefit QA results and exceed the performance of other models
published post it. Our best model, REALM++, incorporates all the best working
findings and achieves significant QA accuracy improvements over baselines
(~5.5% absolute accuracy) without any model design changes. Additionally,
REALM++ matches the performance of large Open Domain QA models which have 3x
more parameters demonstrating the efficiency of the setup.