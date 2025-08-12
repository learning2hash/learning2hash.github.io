---
layout: publication
title: Contextual Multilingual Spellchecker For User Queries
authors: Sanat Sharma, Josep Valls-Vargas, Tracy Holloway King, Francois Guerin, Chirag
  Arora
conference: Proceedings of the 46th International ACM SIGIR Conference on Research
  and Development in Information Retrieval
year: 2023
bibkey: sharma2023contextual
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2305.01082'}]
tags: ["SIGIR"]
short_authors: Sharma et al.
---
Spellchecking is one of the most fundamental and widely used search features.
Correcting incorrectly spelled user queries not only enhances the user
experience but is expected by the user. However, most widely available
spellchecking solutions are either lower accuracy than state-of-the-art
solutions or too slow to be used for search use cases where latency is a key
requirement. Furthermore, most innovative recent architectures focus on English
and are not trained in a multilingual fashion and are trained for spell
correction in longer text, which is a different paradigm from spell correction
for user queries, where context is sparse (most queries are 1-2 words long).
Finally, since most enterprises have unique vocabularies such as product names,
off-the-shelf spelling solutions fall short of users' needs. In this work, we
build a multilingual spellchecker that is extremely fast and scalable and that
adapts its vocabulary and hence speller output based on a specific product's
needs. Furthermore, our speller out-performs general purpose spellers by a wide
margin on in-domain datasets. Our multilingual speller is used in search in
Adobe products, powering autocomplete in various applications.