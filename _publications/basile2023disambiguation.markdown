---
layout: publication
title: Disambiguation Of Company Names Via Deep Recurrent Networks
authors: Alessandro Basile, Riccardo Crupi, Michele Grasso, Alessandro Mercanti, Daniele
  Regoli, Simone Scarsi, Shuyi Yang, Andrea Cosentini
conference: Expert Systems with Applications
year: 2023
bibkey: basile2023disambiguation
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2303.05391'}]
tags: ["Supervised"]
short_authors: Basile et al.
---
Name Entity Disambiguation is the Natural Language Processing task of
identifying textual records corresponding to the same Named Entity, i.e.
real-world entities represented as a list of attributes (names, places,
organisations, etc.). In this work, we face the task of disambiguating
companies on the basis of their written names. We propose a Siamese LSTM
Network approach to extract -- via supervised learning -- an embedding of
company name strings in a (relatively) low dimensional vector space and use
this representation to identify pairs of company names that actually represent
the same company (i.e. the same Entity).
  Given that the manual labelling of string pairs is a rather onerous task, we
analyse how an Active Learning approach to prioritise the samples to be
labelled leads to a more efficient overall learning pipeline.
  With empirical investigations, we show that our proposed Siamese Network
outperforms several benchmark approaches based on standard string matching
algorithms when enough labelled data are available. Moreover, we show that
Active Learning prioritisation is indeed helpful when labelling resources are
limited, and let the learning models reach the out-of-sample performance
saturation with less labelled data with respect to standard (random) data
labelling approaches.