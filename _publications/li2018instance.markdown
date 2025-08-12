---
layout: publication
title: Instance Embedding Transfer To Unsupervised Video Object Segmentation
authors: Siyang Li, Bryan Seybold, Alexey Vorobyov, Alireza Fathi, Qin Huang, C. -C.
  Jay Kuo
conference: 2018 IEEE/CVF Conference on Computer Vision and Pattern Recognition
year: 2018
bibkey: li2018instance
citations: 117
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1801.00908'}]
tags: ["CVPR", "Unsupervised"]
short_authors: Li et al.
---
We propose a method for unsupervised video object segmentation by
transferring the knowledge encapsulated in image-based instance embedding
networks. The instance embedding network produces an embedding vector for each
pixel that enables identifying all pixels belonging to the same object. Though
trained on static images, the instance embeddings are stable over consecutive
video frames, which allows us to link objects together over time. Thus, we
adapt the instance networks trained on static images to video object
segmentation and incorporate the embeddings with objectness and optical flow
features, without model retraining or online fine-tuning. The proposed method
outperforms state-of-the-art unsupervised segmentation methods in the DAVIS
dataset and the FBMS dataset.