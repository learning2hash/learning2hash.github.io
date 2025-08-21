---
layout: publication
title: 'K-nnn: Nearest Neighbors Of Neighbors For Anomaly Detection'
authors: Ori Nizan, Ayellet Tal
conference: 2024 IEEE/CVF Winter Conference on Applications of Computer Vision Workshops
  (WACVW)
year: 2024
bibkey: nizan2023k
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2305.17695'}]
tags: ["Datasets"]
short_authors: Ori Nizan, Ayellet Tal
---
Anomaly detection aims at identifying images that deviate significantly from
the norm. We focus on algorithms that embed the normal training examples in
space and when given a test image, detect anomalies based on the features
distance to the k-nearest training neighbors. We propose a new operator that
takes into account the varying structure & importance of the features in the
embedding space. Interestingly, this is done by taking into account not only
the nearest neighbors, but also the neighbors of these neighbors (k-NNN). We
show that by simply replacing the nearest neighbor component in existing
algorithms by our k-NNN operator, while leaving the rest of the algorithms
untouched, each algorithms own results are improved. This is the case both for
common homogeneous datasets, such as flowers or nuts of a specific type, as
well as for more diverse datasets