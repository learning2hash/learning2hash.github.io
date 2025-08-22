---
layout: publication
title: A Distributed And Approximated Nearest Neighbors Algorithm For An Efficient
  Large Scale Mean Shift Clustering
authors: "Ga\xEBl Beck, Tarn Duong, Mustapha Lebbah, Hanane Azzag, Christophe C\xE9\
  rin"
conference: Journal of Parallel and Distributed Computing
year: 2019
bibkey: beck2019a
citations: 29
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1902.03833'}]
tags: ["Datasets", "Hashing Methods", "Locality-Sensitive-Hashing", "Unsupervised"]
short_authors: Beck et al.
---
In this paper we target the class of modal clustering methods where clusters
are defined in terms of the local modes of the probability density function
which generates the data. The most well-known modal clustering method is the
k-means clustering. Mean Shift clustering is a generalization of the k-means
clustering which computes arbitrarily shaped clusters as defined as the basins
of attraction to the local modes created by the density gradient ascent paths.
Despite its potential, the Mean Shift approach is a computationally expensive
method for unsupervised learning. Thus, we introduce two contributions aiming
to provide clustering algorithms with a linear time complexity, as opposed to
the quadratic time complexity for the exact Mean Shift clustering. Firstly we
propose a scalable procedure to approximate the density gradient ascent.
Second, our proposed scalable cluster labeling technique is presented. Both
propositions are based on Locality Sensitive Hashing (LSH) to approximate
nearest neighbors. These two techniques may be used for moderate sized
datasets. Furthermore, we show that using our proposed approximations of the
density gradient ascent as a pre-processing step in other clustering methods
can also improve dedicated classification metrics. For the latter, a
distributed implementation, written for the Spark/Scala ecosystem is proposed.
For all these considered clustering methods, we present experimental results
illustrating their labeling accuracy and their potential to solve concrete
problems.