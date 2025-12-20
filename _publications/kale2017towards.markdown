---
layout: publication
title: Towards Semantic Query Segmentation
authors: Ajinkya Kale, Thrivikrama Taula, Sanjika Hewavitharana, Amit Srivastava
conference: Arxiv
year: 2017
bibkey: kale2017towards
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1707.07835'}]
tags: ["Evaluation", "Supervised"]
short_authors: Kale et al.
---
Query Segmentation is one of the critical components for understanding users'
search intent in Information Retrieval tasks. It involves grouping tokens in
the search query into meaningful phrases which help downstream tasks like
search relevance and query understanding. In this paper, we propose a novel
approach to segment user queries using distributed query embeddings. Our key
contribution is a supervised approach to the segmentation task using
low-dimensional feature vectors for queries, getting rid of traditional hand
tuned and heuristic NLP features which are quite expensive.
  We benchmark on a 50,000 human-annotated web search engine query corpus
achieving comparable accuracy to state-of-the-art techniques. The advantage of
our technique is its fast and does not use external knowledge-base like
Wikipedia for score boosting. This helps us generalize our approach to other
domains like eCommerce without any fine-tuning. We demonstrate the
effectiveness of this method on another 50,000 human-annotated eCommerce query
corpus from eBay search logs. Our approach is easy to implement and generalizes
well across different search domains proving the power of low-dimensional
embeddings in query segmentation task, opening up a new direction of research
for this problem.