---
layout: publication
title: 'The Shape Of Word Embeddings: Quantifying Non-isometry With Topological Data
  Analysis'
authors: "Ond\u0159ej Draganov, Steven Skiena"
conference: 'Findings of the Association for Computational Linguistics: EMNLP 2024'
year: 2024
bibkey: draganov2024shape
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2404.00500'}]
tags: ["EMNLP"]
short_authors: "Ond\u0159ej Draganov, Steven Skiena"
---
Word embeddings represent language vocabularies as clouds of \(d\)-dimensional
points. We investigate how information is conveyed by the general shape of
these clouds, instead of representing the semantic meaning of each token.
Specifically, we use the notion of persistent homology from topological data
analysis (TDA) to measure the distances between language pairs from the shape
of their unlabeled embeddings. These distances quantify the degree of
non-isometry of the embeddings. To distinguish whether these differences are
random training errors or capture real information about the languages, we use
the computed distance matrices to construct language phylogenetic trees over 81
Indo-European languages. Careful evaluation shows that our reconstructed trees
exhibit strong and statistically-significant similarities to the reference.