---
layout: publication
title: 'LSI: A Learned Secondary Index Structure'
authors: Andreas Kipf, Dominik Horn, Pascal Pfeil, Ryan Marcus, Tim Kraska
conference: Arxiv
year: 2022
bibkey: kipf2022lsi
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2205.05769'}]
tags: ["Evaluation", "Vector Indexing"]
short_authors: Kipf et al.
---
Learned index structures have been shown to achieve favorable lookup
performance and space consumption compared to their traditional counterparts
such as B-trees. However, most learned index studies have focused on the
primary indexing setting, where the base data is sorted. In this work, we
investigate whether learned indexes sustain their advantage in the secondary
indexing setting. We introduce Learned Secondary Index (LSI), a first attempt
to use learned indexes for indexing unsorted data. LSI works by building a
learned index over a permutation vector, which allows binary search to
performed on the unsorted base data using random access. We additionally
augment LSI with a fingerprint vector to accelerate equality lookups. We show
that LSI achieves comparable lookup performance to state-of-the-art secondary
indexes while being up to 6x more space efficient.