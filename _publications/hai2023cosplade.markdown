---
layout: publication
title: 'Cosplade: Contextualizing SPLADE For Conversational Information Retrieval'
authors: Nam Le Hai, Thomas Gerald, Thibault Formal, Jian-Yun Nie, Benjamin Piwowarski,
  Laure Soulier
conference: Lecture Notes in Computer Science
year: 2023
bibkey: hai2023cosplade
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2301.04413'}]
tags: ["Datasets", "Few Shot & Zero Shot"]
short_authors: Hai et al.
---
Conversational search is a difficult task as it aims at retrieving documents
based not only on the current user query but also on the full conversation
history. Most of the previous methods have focused on a multi-stage ranking
approach relying on query reformulation, a critical intermediate step that
might lead to a sub-optimal retrieval. Other approaches have tried to use a
fully neural IR first-stage, but are either zero-shot or rely on full
learning-to-rank based on a dataset with pseudo-labels. In this work,
leveraging the CANARD dataset, we propose an innovative lightweight learning
technique to train a first-stage ranker based on SPLADE. By relying on SPLADE
sparse representations, we show that, when combined with a second-stage ranker
based on T5Mono, the results are competitive on the TREC CAsT 2020 and 2021
tracks.