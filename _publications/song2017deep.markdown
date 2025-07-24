---
layout: publication
title: Deep Region Hashing For Efficient Large-scale Instance Search From Images
authors: Jingkuan Song, Tao He, Lianli Gao, Xing Xu, Heng Tao Shen
conference: 2017 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2017
bibkey: song2017deep
citations: 308
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1701.07901'}]
tags: ["CVPR", "Datasets", "Efficiency", "Evaluation", "Hashing Methods", "Image Retrieval", "Scalability"]
short_authors: Song et al.
---
Instance Search (INS) is a fundamental problem for many applications, while
it is more challenging comparing to traditional image search since the
relevancy is defined at the instance level.
  Existing works have demonstrated the success of many complex ensemble systems
that are typically conducted by firstly generating object proposals, and then
extracting handcrafted and/or CNN features of each proposal for matching.
However, object bounding box proposals and feature extraction are often
conducted in two separated steps, thus the effectiveness of these methods
collapses. Also, due to the large amount of generated proposals, matching speed
becomes the bottleneck that limits its application to large-scale datasets. To
tackle these issues, in this paper we propose an effective and efficient Deep
Region Hashing (DRH) approach for large-scale INS using an image patch as the
query. Specifically, DRH is an end-to-end deep neural network which consists of
object proposal, feature extraction, and hash code generation. DRH shares
full-image convolutional feature map with the region proposal network, thus
enabling nearly cost-free region proposals. Also, each high-dimensional,
real-valued region features are mapped onto a low-dimensional, compact binary
codes for the efficient object region level matching on large-scale dataset.
Experimental results on four datasets show that our DRH can achieve even better
performance than the state-of-the-arts in terms of MAP, while the efficiency is
improved by nearly 100 times.