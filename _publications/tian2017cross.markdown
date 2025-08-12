---
layout: publication
title: Cross-view Image Matching For Geo-localization In Urban Environments
authors: Yicong Tian, Chen Chen, Mubarak Shah
conference: 2017 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2017
bibkey: tian2017cross
citations: 179
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1703.07815'}]
tags: ["CVPR"]
short_authors: Yicong Tian, Chen Chen, Mubarak Shah
---
In this paper, we address the problem of cross-view image geo-localization.
Specifically, we aim to estimate the GPS location of a query street view image
by finding the matching images in a reference database of geo-tagged bird's eye
view images, or vice versa. To this end, we present a new framework for
cross-view image geo-localization by taking advantage of the tremendous success
of deep convolutional neural networks (CNNs) in image classification and object
detection. First, we employ the Faster R-CNN to detect buildings in the query
and reference images. Next, for each building in the query image, we retrieve
the \(k\) nearest neighbors from the reference buildings using a Siamese network
trained on both positive matching image pairs and negative pairs. To find the
correct NN for each query building, we develop an efficient multiple nearest
neighbors matching method based on dominant sets. We evaluate the proposed
framework on a new dataset that consists of pairs of street view and bird's eye
view images. Experimental results show that the proposed method achieves better
geo-localization accuracy than other approaches and is able to generalize to
images at unseen locations.