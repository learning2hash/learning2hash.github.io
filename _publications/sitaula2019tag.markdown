---
layout: publication
title: Tag-based Semantic Features For Scene Image Classification
authors: Chiranjibi Sitaula, Yong Xiang, Anish Basnet, Sunil Aryal, Xuequan Lu
conference: Lecture Notes in Computer Science
year: 2019
bibkey: sitaula2019tag
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1909.09999'}]
tags: []
short_authors: Sitaula et al.
---
The existing image feature extraction methods are primarily based on the
content and structure information of images, and rarely consider the contextual
semantic information. Regarding some types of images such as scenes and
objects, the annotations and descriptions of them available on the web may
provide reliable contextual semantic information for feature extraction. In
this paper, we introduce novel semantic features of an image based on the
annotations and descriptions of its similar images available on the web.
Specifically, we propose a new method which consists of two consecutive steps
to extract our semantic features. For each image in the training set, we
initially search the top \(k\) most similar images from the internet and extract
their annotations/descriptions (e.g., tags or keywords). The annotation
information is employed to design a filter bank for each image category and
generate filter words (codebook). Finally, each image is represented by the
histogram of the occurrences of filter words in all categories. We evaluate the
performance of the proposed features in scene image classification on three
commonly-used scene image datasets (i.e., MIT-67, Scene15 and Event8). Our
method typically produces a lower feature dimension than existing feature
extraction methods. Experimental results show that the proposed features
generate better classification accuracies than vision based and tag based
features, and comparable results to deep learning based features.