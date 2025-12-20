---
layout: publication
title: Improving Neural Ranking Models With Traditional IR Methods
authors: Anik Saha, Oktie Hassanzadeh, Alex Gittens, Jian Ni, Kavitha Srinivas, Bulent
  Yener
conference: Arxiv
year: 2023
bibkey: saha2023improving
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2308.15027'}]
tags: ["Datasets", "Evaluation", "Scalability", "Text Retrieval"]
short_authors: Saha et al.
---
Neural ranking methods based on large transformer models have recently gained
significant attention in the information retrieval community, and have been
adopted by major commercial solutions. Nevertheless, they are computationally
expensive to create, and require a great deal of labeled data for specialized
corpora. In this paper, we explore a low resource alternative which is a
bag-of-embedding model for document retrieval and find that it is competitive
with large transformer models fine tuned on information retrieval tasks. Our
results show that a simple combination of TF-IDF, a traditional keyword
matching method, with a shallow embedding model provides a low cost path to
compete well with the performance of complex neural ranking models on 3
datasets. Furthermore, adding TF-IDF measures improves the performance of
large-scale fine tuned models on these tasks.