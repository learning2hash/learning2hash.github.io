---
layout: publication
title: 'GLIMMER: Generalized Late-interaction Memory Reranker'
authors: Michiel de Jong, Yury Zemlyanskiy, Nicholas Fitzgerald, Sumit Sanghai, William
  W. Cohen, Joshua Ainslie
conference: Arxiv
year: 2023
bibkey: dejong2023glimmer
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2306.10231'}]
tags: ["Evaluation", "Memory Efficiency", "Re-Ranking"]
short_authors: Jong et al.
---
Memory-augmentation is a powerful approach for efficiently incorporating
external information into language models, but leads to reduced performance
relative to retrieving text. Recent work introduced LUMEN, a memory-retrieval
hybrid that partially pre-computes memory and updates memory representations on
the fly with a smaller live encoder.
  We propose GLIMMER, which improves on this approach through 1) exploiting
free access to the powerful memory representations by applying a shallow
reranker on top of memory to drastically improve retrieval quality at low cost,
and 2) incorporating multi-task training to learn a general and higher quality
memory and live encoder. GLIMMER achieves strong gains in performance at faster
speeds compared to LUMEN and FiD on the KILT benchmark of knowledge-intensive
tasks.