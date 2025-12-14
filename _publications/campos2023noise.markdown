---
layout: publication
title: Noise-robust Dense Retrieval Via Contrastive Alignment Post Training
authors: Daniel Campos, Chengxiang Zhai, Alessandro Magnani
conference: Arxiv
year: 2023
bibkey: campos2023noise
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2304.03401'}]
tags: [Robustness]
short_authors: Daniel Campos, Chengxiang Zhai, Alessandro Magnani
---
The success of contextual word representations and advances in neural
information retrieval have made dense vector-based retrieval a standard
approach for passage and document ranking. While effective and efficient,
dual-encoders are brittle to variations in query distributions and noisy
queries. Data augmentation can make models more robust but introduces overhead
to training set generation and requires retraining and index regeneration. We
present Contrastive Alignment POst Training (CAPOT), a highly efficient
finetuning method that improves model robustness without requiring index
regeneration, the training set optimization, or alteration. CAPOT enables
robust retrieval by freezing the document encoder while the query encoder
learns to align noisy queries with their unaltered root. We evaluate CAPOT
noisy variants of MSMARCO, Natural Questions, and Trivia QA passage retrieval,
finding CAPOT has a similar impact as data augmentation with none of its
overhead.