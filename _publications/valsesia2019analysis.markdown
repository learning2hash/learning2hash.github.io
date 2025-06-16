---
layout: publication
title: 'Analysis Of Sparsehash: An Efficient Embedding Of Set-similarity Via Sparse
  Projections'
authors: Diego Valsesia, Sophie Marie Fosson, Chiara Ravazzi, Tiziano Bianchi, Enrico
  Magli
conference: Arxiv
year: 2019
citations: 3
bibkey: valsesia2019analysis
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1909.01802'}]
tags: [Hashing Methods, Tools and Libraries]
---
Embeddings provide compact representations of signals in order to perform
efficient inference in a wide variety of tasks. In particular, random
projections are common tools to construct Euclidean distance-preserving
embeddings, while hashing techniques are extensively used to embed
set-similarity metrics, such as the Jaccard coefficient. In this letter, we
theoretically prove that a class of random projections based on sparse
matrices, called SparseHash, can preserve the Jaccard coefficient between the
supports of sparse signals, which can be used to estimate set similarities.
Moreover, besides the analysis, we provide an efficient implementation and we
test the performance in several numerical experiments, both on synthetic and
real datasets.