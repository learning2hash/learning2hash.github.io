---
layout: publication
title: Unsupervised Space Partitioning for Nearest Neighbor Search
authors: Fahim Abrar, Ali Mohammed Eunus, Cheema Muhammad Aamir
conference: '2021 11th Workshop on Hyperspectral Imaging and Signal Processing: Evolution
  in Remote Sensing (WHISPERS)'
year: 2022
bibkey: fahim2022unsupervised
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2206.08091'}]
tags: [Unsupervised, Supervised]
---
Approximate Nearest Neighbor Search (ANNS) in high dimensional spaces is
crucial for many real-life applications (e.g., e-commerce, web, multimedia,
etc.) dealing with an abundance of data. This paper proposes an end-to-end
learning framework that couples the partitioning (one critical step of ANNS)
and learning-to-search steps using a custom loss function. A key advantage of
our proposed solution is that it does not require any expensive pre-processing
of the dataset, which is one of the critical limitations of the
state-of-the-art approach. We achieve the above edge by formulating a
multi-objective custom loss function that does not need ground truth labels to
quantify the quality of a given data-space partition, making it entirely
unsupervised. We also propose an ensembling technique by adding varying input
weights to the loss function to train an ensemble of models to enhance the
search quality. On several standard benchmarks for ANNS, we show that our
method beats the state-of-the-art space partitioning method and the ubiquitous
K-means clustering method while using fewer parameters and shorter offline
training times. We also show that incorporating our space-partitioning strategy
into state-of-the-art ANNS techniques such as ScaNN can improve their
performance significantly. Finally, we present our unsupervised partitioning
approach as a promising alternative to many widely used clustering methods,
such as K-means clustering and DBSCAN.