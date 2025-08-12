---
layout: publication
title: Large-scale Label Interpretation Learning For Few-shot Named Entity Recognition
authors: Jonas Golde, Felix Hamborg, Alan Akbik
conference: Arxiv
year: 2024
bibkey: golde2024large
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2403.14222'}]
tags: ["Few Shot & Zero Shot", "Scalability"]
short_authors: Jonas Golde, Felix Hamborg, Alan Akbik
---
Few-shot named entity recognition (NER) detects named entities within text
using only a few annotated examples. One promising line of research is to
leverage natural language descriptions of each entity type: the common label
PER might, for example, be verbalized as ''person entity.'' In an initial label
interpretation learning phase, the model learns to interpret such verbalized
descriptions of entity types. In a subsequent few-shot tagset extension phase,
this model is then given a description of a previously unseen entity type (such
as ''music album'') and optionally a few training examples to perform few-shot
NER for this type. In this paper, we systematically explore the impact of a
strong semantic prior to interpret verbalizations of new entity types by
massively scaling up the number and granularity of entity types used for label
interpretation learning. To this end, we leverage an entity linking benchmark
to create a dataset with orders of magnitude of more distinct entity types and
descriptions as currently used datasets. We find that this increased signal
yields strong results in zero- and few-shot NER in in-domain, cross-domain, and
even cross-lingual settings. Our findings indicate significant potential for
improving few-shot NER through heuristical data-based optimization.