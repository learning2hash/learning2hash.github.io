---
layout: publication
title: Image Patch Matching Using Convolutional Descriptors With Euclidean Distance
authors: Iaroslav Melekhov, Juho Kannala, Esa Rahtu
conference: Lecture Notes in Computer Science
year: 2017
bibkey: melekhov2017image
citations: 28
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1710.11359'}]
tags: ["Distance Metric Learning"]
short_authors: Iaroslav Melekhov, Juho Kannala, Esa Rahtu
---
In this work we propose a neural network based image descriptor suitable for
image patch matching, which is an important task in many computer vision
applications. Our approach is influenced by recent success of deep
convolutional neural networks (CNNs) in object detection and classification
tasks. We develop a model which maps the raw input patch to a low dimensional
feature vector so that the distance between representations is small for
similar patches and large otherwise. As a distance metric we utilize L2 norm,
i.e. Euclidean distance, which is fast to evaluate and used in most popular
hand-crafted descriptors, such as SIFT. According to the results, our approach
outperforms state-of-the-art L2-based descriptors and can be considered as a
direct replacement of SIFT. In addition, we conducted experiments with batch
normalization and histogram equalization as a preprocessing method of the input
data. The results confirm that these techniques further improve the performance
of the proposed descriptor. Finally, we show promising preliminary results by
appending our CNNs with recently proposed spatial transformer networks and
provide a visualisation and interpretation of their impact.