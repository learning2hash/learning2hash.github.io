---
layout: publication
title: Object-centric Sampling For Fine-grained Image Classification
authors: Xiaoyu Wang, Tianbao Yang, Guobin Chen, Yuanqing Lin
conference: Arxiv
year: 2014
bibkey: wang2014object
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1412.3161'}]
tags: []
short_authors: Wang et al.
---
This paper proposes to go beyond the state-of-the-art deep convolutional
neural network (CNN) by incorporating the information from object detection,
focusing on dealing with fine-grained image classification. Unfortunately, CNN
suffers from over-fiting when it is trained on existing fine-grained image
classification benchmarks, which typically only consist of less than a few tens
of thousands training images. Therefore, we first construct a large-scale
fine-grained car recognition dataset that consists of 333 car classes with more
than 150 thousand training images. With this large-scale dataset, we are able
to build a strong baseline for CNN with top-1 classification accuracy of 81.6%.
One major challenge in fine-grained image classification is that many classes
are very similar to each other while having large within-class variation. One
contributing factor to the within-class variation is cluttered image
background. However, the existing CNN training takes uniform window sampling
over the image, acting as blind on the location of the object of interest. In
contrast, this paper proposes an *object-centric sampling* (OCS) scheme
that samples image windows based on the object location information. The
challenge in using the location information lies in how to design powerful
object detector and how to handle the imperfectness of detection results. To
that end, we design a saliency-aware object detection approach specific for the
setting of fine-grained image classification, and the uncertainty of detection
results are naturally handled in our OCS scheme. Our framework is demonstrated
to be very effective, improving top-1 accuracy to 89.3% (from 81.6%) on the
large-scale fine-grained car classification dataset.