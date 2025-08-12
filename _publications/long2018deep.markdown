---
layout: publication
title: Deep Neural Networks In Fully Connected CRF For Image Labeling With Social
  Network Metadata
authors: Chengjiang Long, Roddy Collins, Eran Swears, Anthony Hoogs
conference: The 41st International ACM SIGIR Conference on Research &amp; Development
  in Information Retrieval
year: 2018
bibkey: long2018deep
citations: 22
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1801.09108'}]
tags: ["SIGIR"]
short_authors: Long et al.
---
We propose a novel method for predicting image labels by fusing image content
descriptors with the social media context of each image. An image uploaded to a
social media site such as Flickr often has meaningful, associated information,
such as comments and other images the user has uploaded, that is complementary
to pixel content and helpful in predicting labels. Prediction challenges such
as ImageNet~\cite\{imagenet_cvpr09\} and MSCOCO~\cite\{LinMBHPRDZ:ECCV14\} use only
pixels, while other methods make predictions purely from social media context
\cite\{McAuleyECCV12\}. Our method is based on a novel fully connected
Conditional Random Field (CRF) framework, where each node is an image, and
consists of two deep Convolutional Neural Networks (CNN) and one Recurrent
Neural Network (RNN) that model both textual and visual node/image information.
The edge weights of the CRF graph represent textual similarity and link-based
metadata such as user sets and image groups. We model the CRF as an RNN for
both learning and inference, and incorporate the weighted ranking loss and
cross entropy loss into the CRF parameter optimization to handle the training
data imbalance issue. Our proposed approach is evaluated on the MIR-9K dataset
and experimentally outperforms current state-of-the-art approaches.