---
layout: publication
title: Hash Embeddings for Efficient Word Representations
authors: D A N T I T O S V E N S T R U P, J O N A S H A N S E N, O L E W I N T H E R
conference: "Neural Information Processing Systems"
year: 2017
bibkey: tito2017hash
additional_links:
  - {name: "Paper", url: "https://papers.nips.cc/paper/2017/hash/f0f6ba4b5e0000340312d33c212c3ae8-Abstract.html"}
tags: ['Independent', 'NEURIPS']
---
We present hash embeddings an efficient method for representing words in a continuous vector form. A hash embedding may be seen as an interpolation between a standard word embedding and a word embedding created using a random hash function (the hashing trick). In hash embeddings each token is represented by k d-dimensional embeddings vectors and one k dimensional weight vector. The final d dimensional representation of the token is the product of the two. Rather than fitting the embedding vectors for each token these are selected by the hashing trick from a shared pool of B embedding vectors. Our experiments show that hash embeddings can easily deal with huge vocabularies consisting of millions tokens. When using a hash embedding there is no need to create a dictionary before training nor to perform any kind of vocabulary pruning after training. We show that models trained using hash embeddings exhibit at least the same level of performance as models trained using regular embeddings across a wide range of tasks. Furthermore the number of parameters needed by such an embedding is only a fraction of what is required by a regular embedding. Since standard embeddings and embeddings constructed using the hashing trick are actually just special cases of a hash embedding hash embeddings can be considered an extension and improvement over the existing regular embedding types.
