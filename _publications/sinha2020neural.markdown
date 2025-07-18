---
layout: publication
title: Neural Neighborhood Encoding For Classification
authors: Sinha Kaushik, Ram Parikshit
conference: Proceedings of the 27th ACM SIGKDD Conference on Knowledge Discovery &amp;
  Data Mining
year: 2020
bibkey: sinha2020neural
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2008.08685'}]
tags: [KDD, Evaluation]
---
Inspired by the fruit-fly olfactory circuit, the Fly Bloom Filter [Dasgupta
et al., 2018] is able to efficiently summarize the data with a single pass and
has been used for novelty detection. We propose a new classifier (for binary
and multi-class classification) that effectively encodes the different local
neighborhoods for each class with a per-class Fly Bloom Filter. The inference
on test data requires an efficient \{\tt FlyHash\} [Dasgupta, et al., 2017]
operation followed by a high-dimensional, but \{\em sparse\}, dot product with
the per-class Bloom Filters. The learning is trivially parallelizable. On the
theoretical side, we establish conditions under which the prediction of our
proposed classifier on any test example agrees with the prediction of the
nearest neighbor classifier with high probability. We extensively evaluate our
proposed scheme with over \\(50\\) data sets of varied data dimensionality to
demonstrate that the predictive performance of our proposed neuroscience
inspired classifier is competitive the the nearest-neighbor classifiers and
other single-pass classifiers.