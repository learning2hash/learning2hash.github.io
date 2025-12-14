---
layout: publication
title: Semantic Table Retrieval Using Keyword And Table Queries
authors: Shuo Zhang, Krisztian Balog
conference: ACM Transactions on the Web
year: 2021
bibkey: zhang2021semantic
citations: 11
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2105.06365'}]
tags: [Supervised, Tools & Libraries]
short_authors: Shuo Zhang, Krisztian Balog
---
Tables on the Web contain a vast amount of knowledge in a structured form. To
tap into this valuable resource, we address the problem of table retrieval:
answering an information need with a ranked list of tables. We investigate this
problem in two different variants, based on how the information need is
expressed: as a keyword query or as an existing table ("query-by-table"). The
main novel contribution of this work is a semantic table retrieval framework
for matching information needs (keyword or table queries) against tables.
Specifically, we (i) represent queries and tables in multiple semantic spaces
(both discrete sparse and continuous dense vector representations) and (ii)
introduce various similarity measures for matching those semantic
representations. We consider all possible combinations of semantic
representations and similarity measures and use these as features in a
supervised learning model. Using two purpose-built test collections based on
Wikipedia tables, we demonstrate significant and substantial improvements over
state-of-the-art baselines.