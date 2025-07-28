---
layout: publication
title: 'Deepcat: Deep Category Representation For Query Understanding In E-commerce
  Search'
authors: Ali Ahmadvand, Surya Kallumadi, Faizan Javed, Eugene Agichtein
conference: Arxiv
year: 2021
bibkey: ahmadvand2021deepcat
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2104.11760'}]
tags: []
short_authors: Ahmadvand et al.
---
Mapping a search query to a set of relevant categories in the product
taxonomy is a significant challenge in e-commerce search for two reasons: 1)
Training data exhibits severe class imbalance problem due to biased click
behavior, and 2) queries with little customer feedback (e.g., tail queries) are
not well-represented in the training set, and cause difficulties for query
understanding. To address these problems, we propose a deep learning model,
DeepCAT, which learns joint word-category representations to enhance the query
understanding process. We believe learning category interactions helps to
improve the performance of category mapping on minority classes, tail and torso
queries. DeepCAT contains a novel word-category representation model that
trains the category representations based on word-category co-occurrences in
the training set. The category representation is then leveraged to introduce a
new loss function to estimate the category-category co-occurrences for refining
joint word-category embeddings. To demonstrate our model's effectiveness on
minority categories and tail queries, we conduct two sets of experiments. The
results show that DeepCAT reaches a 10% improvement on minority classes and a
7.1% improvement on tail queries over a state-of-the-art label embedding model.
Our findings suggest a promising direction for improving e-commerce search by
semantic modeling of taxonomy hierarchies.