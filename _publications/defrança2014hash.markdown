---
layout: publication
title: 'A Hash-based Co-clustering Algorithm For Categorical Data'
authors: Fabricio Olivetti De França
conference: "Arxiv"
year: 2014
citations: 12
bibkey: defrança2014hash
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/1407.7753'}
tags: ['Hashing Fundamentals', 'Hashing Methods', 'KDD']
---
Many real-life data are described by categorical attributes without a
pre-classification. A common data mining method used to extract information
from this type of data is clustering. This method group together the samples
from the data that are more similar than all other samples. But, categorical
data pose a challenge when extracting information because: the calculation of
two objects similarity is usually done by measuring the number of common
features, but ignore a possible importance weighting; if the data may be
divided differently according to different subsets of the features, the
algorithm may find clusters with different meanings from each other,
difficulting the post analysis. Data Co-Clustering of categorical data is the
technique that tries to find subsets of samples that share a subset of features
in common. By doing so, not only a sample may belong to more than one cluster
but, the feature selection of each cluster describe its own characteristics. In
this paper a novel Co-Clustering technique for categorical data is proposed by
using Locality Sensitive Hashing technique in order to preprocess a list of
Co-Clusters seeds based on a previous research. Results indicate this technique
is capable of finding high quality Co-Clusters in many different categorical
data sets and scales linearly with the data set size.
