---
layout: publication
title: 'Families In The Wild (FIW): Large-scale Kinship Image Database And Benchmarks'
authors: Joseph P. Robinson, Ming Shao, Yue Wu, Yun Fu
conference: ACM MM (2016) 242-246
year: 2016
bibkey: robinson2016families
citations: 71
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1604.02182'}]
tags: ["Datasets", "Scalability"]
short_authors: Robinson et al.
---
We present the largest kinship recognition dataset to date, Families in the
Wild (FIW). Motivated by the lack of a single, unified dataset for kinship
recognition, we aim to provide a dataset that captivates the interest of the
research community. With only a small team, we were able to collect, organize,
and label over 10,000 family photos of 1,000 families with our annotation tool
designed to mark complex hierarchical relationships and local label information
in a quick and efficient manner. We include several benchmarks for two
image-based tasks, kinship verification and family recognition. For this, we
incorporate several visual features and metric learning methods as baselines.
Also, we demonstrate that a pre-trained Convolutional Neural Network (CNN) as
an off-the-shelf feature extractor outperforms the other feature types. Then,
results were further boosted by fine-tuning two deep CNNs on FIW data: (1) for
kinship verification, a triplet loss function was learned on top of the network
of pre-trained weights; (2) for family recognition, a family-specific softmax
classifier was added to the network.