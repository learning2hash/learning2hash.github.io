---
layout: publication
title: A Comprehensive Study Of Imagenet Pre-training For Historical Document Image
  Analysis
authors: Linda Studer, Michele Alberti, Vinaychandran Pondenkandath, Pinar Goktepe,
  Thomas Kolonko, Andreas Fischer, Marcus Liwicki, Rolf Ingold
conference: 2019 International Conference on Document Analysis and Recognition (ICDAR)
year: 2019
bibkey: studer2019comprehensive
citations: 66
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1905.09113'}]
tags: ["Survey Paper"]
short_authors: Studer et al.
---
Automatic analysis of scanned historical documents comprises a wide range of
image analysis tasks, which are often challenging for machine learning due to a
lack of human-annotated learning samples. With the advent of deep neural
networks, a promising way to cope with the lack of training data is to
pre-train models on images from a different domain and then fine-tune them on
historical documents. In the current research, a typical example of such
cross-domain transfer learning is the use of neural networks that have been
pre-trained on the ImageNet database for object recognition. It remains a
mostly open question whether or not this pre-training helps to analyse
historical documents, which have fundamentally different image properties when
compared with ImageNet. In this paper, we present a comprehensive empirical
survey on the effect of ImageNet pre-training for diverse historical document
analysis tasks, including character recognition, style classification,
manuscript dating, semantic segmentation, and content-based retrieval. While we
obtain mixed results for semantic segmentation at pixel-level, we observe a
clear trend across different network architectures that ImageNet pre-training
has a positive effect on classification as well as content-based retrieval.