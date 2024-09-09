---
layout: publication
title: "Deep Hashing with Triplet Quantization Loss"
authors: Zhou Yuefu, Huang Shanshan, Zhang Ya, Wang Yanfeng
conference: Arxiv
year: 2017
bibkey: zhou2017deep
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1710.11445"}
tags: ['ARXIV', 'Image Retrieval', 'Quantisation']
---
With the explosive growth of image databases, deep hashing, which learns compact binary descriptors for images, has become critical for fast image retrieval. Many existing deep hashing methods leverage quantization loss, defined as distance between the features before and after quantization, to reduce the error from binarizing features. While minimizing the quantization loss guarantees that quantization has minimal effect on retrieval accuracy, it unfortunately significantly reduces the expressiveness of features even before the quantization. In this paper, we show that the above definition of quantization loss is too restricted and in fact not necessary for maintaining high retrieval accuracy. We therefore propose a new form of quantization loss measured in triplets. The core idea of the triplet quantization loss is to learn discriminative real-valued descriptors which lead to minimal loss on retrieval accuracy after quantization. Extensive experiments on two widely used benchmark data sets of different scales, CIFAR-10 and In-shop, demonstrate that the proposed method outperforms the state-of-the-art deep hashing methods. Moreover, we show that the compact binary descriptors obtained with triplet quantization loss lead to very small performance drop after quantization.