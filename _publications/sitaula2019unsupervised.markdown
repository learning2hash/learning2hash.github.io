---
layout: publication
title: Unsupervised Deep Features For Privacy Image Classification
authors: Chiranjibi Sitaula, Yong Xiang, Sunil Aryal, Xuequan Lu
conference: Lecture Notes in Computer Science
year: 2019
bibkey: sitaula2019unsupervised
citations: 14
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1909.10708'}]
tags: ["Unsupervised"]
short_authors: Sitaula et al.
---
Sharing images online poses security threats to a wide range of users due to
the unawareness of privacy information. Deep features have been demonstrated to
be a powerful representation for images. However, deep features usually suffer
from the issues of a large size and requiring a huge amount of data for
fine-tuning. In contrast to normal images (e.g., scene images), privacy images
are often limited because of sensitive information. In this paper, we propose a
novel approach that can work on limited data and generate deep features of
smaller size. For training images, we first extract the initial deep features
from the pre-trained model and then employ the K-means clustering algorithm to
learn the centroids of these initial deep features. We use the learned
centroids from training features to extract the final features for each testing
image and encode our final features with the triangle encoding. To improve the
discriminability of the features, we further perform the fusion of two proposed
unsupervised deep features obtained from different layers. Experimental results
show that the proposed features outperform state-of-the-art deep features, in
terms of both classification accuracy and testing time.