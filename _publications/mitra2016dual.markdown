---
layout: publication
title: A Dual Embedding Space Model For Document Ranking
authors: Mitra Bhaskar, Nalisnick Eric, Craswell Nick, Caruana Rich
conference: Arxiv
year: 2016
bibkey: mitra2016dual
citations: 110
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1602.01137'}]
tags: ["Evaluation"]
short_authors: Mitra et al.
---
A fundamental goal of search engines is to identify, given a query, documents
that have relevant text. This is intrinsically difficult because the query and
the document may use different vocabulary, or the document may contain query
words without being relevant. We investigate neural word embeddings as a source
of evidence in document ranking. We train a word2vec embedding model on a large
unlabelled query corpus, but in contrast to how the model is commonly used, we
retain both the input and the output projections, allowing us to leverage both
the embedding spaces to derive richer distributional relationships. During
ranking we map the query words into the input space and the document words into
the output space, and compute a query-document relevance score by aggregating
the cosine similarities across all the query-document word pairs.
  We postulate that the proposed Dual Embedding Space Model (DESM) captures
evidence on whether a document is about a query term in addition to what is
modelled by traditional term-frequency based approaches. Our experiments show
that the DESM can re-rank top documents returned by a commercial Web search
engine, like Bing, better than a term-matching based signal like TF-IDF.
However, when ranking a larger set of candidate documents, we find the
embeddings-based approach is prone to false positives, retrieving documents
that are only loosely related to the query. We demonstrate that this problem
can be solved effectively by ranking based on a linear mixture of the DESM and
the word counting features.