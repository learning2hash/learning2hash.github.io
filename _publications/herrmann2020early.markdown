---
layout: publication
title: Early Abandoning Pruneddtw And Its Application To Similarity Search
authors: Matthieu Herrmann, Geoffrey I. Webb
conference: Arxiv
year: 2020
bibkey: herrmann2020early
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2010.05371'}]
tags: ["Efficiency", "Scalability", "Similarity Search"]
short_authors: Matthieu Herrmann, Geoffrey I. Webb
---
The Dynamic Time Warping ("DTW") distance is widely used in time series
analysis, be it for classification, clustering or similarity search. However,
its quadratic time complexity prevents it from scaling. Strategies, based on
early abandoning DTW or skipping its computation altogether thanks to lower
bounds, have been developed for certain use cases such as nearest neighbour
search. But vectorization and approximation aside, no advance was made on DTW
itself until recently with the introduction of PrunedDTW. This algorithm, able
to prune unpromising alignments, was later fitted with early abandoning. We
present a new version of PrunedDTW, "EAPrunedDTW", designed with early abandon
in mind from the start, and able to early abandon faster than before. We show
that EAPrunedDTW significantly improves the computation time of similarity
search in the UCR Suite, and renders lower bounds dispensable.