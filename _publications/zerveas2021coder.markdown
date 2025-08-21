---
layout: publication
title: 'CODER: An Efficient Framework For Improving Retrieval Through Contextual Document
  Embedding Reranking'
authors: George Zerveas, Navid Rekabsaz, Daniel Cohen, Carsten Eickhoff
conference: Proceedings of the 2022 Conference on Empirical Methods in Natural Language
  Processing
year: 2022
bibkey: zerveas2021coder
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2112.08766'}]
tags: ["EMNLP", "Evaluation", "Self-Supervised", "Similarity Search", "Tools & Libraries"]
short_authors: Zerveas et al.
---
Contrastive learning has been the dominant approach to training dense
retrieval models. In this work, we investigate the impact of ranking context -
an often overlooked aspect of learning dense retrieval models. In particular,
we examine the effect of its constituent parts: jointly scoring a large number
of negatives per query, using retrieved (query-specific) instead of random
negatives, and a fully list-wise loss. To incorporate these factors into
training, we introduce Contextual Document Embedding Reranking (CODER), a
highly efficient retrieval framework. When reranking, it incurs only a
negligible computational overhead on top of a first-stage method at run time
(delay per query in the order of milliseconds), allowing it to be easily
combined with any state-of-the-art dual encoder method. After fine-tuning
through CODER, which is a lightweight and fast process, models can also be used
as stand-alone retrievers. Evaluating CODER in a large set of experiments on
the MS~MARCO and TripClick collections, we show that the contextual reranking
of precomputed document embeddings leads to a significant improvement in
retrieval performance. This improvement becomes even more pronounced when more
relevance information per query is available, shown in the TripClick
collection, where we establish new state-of-the-art results by a large margin.