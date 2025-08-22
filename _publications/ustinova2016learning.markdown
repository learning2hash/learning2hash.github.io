---
layout: publication
title: Learning Deep Embeddings With Histogram Loss
authors: Evgeniya Ustinova, Victor Lempitsky
conference: Arxiv
year: 2016
bibkey: ustinova2016learning
citations: 271
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1611.00822'}]
tags: ["Datasets"]
short_authors: Evgeniya Ustinova, Victor Lempitsky
---
We suggest a loss for learning deep embeddings. The new loss does not
introduce parameters that need to be tuned and results in very good embeddings
across a range of datasets and problems. The loss is computed by estimating two
distribution of similarities for positive (matching) and negative
(non-matching) sample pairs, and then computing the probability of a positive
pair to have a lower similarity score than a negative pair based on the
estimated similarity distributions. We show that such operations can be
performed in a simple and piecewise-differentiable manner using 1D histograms
with soft assignment operations. This makes the proposed loss suitable for
learning deep embeddings using stochastic optimization. In the experiments, the
new loss performs favourably compared to recently proposed alternatives.