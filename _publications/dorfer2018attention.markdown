---
layout: publication
title: Attention As A Perspective For Learning Tempo-invariant Audio Queries
authors: "Matthias Dorfer, Jan Haji\u010D, Gerhard Widmer"
conference: Arxiv
year: 2018
bibkey: dorfer2018attention
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1809.05689'}]
tags: ["Audio Retrieval", "Evaluation", "Multimodal Retrieval"]
short_authors: "Matthias Dorfer, Jan Haji\u010D, Gerhard Widmer"
---
Current models for audio--sheet music retrieval via multimodal embedding
space learning use convolutional neural networks with a fixed-size window for
the input audio. Depending on the tempo of a query performance, this window
captures more or less musical content, while notehead density in the score is
largely tempo-independent. In this work we address this disparity with a soft
attention mechanism, which allows the model to encode only those parts of an
audio excerpt that are most relevant with respect to efficient query codes.
Empirical results on classical piano music indicate that attention is
beneficial for retrieval performance, and exhibits intuitively appealing
behavior.