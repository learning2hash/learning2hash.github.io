---
layout: publication
title: Pruned Wasserstein Index Generation Model And Wigpy Package
authors: Fangzhou Xie
conference: CARMA 2020 - 3rd International Conference on Advanced Research Methods
  and Analytics
year: 2020
bibkey: xie2020pruned
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2004.00999'}]
tags: []
short_authors: Fangzhou Xie
---
Recent proposal of Wasserstein Index Generation model (WIG) has shown a new
direction for automatically generating indices. However, it is challenging in
practice to fit large datasets for two reasons. First, the Sinkhorn distance is
notoriously expensive to compute and suffers from dimensionality severely.
Second, it requires to compute a full \(N\times N\) matrix to be fit into memory,
where \(N\) is the dimension of vocabulary. When the dimensionality is too large,
it is even impossible to compute at all. I hereby propose a Lasso-based
shrinkage method to reduce dimensionality for the vocabulary as a
pre-processing step prior to fitting the WIG model. After we get the word
embedding from Word2Vec model, we could cluster these high-dimensional vectors
by \(k\)-means clustering, and pick most frequent tokens within each cluster to
form the "base vocabulary". Non-base tokens are then regressed on the vectors
of base token to get a transformation weight and we could thus represent the
whole vocabulary by only the "base tokens". This variant, called pruned WIG
(pWIG), will enable us to shrink vocabulary dimension at will but could still
achieve high accuracy. I also provide a \textit\{wigpy\} module in Python to
carry out computation in both flavor. Application to Economic Policy
Uncertainty (EPU) index is showcased as comparison with existing methods of
generating time-series sentiment indices.