---
layout: publication
title: End-to-end Entity Linking And Disambiguation Leveraging Word And Knowledge
  Graph Embeddings
authors: Rostislav Nedelchev, Debanjan Chaudhuri, Jens Lehmann, Asja Fischer
conference: Arxiv
year: 2020
bibkey: nedelchev2020end
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2002.11143'}]
tags: ["Evaluation"]
short_authors: Nedelchev et al.
---
Entity linking - connecting entity mentions in a natural language utterance
to knowledge graph (KG) entities is a crucial step for question answering over
KGs. It is often based on measuring the string similarity between the entity
label and its mention in the question. The relation referred to in the question
can help to disambiguate between entities with the same label. This can be
misleading if an incorrect relation has been identified in the relation linking
step. However, an incorrect relation may still be semantically similar to the
relation in which the correct entity forms a triple within the KG; which could
be captured by the similarity of their KG embeddings. Based on this idea, we
propose the first end-to-end neural network approach that employs KG as well as
word embeddings to perform joint relation and entity classification of simple
questions while implicitly performing entity disambiguation with the help of a
novel gating mechanism. An empirical evaluation shows that the proposed
approach achieves a performance comparable to state-of-the-art entity linking
while requiring less post-processing.