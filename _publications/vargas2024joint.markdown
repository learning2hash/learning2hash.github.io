---
layout: publication
title: Joint Neural Networks For One-shot Object Recognition And Detection
authors: Camilo J. Vargas, Qianni Zhang, Ebroul Izquierdo
conference: Arxiv
year: 2024
bibkey: vargas2024joint
citations: 2
additional_links: [{name: Code, url: 'https://github.com/cjvargasc/JNN'}, {name: Code,
    url: 'https://github.com/cjvargasc/JNN'}, {name: Paper, url: 'https://arxiv.org/abs/2408.00701'}]
tags: []
short_authors: Camilo J. Vargas, Qianni Zhang, Ebroul Izquierdo
---
This paper presents a novel joint neural networks approach to address the
challenging one-shot object recognition and detection tasks. Inspired by
Siamese neural networks and state-of-art multi-box detection approaches, the
joint neural networks are able to perform object recognition and detection for
categories that remain unseen during the training process. Following the
one-shot object recognition/detection constraints, the training and testing
datasets do not contain overlapped classes, in other words, all the test
classes remain unseen during training. The joint networks architecture is able
to effectively compare pairs of images via stacked convolutional layers of the
query and target inputs, recognising patterns of the same input query category
without relying on previous training around this category. The proposed
approach achieves 61.41% accuracy for one-shot object recognition on the
MiniImageNet dataset and 47.1% mAP for one-shot object detection when trained
on the COCO dataset and tested using the Pascal VOC dataset. Code available at
https://github.com/cjvargasc/JNN recog and https://github.com/cjvargasc/JNN
detection/