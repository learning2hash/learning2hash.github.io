---
layout: publication
title: Rethink Training Of BERT Rerankers In Multi-stage Retrieval Pipeline
authors: Luyu Gao, Zhuyun Dai, Jamie Callan
conference: Lecture Notes in Computer Science
year: 2021
bibkey: gao2021rethink
citations: 71
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2101.08751'}]
tags: ["Evaluation", "Hybrid ANN Methods", "Re-Ranking", "Text Retrieval", "Vector Indexing"]
short_authors: Luyu Gao, Zhuyun Dai, Jamie Callan
---
Pre-trained deep language models~(LM) have advanced the state-of-the-art of
text retrieval. Rerankers fine-tuned from deep LM estimates candidate relevance
based on rich contextualized matching signals. Meanwhile, deep LMs can also be
leveraged to improve search index, building retrievers with better recall. One
would expect a straightforward combination of both in a pipeline to have
additive performance gain. In this paper, we discover otherwise and that
popular reranker cannot fully exploit the improved retrieval result. We,
therefore, propose a Localized Contrastive Estimation (LCE) for training
rerankers and demonstrate it significantly improves deep two-stage models.