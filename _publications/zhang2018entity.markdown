---
layout: publication
title: Entity Synonym Discovery Via Multipiece Bilateral Context Matching
authors: Chenwei Zhang, Yaliang Li, Nan Du, Wei Fan, Philip S. Yu
conference: Proceedings of the Twenty-Ninth International Joint Conference on Artificial
  Intelligence
year: 2020
bibkey: zhang2018entity
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1901.00056'}]
tags: ["IJCAI"]
short_authors: Zhang et al.
---
Being able to automatically discover synonymous entities in an open-world
setting benefits various tasks such as entity disambiguation or knowledge graph
canonicalization. Existing works either only utilize entity features, or rely
on structured annotations from a single piece of context where the entity is
mentioned. To leverage diverse contexts where entities are mentioned, in this
paper, we generalize the distributional hypothesis to a multi-context setting
and propose a synonym discovery framework that detects entity synonyms from
free-text corpora with considerations on effectiveness and robustness. As one
of the key components in synonym discovery, we introduce a neural network model
SYNONYMNET to determine whether or not two given entities are synonym with each
other. Instead of using entities features, SYNONYMNET makes use of multiple
pieces of contexts in which the entity is mentioned, and compares the
context-level similarity via a bilateral matching schema. Experimental results
demonstrate that the proposed model is able to detect synonym sets that are not
observed during training on both generic and domain-specific datasets:
Wiki+Freebase, PubMed+UMLS, and MedBook+MKG, with up to 4.16% improvement in
terms of Area Under the Curve and 3.19% in terms of Mean Average Precision
compared to the best baseline method.