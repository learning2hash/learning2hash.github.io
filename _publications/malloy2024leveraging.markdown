---
layout: publication
title: Leveraging A Cognitive Model To Measure Subjective Similarity Of Human And
  GPT-4 Written Content
authors: "Tailia Malloy, Maria Jos\xE9 Ferreira, Fei Fang, Cleotilde Gonzalez"
conference: Proceedings of the 28th Conference on Computational Natural Language Learning
year: 2024
bibkey: malloy2024leveraging
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2409.00269'}]
tags: ["Distance Metric Learning"]
short_authors: Malloy et al.
---
Cosine similarity between two documents can be computed using token embeddings formed by Large Language Models (LLMs) such as GPT-4, and used to categorize those documents across a range of uses. However, these similarities are ultimately dependent on the corpora used to train these LLMs, and may not reflect subjective similarity of individuals or how their biases and constraints impact similarity metrics. This lack of cognitively-aware personalization of similarity metrics can be particularly problematic in educational and recommendation settings where there is a limited number of individual judgements of category or preference, and biases can be particularly relevant. To address this, we rely on an integration of an Instance-Based Learning (IBL) cognitive model with LLM embeddings to develop the Instance-Based Individualized Similarity (IBIS) metric. This similarity metric is beneficial in that it takes into account individual biases and constraints in a manner that is grounded in the cognitive mechanisms of decision making. To evaluate the IBIS metric, we also introduce a dataset of human categorizations of emails as being either dangerous (phishing) or safe (ham). This dataset is used to demonstrate the benefits of leveraging a cognitive model to measure the subjective similarity of human participants in an educational setting.