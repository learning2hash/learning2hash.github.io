---
layout: publication
title: Bounding Box Embedding For Single Shot Person Instance Segmentation
authors: Jacob Richeimer, Jonathan Mitchell
conference: Arxiv
year: 2018
bibkey: richeimer2018bounding
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1807.07674'}]
tags: []
short_authors: Jacob Richeimer, Jonathan Mitchell
---
We present a bottom-up approach for the task of object instance segmentation
using a single-shot model. The proposed model employs a fully convolutional
network which is trained to predict class-wise segmentation masks as well as
the bounding boxes of the object instances to which each pixel belongs. This
allows us to group object pixels into individual instances. Our network
architecture is based on the DeepLabv3+ model, and requires only minimal extra
computation to achieve pixel-wise instance assignments. We apply our method to
the task of person instance segmentation, a common task relevant to many
applications. We train our model with COCO data and report competitive results
for the person class in the COCO instance segmentation task.