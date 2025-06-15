---
layout: publication
title: 'Improving Zero-shot Learning By Mitigating The Hubness Problem'
authors: Georgiana Dinu, Angeliki Lazaridou, Marco Baroni
conference: "Arxiv"
year: 2014
citations: 284
bibkey: dinu2014improving
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/1412.6568'}
tags: ['Cross-Modal', 'Retrieval Models', 'Shallow', 'Supervised', 'Applications']
---
The zero-shot paradigm exploits vector-based word representations extracted
from text corpora with unsupervised methods to learn general mapping functions
from other feature spaces onto word space, where the words associated to the
nearest neighbours of the mapped vectors are used as their linguistic labels.
We show that the neighbourhoods of the mapped elements are strongly polluted by
hubs, vectors that tend to be near a high proportion of items, pushing their
correct labels down the neighbour list. After illustrating the problem
empirically, we propose a simple method to correct it by taking the proximity
distribution of potential neighbours across many mapped vectors into account.
We show that this correction leads to consistent improvements in realistic
zero-shot experiments in the cross-lingual, image labeling and image retrieval
domains.
