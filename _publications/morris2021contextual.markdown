---
layout: publication
title: Contextual Document Embeddings
authors: Morris John X., Rush Alexander M.
conference: 'Proceedings of the 59th Annual Meeting of the Association for Computational
  Linguistics and the 11th International Joint Conference on Natural Language Processing
  (Volume 2: Short Papers)'
year: 2021
bibkey: morris2021contextual
citations: 190
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2410.02525'}]
tags: []
---
Dense document embeddings are central to neural retrieval. The dominant
paradigm is to train and construct embeddings by running encoders directly on
individual documents. In this work, we argue that these embeddings, while
effective, are implicitly out-of-context for targeted use cases of retrieval,
and that a contextualized document embedding should take into account both the
document and neighboring documents in context - analogous to contextualized
word embeddings. We propose two complementary methods for contextualized
document embeddings: first, an alternative contrastive learning objective that
explicitly incorporates the document neighbors into the intra-batch contextual
loss; second, a new contextual architecture that explicitly encodes neighbor
document information into the encoded representation. Results show that both
methods achieve better performance than biencoders in several settings, with
differences especially pronounced out-of-domain. We achieve state-of-the-art
results on the MTEB benchmark with no hard negative mining, score distillation,
dataset-specific instructions, intra-GPU example-sharing, or extremely large
batch sizes. Our method can be applied to improve performance on any
contrastive learning dataset and any biencoder.