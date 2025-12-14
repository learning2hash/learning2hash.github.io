---
layout: publication
title: CBIR Using Pre-trained Neural Networks
authors: Agnel Lazar Alappat, Prajwal Nakhate, Sagar Suman, Ambarish Chandurkar, Varad
  Pimpalkhute, Tapan Jain
conference: Arxiv
year: 2021
bibkey: alappat2021cbir
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2110.14455'}]
tags: [Image Retrieval, Datasets]
short_authors: Alappat et al.
---
Much of the recent research work in image retrieval, has been focused around
using Neural Networks as the core component. Many of the papers in other domain
have shown that training multiple models, and then combining their outcomes,
provide good results. This is since, a single Neural Network model, may not
extract sufficient information from the input. In this paper, we aim to follow
a different approach. Instead of the using a single model, we use a pretrained
Inception V3 model, and extract activation of its last fully connected layer,
which forms a low dimensional representation of the image. This feature matrix,
is then divided into branches and separate feature extraction is done for each
branch, to obtain multiple features flattened into a vector. Such individual
vectors are then combined, to get a single combined feature. We make use of
CUB200-2011 Dataset, which comprises of 200 birds classes to train the model
on. We achieved a training accuracy of 99.46% and validation accuracy of 84.56%
for the same. On further use of 3 branched global descriptors, we improve the
validation accuracy to 88.89%. For this, we made use of MS-RMAC feature
extraction method.