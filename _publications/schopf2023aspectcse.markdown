---
layout: publication
title: 'Aspectcse: Sentence Embeddings For Aspect-based Semantic Textual Similarity
  Using Contrastive Learning And Structured Knowledge'
authors: Tim Schopf, Emanuel Gerber, Malte Ostendorff, Florian Matthes
conference: Proceedings of the Conference Recent Advances in Natural Language Processing
  - Large Language Models for Natural Language Processings
year: 2023
bibkey: schopf2023aspectcse
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2307.07851'}]
tags: ["Self-Supervised"]
short_authors: Schopf et al.
---
Generic sentence embeddings provide a coarse-grained approximation of
semantic textual similarity but ignore specific aspects that make texts
similar. Conversely, aspect-based sentence embeddings provide similarities
between texts based on certain predefined aspects. Thus, similarity predictions
of texts are more targeted to specific requirements and more easily
explainable. In this paper, we present AspectCSE, an approach for aspect-based
contrastive learning of sentence embeddings. Results indicate that AspectCSE
achieves an average improvement of 3.97% on information retrieval tasks across
multiple aspects compared to the previous best results. We also propose using
Wikidata knowledge graph properties to train models of multi-aspect sentence
embeddings in which multiple specific aspects are simultaneously considered
during similarity predictions. We demonstrate that multi-aspect embeddings
outperform single-aspect embeddings on aspect-specific information retrieval
tasks. Finally, we examine the aspect-based sentence embedding space and
demonstrate that embeddings of semantically similar aspect labels are often
close, even without explicit similarity training between different aspect
labels.