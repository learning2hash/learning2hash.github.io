---
layout: publication
title: Parsimonious Morpheme Segmentation With An Application To Enriching Word Embeddings
authors: Ahmed El-Kishky, Frank Xu, Aston Zhang, Jiawei Han
conference: 2019 IEEE International Conference on Big Data (Big Data)
year: 2019
bibkey: elkishky2019parsimonious
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1908.07832'}]
tags: ["Unsupervised"]
short_authors: El-Kishky et al.
---
Traditionally, many text-mining tasks treat individual word-tokens as the
finest meaningful semantic granularity. However, in many languages and
specialized corpora, words are composed by concatenating semantically
meaningful subword structures. Word-level analysis cannot leverage the semantic
information present in such subword structures. With regard to word embedding
techniques, this leads to not only poor embeddings for infrequent words in
long-tailed text corpora but also weak capabilities for handling
out-of-vocabulary words. In this paper we propose MorphMine for unsupervised
morpheme segmentation. MorphMine applies a parsimony criterion to
hierarchically segment words into the fewest number of morphemes at each level
of the hierarchy. This leads to longer shared morphemes at each level of
segmentation. Experiments show that MorphMine segments words in a variety of
languages into human-verified morphemes. Additionally, we experimentally
demonstrate that utilizing MorphMine morphemes to enrich word embeddings
consistently improves embedding quality on a variety of of embedding
evaluations and a downstream language modeling task.