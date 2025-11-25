---
layout: publication
title: Document Network Projection In Pretrained Word Embedding Space
authors: Antoine Gourru, Adrien Guille, Julien Velcin, Julien Jacques
conference: Lecture Notes in Computer Science
year: 2020
bibkey: gourru2020document
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2001.05727'}]
tags: ["Recommender Systems", "Similarity Search", "Unsupervised"]
short_authors: Gourru et al.
---
We present Regularized Linear Embedding (RLE), a novel method that projects a
collection of linked documents (e.g. citation network) into a pretrained word
embedding space. In addition to the textual content, we leverage a matrix of
pairwise similarities providing complementary information (e.g., the network
proximity of two documents in a citation graph). We first build a simple word
vector average for each document, and we use the similarities to alter this
average representation. The document representations can help to solve many
information retrieval tasks, such as recommendation, classification and
clustering. We demonstrate that our approach outperforms or matches existing
document network embedding methods on node classification and link prediction
tasks. Furthermore, we show that it helps identifying relevant keywords to
describe document classes.