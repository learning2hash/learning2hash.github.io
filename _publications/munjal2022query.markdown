---
layout: publication
title: Query-guided Networks For Few-shot Fine-grained Classification And Person Search
authors: Bharti Munjal, Alessandro Flaborea, Sikandar Amin, Federico Tombari, Fabio
  Galasso
conference: Pattern Recognition
year: 2022
bibkey: munjal2022query
citations: 22
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2209.10250'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Munjal et al.
---
Few-shot fine-grained classification and person search appear as distinct
tasks and literature has treated them separately. But a closer look unveils
important similarities: both tasks target categories that can only be
discriminated by specific object details; and the relevant models should
generalize to new categories, not seen during training.
  We propose a novel unified Query-Guided Network (QGN) applicable to both
tasks. QGN consists of a Query-guided Siamese-Squeeze-and-Excitation subnetwork
which re-weights both the query and gallery features across all network layers,
a Query-guided Region Proposal subnetwork for query-specific localisation, and
a Query-guided Similarity subnetwork for metric learning.
  QGN improves on a few recent few-shot fine-grained datasets, outperforming
other techniques on CUB by a large margin. QGN also performs competitively on
the person search CUHK-SYSU and PRW datasets, where we perform in-depth
analysis.