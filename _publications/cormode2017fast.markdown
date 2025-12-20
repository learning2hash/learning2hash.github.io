---
layout: publication
title: Fast Sketch-based Recovery Of Correlation Outliers
authors: Graham Cormode, Jacques Dark
conference: Arxiv
year: 2017
bibkey: cormode2017fast
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1710.01985'}]
tags: ["Evaluation", "Hashing Methods", "Locality-Sensitive-Hashing"]
short_authors: Graham Cormode, Jacques Dark
---
Many data sources can be interpreted as time-series, and a key problem is to
identify which pairs out of a large collection of signals are highly
correlated. We expect that there will be few, large, interesting correlations,
while most signal pairs do not have any strong correlation. We abstract this as
the problem of identifying the highly correlated pairs in a collection of n
mostly pairwise uncorrelated random variables, where observations of the
variables arrives as a stream. Dimensionality reduction can remove dependence
on the number of observations, but further techniques are required to tame the
quadratic (in n) cost of a search through all possible pairs.
  We develop a new algorithm for rapidly finding large correlations based on
sketch techniques with an added twist: we quickly generate sketches of random
combinations of signals, and use these in concert with ideas from coding theory
to decode the identity of correlated pairs. We prove correctness and compare
performance and effectiveness with the best LSH (locality sensitive hashing)
based approach.