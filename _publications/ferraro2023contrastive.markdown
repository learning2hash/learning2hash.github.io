---
layout: publication
title: Contrastive Learning for Cross-modal Artist Retrieval
authors: Ferraro et al.
conference: 2021 IEEE International Conference on Big Data (Big Data)
year: 2023
bibkey: ferraro2023contrastive
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2308.06556'}]
tags: [Self Supervised]
---
Music retrieval and recommendation applications often rely on content
features encoded as embeddings, which provide vector representations of items
in a music dataset. Numerous complementary embeddings can be derived from
processing items originally represented in several modalities, e.g., audio
signals, user interaction data, or editorial data. However, data of any given
modality might not be available for all items in any music dataset. In this
work, we propose a method based on contrastive learning to combine embeddings
from multiple modalities and explore the impact of the presence or absence of
embeddings from diverse modalities in an artist similarity task. Experiments on
two datasets suggest that our contrastive method outperforms single-modality
embeddings and baseline algorithms for combining modalities, both in terms of
artist retrieval accuracy and coverage. Improvements with respect to other
methods are particularly significant for less popular query artists. We
demonstrate our method successfully combines complementary information from
diverse modalities, and is more robust to missing modality data (i.e., it
better handles the retrieval of artists with different modality embeddings than
the query artist's).