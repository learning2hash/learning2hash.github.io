---
layout: publication
title: 'Beyond Lexical: A Semantic Retrieval Framework For Textual Searchengine'
authors: Kuan Fang, Long Zhao, Zhan Shen, Ruixing Wang, Rikang Zhour, Liwen Fan
conference: Arxiv
year: 2020
bibkey: fang2020beyond
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2008.03917'}]
tags: ["Evaluation", "Text Retrieval", "Tools & Libraries"]
short_authors: Fang et al.
---
Search engine has become a fundamental component in various web and mobile
applications. Retrieving relevant documents from the massive datasets is
challenging for a search engine system, especially when faced with verbose or
tail queries. In this paper, we explore a vector space search framework for
document retrieval. Specifically, we trained a deep semantic matching model so
that each query and document can be encoded as a low dimensional embedding. Our
model was trained based on BERT architecture. We deployed a fast
k-nearest-neighbor index service for online serving. Both offline and online
metrics demonstrate that our method improved retrieval performance and search
quality considerably, particularly for tail