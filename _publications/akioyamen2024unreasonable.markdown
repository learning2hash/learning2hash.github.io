---
layout: publication
title: The Unreasonable Effectiveness Of Llms For Query Optimization
authors: Peter Akioyamen, Zixuan Yi, Ryan Marcus
conference: Arxiv
year: 2024
bibkey: akioyamen2024unreasonable
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2411.02862'}]
tags: ["Evaluation"]
short_authors: Peter Akioyamen, Zixuan Yi, Ryan Marcus
---
Recent work in database query optimization has used complex machine learning
strategies, such as customized reinforcement learning schemes. Surprisingly, we
show that LLM embeddings of query text contain useful semantic information for
query optimization. Specifically, we show that a simple binary classifier
deciding between alternative query plans, trained only on a small number of
labeled embedded query vectors, can outperform existing heuristic systems.
Although we only present some preliminary results, an LLM-powered query
optimizer could provide significant benefits, both in terms of performance and
simplicity.