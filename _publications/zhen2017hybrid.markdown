---
layout: publication
title: A Hybrid Supervised-unsupervised Method On Image Topic Visualization With Convolutional
  Neural Network And LDA
authors: Kai Zhen, Mridul Birla, David Crandall, Bingjing Zhang, Judy Qiu
conference: Arxiv
year: 2017
bibkey: zhen2017hybrid
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1703.05243'}]
tags: ["Supervised", "Unsupervised"]
short_authors: Zhen et al.
---
Given the progress in image recognition with recent data driven paradigms,
it's still expensive to manually label a large training data to fit a
convolutional neural network (CNN) model. This paper proposes a hybrid
supervised-unsupervised method combining a pre-trained AlexNet with Latent
Dirichlet Allocation (LDA) to extract image topics from both an unlabeled
life-logging dataset and the COCO dataset. We generate the bag-of-words
representations of an egocentric dataset from the softmax layer of AlexNet and
use LDA to visualize the subject's living genre with duplicated images. We use
a subset of COCO on 4 categories as ground truth, and define consistent rate to
quantitatively analyze the performance of the method, it achieves 84% for
consistent rate on average comparing to 18.75% from a raw CNN model. The method
is capable of detecting false labels and multi-labels from COCO dataset. For
scalability test, parallelization experiments are conducted with Harp-LDA on a
Intel Knights Landing cluster: to extract 1,000 topic assignments for 241,035
COCO images, it takes 10 minutes with 60 threads.