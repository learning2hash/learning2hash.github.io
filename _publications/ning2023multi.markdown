---
layout: publication
title: Multi-domain Recommendation With Embedding Disentangling And Domain Alignment
authors: Ning et al.
conference: Proceedings of the 32nd ACM International Conference on Information and
  Knowledge Management
year: 2023
bibkey: ning2023multi
citations: 11
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2308.05508'}]
tags: [CIKM, Recommender Systems]
---
Multi-domain recommendation (MDR) aims to provide recommendations for
different domains (e.g., types of products) with overlapping users/items and is
common for platforms such as Amazon, Facebook, and LinkedIn that host multiple
services. Existing MDR models face two challenges: First, it is difficult to
disentangle knowledge that generalizes across domains (e.g., a user likes cheap
items) and knowledge specific to a single domain (e.g., a user likes blue
clothing but not blue cars). Second, they have limited ability to transfer
knowledge across domains with small overlaps. We propose a new MDR method named
EDDA with two key components, i.e., embedding disentangling recommender and
domain alignment, to tackle the two challenges respectively. In particular, the
embedding disentangling recommender separates both the model and embedding for
the inter-domain part and the intra-domain part, while most existing MDR
methods only focus on model-level disentangling. The domain alignment leverages
random walks from graph processing to identify similar user/item pairs from
different domains and encourages similar user/item pairs to have similar
embeddings, enhancing knowledge transfer. We compare EDDA with 12
state-of-the-art baselines on 3 real datasets. The results show that EDDA
consistently outperforms the baselines on all datasets and domains. All
datasets and codes are available at https://github.com/Stevenn9981/EDDA.