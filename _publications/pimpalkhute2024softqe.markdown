---
layout: publication
title: 'Softqe: Learned Representations Of Queries Expanded By Llms'
authors: Varad Pimpalkhute, John Heyer, Xusen Yin, Sameer Gupta
conference: Lecture Notes in Computer Science
year: 2024
bibkey: pimpalkhute2024softqe
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2402.12663'}]
tags: ["Evaluation"]
short_authors: Pimpalkhute et al.
---
We investigate the integration of Large Language Models (LLMs) into query
encoders to improve dense retrieval without increasing latency and cost, by
circumventing the dependency on LLMs at inference time. SoftQE incorporates
knowledge from LLMs by mapping embeddings of input queries to those of the
LLM-expanded queries. While improvements over various strong baselines on
in-domain MS-MARCO metrics are marginal, SoftQE improves performance by 2.83
absolute percentage points on average on five out-of-domain BEIR tasks.