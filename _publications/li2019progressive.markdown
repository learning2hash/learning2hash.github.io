---
layout: publication
title: Progressive Sample Mining And Representation Learning For One-shot Person Re-identification
  With Adversarial Samples
authors: Hui Li, Jimin Xiao, Mingjie Sun, Eng Gee Lim, Yao Zhao
conference: Arxiv
year: 2019
bibkey: li2019progressive
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1911.00666'}]
tags: []
short_authors: Li et al.
---
In this paper, we aim to tackle the one-shot person re-identification problem
where only one image is labelled for each person, while other images are
unlabelled. This task is challenging due to the lack of sufficient labelled
training data. To tackle this problem, we propose to iteratively guess pseudo
labels for the unlabeled image samples, which are later used to update the
re-identification model together with the labelled samples. A new sampling
mechanism is designed to select unlabeled samples to pseudo labelled samples
based on the distance matrix, and to form a training triplet batch including
both labelled samples and pseudo labelled samples. We also design an
HSoften-Triplet-Loss to soften the negative impact of the incorrect pseudo
label, considering the unreliable nature of pseudo labelled samples. Finally,
we deploy an adversarial learning method to expand the image samples to
different camera views. Our experiments show that our framework achieves a new
state-of-the-art one-shot Re-ID performance on Market-1501 (mAP 42.7%) and
DukeMTMC-Reid dataset (mAP 40.3%). Code will be available soon.