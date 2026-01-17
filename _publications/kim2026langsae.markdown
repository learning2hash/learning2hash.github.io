---
layout: publication
title: 'LANGSAE EDITING: Improving Multilingual Information Retrieval Via Post-hoc
  Language Identity Removal'
authors: Dongjun Kim, Jeongho Yoon, Chanjun Park, Heuiseok Lim
conference: Arxiv
year: 2026
bibkey: kim2026langsae
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2601.04768'}]
tags: ["Uncategorized"]
short_authors: Kim et al.
---
Dense retrieval in multilingual settings often searches over mixed-language collections, yet multilingual embeddings encode language identity alongside semantics. This language signal can inflate similarity for same-language pairs and crowd out relevant evidence written in other languages. We propose LANGSAE EDITING, a post-hoc sparse autoencoder trained on pooled embeddings that enables controllable removal of language-identity signal directly in vector space. The method identifies language-associated latent units using cross-language activation statistics, suppresses these units at inference time, and reconstructs embeddings in the original dimensionality, making it compatible with existing vector databases without retraining the base encoder or re-encoding raw text. Experiments across multiple languages show consistent improvements in ranking quality and cross-language coverage, with especially strong gains for script-distinct languages.