---
layout: publication
title: What Are You Token About? Dense Retrieval As Distributions Over The Vocabulary
authors: Ori Ram, Liat Bezalel, Adi Zicher, Yonatan Belinkov, Jonathan Berant, Amir
  Globerson
conference: Arxiv
year: 2022
bibkey: ram2022what
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2212.10380'}]
tags: ["Evaluation", "Few Shot & Zero Shot"]
short_authors: Ram et al.
---
Dual encoders are now the dominant architecture for dense retrieval. Yet, we
have little understanding of how they represent text, and why this leads to
good performance. In this work, we shed light on this question via
distributions over the vocabulary. We propose to interpret the vector
representations produced by dual encoders by projecting them into the model's
vocabulary space. We show that the resulting projections contain rich semantic
information, and draw connection between them and sparse retrieval. We find
that this view can offer an explanation for some of the failure cases of dense
retrievers. For example, we observe that the inability of models to handle tail
entities is correlated with a tendency of the token distributions to forget
some of the tokens of those entities. We leverage this insight and propose a
simple way to enrich query and passage representations with lexical information
at inference time, and show that this significantly improves performance
compared to the original model in zero-shot settings, and specifically on the
BEIR benchmark.