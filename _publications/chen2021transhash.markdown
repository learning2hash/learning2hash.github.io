---
layout: publication
title: Transhash Transformer45;based Hamming Hashing For Efficient Image Retrieval
authors: Chen Yongbiao, Zhang Sheng, Liu Fangxin, Chang Zhigang, Ye Mang, Qi Zhengwei
conference: "Arxiv"
year: 2021
bibkey: chen2021transhash
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2105.01823"}
tags: ['ARXIV', 'Image Retrieval', 'Supervised']
---
Deep hamming hashing has gained growing popularity in approximate nearest neighbour search for large45;scale image retrieval. Until now the deep hashing for the image retrieval community has been dominated by convolutional neural network architectures e.g. texttt123;Resnet125;cite123;he2016deep125;. In this paper inspired by the recent advancements of vision transformers we present textbf123;Transhash125; a pure transformer45;based framework for deep hashing learning. Concretely our framework is composed of two major modules (1) Based on textit123;Vision Transformer125; (ViT) we design a siamese vision transformer backbone for image feature extraction. To learn fine45;grained features we innovate a dual45;stream feature learning on top of the transformer to learn discriminative global and local features. (2) Besides we adopt a Bayesian learning scheme with a dynamically constructed similarity matrix to learn compact binary hash codes. The entire framework is jointly trained in an end45;to45;end manner.~To the best of our knowledge this is the first work to tackle deep hashing learning problems without convolutional neural networks (textit123;CNNs125;). We perform comprehensive experiments on three widely45;studied datasets textbf123;CIFAR45;10125; textbf123;NUSWIDE125; and textbf123;IMAGENET125;. The experiments have evidenced our superiority against the existing state45;of45;the45;art deep hashing methods. Specifically we achieve 8.237; 2.637; 12.737; performance gains in terms of average textit123;mAP125; for different hash bit lengths on three public datasets respectively.
