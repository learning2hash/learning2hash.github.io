---
layout: publication
title: 'Cole And LYS At Bioasq MESINESP8 Task: Similarity Based Descriptor Assignment
  In Spanish'
authors: Francisco J. Ribadas-Pena, Shuyuan Cao, Elmurod Kuriyozov
conference: Working Notes of CLEF 2020. Vol. 2696 of CEUR Workshop Proceedings (CEUR-WS.org)
year: 2024
bibkey: ribadaspena2024cole
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2402.01916'}]
tags: ["Text Retrieval"]
short_authors: Francisco J. Ribadas-Pena, Shuyuan Cao, Elmurod Kuriyozov
---
In this paper, we describe our participation in the MESINESP Task of the
BioASQ biomedical semantic indexing challenge. The participating system follows
an approach based solely on conventional information retrieval tools. We have
evaluated various alternatives for extracting index terms from IBECS/LILACS
documents in order to be stored in an Apache Lucene index. Those indexed
representations are queried using the contents of the article to be annotated
and a ranked list of candidate labels is created from the retrieved documents.
We also have evaluated a sort of limited Label Powerset approach which creates
meta-labels joining pairs of DeCS labels with high co-occurrence scores, and an
alternative method based on label profile matching. Results obtained in
official runs seem to confirm the suitability of this approach for languages
like Spanish.