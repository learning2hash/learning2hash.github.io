---
layout: publication
title: Understanding BERT Rankers Under Distillation
authors: Luyu Gao, Zhuyun Dai, Jamie Callan
conference: Proceedings of the 2020 ACM SIGIR on International Conference on Theory
  of Information Retrieval
year: 2020
bibkey: gao2020understanding
citations: 23
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2007.11088'}]
tags: ["Efficiency", "Evaluation", "SIGIR"]
short_authors: Luyu Gao, Zhuyun Dai, Jamie Callan
---
Deep language models such as BERT pre-trained on large corpus have given a
huge performance boost to the state-of-the-art information retrieval ranking
systems. Knowledge embedded in such models allows them to pick up complex
matching signals between passages and queries. However, the high computation
cost during inference limits their deployment in real-world search scenarios.
In this paper, we study if and how the knowledge for search within BERT can be
transferred to a smaller ranker through distillation. Our experiments
demonstrate that it is crucial to use a proper distillation procedure, which
produces up to nine times speedup while preserving the state-of-the-art
performance.