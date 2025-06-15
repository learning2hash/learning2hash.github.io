---
layout: publication
title: 'A New Hashing Based Nearest Neighbors Selection Technique For Big Datasets'
authors: Jude Tchaye-kondi, Yanlong Zhai, Liehuang Zhu
conference: "Arxiv"
year: 2020
citations: 1
bibkey: tchayekondi2020new
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2004.02290'}
tags: ['Efficiency', 'Unimodal', 'Retrieval Models', 'Shallow', 'Datasets', 'Supervised', 'Training Strategy', 'Hashing']
---
KNN has the reputation to be the word simplest but efficient supervised
learning algorithm used for either classification or regression. KNN prediction
efficiency highly depends on the size of its training data but when this
training data grows KNN suffers from slowness in making decisions since it
needs to search nearest neighbors within the entire dataset at each decision
making. This paper proposes a new technique that enables the selection of
nearest neighbors directly in the neighborhood of a given observation. The
proposed approach consists of dividing the data space into subcells of a
virtual grid built on top of data space. The mapping between the data points
and subcells is performed using hashing. When it comes to select the nearest
neighbors of a given observation, we firstly identify the cell the observation
belongs by using hashing, and then we look for nearest neighbors from that
central cell and cells around it layer by layer. From our experiment
performance analysis on publicly available datasets, our algorithm outperforms
the original KNN in time efficiency with a prediction quality as good as that
of KNN it also offers competitive performance with solutions like KDtree
