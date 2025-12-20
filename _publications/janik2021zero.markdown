---
layout: publication
title: 'Zero In On Shape: A Generic 2D-3D Instance Similarity Metric Learned From
  Synthetic Data'
authors: MacIej Janik, Niklas Gard, Anna Hilsmann, Peter Eisert
conference: 2021 IEEE International Conference on Image Processing (ICIP)
year: 2021
bibkey: janik2021zero
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2108.04091'}]
tags: ["Datasets", "Distance Metric Learning", "Evaluation", "Few Shot & Zero Shot"]
short_authors: Janik et al.
---
We present a network architecture which compares RGB images and untextured 3D
models by the similarity of the represented shape. Our system is optimised for
zero-shot retrieval, meaning it can recognise shapes never shown in training.
We use a view-based shape descriptor and a siamese network to learn object
geometry from pairs of 3D models and 2D images. Due to scarcity of datasets
with exact photograph-mesh correspondences, we train our network with only
synthetic data. Our experiments investigate the effect of different qualities
and quantities of training data on retrieval accuracy and present insights from
bridging the domain gap. We show that increasing the variety of synthetic data
improves retrieval accuracy and that our system's performance in zero-shot mode
can match that of the instance-aware mode, as far as narrowing down the search
to the top 10% of objects.