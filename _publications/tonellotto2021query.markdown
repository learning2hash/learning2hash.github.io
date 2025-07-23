---
layout: publication
title: Query Embedding Pruning For Dense Retrieval
authors: Tonellotto Nicola, Macdonald Craig
conference: Proceedings of the 30th ACM International Conference on Information &amp;
  Knowledge Management
year: 2021
bibkey: tonellotto2021query
citations: 16
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2108.10341'}]
tags: ["CIKM", "Efficiency", "Large-Scale Search", "Memory Efficiency", "Similarity Search", "Text Retrieval"]
short_authors: Tonellotto Nicola, Macdonald Craig
---
Recent advances in dense retrieval techniques have offered the promise of
being able not just to re-rank documents using contextualised language models
such as BERT, but also to use such models to identify documents from the
collection in the first place. However, when using dense retrieval approaches
that use multiple embedded representations for each query, a large number of
documents can be retrieved for each query, hindering the efficiency of the
method. Hence, this work is the first to consider efficiency improvements in
the context of a dense retrieval approach (namely ColBERT), by pruning query
term embeddings that are estimated not to be useful for retrieving relevant
documents. Our proposed query embeddings pruning reduces the cost of the dense
retrieval operation, as well as reducing the number of documents that are
retrieved and hence require to be fully scored. Experiments conducted on the
MSMARCO passage ranking corpus demonstrate that, when reducing the number of
query embeddings used from 32 to 3 based on the collection frequency of the
corresponding tokens, query embedding pruning results in no statistically
significant differences in effectiveness, while reducing the number of
documents retrieved by 70%. In terms of mean response time for the end-to-end
to end system, this results in a 2.65x speedup.