---
layout: publication
title: Content-based Landmark Retrieval Combining Global And Local Features Using
  Siamese Neural Networks
authors: Tianyi Hu, Monika Kwiatkowski, Simon Matern, Olaf Hellwich
conference: Arxiv
year: 2022
bibkey: hu2022content
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2208.04201'}]
tags: [Evaluation, Re-ranking, Distance Metric Learning, Datasets, Hybrid ANN Methods]
short_authors: Hu et al.
---
In this work, we present a method for landmark retrieval that utilizes global
and local features. A Siamese network is used for global feature extraction and
metric learning, which gives an initial ranking of the landmark search. We
utilize the extracted feature maps from the Siamese architecture as local
descriptors, the search results are then further refined using a cosine
similarity between local descriptors. We conduct a deeper analysis of the
Google Landmark Dataset, which is used for evaluation, and augment the dataset
to handle various intra-class variances. Furthermore, we conduct several
experiments to compare the effects of transfer learning and metric learning, as
well as experiments using other local descriptors. We show that a re-ranking
using local features can improve the search results. We believe that the
proposed local feature extraction using cosine similarity is a simple approach
that can be extended to many other retrieval tasks.