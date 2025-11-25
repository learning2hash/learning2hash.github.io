---
layout: publication
title: 'Blowfish: Topological And Statistical Signatures For Quantifying Ambiguity
  In Semantic Search'
authors: Thomas Roland Barillot, Alex de Castro
conference: Arxiv
year: 2024
bibkey: barillot2024blowfish
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2406.07990'}]
tags: ["Datasets", "Similarity Search", "Vector Indexing"]
short_authors: Thomas Roland Barillot, Alex de Castro
---
This works reports evidence for the topological signatures of ambiguity in
sentence embeddings that could be leveraged for ranking and/or explanation
purposes in the context of vector search and Retrieval Augmented Generation
(RAG) systems. We proposed a working definition of ambiguity and designed an
experiment where we have broken down a proprietary dataset into collections of
chunks of varying size - 3, 5, and 10 lines and used the different collections
successively as queries and answers sets. It allowed us to test the signatures
of ambiguity with removal of confounding factors. Our results show that proxy
ambiguous queries (size 10 queries against size 3 documents) display different
distributions of homologies 0 and 1 based features than proxy clear queries
(size 5 queries against size 10 documents). We then discuss those results in
terms increased manifold complexity and/or approximately discontinuous
embedding submanifolds. Finally we propose a strategy to leverage those
findings as a new scoring strategy of semantic similarities.