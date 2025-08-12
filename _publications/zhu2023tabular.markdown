---
layout: publication
title: Tabular Few-shot Generalization Across Heterogeneous Feature Spaces
authors: Max Zhu, Katarzyna Kobalczyk, Andrija Petrovic, Mladen Nikolic, Mihaela van
  Der Schaar, Boris Delibasic, Petro Lio
conference: Arxiv
year: 2023
bibkey: zhu2023tabular
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2311.10051'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Zhu et al.
---
Despite the prevalence of tabular datasets, few-shot learning remains
under-explored within this domain. Existing few-shot methods are not directly
applicable to tabular datasets due to varying column relationships, meanings,
and permutational invariance. To address these challenges, we propose FLAT-a
novel approach to tabular few-shot learning, encompassing knowledge sharing
between datasets with heterogeneous feature spaces. Utilizing an encoder
inspired by Dataset2Vec, FLAT learns low-dimensional embeddings of datasets and
their individual columns, which facilitate knowledge transfer and
generalization to previously unseen datasets. A decoder network parametrizes
the predictive target network, implemented as a Graph Attention Network, to
accommodate the heterogeneous nature of tabular datasets. Experiments on a
diverse collection of 118 UCI datasets demonstrate FLAT's successful
generalization to new tabular datasets and a considerable improvement over the
baselines.