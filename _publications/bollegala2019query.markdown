---
layout: publication
title: Query Obfuscation Semantic Decomposition
authors: Danushka Bollegala, Tomoya MacHide, Ken-Ichi Kawarabayashi
conference: Arxiv
year: 2019
bibkey: bollegala2019query
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1909.05819'}]
tags: ["Robustness"]
short_authors: Danushka Bollegala, Tomoya MacHide, Ken-Ichi Kawarabayashi
---
We propose a method to protect the privacy of search engine users by
decomposing the queries using semantically *related* and unrelated
*distractor* terms. Instead of a single query, the search engine receives
multiple decomposed query terms. Next, we reconstruct the search results
relevant to the original query term by aggregating the search results retrieved
for the decomposed query terms. We show that the word embeddings learnt using a
distributed representation learning method can be used to find semantically
related and distractor query terms. We derive the relationship between the
*obfuscity* achieved through the proposed query anonymisation method and
the *reconstructability* of the original search results using the
decomposed queries. We analytically study the risk of discovering the search
engine users' information intents under the proposed query obfuscation method,
and empirically evaluate its robustness against clustering-based attacks. Our
experimental results show that the proposed method can accurately reconstruct
the search results for user queries, without compromising the privacy of the
search engine users.