---
layout: publication
title: Feature Weighting And Boosting For Few-shot Segmentation
authors: Khoi Nguyen, Sinisa Todorovic
conference: 2019 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2019
bibkey: nguyen2019feature
citations: 306
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1909.13140'}]
tags: ["Few Shot & Zero Shot", "ICCV"]
short_authors: Khoi Nguyen, Sinisa Todorovic
---
This paper is about few-shot segmentation of foreground objects in images. We
train a CNN on small subsets of training images, each mimicking the few-shot
setting. In each subset, one image serves as the query and the other(s) as
support image(s) with ground-truth segmentation. The CNN first extracts feature
maps from the query and support images. Then, a class feature vector is
computed as an average of the support's feature maps over the known foreground.
Finally, the target object is segmented in the query image by using a cosine
similarity between the class feature vector and the query's feature map. We
make two contributions by: (1) Improving discriminativeness of features so
their activations are high on the foreground and low elsewhere; and (2)
Boosting inference with an ensemble of experts guided with the gradient of loss
incurred when segmenting the support images in testing. Our evaluations on the
PASCAL-\(5^i\) and COCO-\(20^i\) datasets demonstrate that we significantly
outperform existing approaches.