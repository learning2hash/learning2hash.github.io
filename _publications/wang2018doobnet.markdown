---
layout: publication
title: 'Doobnet: Deep Object Occlusion Boundary Detection From An Image'
authors: Guoxia Wang, Xiaohui Liang, Frederick W. B. Li
conference: Lecture Notes in Computer Science
year: 2019
bibkey: wang2018doobnet
citations: 26
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1806.03772'}]
tags: []
short_authors: Guoxia Wang, Xiaohui Liang, Frederick W. B. Li
---
Object occlusion boundary detection is a fundamental and crucial research
problem in computer vision. This is challenging to solve as encountering the
extreme boundary/non-boundary class imbalance during training an object
occlusion boundary detector. In this paper, we propose to address this class
imbalance by up-weighting the loss contribution of false negative and false
positive examples with our novel Attention Loss function. We also propose a
unified end-to-end multi-task deep object occlusion boundary detection network
(DOOBNet) by sharing convolutional features to simultaneously predict object
boundary and occlusion orientation. DOOBNet adopts an encoder-decoder structure
with skip connection in order to automatically learn multi-scale and
multi-level features. We significantly surpass the state-of-the-art on the PIOD
dataset (ODS F-score of .702) and the BSDS ownership dataset (ODS F-score of
.555), as well as improving the detecting speed to as 0.037s per image on the
PIOD dataset.