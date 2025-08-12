---
layout: publication
title: Entity Linking And Discovery Via Arborescence-based Supervised Clustering
authors: Dhruv Agarwal, Rico Angell, Nicholas Monath, Andrew McCallum
conference: Arxiv
year: 2021
bibkey: agarwal2021entity
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2109.01242'}]
tags: ["Supervised"]
short_authors: Agarwal et al.
---
Previous work has shown promising results in performing entity linking by
measuring not only the affinities between mentions and entities but also those
amongst mentions. In this paper, we present novel training and inference
procedures that fully utilize mention-to-mention affinities by building minimum
arborescences (i.e., directed spanning trees) over mentions and entities across
documents in order to make linking decisions. We also show that this method
gracefully extends to entity discovery, enabling the clustering of mentions
that do not have an associated entity in the knowledge base. We evaluate our
approach on the Zero-Shot Entity Linking dataset and MedMentions, the largest
publicly available biomedical dataset, and show significant improvements in
performance for both entity linking and discovery compared to identically
parameterized models. We further show significant efficiency improvements with
only a small loss in accuracy over previous work, which use more
computationally expensive models.