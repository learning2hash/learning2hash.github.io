---
layout: publication
title: Adversarial Semantic Collisions
authors: Congzheng Song, Alexander M. Rush, Vitaly Shmatikov
conference: Proceedings of the 2020 Conference on Empirical Methods in Natural Language
  Processing (EMNLP)
year: 2020
bibkey: song2020adversarial
citations: 28
additional_links: [{name: Code, url: 'https://github.com/csong27/collision-bert'},
  {name: Paper, url: 'https://arxiv.org/abs/2011.04743'}]
tags: [EMNLP, Robustness, Text Retrieval]
short_authors: Congzheng Song, Alexander M. Rush, Vitaly Shmatikov
---
We study semantic collisions: texts that are semantically unrelated but
judged as similar by NLP models. We develop gradient-based approaches for
generating semantic collisions and demonstrate that state-of-the-art models for
many tasks which rely on analyzing the meaning and similarity of texts--
including paraphrase identification, document retrieval, response suggestion,
and extractive summarization-- are vulnerable to semantic collisions. For
example, given a target query, inserting a crafted collision into an irrelevant
document can shift its retrieval rank from 1000 to top 3. We show how to
generate semantic collisions that evade perplexity-based filtering and discuss
other potential mitigations. Our code is available at
https://github.com/csong27/collision-bert.