---
layout: publication
title: Lucene For Approximate Nearest-neighbors Search On Arbitrary Dense Vectors
authors: Tommaso Teofili, Jimmy Lin
conference: Arxiv
year: 2019
bibkey: teofili2019lucene
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1910.10208'}]
tags: [Neural Hashing, Efficiency, Tree-based ANN, Locality Sensitive Hashing, Tools
    & Libraries, Similarity Search]
short_authors: Tommaso Teofili, Jimmy Lin
---
We demonstrate three approaches for adapting the open-source Lucene search
library to perform approximate nearest-neighbor search on arbitrary dense
vectors, using similarity search on word embeddings as a case study. At its
core, Lucene is built around inverted indexes of a document collection's
(sparse) term-document matrix, which is incompatible with the lower-dimensional
dense vectors that are common in deep learning applications. We evaluate three
techniques to overcome these challenges that can all be natively integrated
into Lucene: the creation of documents populated with fake words, LSH applied
to lexical realizations of dense vectors, and k-d trees coupled with
dimensionality reduction. Experiments show that the "fake words" approach
represents the best balance between effectiveness and efficiency. These
techniques are integrated into the Anserini open-source toolkit and made
available to the community.