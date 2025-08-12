---
layout: publication
title: 'Synapse At Cap 2017 NER Challenge: Fasttext CRF'
authors: Damien Sileo, Camille Pradel, Philippe Muller, Tim van de Cruys
conference: CAP2017
year: 2017
bibkey: sileo2017synapse
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1709.04820'}]
tags: []
short_authors: Sileo et al.
---
We present our system for the CAp 2017 NER challenge which is about named
entity recognition on French tweets. Our system leverages unsupervised learning
on a larger dataset of French tweets to learn features feeding a CRF model. It
was ranked first without using any gazetteer or structured external data, with
an F-measure of 58.89%. To the best of our knowledge, it is the first system
to use fasttext embeddings (which include subword representations) and an
embedding-based sentence representation for NER.