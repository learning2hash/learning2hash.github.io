---
layout: publication
title: Detection And Localization Of Image Forgeries Using Resampling Features And
  Deep Learning
authors: Jason Bunk, Jawadul H. Bappy, Tajuddin Manhar Mohammed, Lakshmanan Nataraj,
  Arjuna Flenner, B. S. Manjunath, Shivkumar Chandrasekaran, Amit K. Roy-Chowdhury,
  Lawrence Peterson
conference: 2017 IEEE Conference on Computer Vision and Pattern Recognition Workshops
  (CVPRW)
year: 2017
bibkey: bunk2017detection
citations: 151
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1707.00433'}]
tags: ["CVPR"]
short_authors: Bunk et al.
---
Resampling is an important signature of manipulated images. In this paper, we
propose two methods to detect and localize image manipulations based on a
combination of resampling features and deep learning. In the first method, the
Radon transform of resampling features are computed on overlapping image
patches. Deep learning classifiers and a Gaussian conditional random field
model are then used to create a heatmap. Tampered regions are located using a
Random Walker segmentation method. In the second method, resampling features
computed on overlapping image patches are passed through a Long short-term
memory (LSTM) based network for classification and localization. We compare the
performance of detection/localization of both these methods. Our experimental
results show that both techniques are effective in detecting and localizing
digital image forgeries.