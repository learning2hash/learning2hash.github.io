---
layout: publication
title: Improving Bert-based Query-by-document Retrieval With Multi-task Optimization
authors: Amin Abolghasemi, Suzan Verberne, Leif Azzopardi
conference: Lecture Notes in Computer Science
year: 2022
bibkey: abolghasemi2022improving
citations: 20
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2202.00373'}]
tags: ["Evaluation", "Text Retrieval"]
short_authors: Amin Abolghasemi, Suzan Verberne, Leif Azzopardi
---
Query-by-document (QBD) retrieval is an Information Retrieval task in which a
seed document acts as the query and the goal is to retrieve related documents
-- it is particular common in professional search tasks. In this work we
improve the retrieval effectiveness of the BERT re-ranker, proposing an
extension to its fine-tuning step to better exploit the context of queries. To
this end, we use an additional document-level representation learning objective
besides the ranking objective when fine-tuning the BERT re-ranker. Our
experiments on two QBD retrieval benchmarks show that the proposed multi-task
optimization significantly improves the ranking effectiveness without changing
the BERT re-ranker or using additional training samples. In future work, the
generalizability of our approach to other retrieval tasks should be further
investigated.