---
layout: publication
title: 'Image Forensics: Detecting Duplication Of Scientific Images With Manipulation-invariant
  Image Similarity'
authors: Cicconet M., Elliott H., Richmond D. L., Wainstock D., Walsh M.
conference: Arxiv
year: 2018
bibkey: cicconet2018image
citations: 20
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1802.06515'}]
tags: ["Evaluation", "Image Retrieval", "Privacy & Security"]
short_authors: Cicconet et al.
---
Manipulation and re-use of images in scientific publications is a concerning
problem that currently lacks a scalable solution. Current tools for detecting
image duplication are mostly manual or semi-automated, despite the availability
of an overwhelming target dataset for a learning-based approach. This paper
addresses the problem of determining if, given two images, one is a manipulated
version of the other by means of copy, rotation, translation, scale,
perspective transform, histogram adjustment, or partial erasing. We propose a
data-driven solution based on a 3-branch Siamese Convolutional Neural Network.
The ConvNet model is trained to map images into a 128-dimensional space, where
the Euclidean distance between duplicate images is smaller than or equal to 1,
and the distance between unique images is greater than 1. Our results suggest
that such an approach has the potential to improve surveillance of the
published and in-peer-review literature for image manipulation.