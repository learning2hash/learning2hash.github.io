---
layout: publication
title: Deep Clustering For Mars Rover Image Datasets
authors: Vikas Ramachandra
conference: Arxiv
year: 2019
bibkey: ramachandra2019deep
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1911.06623'}]
tags: ["Datasets", "Unsupervised"]
short_authors: Vikas Ramachandra
---
In this paper, we build autoencoders to learn a latent space from unlabeled
image datasets obtained from the Mars rover. Then, once the latent feature
space has been learnt, we use k-means to cluster the data. We test the
performance of the algorithm on a smaller labeled dataset, and report good
accuracy and concordance with the ground truth labels. This is the first
attempt to use deep learning based unsupervised algorithms to cluster Mars
Rover images. This algorithm can be used to augment human annotations for such
datasets (which are time consuming) and speed up the generation of ground truth
labels for Mars Rover image data, and potentially other planetary and space
images.