---
layout: publication
title: 'Sensefitting: Sense Level Semantic Specialization Of Word Embeddings For Word
  Sense Disambiguation'
authors: Manuel Stoeckel, Sajawel Ahmed, Alexander Mehler
conference: Arxiv
year: 2019
bibkey: stoeckel2019sensefitting
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1907.13237'}]
tags: []
short_authors: Manuel Stoeckel, Sajawel Ahmed, Alexander Mehler
---
We introduce a neural network-based system of Word Sense Disambiguation (WSD)
for German that is based on SenseFitting, a novel method for optimizing WSD. We
outperform knowledge-based WSD methods by up to 25% F1-score and produce a new
state-of-the-art on the German sense-annotated dataset WebCAGe. Our method uses
three feature vectors consisting of a) sense, b) gloss, and c) relational
vectors to represent target senses and to compare them with the vector
centroids of sample contexts. Utilizing widely available word embeddings and
lexical resources, we are able to compensate for the lower resource
availability of German. SenseFitting builds upon the recently introduced
semantic specialization procedure Attract-Repel, and leverages sense level
semantic constraints from lexical-semantic networks (e.g. GermaNet) or online
social dictionaries (e.g. Wiktionary) to produce high-quality sense embeddings
from pre-trained word embeddings. We evaluate our sense embeddings with a new
SimLex-999 based similarity dataset, called SimSense, that we developed for
this work. We achieve results that outperform current lemma-based
specialization methods for German, making them comparable to results achieved
for English.