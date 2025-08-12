---
layout: publication
title: Modelling Commonsense Commonalities With Multi-facet Concept Embeddings
authors: Hanane Kteich, Na Li, Usashi Chatterjee, Zied Bouraoui, Steven Schockaert
conference: Findings of the Association for Computational Linguistics ACL 2024
year: 2024
bibkey: kteich2024modelling
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2403.16984'}]
tags: []
short_authors: Kteich et al.
---
Concept embeddings offer a practical and efficient mechanism for injecting
commonsense knowledge into downstream tasks. Their core purpose is often not to
predict the commonsense properties of concepts themselves, but rather to
identify commonalities, i.e.\ sets of concepts which share some property of
interest. Such commonalities are the basis for inductive generalisation, hence
high-quality concept embeddings can make learning easier and more robust.
Unfortunately, standard embeddings primarily reflect basic taxonomic
categories, making them unsuitable for finding commonalities that refer to more
specific aspects (e.g.\ the colour of objects or the materials they are made
of). In this paper, we address this limitation by explicitly modelling the
different facets of interest when learning concept embeddings. We show that
this leads to embeddings which capture a more diverse range of commonsense
properties, and consistently improves results in downstream tasks such as
ultra-fine entity typing and ontology completion.