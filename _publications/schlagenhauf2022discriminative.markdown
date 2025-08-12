---
layout: publication
title: Discriminative Feature Learning Through Feature Distance Loss
authors: Tobias Schlagenhauf, Yiwen Lin, Benjamin Noack
conference: Machine Vision and Applications
year: 2023
bibkey: schlagenhauf2022discriminative
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2205.11606'}]
tags: []
short_authors: Tobias Schlagenhauf, Yiwen Lin, Benjamin Noack
---
Ensembles of Convolutional neural networks have shown remarkable results in
learning discriminative semantic features for image classification tasks.
Though, the models in the ensemble often concentrate on similar regions in
images. This work proposes a novel method that forces a set of base models to
learn different features for a classification task. These models are combined
in an ensemble to make a collective classification. The key finding is that by
forcing the models to concentrate on different features, the classification
accuracy is increased. To learn different feature concepts, a so-called feature
distance loss is implemented on the feature maps. The experiments on benchmark
convolutional neural networks (VGG16, ResNet, AlexNet), popular datasets
(Cifar10, Cifar100, miniImageNet, NEU, BSD, TEX), and different training
samples (3, 5, 10, 20, 50, 100 per class) show the effectiveness of the
proposed feature loss. The proposed method outperforms classical ensemble
versions of the base models. The Class Activation Maps explicitly prove the
ability to learn different feature concepts. The code is available at:
https://github.com/2Obe/Feature-Distance-Loss.git