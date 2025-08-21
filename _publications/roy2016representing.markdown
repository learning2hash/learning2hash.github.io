---
layout: publication
title: Representing Documents And Queries As Sets Of Word Embedded Vectors For Information
  Retrieval
authors: Dwaipayan Roy, Debasis Ganguly, Mandar Mitra, Gareth J. F. Jones
conference: Arxiv
year: 2016
bibkey: roy2016representing
citations: 11
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1606.07869'}]
tags: ["Datasets", "Distance Metric Learning", "Evaluation"]
short_authors: Roy et al.
---
A major difficulty in applying word vector embeddings in IR is in devising an
effective and efficient strategy for obtaining representations of compound
units of text, such as whole documents, (in comparison to the atomic words),
for the purpose of indexing and scoring documents. Instead of striving for a
suitable method for obtaining a single vector representation of a large
document of text, we rather aim for developing a similarity metric that makes
use of the similarities between the individual embedded word vectors in a
document and a query. More specifically, we represent a document and a query as
sets of word vectors, and use a standard notion of similarity measure between
these sets, computed as a function of the similarities between each constituent
word pair from these sets. We then make use of this similarity measure in
combination with standard IR based similarities for document ranking. The
results of our initial experimental investigations shows that our proposed
method improves MAP by up to \(5.77%\), in comparison to standard text-based
language model similarity, on the TREC ad-hoc dataset.