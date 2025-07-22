---
layout: publication
title: Unsupervised Semantic Hashing With Pairwise Reconstruction
authors: Hansen Casper, Hansen Christian, Simonsen Jakob Grue, Alstrup Stephen, Lioma
  Christina
conference: Proceedings of the 43rd International ACM SIGIR Conference on Research
  and Development in Information Retrieval
year: 2020
bibkey: hansen2020unsupervised
citations: 22
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2007.00380'}]
tags: ["Hashing-Methods", "Text-Retrieval", "Scalability", "Similarity-Search", "SIGIR", "Datasets", "Supervised", "Evaluation", "Unsupervised"]
short_authors: Hansen et al.
---
Semantic Hashing is a popular family of methods for efficient similarity
search in large-scale datasets. In Semantic Hashing, documents are encoded as
short binary vectors (i.e., hash codes), such that semantic similarity can be
efficiently computed using the Hamming distance. Recent state-of-the-art
approaches have utilized weak supervision to train better performing hashing
models. Inspired by this, we present Semantic Hashing with Pairwise
Reconstruction (PairRec), which is a discrete variational autoencoder based
hashing model. PairRec first encodes weakly supervised training pairs (a query
document and a semantically similar document) into two hash codes, and then
learns to reconstruct the same query document from both of these hash codes
(i.e., pairwise reconstruction). This pairwise reconstruction enables our model
to encode local neighbourhood structures within the hash code directly through
the decoder. We experimentally compare PairRec to traditional and
state-of-the-art approaches, and obtain significant performance improvements in
the task of document similarity search.