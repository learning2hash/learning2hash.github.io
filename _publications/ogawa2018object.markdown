---
layout: publication
title: Object Detection For Comics Using Manga109 Annotations
authors: Toru Ogawa, Atsushi Otsubo, Rei Narita, Yusuke Matsui, Toshihiko Yamasaki,
  Kiyoharu Aizawa
conference: Arxiv
year: 2018
bibkey: ogawa2018object
citations: 41
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1803.08670'}]
tags: ["Datasets"]
short_authors: Ogawa et al.
---
With the growth of digitized comics, image understanding techniques are
becoming important. In this paper, we focus on object detection, which is a
fundamental task of image understanding. Although convolutional neural networks
(CNN)-based methods archived good performance in object detection for
naturalistic images, there are two problems in applying these methods to the
comic object detection task. First, there is no large-scale annotated comics
dataset. The CNN-based methods require large-scale annotations for training.
Secondly, the objects in comics are highly overlapped compared to naturalistic
images. This overlap causes the assignment problem in the existing CNN-based
methods. To solve these problems, we proposed a new annotation dataset and a
new CNN model. We annotated an existing image dataset of comics and created the
largest annotation dataset, named Manga109-annotations. For the assignment
problem, we proposed a new CNN-based detector, SSD300-fork. We compared
SSD300-fork with other detection methods using Manga109-annotations and
confirmed that our model outperformed them based on the mAP score.