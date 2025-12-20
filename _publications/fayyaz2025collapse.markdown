---
layout: publication
title: 'Collapse Of Dense Retrievers: Short, Early, And Literal Biases Outranking
  Factual Evidence'
authors: Mohsen Fayyaz, Ali Modarressi, Hinrich Schuetze, Nanyun Peng
conference: 'Proceedings of the 63rd Annual Meeting of the Association for Computational
  Linguistics (Volume 1: Long Papers)'
year: 2025
bibkey: fayyaz2025collapse
citations: 1
additional_links: [{name: Code, url: 'https://huggingface.co/datasets/mohsenfayyaz/ColDeR'},
  {name: Paper, url: 'https://arxiv.org/abs/2503.05037'}]
tags: ["Datasets", "Evaluation", "Robustness"]
short_authors: Fayyaz et al.
---
Dense retrieval models are commonly used in Information Retrieval (IR) applications, such as Retrieval-Augmented Generation (RAG). Since they often serve as the first step in these systems, their robustness is critical to avoid downstream failures. In this work, we repurpose a relation extraction dataset (e.g., Re-DocRED) to design controlled experiments that quantify the impact of heuristic biases, such as a preference for shorter documents, on retrievers like Dragon+ and Contriever. We uncover major vulnerabilities, showing retrievers favor shorter documents, early positions, repeated entities, and literal matches, all while ignoring the answer's presence! Notably, when multiple biases combine, models exhibit catastrophic performance degradation, selecting the answer-containing document in less than 10% of cases over a synthetic biased document without the answer. Furthermore, we show that these biases have direct consequences for downstream applications like RAG, where retrieval-preferred documents can mislead LLMs, resulting in a 34% performance drop than providing no documents at all. https://huggingface.co/datasets/mohsenfayyaz/ColDeR