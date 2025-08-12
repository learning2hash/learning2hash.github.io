---
layout: publication
title: Faster R-CNN Features For Instance Search
authors: Amaia Salvador, Xavier Giro-I-Nieto, Ferran Marques, Shin'Ichi Satoh
conference: 2016 IEEE Conference on Computer Vision and Pattern Recognition Workshops
  (CVPRW)
year: 2016
bibkey: salvador2016faster
citations: 121
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1604.08893'}]
tags: ["CVPR"]
short_authors: Salvador et al.
---
Image representations derived from pre-trained Convolutional Neural Networks
(CNNs) have become the new state of the art in computer vision tasks such as
instance retrieval. This work explores the suitability for instance retrieval
of image- and region-wise representations pooled from an object detection CNN
such as Faster R-CNN. We take advantage of the object proposals learned by a
Region Proposal Network (RPN) and their associated CNN features to build an
instance search pipeline composed of a first filtering stage followed by a
spatial reranking. We further investigate the suitability of Faster R-CNN
features when the network is fine-tuned for the same objects one wants to
retrieve. We assess the performance of our proposed system with the Oxford
Buildings 5k, Paris Buildings 6k and a subset of TRECVid Instance Search 2013,
achieving competitive results.