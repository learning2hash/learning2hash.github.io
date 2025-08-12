---
layout: publication
title: Cross-modulation Networks For Few-shot Learning
authors: Hugo Prol, Vincent Dumoulin, Luis Herranz
conference: Arxiv
year: 2018
bibkey: prol2018cross
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1812.00273'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Hugo Prol, Vincent Dumoulin, Luis Herranz
---
A family of recent successful approaches to few-shot learning relies on
learning an embedding space in which predictions are made by computing
similarities between examples. This corresponds to combining information
between support and query examples at a very late stage of the prediction
pipeline. Inspired by this observation, we hypothesize that there may be
benefits to combining the information at various levels of abstraction along
the pipeline. We present an architecture called Cross-Modulation Networks which
allows support and query examples to interact throughout the feature extraction
process via a feature-wise modulation mechanism. We adapt the Matching Networks
architecture to take advantage of these interactions and show encouraging
initial results on miniImageNet in the 5-way, 1-shot setting, where we close
the gap with state-of-the-art.