---
layout: publication
title: Learning Sense-specific Static Embeddings Using Contextualised Word Embeddings
  As A Proxy
authors: Yi Zhou, Danushka Bollegala
conference: Arxiv
year: 2021
bibkey: zhou2021learning
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2110.02204'}]
tags: ["Evaluation"]
short_authors: Yi Zhou, Danushka Bollegala
---
Contextualised word embeddings generated from Neural Language Models (NLMs),
such as BERT, represent a word with a vector that considers the semantics of
the target word as well its context. On the other hand, static word embeddings
such as GloVe represent words by relatively low-dimensional, memory- and
compute-efficient vectors but are not sensitive to the different senses of the
word. We propose Context Derived Embeddings of Senses (CDES), a method that
extracts sense related information from contextualised embeddings and injects
it into static embeddings to create sense-specific static embeddings.
Experimental results on multiple benchmarks for word sense disambiguation and
sense discrimination tasks show that CDES can accurately learn sense-specific
static embeddings reporting comparable performance to the current
state-of-the-art sense embeddings.