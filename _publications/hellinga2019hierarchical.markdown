---
layout: publication
title: Hierarchical Annotation Of Images With Two-alternative-forced-choice Metric
  Learning
authors: Niels Hellinga, Vlado Menkovski
conference: Arxiv
year: 2019
bibkey: hellinga2019hierarchical
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1905.09523'}]
tags: ["Datasets", "Distance Metric Learning", "Recommender Systems"]
short_authors: Niels Hellinga, Vlado Menkovski
---
Many tasks such as retrieval and recommendations can significantly benefit
from structuring the data, commonly in a hierarchical way. To achieve this
through annotations of high dimensional data such as images or natural text can
be significantly labor intensive. We propose an approach for uncovering the
hierarchical structure of data based on efficient discriminative testing rather
than annotations of individual datapoints. Using two-alternative-forced-choice
(2AFC) testing and deep metric learning we achieve embedding of the data in
semantic space where we are able to successfully hierarchically cluster. We
actively select triplets for the 2AFC test such that the modeling process is
highly efficient with respect to the number of tests presented to the
annotator. We empirically demonstrate the feasibility of the method by
confirming the shape bias on synthetic data and extract hierarchical structure
on the Fashion-MNIST dataset to a finer granularity than the original labels.