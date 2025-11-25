---
layout: publication
title: Approximating Categorical Similarity In Sponsored Search Relevance
authors: Hiba Ahsan, Rahul Agrawal
conference: Arxiv
year: 2018
bibkey: ahsan2018approximating
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1812.00158'}]
tags: ["Large Scale Search", "Neural Hashing", "Similarity Search"]
short_authors: Hiba Ahsan, Rahul Agrawal
---
Sponsored Search is a major source of revenue for web search engines. Since
sponsored search follows a pay-per-click model, showing relevant ads for
receiving clicks is crucial. Matching categories of a query and its ad
candidates have been explored in modeling relevance of query-ad pairs. The
approach involves matching cached categories of queries seen in the past to
categories of candidate ads. Since queries have a heavy tail distribution, the
approach has limited coverage. In this work, we propose approximating
categorical similarity of a query-ad pairs using neural networks, particularly
CLSM. Embedding of a query (or document) is generated using its tri-letter
representation which allows coverage of tail queries. Offline experiments of
incorporating this feature as opposed to using the categories directly show a
5.23% improvement in AUC ROC. A/B testing results show an improvement of 8.2%
in relevance.