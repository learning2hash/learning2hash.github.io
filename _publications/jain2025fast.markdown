---
layout: publication
title: Fast Similarity Search For Learned Metrics
authors: P. Jain, Kulis, Grauman
conference: IEEE Transactions on Pattern Analysis and Machine Intelligence
year: 2025
bibkey: jain2025fast
citations: 265
additional_links: [{name: Paper, url: 'https://www.cs.utexas.edu/~pjain/pubs/hashing_tr.pdf'}]
tags: [Hashing Methods, Distance Metric Learning, Datasets, Similarity Search]
short_authors: P. Jain, Kulis, Grauman
---
We propose a method to efficiently index into a large database of examples according to a learned metric.
Given a collection of examples, we learn a Mahalanobis distance using an information-theoretic metric
learning technique that adapts prior knowledge about pairwise distances to incorporate similarity and dissimilarity
constraints. To enable sub-linear time similarity search under the learned metric, we show how
to encode a learned Mahalanobis parameterization into randomized locality-sensitive hash functions. We
further formulate an indirect solution that enables metric learning and hashing for sparse input vector spaces
whose high dimensionality make it infeasible to learn an explicit weighting over the feature dimensions.
We demonstrate the approach applied to systems and image datasets, and show that our learned metrics
improve accuracy relative to commonly-used metric baselines, while our hashing construction permits effi-
cient indexing with a learned distance and very large databases.