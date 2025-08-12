---
layout: publication
title: 'Reveal The Unknown: Out-of-knowledge-base Mention Discovery With Entity Linking'
authors: Hang Dong, Jiaoyan Chen, Yuan He, Yinan Liu, Ian Horrocks
conference: Proceedings of the 32nd ACM International Conference on Information and
  Knowledge Management
year: 2023
bibkey: dong2023reveal
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2302.07189'}]
tags: ["CIKM"]
short_authors: Dong et al.
---
Discovering entity mentions that are out of a Knowledge Base (KB) from texts
plays a critical role in KB maintenance, but has not yet been fully explored.
The current methods are mostly limited to the simple threshold-based approach
and feature-based classification, and the datasets for evaluation are
relatively rare. We propose BLINKout, a new BERT-based Entity Linking (EL)
method which can identify mentions that do not have corresponding KB entities
by matching them to a special NIL entity. To better utilize BERT, we propose
new techniques including NIL entity representation and classification, with
synonym enhancement. We also apply KB Pruning and Versioning strategies to
automatically construct out-of-KB datasets from common in-KB EL datasets.
Results on five datasets of clinical notes, biomedical publications, and
Wikipedia articles in various domains show the advantages of BLINKout over
existing methods to identify out-of-KB mentions for the medical ontologies,
UMLS, SNOMED CT, and the general KB, WikiData.