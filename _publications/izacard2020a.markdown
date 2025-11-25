---
layout: publication
title: A Memory Efficient Baseline For Open Domain Question Answering
authors: Gautier Izacard, Fabio Petroni, Lucas Hosseini, Nicola de Cao, Sebastian
  Riedel, Edouard Grave
conference: Arxiv
year: 2020
bibkey: izacard2020a
citations: 29
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2012.15156'}]
tags: ["Memory Efficiency", "Quantization"]
short_authors: Izacard et al.
---
Recently, retrieval systems based on dense representations have led to
important improvements in open-domain question answering, and related tasks.
While very effective, this approach is also memory intensive, as the dense
vectors for the whole knowledge source need to be kept in memory. In this
paper, we study how the memory footprint of dense retriever-reader systems can
be reduced. We consider three strategies to reduce the index size: dimension
reduction, vector quantization and passage filtering. We evaluate our approach
on two question answering benchmarks: TriviaQA and NaturalQuestions, showing
that it is possible to get competitive systems using less than 6Gb of memory.