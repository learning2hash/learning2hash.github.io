---
layout: publication
title: Binary Paragraph Vectors
authors: Grzegorczyk Karol, Kurdziel Marcin
conference: Proceedings of the 2nd Workshop on Representation Learning for NLP
year: 2017
bibkey: grzegorczyk2017binary
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1611.01116'}]
---
Recently Le & Mikolov described two log-linear models, called Paragraph
Vector, that can be used to learn state-of-the-art distributed representations
of documents. Inspired by this work, we present Binary Paragraph Vector models:
simple neural networks that learn short binary codes for fast information
retrieval. We show that binary paragraph vectors outperform autoencoder-based
binary codes, despite using fewer bits. We also evaluate their precision in
transfer learning settings, where binary codes are inferred for documents
unrelated to the training corpus. Results from these experiments indicate that
binary paragraph vectors can capture semantics relevant for various
domain-specific documents. Finally, we present a model that simultaneously
learns short binary codes and longer, real-valued representations. This model
can be used to rapidly retrieve a short list of highly relevant documents from
a large document collection.