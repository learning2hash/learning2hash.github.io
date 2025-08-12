---
layout: publication
title: Initkmix -- A Novel Initial Partition Generation Algorithm For Clustering Mixed
  Data Using K-means-based Clustering
authors: Amir Ahmad, Shehroz S. Khan
conference: Expert Systems with Applications
year: 2020
bibkey: ahmad2019initkmix
citations: 31
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1902.00127'}]
tags: []
short_authors: Amir Ahmad, Shehroz S. Khan
---
Mixed datasets consist of both numeric and categorical attributes. Various
k-means-based clustering algorithms have been developed for these datasets.
Generally, these algorithms use random partition as a starting point, which
tends to produce different clustering results for different runs. In this
paper, we propose, initKmix, a novel algorithm for finding an initial partition
for k-means-based clustering algorithms for mixed datasets. In the initKmix
algorithm, a k-means-based clustering algorithm is run many times, and in each
run, one of the attributes is used to create initial clusters for that run. The
clustering results of various runs are combined to produce the initial
partition. This initial partition is then used as a seed to a k-means-based
clustering algorithm to cluster mixed data. Experiments with various
categorical and mixed datasets showed that initKmix produced accurate and
consistent results, and outperformed the random initial partition method and
other state-of-the-art initialization methods. Experiments also showed that
k-means-based clustering for mixed datasets with initKmix performed similar to
or better than many state-of-the-art clustering algorithms for categorical and
mixed datasets.