---
layout: publication
title: Knowledge-aware Neural Collective Matrix Factorization For Cross-domain Recommendation
authors: Li Zhang, Yan Ge, Jun Ma, Jianmo Ni, Haiping Lu
conference: 'Findings of the Association for Computational Linguistics: EMNLP 2022'
year: 2022
bibkey: zhang2022knowledge
citations: 17
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2206.13255'}]
tags: ["EMNLP", "Recommender Systems"]
short_authors: Zhang et al.
---
Cross-domain recommendation (CDR) can help customers find more satisfying
items in different domains. Existing CDR models mainly use common users or
mapping functions as bridges between domains but have very limited exploration
in fully utilizing extra knowledge across domains. In this paper, we propose to
incorporate the knowledge graph (KG) for CDR, which enables items in different
domains to share knowledge. To this end, we first construct a new dataset
AmazonKG4CDR from the Freebase KG and a subset (two domain pairs: movies-music,
movie-book) of Amazon Review Data. This new dataset facilitates linking
knowledge to bridge within- and cross-domain items for CDR. Then we propose a
new framework, KG-aware Neural Collective Matrix Factorization (KG-NeuCMF),
leveraging KG to enrich item representations. It first learns item embeddings
by graph convolutional autoencoder to capture both domain-specific and
domain-general knowledge from adjacent and higher-order neighbours in the KG.
Then, we maximize the mutual information between item embeddings learned from
the KG and user-item matrix to establish cross-domain relationships for better
CDR. Finally, we conduct extensive experiments on the newly constructed dataset
and demonstrate that our model significantly outperforms the best-performing
baselines.