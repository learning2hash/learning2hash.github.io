---
layout: publication
title: Quantifying Positional Biases In Text Embedding Models
authors: Samarth Goel, Reagan J. Lee, Kannan Ramchandran
conference: Arxiv
year: 2024
bibkey: goel2024quantifying
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.15241'}]
tags: [Distance Metric Learning, Robustness]
short_authors: Samarth Goel, Reagan J. Lee, Kannan Ramchandran
---
Embedding models are crucial for tasks in Information Retrieval (IR) and
semantic similarity measurement, yet their handling of longer texts and
associated positional biases remains underexplored. In this study, we
investigate the impact of content position and input size on text embeddings.
Our experiments reveal that embedding models, irrespective of their positional
encoding mechanisms, disproportionately prioritize the beginning of an input.
Ablation studies demonstrate that insertion of irrelevant text or removal at
the start of a document reduces cosine similarity between altered and original
embeddings by up to 12.3% more than ablations at the end. Regression analysis
further confirms this bias, with sentence importance declining as position
moves further from the start, even with with content-agnosticity. We
hypothesize that this effect arises from pre-processing strategies and chosen
positional encoding techniques. These findings quantify the sensitivity of
retrieval systems and suggest a new lens towards embedding model robustness.