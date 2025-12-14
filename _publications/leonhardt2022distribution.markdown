---
layout: publication
title: Distribution-aligned Fine-tuning For Efficient Neural Retrieval
authors: Jurek Leonhardt, Marcel Jahnke, Avishek Anand
conference: Arxiv
year: 2022
bibkey: leonhardt2022distribution
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2211.04942'}]
tags: [Distance Metric Learning, Evaluation]
short_authors: Jurek Leonhardt, Marcel Jahnke, Avishek Anand
---
Dual-encoder-based neural retrieval models achieve appreciable performance
and complement traditional lexical retrievers well due to their semantic
matching capabilities, which makes them a common choice for hybrid IR systems.
However, these models exhibit a performance bottleneck in the online query
encoding step, as the corresponding query encoders are usually large and
complex Transformer models.
  In this paper we investigate heterogeneous dual-encoder models, where the two
encoders are separate models that do not share parameters or initializations.
We empirically show that heterogeneous dual-encoders are susceptible to
collapsing representations, causing them to output constant trivial
representations when they are fine-tuned using a standard contrastive loss due
to a distribution mismatch. We propose DAFT, a simple two-stage fine-tuning
approach that aligns the two encoders in order to prevent them from collapsing.
We further demonstrate how DAFT can be used to train efficient heterogeneous
dual-encoder models using lightweight query encoders.