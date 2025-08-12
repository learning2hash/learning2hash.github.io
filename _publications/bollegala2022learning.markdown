---
layout: publication
title: Learning Meta Word Embeddings By Unsupervised Weighted Concatenation Of Source
  Embeddings
authors: Danushka Bollegala
conference: Proceedings of the Thirty-First International Joint Conference on Artificial
  Intelligence
year: 2022
bibkey: bollegala2022learning
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2204.12386'}]
tags: ["Unsupervised"]
short_authors: Danushka Bollegala
---
Given multiple source word embeddings learnt using diverse algorithms and
lexical resources, meta word embedding learning methods attempt to learn more
accurate and wide-coverage word embeddings.
  Prior work on meta-embedding has repeatedly discovered that simple vector
concatenation of the source embeddings to be a competitive baseline.
  However, it remains unclear as to why and when simple vector concatenation
can produce accurate meta-embeddings.
  We show that weighted concatenation can be seen as a spectrum matching
operation between each source embedding and the meta-embedding, minimising the
pairwise inner-product loss.
  Following this theoretical analysis, we propose two *unsupervised*
methods to learn the optimal concatenation weights for creating meta-embeddings
from a given set of source embeddings.
  Experimental results on multiple benchmark datasets show that the proposed
weighted concatenated meta-embedding methods outperform previously proposed
meta-embedding learning methods.