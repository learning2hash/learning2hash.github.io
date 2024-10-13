---
layout: publication
title: Composite Code Sparse Autoencoders For First Stage Retrieval
authors: Lassance Carlos, Formal Thibault, Clinchant Stephane
conference: "Arxiv"
year: 2022
bibkey: lassance2022composite
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2204.07023"}
tags: ['ARXIV', 'Graph', 'Image Retrieval', 'Quantisation', 'Supervised']
---
We propose a Composite Code Sparse Autoencoder (CCSA) approach for
Approximate Nearest Neighbor (ANN) search of document representations based on
Siamese-BERT models. In Information Retrieval (IR), the ranking pipeline is
generally decomposed in two stages: the first stage focus on retrieving a
candidate set from the whole collection. The second stage re-ranks the
candidate set by relying on more complex models. Recently, Siamese-BERT models
have been used as first stage ranker to replace or complement the traditional
bag-of-word models. However, indexing and searching a large document collection
require efficient similarity search on dense vectors and this is why ANN
techniques come into play. Since composite codes are naturally sparse, we first
show how CCSA can learn efficient parallel inverted index thanks to an
uniformity regularizer. Second, CCSA can be used as a binary quantization
method and we propose to combine it with the recent graph based ANN techniques.
Our experiments on MSMARCO dataset reveal that CCSA outperforms IVF with
product quantization. Furthermore, CCSA binary quantization is beneficial for
the index size, and memory usage for the graph-based HNSW method, while
maintaining a good level of recall and MRR. Third, we compare with recent
supervised quantization methods for image retrieval and find that CCSA is able
to outperform them.
