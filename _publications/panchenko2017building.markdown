---
layout: publication
title: Building A Web-scale Dependency-parsed Corpus From Commoncrawl
authors: Alexander Panchenko, Eugen Ruppert, Stefano Faralli, Simone Paolo Ponzetto,
  Chris Biemann
conference: Arxiv
year: 2017
bibkey: panchenko2017building
citations: 24
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1710.01779'}]
tags: ["Datasets", "Scalability"]
short_authors: Panchenko et al.
---
We present DepCC, the largest-to-date linguistically analyzed corpus in
English including 365 million documents, composed of 252 billion tokens and 7.5
billion of named entity occurrences in 14.3 billion sentences from a web-scale
crawl of the \textsc\{Common Crawl\} project. The sentences are processed with a
dependency parser and with a named entity tagger and contain provenance
information, enabling various applications ranging from training syntax-based
word embeddings to open information extraction and question answering. We built
an index of all sentences and their linguistic meta-data enabling quick search
across the corpus. We demonstrate the utility of this corpus on the verb
similarity task by showing that a distributional model trained on our corpus
yields better results than models trained on smaller corpora, like Wikipedia.
This distributional model outperforms the state of art models of verb
similarity trained on smaller corpora on the SimVerb3500 dataset.