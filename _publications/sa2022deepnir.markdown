---
layout: publication
title: 'Deepnir: Datasets For Generating Synthetic NIR Images And Improved Fruit Detection
  System Using Deep Learning Techniques'
authors: Inkyu Sa, Jongyoon Lim, Ho Seok Ahn, Bruce MacDonald
conference: Sensors
year: 2022
bibkey: sa2022deepnir
citations: 19
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2203.09091'}]
tags: ["Datasets"]
short_authors: Sa et al.
---
This paper presents datasets utilised for synthetic near-infrared (NIR) image
generation and bounding-box level fruit detection systems. It is undeniable
that high-calibre machine learning frameworks such as Tensorflow or Pytorch,
and large-scale ImageNet or COCO datasets with the aid of accelerated GPU
hardware have pushed the limit of machine learning techniques for more than
decades. Among these breakthroughs, a high-quality dataset is one of the
essential building blocks that can lead to success in model generalisation and
the deployment of data-driven deep neural networks. In particular, synthetic
data generation tasks often require more training samples than other supervised
approaches. Therefore, in this paper, we share the NIR+RGB datasets that are
re-processed from two public datasets (i.e., nirscene and SEN12MS) and our
novel NIR+RGB sweet pepper(capsicum) dataset. We quantitatively and
qualitatively demonstrate that these NIR+RGB datasets are sufficient to be used
for synthetic NIR image generation. We achieved Frechet Inception Distance
(FID) of 11.36, 26.53, and 40.15 for nirscene1, SEN12MS, and sweet pepper
datasets respectively. In addition, we release manual annotations of 11 fruit
bounding boxes that can be exported as various formats using cloud service.
Four newly added fruits [blueberry, cherry, kiwi, and wheat] compound 11 novel
bounding box datasets on top of our previous work presented in the deepFruits
project [apple, avocado, capsicum, mango, orange, rockmelon, strawberry]. The
total number of bounding box instances of the dataset is 162k and it is ready
to use from cloud service. For the evaluation of the dataset, Yolov5 single
stage detector is exploited and reported impressive
mean-average-precision,mAP[0.5:0.95] results of[min:0.49, max:0.812]. We hope
these datasets are useful and serve as a baseline for the future studies.