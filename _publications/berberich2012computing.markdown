---
layout: publication
title: Computing N-gram Statistics In Mapreduce
authors: Klaus Berberich, Srikanta Bedathur
conference: Proceedings of the 16th International Conference on Extending Database
  Technology
year: 2013
bibkey: berberich2012computing
citations: 22
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1207.4371'}]
tags: []
short_authors: Klaus Berberich, Srikanta Bedathur
---
Statistics about n-grams (i.e., sequences of contiguous words or other tokens
in text documents or other string data) are an important building block in
information retrieval and natural language processing. In this work, we study
how n-gram statistics, optionally restricted by a maximum n-gram length and
minimum collection frequency, can be computed efficiently harnessing MapReduce
for distributed data processing. We describe different algorithms, ranging from
an extension of word counting, via methods based on the Apriori principle, to a
novel method Suffix-\sigma that relies on sorting and aggregating suffixes. We
examine possible extensions of our method to support the notions of
maximality/closedness and to perform aggregations beyond occurrence counting.
Assuming Hadoop as a concrete MapReduce implementation, we provide insights on
an efficient implementation of the methods. Extensive experiments on The New
York Times Annotated Corpus and ClueWeb09 expose the relative benefits and
trade-offs of the methods.