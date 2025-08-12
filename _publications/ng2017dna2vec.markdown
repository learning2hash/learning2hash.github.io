---
layout: publication
title: 'Dna2vec: Consistent Vector Representations Of Variable-length K-mers'
authors: Patrick Ng
conference: Arxiv
year: 2017
bibkey: ng2017dna2vec
citations: 129
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1701.06279'}]
tags: ["Distance Metric Learning"]
short_authors: Patrick Ng
---
One of the ubiquitous representation of long DNA sequence is dividing it into
shorter k-mer components. Unfortunately, the straightforward vector encoding of
k-mer as a one-hot vector is vulnerable to the curse of dimensionality. Worse
yet, the distance between any pair of one-hot vectors is equidistant. This is
particularly problematic when applying the latest machine learning algorithms
to solve problems in biological sequence analysis. In this paper, we propose a
novel method to train distributed representations of variable-length k-mers.
Our method is based on the popular word embedding model word2vec, which is
trained on a shallow two-layer neural network. Our experiments provide evidence
that the summing of dna2vec vectors is akin to nucleotides concatenation. We
also demonstrate that there is correlation between Needleman-Wunsch similarity
score and cosine similarity of dna2vec vectors.