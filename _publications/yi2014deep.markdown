---
layout: publication
title: Deep Metric Learning For Practical Person Re-identification
authors: Yi Dong, Lei Zhen, Li Stan Z.
conference: Arxiv
year: 2014
bibkey: yi2014deep
citations: 143
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1407.4979'}]
tags: ["Datasets", "Distance Metric Learning", "Image Retrieval"]
short_authors: Yi Dong, Lei Zhen, Li Stan Z.
---
Various hand-crafted features and metric learning methods prevail in the
field of person re-identification. Compared to these methods, this paper
proposes a more general way that can learn a similarity metric from image
pixels directly. By using a "siamese" deep neural network, the proposed method
can jointly learn the color feature, texture feature and metric in a unified
framework. The network has a symmetry structure with two sub-networks which are
connected by Cosine function. To deal with the big variations of person images,
binomial deviance is used to evaluate the cost between similarities and labels,
which is proved to be robust to outliers.
  Compared to existing researches, a more practical setting is studied in the
experiments that is training and test on different datasets (cross dataset
person re-identification). Both in "intra dataset" and "cross dataset"
settings, the superiorities of the proposed method are illustrated on VIPeR and
PRID.