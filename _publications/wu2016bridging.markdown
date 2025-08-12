---
layout: publication
title: Bridging Category-level And Instance-level Semantic Image Segmentation
authors: Zifeng Wu, Chunhua Shen, Anton van Den Hengel
conference: Arxiv
year: 2016
bibkey: wu2016bridging
citations: 162
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1605.06885'}]
tags: ["Datasets", "Evaluation"]
short_authors: Zifeng Wu, Chunhua Shen, Anton van Den Hengel
---
We propose an approach to instance-level image segmentation that is built on
top of category-level segmentation. Specifically, for each pixel in a semantic
category mask, its corresponding instance bounding box is predicted using a
deep fully convolutional regression network. Thus it follows a different
pipeline to the popular detect-then-segment approaches that first predict
instances' bounding boxes, which are the current state-of-the-art in instance
segmentation. We show that, by leveraging the strength of our state-of-the-art
semantic segmentation models, the proposed method can achieve comparable or
even better results to detect-then-segment approaches. We make the following
contributions. (i) First, we propose a simple yet effective approach to
semantic instance segmentation. (ii) Second, we propose an online bootstrapping
method during training, which is critically important for achieving good
performance for both semantic category segmentation and instance-level
segmentation. (iii) As the performance of semantic category segmentation has a
significant impact on the instance-level segmentation, which is the second step
of our approach, we train fully convolutional residual networks to achieve the
best semantic category segmentation accuracy. On the PASCAL VOC 2012 dataset,
we obtain the currently best mean intersection-over-union score of 79.1%. (iv)
We also achieve state-of-the-art results for instance-level segmentation.