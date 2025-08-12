---
layout: publication
title: Automatic Graphic Logo Detection Via Fast Region-based Convolutional Networks
authors: "Gon\xE7alo Oliveira, Xavier Fraz\xE3o, Andr\xE9 Pimentel, Bernardete Ribeiro"
conference: 2016 International Joint Conference on Neural Networks (IJCNN)
year: 2016
bibkey: oliveira2016automatic
citations: 51
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1604.06083'}]
tags: []
short_authors: Oliveira et al.
---
Brand recognition is a very challenging topic with many useful applications
in localization recognition, advertisement and marketing. In this paper we
present an automatic graphic logo detection system that robustly handles
unconstrained imaging conditions. Our approach is based on Fast Region-based
Convolutional Networks (FRCN) proposed by Ross Girshick, which have shown
state-of-the-art performance in several generic object recognition tasks
(PASCAL Visual Object Classes challenges). In particular, we use two CNN models
pre-trained with the ILSVRC ImageNet dataset and we look at the selective
search of windows `proposals' in the pre-processing stage and data augmentation
to enhance the logo recognition rate. The novelty lies in the use of transfer
learning to leverage powerful Convolutional Neural Network models trained with
large-scale datasets and repurpose them in the context of graphic logo
detection. Another benefit of this framework is that it allows for multiple
detections of graphic logos using regions that are likely to have an object.
Experimental results with the FlickrLogos-32 dataset show not only the
promising performance of our developed models with respect to noise and other
transformations a graphic logo can be subject to, but also its superiority over
state-of-the-art systems with hand-crafted models and features.