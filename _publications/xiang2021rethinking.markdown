---
layout: publication
title: Rethinking Person Re-identification Via Semantic-based Pretraining
authors: Suncheng Xiang, Jingsheng Gao, Zirui Zhang, Mengyuan Guan, Binjie Yan, Ting
  Liu, Dahong Qian, Yuzhuo Fu
conference: ACM Transactions on Multimedia Computing, Communications, and Applications
year: 2023
bibkey: xiang2021rethinking
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2110.05074'}]
tags: []
short_authors: Xiang et al.
---
Pretraining is a dominant paradigm in computer vision. Generally, supervised
ImageNet pretraining is commonly used to initialize the backbones of person
re-identification (Re-ID) models. However, recent works show a surprising
result that CNN-based pretraining on ImageNet has limited impacts on Re-ID
system due to the large domain gap between ImageNet and person Re-ID data. To
seek an alternative to traditional pretraining, here we investigate
semantic-based pretraining as another method to utilize additional textual data
against ImageNet pretraining. Specifically, we manually construct a diversified
FineGPR-C caption dataset for the first time on person Re-ID events. Based on
it, a pure semantic-based pretraining approach named VTBR is proposed to adopt
dense captions to learn visual representations with fewer images. We train
convolutional neural networks from scratch on the captions of FineGPR-C
dataset, and then transfer them to downstream Re-ID tasks. Comprehensive
experiments conducted on benchmark datasets show that our VTBR can achieve
competitive performance compared with ImageNet pretraining - despite using up
to 1.4x fewer images, revealing its potential in Re-ID pretraining.