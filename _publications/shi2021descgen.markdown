---
layout: publication
title: 'DESCGEN: A Distantly Supervised Dataset For Generating Abstractive Entity
  Descriptions'
authors: Weijia Shi, Mandar Joshi, Luke Zettlemoyer
conference: ACL-IJCNLP 2021
year: 2021
bibkey: shi2021descgen
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2106.05365'}]
tags: ["Datasets"]
short_authors: Weijia Shi, Mandar Joshi, Luke Zettlemoyer
---
Short textual descriptions of entities provide summaries of their key
attributes and have been shown to be useful sources of background knowledge for
tasks such as entity linking and question answering. However, generating entity
descriptions, especially for new and long-tail entities, can be challenging
since relevant information is often scattered across multiple sources with
varied content and style. We introduce DESCGEN: given mentions spread over
multiple documents, the goal is to generate an entity summary description.
DESCGEN consists of 37K entity descriptions from Wikipedia and Fandom, each
paired with nine evidence documents on average. The documents were collected
using a combination of entity linking and hyperlinks to the Wikipedia and
Fandom entity pages, which together provide high-quality distant supervision.
The resulting summaries are more abstractive than those found in existing
datasets and provide a better proxy for the challenge of describing new and
emerging entities. We also propose a two-stage extract-then-generate baseline
and show that there exists a large gap (19.9% in ROUGE-L) between
state-of-the-art models and human performance, suggesting that the data will
support significant future work.