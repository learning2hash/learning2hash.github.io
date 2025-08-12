---
layout: publication
title: Variance-adjusted Cosine Distance As Similarity Metric
authors: Satyajeet Sahoo, Jhareswar Maiti
conference: Arxiv
year: 2025
bibkey: sahoo2025variance
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2502.02233'}]
tags: ["Distance Metric Learning"]
short_authors: Satyajeet Sahoo, Jhareswar Maiti
---
Cosine similarity is a popular distance measure that measures the similarity
between two vectors in the inner product space. It is widely used in many data
classification algorithms like K-Nearest Neighbors, Clustering etc. This study
demonstrates limitations of application of cosine similarity. Particularly,
this study demonstrates that traditional cosine similarity metric is valid only
in the Euclidean space, whereas the original data resides in a random variable
space. When there is variance and correlation in the data, then cosine distance
is not a completely accurate measure of similarity. While new similarity and
distance metrics have been developed to make up for the limitations of cosine
similarity, these metrics are used as substitutes to cosine distance, and do
not make modifications to cosine distance to overcome its limitations.
Subsequently, we propose a modified cosine similarity metric, where cosine
distance is adjusted by variance-covariance of the data. Application of
variance-adjusted cosine distance gives better similarity performance compared
to traditional cosine distance. KNN modelling on the Wisconsin Breast Cancer
Dataset is performed using both traditional and modified cosine similarity
measures and compared. The modified formula shows 100% test accuracy on the
data.