---
layout: publication
title: CBIR Using Features Derived By Deep Learning
authors: Subhadip Maji, Smarajit Bose
conference: ACM/IMS Transactions on Data Science
year: 2020
bibkey: maji2020cbir
citations: 39
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2002.07877'}]
tags: ["Image Retrieval", "Neural Hashing"]
short_authors: Subhadip Maji, Smarajit Bose
---
In a Content Based Image Retrieval (CBIR) System, the task is to retrieve
similar images from a large database given a query image. The usual procedure
is to extract some useful features from the query image, and retrieve images
which have similar set of features. For this purpose, a suitable similarity
measure is chosen, and images with high similarity scores are retrieved.
Naturally the choice of these features play a very important role in the
success of this system, and high level features are required to reduce the
semantic gap.
  In this paper, we propose to use features derived from pre-trained network
models from a deep-learning convolution network trained for a large image
classification problem. This approach appears to produce vastly superior
results for a variety of databases, and it outperforms many contemporary CBIR
systems. We analyse the retrieval time of the method, and also propose a
pre-clustering of the database based on the above-mentioned features which
yields comparable results in a much shorter time in most of the cases.