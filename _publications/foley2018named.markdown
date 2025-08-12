---
layout: publication
title: Named Entity Recognition With Extremely Limited Data
authors: John Foley, Sheikh Muhammad Sarwar, James Allan
conference: Arxiv
year: 2018
bibkey: foley2018named
citations: 11
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1806.04411'}]
tags: ["Few Shot & Zero Shot"]
short_authors: John Foley, Sheikh Muhammad Sarwar, James Allan
---
Traditional information retrieval treats named entity recognition as a
pre-indexing corpus annotation task, allowing entity tags to be indexed and
used during search. Named entity taggers themselves are typically trained on
thousands or tens of thousands of examples labeled by humans.
  However, there is a long tail of named entities classes, and for these cases,
labeled data may be impossible to find or justify financially. We propose
exploring named entity recognition as a search task, where the named entity
class of interest is a query, and entities of that class are the relevant
"documents". What should that query look like? Can we even perform NER-style
labeling with tens of labels? This study presents an exploration of CRF-based
NER models with handcrafted features and of how we might transform them into
search queries.